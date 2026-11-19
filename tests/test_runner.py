#!/usr/bin/env python3
"""Tests of the standalone runner (runner/crucible-runner.mjs) and of the Codex side of scripts/crucible_agent.py.
No model is called: the runner gets a stand-in agent command, and the Codex adapter a stand-in `codex` binary that
records how it was called.   python3 tests/test_runner.py"""
import json, os, stat, subprocess, sys, tempfile, time, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNNER = ROOT / "runner" / "crucible-runner.mjs"
TMP = Path(tempfile.mkdtemp(prefix="crucible-runner-test-"))
sys.path.insert(0, str(ROOT / "scripts"))
import crucible_agent as ca      # noqa: E402

# a small workflow script: three agents side by side, one that fails, a pipeline, phases, a returned object
SCRIPT = TMP / "flow.js"
SCRIPT.write_text("""export const meta = { name: 't', description: 'd' }
phase('One')
const S = { type: 'object', properties: { v: { type: 'string' } }, required: ['v'] }
const got = await parallel(['a', 'b', 'c', 'FAIL'].map(x => () => agent('say ' + x + ' in ' + args.runDir, { label: 'say:' + x, schema: S, model: x === 'a' ? 'opus' : undefined, effort: 'high' })))
phase('Two')
const piped = await pipeline(['p'], async it => agent('pipe ' + it, { label: 'pipe:' + it }), async v => String(v).toUpperCase())
let threw = ''
try { await agent('boom FAIL limit', { label: 'limit' }) } catch (e) { threw = String(e.message) }
log('done ' + got.filter(Boolean).length)
return { runDir: args.runDir, results: got.map(g => g && g.v), piped, threw }
""")
# the stand-in agent: answers from the prompt, sleeps a little so overlap can be measured, fails on request
STUB = TMP / "stub.py"
STUB.write_text("""import json, sys, time
from pathlib import Path
a = sys.argv[1:]; o = {a[i]: a[i + 1] for i in range(1, len(a) - 1) if a[i].startswith('--')}
prompt = Path(o['--prompt-file']).read_text()
log = Path(o['--out']).parent.parent / 'calls.jsonl'
with log.open('a') as fh: fh.write(json.dumps({'t0': time.time(), 'prompt': prompt, 'model': o.get('--model'), 'effort': o.get('--effort'), 'provider': o.get('--provider'), 'schema': bool(o.get('--schema-file'))}) + '\\n')
time.sleep(0.4)
with log.open('a') as fh: fh.write(json.dumps({'t1': time.time(), 'prompt': prompt}) + '\\n')
if 'FAIL' in prompt:
    out = {'ok': False, 'kind': 'limit' if 'limit' in prompt else 'timeout', 'error': 'You have hit your usage limit' if 'limit' in prompt else 'timeout after 1s'}
elif o.get('--schema-file'):
    out = {'ok': True, 'result': {'v': prompt.split()[1], '_ck': 'x'}, 'usage': {'in': 100, 'out': 7}, 'model': o.get('--model') or 'default-model'}
else:
    out = {'ok': True, 'result': 'text for ' + prompt.split()[1]}
Path(o['--out']).write_text(json.dumps(out))
""")


def run(run_dir, *extra, jobs="2"):
    args = TMP / f"args-{run_dir.name}.json"
    args.write_text(json.dumps({"runDir": str(run_dir)}))
    env = {**os.environ, "CRUCIBLE_AGENT_CMD": json.dumps([sys.executable, str(STUB)])}
    return subprocess.run(["node", str(RUNNER), "--args", str(args), "--engine", str(SCRIPT), "--provider", "codex", "--jobs", jobs, *extra], capture_output=True, text=True, env=env, cwd=str(TMP))


def lines(f):
    return [json.loads(l) for l in f.read_text().splitlines() if l.strip()]


class Runner(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rd = TMP / "run1"; cls.rd.mkdir()
        cls.first = run(cls.rd)
        cls.st = cls.rd / ".runner"
        cls.calls1 = lines(cls.st / "calls.jsonl")
        cls.second = run(cls.rd)
        cls.calls2 = lines(cls.st / "calls.jsonl")

    def test_the_script_runs_to_its_result(self):
        self.assertEqual(self.first.returncode, 0, self.first.stderr[-800:])
        out = json.loads((self.st / "output.json").read_text())
        self.assertEqual(out["result"]["results"], ["a", "b", "c", None])          # a failed agent is null in parallel(), as in a Workflow run
        self.assertEqual(out["result"]["piped"], ["TEXT FOR P"]); self.assertEqual(out["transcriptDir"], str(self.st))

    def test_a_failed_agent_throws_with_the_providers_words_so_the_engine_can_pause(self):
        self.assertIn("usage limit", json.loads((self.st / "output.json").read_text())["result"]["threw"])

    def test_model_effort_provider_and_reply_format_reach_the_agent(self):
        by = {c["prompt"].split(" in ")[0]: c for c in self.calls1 if "t0" in c}
        self.assertEqual((by["say a"]["model"], by["say a"]["effort"], by["say a"]["provider"], by["say a"]["schema"]), ("opus", "high", "codex", True))
        self.assertIsNone(by["say b"]["model"]); self.assertFalse(by["pipe p"]["schema"])

    def test_no_more_agents_alive_at_once_than_asked(self):
        ev = sorted([(c["t0"], 1) for c in self.calls1 if "t0" in c] + [(c["t1"], -1) for c in self.calls1 if "t1" in c])
        live = peak = 0
        for _, d in ev:
            live += d; peak = max(peak, live)
        self.assertEqual(peak, 2)

    def test_the_journal_is_what_the_save_step_reads(self):
        j = lines(self.st / "journal.jsonl")
        started = {e["agentId"]: e for e in j if e["type"] == "started"}
        results = {e["agentId"]: e for e in j if e["type"] == "result"}
        self.assertEqual(sorted(e["label"] for e in started.values()), ["limit", "limit", "pipe:p", "say:FAIL", "say:FAIL", "say:a", "say:b", "say:c"])
        self.assertEqual({started[i]["label"]: r["result"] for i, r in results.items() if started[i]["label"] == "say:a"}, {"say:a": {"v": "a"}})   # the checksum field is not kept
        self.assertEqual(started[next(iter(started))]["phase"], "One")
        sys.path.insert(0, str(ROOT / "scripts")); import crucible_run as cr
        a = next(i for i, e in started.items() if e["label"] == "say:a")
        st = cr._agent_stats(self.st / f"agent-{a}.jsonl")
        self.assertEqual((st["input"], st["output"], st["ctx_peak"]), (100, 7, 0)); self.assertTrue(st["first"] and st["last"])

    def test_a_relaunch_replays_finished_agents_and_reruns_only_the_failed(self):
        self.assertEqual(self.second.returncode, 0, self.second.stderr[-800:])
        again = [c["prompt"] for c in self.calls2[len(self.calls1):] if "t0" in c]
        self.assertEqual(sorted(p.split(" in ")[0] for p in again), ["boom FAIL limit", "say FAIL"])
        self.assertEqual(json.loads(self.second.stdout.strip().splitlines()[-1])["replayed"], 4)

    def test_status_of_a_finished_run(self):
        r = subprocess.run(["node", str(RUNNER), "--status", str(self.rd)], capture_output=True, text=True)
        s = json.loads(r.stdout)
        self.assertTrue(s["finished"]); self.assertFalse(s["running"]); self.assertEqual(s["output"], str(self.st / "output.json")); self.assertEqual(s["agents"]["returned"], 4)

    def test_detach_status_and_stop(self):
        rd = TMP / "run2"; rd.mkdir()
        (TMP / "slow.js").write_text("export const meta = { name: 's', description: 'd' }\nconst r = await parallel([1, 2, 3, 4, 5, 6, 7, 8].map(i => () => agent('slow ' + i, { label: 'slow:' + i })))\nreturn { runDir: args.runDir, results: r }\n")
        args = TMP / "args-run2.json"; args.write_text(json.dumps({"runDir": str(rd)}))
        env = {**os.environ, "CRUCIBLE_AGENT_CMD": json.dumps([sys.executable, str(STUB)])}
        cmd = ["node", str(RUNNER), "--args", str(args), "--engine", str(TMP / "slow.js"), "--jobs", "1"]
        d = json.loads(subprocess.run(cmd + ["--detach"], capture_output=True, text=True, env=env, cwd=str(TMP)).stdout)
        self.assertTrue(d["started"])
        time.sleep(1.2)
        self.assertIn("already running", subprocess.run(cmd + ["--detach"], capture_output=True, text=True, env=env, cwd=str(TMP)).stdout)
        s = json.loads(subprocess.run(["node", str(RUNNER), "--status", str(rd)], capture_output=True, text=True).stdout)
        self.assertTrue(s["running"]); self.assertFalse(s["finished"]); self.assertEqual(len(s["agents"]["alive"]), 1)
        self.assertTrue(json.loads(subprocess.run(["node", str(RUNNER), "--stop", str(rd)], capture_output=True, text=True).stdout)["stopped"])
        time.sleep(0.8)
        s = json.loads(subprocess.run(["node", str(RUNNER), "--status", str(rd)], capture_output=True, text=True).stdout)
        self.assertFalse(s["running"]); self.assertFalse(s["finished"]); self.assertIn("relaunch with the same args", s["note"])
        done = s["agents"]["returned"]
        self.assertTrue(0 < done < 8)
        r = subprocess.run(cmd, capture_output=True, text=True, env=env, cwd=str(TMP))      # the relaunch continues from the finished agents
        self.assertEqual(json.loads(r.stdout.strip().splitlines()[-1])["replayed"], done)


# a stand-in `codex`: records its arguments, then answers as told by the test
FAKE = TMP / "bin" / "codex"
FAKE.parent.mkdir()
FAKE.write_text(f"""#!{sys.executable}
import json, os, sys
from pathlib import Path
a = sys.argv[1:]
Path(os.environ['FAKE_LOG']).open('a').write(json.dumps(a) + '\\n')
mode = os.environ.get('FAKE_MODE', 'ok')
schema = a[a.index('--output-schema') + 1] if '--output-schema' in a else None
if mode == 'refuse-schema' and schema:
    sys.stderr.write("Invalid schema for response_format 'out': additionalProperties is required"); sys.exit(1)
if mode == 'limit':
    sys.stderr.write("You've hit your usage limit. Try again later."); sys.exit(1)
if mode == 'code-mode-breaks' and 'features.code_mode=true' in a:
    sys.stderr.write("error: unknown feature code_mode"); sys.exit(2)
print(json.dumps({{"type": "turn.completed", "usage": {{"input_tokens": 1200, "cached_input_tokens": 1000, "output_tokens": 30}}}}))
reply = {{"verdict": "ok", "note": None, "items": [{{"id": "a", "why": None}}]}} if (schema or 'FINAL ANSWER FORMAT' in a[-1]) else None
Path(a[a.index('-o') + 1]).write_text(json.dumps(reply) if reply else 'plain words')
""")
FAKE.chmod(FAKE.stat().st_mode | stat.S_IEXEC)
SCHEMA = {"type": "object", "properties": {"verdict": {"type": "string", "enum": ["ok", "bad"]}, "note": {"type": "string"},
                                           "items": {"type": "array", "minItems": 1, "items": {"type": "object", "properties": {"id": {"type": "string"}, "why": {"type": "string", "enum": ["x", "y"]}}, "required": ["id"]}}},
          "required": ["verdict", "items"]}


class Codex(unittest.TestCase):
    def call(self, mode="ok", schema=SCHEMA, model=None, effort="high", cfg=None):
        log = TMP / f"fake-{time.time_ns()}.jsonl"
        keep_path, keep_file = os.environ.get("PATH", ""), ca.PROVIDERS_FILE
        os.environ.update({"PATH": f"{FAKE.parent}:{keep_path}", "FAKE_LOG": str(log), "FAKE_MODE": mode})
        ca.PROVIDERS_FILE = TMP / f"providers-{time.time_ns()}.json"
        if cfg is not None:
            ca.PROVIDERS_FILE.write_text(json.dumps({"codex": cfg}))
        try:
            out = ca.run_agent("codex", model, effort, "do the thing", schema, TMP, 30)
        finally:
            os.environ["PATH"] = keep_path; ca.PROVIDERS_FILE = keep_file
        return out, lines(log) if log.exists() else []

    def test_the_command_is_the_documented_headless_one(self):
        out, calls = self.call()
        a = calls[0]
        self.assertEqual(a[0], "exec")
        for flag in ("--sandbox", "--skip-git-repo-check", "--ephemeral", "--json", "-o", "--output-schema"):
            self.assertIn(flag, a)
        self.assertEqual(a[a.index("--sandbox") + 1], "workspace-write"); self.assertIn('model_reasoning_effort="high"', a); self.assertIn("sandbox_workspace_write.network_access=true", a)
        self.assertNotIn("-m", a)                      # no model named: the CLI's own default
        self.assertIn("features.code_mode=true", a)    # Codex's code mode is asked for unless the user turns it off
        self.assertEqual(a[-1], "do the thing")

    def test_the_reply_format_is_sent_strict_and_the_reply_is_read_back_into_the_original_one(self):
        out, calls = self.call()
        a = calls[0]
        self.assertTrue(out["ok"], out)
        self.assertEqual({k: v for k, v in out["result"].items() if k != "_ck"}, {"verdict": "ok", "items": [{"id": "a"}]})      # nulls for optional fields are dropped again
        self.assertEqual(out["usage"]["in"], 1200); self.assertEqual(out["usage"]["out"], 30)

    def test_strict_form(self):
        s = ca.strict_schema(SCHEMA)
        self.assertEqual(s["required"], ["verdict", "note", "items"]); self.assertIs(s["additionalProperties"], False)
        self.assertEqual(s["properties"]["note"]["type"], ["string", "null"]); self.assertEqual(s["properties"]["verdict"]["type"], "string")
        it = s["properties"]["items"]
        self.assertNotIn("minItems", it); self.assertIs(it["items"]["additionalProperties"], False); self.assertEqual(it["items"]["properties"]["why"]["enum"], ["x", "y", None])
        self.assertEqual(ca.validate({"verdict": "ok", "items": []}, SCHEMA), ["$.items: needs at least 1 item(s)"])     # limits are still checked here

    def test_a_refused_reply_format_is_tried_once_more_in_the_prompt(self):
        out, calls = self.call("refuse-schema")
        self.assertTrue(out["ok"], out); self.assertEqual(len(calls), 2)
        self.assertIn("--output-schema", calls[0]); self.assertNotIn("--output-schema", calls[1]); self.assertIn("FINAL ANSWER FORMAT", calls[1][-1])

    def test_a_usage_limit_is_named_as_one(self):
        out, calls = self.call("limit")
        self.assertFalse(out["ok"]); self.assertEqual(out["kind"], "limit"); self.assertIn("usage limit", out["error"]); self.assertEqual(len(calls), 1)

    def test_role_names_of_the_routing_table_are_not_passed_to_codex_as_models(self):
        _, calls = self.call(model="opus")
        self.assertNotIn("-m", calls[0])
        _, calls = self.call(model="opus", effort="xhigh", cfg={"model": "base-model", "models": {"opus": "big-model"}, "effort": {"xhigh": "high"}, "network": False, "code_mode": False, "args": ["--color", "never"]})
        a = calls[0]
        self.assertEqual(a[a.index("-m") + 1], "big-model"); self.assertIn('model_reasoning_effort="high"', a); self.assertNotIn("sandbox_workspace_write.network_access=true", a); self.assertEqual(a[-3:-1], ["--color", "never"])
        _, calls = self.call(model="sonnet", cfg={"model": "base-model", "models": {"opus": "big-model"}})
        self.assertEqual(calls[0][calls[0].index("-m") + 1], "base-model")
        _, calls = self.call(model="some-codex-model")
        self.assertEqual(calls[0][calls[0].index("-m") + 1], "some-codex-model")

    def test_an_agent_that_fails_with_code_mode_is_run_once_more_without_it(self):
        out, calls = self.call("code-mode-breaks")
        self.assertTrue(out["ok"], out); self.assertEqual(len(calls), 2); self.assertEqual(out["code_mode"], "failed with it, ran without")
        self.assertIn("features.code_mode=true", calls[0]); self.assertNotIn("features.code_mode=true", calls[1]); self.assertIn("--output-schema", calls[1])
        out, calls = self.call("limit")                 # a usage limit is not a reason to try again
        self.assertEqual(len(calls), 1)
        _, calls = self.call(cfg={"code_mode": False})
        self.assertNotIn("features.code_mode=true", calls[0])

    def test_headless_claude_is_never_asked_for_code_mode(self):
        import inspect
        self.assertIn('"CLAUDE_CODE_EXPERIMENTAL_CODE_MODE")}', inspect.getsource(ca.run_claude))

    def test_plain_text_reply(self):
        out, _ = self.call(schema=None)
        self.assertEqual(out["result"], "plain words")

    def test_claude_without_a_model_uses_the_clis_default(self):
        import inspect
        self.assertIn('if model:', inspect.getsource(ca.run_claude))


class Install(unittest.TestCase):
    def test_the_codex_front_desk_is_installed_with_the_frameworks_path(self):
        env = {**os.environ, "CRUCIBLE_CODEX_SKILLS": str(TMP / "skills")}
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / "crucible_run.py"), "install", "--host", "codex"], capture_output=True, text=True, env=env)
        self.assertEqual(r.returncode, 0, r.stderr)
        text = (TMP / "skills" / "crucible" / "SKILL.md").read_text()
        self.assertTrue(text.startswith("---\nname: crucible\n")); self.assertNotIn("{{CRUCIBLE_DIR}}", text); self.assertIn(str(ROOT.resolve()), text)


if __name__ == "__main__":
    unittest.main(verbosity=1)
