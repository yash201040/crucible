#!/usr/bin/env python3
"""Tests of helper sessions (scripts/crucible_helper.py): counted, capped, recorded and always closed. No model: the
`claude` command is replaced by tests/fake_claude.py.
    python3 tests/test_helper.py"""
import json, os, signal, subprocess, sys, tempfile, time, unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import crucible_helper as h       # noqa: E402

HELPER = str(REPO / "scripts" / "crucible_helper.py")
FAKE = str(REPO / "tests" / "fake_claude.py")
LONG = "This task is long enough to be accepted as a real handoff to a helper. "


def alive(pid):
    try:
        os.kill(int(pid), 0); return True
    except Exception:
        return False


class Base(unittest.TestCase):
    cfg = {}

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.run_dir = Path(self.tmp.name).resolve() / "run"
        (self.run_dir / "helpers").mkdir(parents=True)
        os.chmod(FAKE, 0o755)
        (self.run_dir / "helpers" / "config.json").write_text(json.dumps({"claude": FAKE, "allow": 5, "depth_max": 2, **self.cfg}))
        self.env = {**{k: v for k, v in os.environ.items() if not k.startswith("CRUCIBLE_HELPER_")}, "CRUCIBLE_HELPER_ANCHOR": "0",
                    "CRUCIBLE_HELPER_PROJECTS": str(Path(self.tmp.name) / "projects")}

    def tearDown(self):
        h.reap(self.run_dir, "test over")
        self.tmp.cleanup()

    def task(self, text, name="t.md"):
        p = Path(self.tmp.name) / name
        p.write_text(LONG + text)
        return str(p)

    def call(self, *args, env=None, timeout=60):
        return subprocess.run([sys.executable, HELPER, *args], capture_output=True, text=True, env=env or self.env, timeout=timeout)

    def start(self, text, owner="solver:s1:r1", *extra, env=None):
        r = self.call("start", "--run", str(self.run_dir), "--owner", owner, "--task-file", self.task(text), *extra, env=env)
        return (r.stdout.split()[1] if r.returncode == 0 else None), r

    def rec(self, hid):
        return h.record(self.run_dir, hid)

    def until(self, cond, seconds=20):
        end = time.time() + seconds
        while time.time() < end:
            if cond():
                return True
            time.sleep(0.1)
        return False


class Handoff(Base):
    def test_a_helper_runs_and_its_handoff_comes_back_with_its_cost(self):
        r = self.call("run", "--run", str(self.run_dir), "--owner", "solver:s1:r1", "--task-file", self.task("FAKE:ok"), "--model", "haiku", "--effort", "low")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("helper h001: done (haiku@low", r.stdout)
        self.assertIn("1. Answer: done.", r.stdout)
        self.assertIn("unverified material", r.stdout)
        rec = self.rec("h001")
        self.assertEqual((rec["status"], rec["owner"], rec["depth"], rec["parent"], rec["collected"]), ("done", "solver:s1:r1", 1, None, True))
        self.assertAlmostEqual(rec["cost_usd"], 1.42)
        self.assertAlmostEqual(rec["eq"], 0.1, places=3)                      # 1.42 USD against 14.2 for an average agent
        self.assertEqual(rec["usage"]["claude-haiku-5-5"]["read"], 200000)
        d = self.run_dir / "helpers" / "h001"
        self.assertTrue(all((d / f).exists() for f in ("task.md", "prompt.md", "result.md", "record.json")))
        self.assertIn("FAKE:ok", (d / "task.md").read_text())

    def test_the_session_is_started_headless_without_the_tools_that_start_agents(self):
        self.call("run", "--run", str(self.run_dir), "--owner", "solver:s1:r1", "--task-file", self.task("FAKE:ok"))
        got = json.loads((self.run_dir / "helpers" / "h001" / "fake-argv.json").read_text())
        a = got["argv"]
        self.assertEqual(a[a.index("--disallowedTools") + 1], "Agent,Workflow")
        self.assertIn("-p", a)
        self.assertEqual(a[a.index("--effort") + 1], "medium")
        self.assertNotIn("CLAUDECODE", got["env"])
        self.assertEqual(got["env"]["CRUCIBLE_HELPER_ID"], "h001")
        self.assertNotIn("--permission-mode", a)

    def test_a_started_helper_is_collected_later_and_unread_ones_are_counted(self):
        a, _ = self.start("FAKE:ok")
        b, _ = self.start("FAKE:ok")
        self.assertTrue(self.until(lambda: self.rec(b)["status"] == "done"))
        self.assertEqual(h.summary(self.run_dir)["unread"], 2)
        r = self.call("wait", a, "--run", str(self.run_dir))
        self.assertIn(f"helper {a}: done", r.stdout)
        self.assertEqual(h.summary(self.run_dir)["unread"], 1)
        r = self.call("close", "--run", str(self.run_dir), "--owner", "solver:s1:r1")
        self.assertIn(f"You never read the handoff of {b}", r.stdout)

    def test_waiting_gives_up_politely_while_the_helper_goes_on(self):
        a, _ = self.start("FAKE:sleep=4")
        r = self.call("wait", a, "--run", str(self.run_dir), "--wait-minutes", "0.01")
        self.assertIn("still", r.stdout)
        r = self.call("wait", a, "--run", str(self.run_dir), "--wait-minutes", "1")
        self.assertIn(f"helper {a}: done", r.stdout)


class Refusals(Base):
    cfg = {"per_owner": 2}

    def refused(self, r, code):
        self.assertEqual(r.returncode, 3, r.stdout)
        self.assertIn(f"helper refused ({code})", r.stdout)
        self.assertIn("Do this work yourself", r.stdout)

    def test_only_the_solving_side_may_own_a_helper(self):
        for owner in ("critic:s1:r1", "debunk:s1:0", "referee:s1", ""):
            self.refused(self.start("FAKE:ok", owner)[1], "role")
        self.assertEqual(h.summary(self.run_dir)["refused_by"], {"role": 4})

    def test_a_thin_task_a_wrong_model_and_effort_max_are_refused(self):
        p = Path(self.tmp.name) / "thin.md"; p.write_text("look around")
        self.refused(self.call("start", "--run", str(self.run_dir), "--owner", "solver:a:r1", "--task-file", str(p)), "task")
        self.refused(self.start("FAKE:ok", "solver:a:r1", "--model", "fable")[1], "model")
        self.refused(self.start("FAKE:ok", "solver:a:r1", "--effort", "max")[1], "effort")
        self.refused(self.start("FAKE:ok", "solver:a:r1", "--effort", "xhigh")[1], "effort")

    def test_one_owner_gets_only_so_many(self):
        self.assertTrue(self.start("FAKE:ok")[0]); self.assertTrue(self.start("FAKE:ok")[0])
        self.refused(self.start("FAKE:ok")[1], "count")
        self.assertTrue(self.start("FAKE:ok", "solver:s2:r1")[0])              # another agent has its own count

    def test_the_allowance_of_the_run_holds(self):
        (self.run_dir / "helpers" / "config.json").write_text(json.dumps({"claude": FAKE, "allow": 0.25, "per_owner": 9}))
        a, _ = self.start("FAKE:usd=2.84")                                      # 0.2 of an average agent
        self.assertTrue(self.until(lambda: self.rec(a)["status"] == "done"))
        self.refused(self.start("FAKE:ok")[1], "allowance")                     # 0.2 used + 0.1 held would pass 0.25
        s = h.summary(self.run_dir)
        self.assertEqual((s["weighted_agents"], s["allowance"], s["allowance_used"]), (0.2, 0.25, 0.8))

    def test_what_is_held_for_helpers_still_working_counts(self):
        (self.run_dir / "helpers" / "config.json").write_text(json.dumps({"claude": FAKE, "allow": 0.25, "per_owner": 9}))
        self.assertTrue(self.start("FAKE:sleep=5")[0]); self.assertTrue(self.start("FAKE:sleep=5")[0])
        self.refused(self.start("FAKE:ok")[1], "allowance")

    def test_the_figures_of_the_engine_set_the_limits_and_the_allowance_only_grows(self):
        os.remove(self.run_dir / "helpers" / "config.json")
        env = {**self.env, "PATH": f"{Path(self.tmp.name)}:{self.env['PATH']}"}
        os.symlink(FAKE, Path(self.tmp.name) / "claude")
        self.assertTrue(self.start("FAKE:ok", "solver:s1:r1", "--allow", "3.5", "--depth-max", "3", env=env)[0])
        self.assertTrue(self.start("FAKE:ok", "solver:s1:r1", "--allow", "1", "--depth-max", "3", env=env)[0])
        c = json.loads((self.run_dir / "helpers" / "config.json").read_text())
        self.assertEqual((c["allow"], c["depth_max"]), (3.5, 3))


class Nesting(Base):
    def test_a_helper_starts_a_helper_and_both_are_recorded_under_the_same_owner(self):
        r = self.call("run", "--run", str(self.run_dir), "--owner", "solver:s1:r1", "--task-file", self.task("FAKE:nest=FAKE:ok"))
        self.assertIn("NESTED:", r.stdout)
        self.assertIn("helper h002: done", r.stdout)
        a, b = self.rec("h001"), self.rec("h002")
        self.assertEqual((a["depth"], b["depth"], b["parent"], b["owner"]), (1, 2, "h001", "solver:s1:r1"))
        self.assertLessEqual(b["deadline"], a["deadline"])                      # it cannot outlive the one that started it
        s = h.summary(self.run_dir)
        self.assertEqual((s["count"], s["max_depth"], s["by_depth"]), (2, 2, {"1": 1, "2": 1}))
        self.assertAlmostEqual(s["weighted_agents"], 0.2)

    def test_the_last_level_is_told_to_work_alone_and_is_refused_if_it_tries(self):
        r = self.call("run", "--run", str(self.run_dir), "--owner", "solver:s1:r1", "--task-file", self.task("FAKE:nest=FAKE:nest=FAKE:ok"))
        self.assertIn("helper h002: done", r.stdout)
        self.assertIn("I was told to do all of the work myself", (self.run_dir / "helpers" / "h002" / "result.md").read_text())
        self.assertIn("Do all of the work yourself.", (self.run_dir / "helpers" / "h002" / "prompt.md").read_text())
        env = {**self.env, "CRUCIBLE_HELPER_ID": "h002", "CRUCIBLE_HELPER_RUN": str(self.run_dir), "CRUCIBLE_HELPER_DEPTH": "2", "CRUCIBLE_HELPER_OWNER": "solver:s1:r1"}
        r = self.call("run", "--task-file", self.task("FAKE:ok"), env=env)
        self.assertEqual(r.returncode, 3); self.assertIn("helper refused (depth)", r.stdout)

    def test_the_depth_is_the_runs_to_set(self):
        (self.run_dir / "helpers" / "config.json").write_text(json.dumps({"claude": FAKE, "allow": 5, "depth_max": 4}))
        r = self.call("run", "--run", str(self.run_dir), "--owner", "solver:s1:r1", "--task-file", self.task("FAKE:nest=FAKE:nest=FAKE:nest=FAKE:ok"))
        self.assertEqual(h.summary(self.run_dir)["by_depth"], {"1": 1, "2": 1, "3": 1, "4": 1}, r.stdout)


class WorkingAtOnce(Base):
    cfg = {"slots": 2, "per_owner": 9}

    def test_no_more_than_the_slots_of_a_level_work_at_once(self):
        ids = [self.start("FAKE:sleep=2")[0] for _ in range(5)]
        peak, end = 0, time.time() + 30
        while time.time() < end and any(self.rec(i)["status"] in h.LIVE for i in ids):
            peak = max(peak, sum(1 for i in ids if self.rec(i)["status"] == "running"))
            time.sleep(0.05)
        self.assertEqual(peak, 2)
        self.assertTrue(all(self.rec(i)["status"] == "done" for i in ids))


class Closing(Base):
    cfg = {"per_owner": 9}

    def test_a_helper_past_its_time_is_ended_and_its_notes_are_handed_over(self):
        a, _ = self.start("FAKE:notes", "solver:s1:r1", "--minutes", "0.05")
        r = self.call("wait", a, "--run", str(self.run_dir), "--wait-minutes", "1")
        self.assertIn(f"helper {a}: timed_out", r.stdout)
        self.assertIn("notes.md", r.stdout); self.assertIn("Do not start the same task again", r.stdout)
        self.assertIsNone(self.rec(a)["pid"])

    def test_closing_ends_the_session_and_everything_it_started(self):
        a, _ = self.start("FAKE:child")
        pidfile = self.run_dir / "helpers" / a / "child.pid"
        self.assertTrue(self.until(pidfile.exists))
        child, session = int(pidfile.read_text()), self.rec(a)["pid"]
        self.assertTrue(alive(child) and alive(session))
        r = self.call("close", "--run", str(self.run_dir), "--owner", "solver:s1:r1")
        self.assertIn("1 still running, now stopped", r.stdout)
        self.assertEqual(self.rec(a)["status"], "stopped")
        self.assertTrue(self.until(lambda: not alive(child) and not alive(session), 10))

    def test_a_stopped_run_ends_every_helper_and_starts_no_more_until_it_is_opened_again(self):
        ids = [self.start("FAKE:sleep=60", f"solver:s{i}:r1")[0] for i in range(3)]
        self.assertTrue(self.until(lambda: all(self.rec(i)["status"] == "running" for i in ids)))
        pids = [self.rec(i)["pid"] for i in ids]
        self.assertEqual(json.loads(self.call("reap", str(self.run_dir), "--why", "the user stopped the run").stdout)["stopped"], 3)
        self.assertTrue(all(self.rec(i)["status"] == "stopped" for i in ids))
        self.assertTrue(self.until(lambda: not any(alive(p) for p in pids), 10))
        self.assertEqual(h.summary(self.run_dir)["still_alive"], 0)
        _, r = self.start("FAKE:ok"); self.assertIn("helper refused (stopped)", r.stdout)
        self.assertIn("cmd", json.loads(self.call("open", str(self.run_dir)).stdout))
        self.assertTrue(self.start("FAKE:ok")[0])

    def test_when_the_session_that_asked_is_gone_the_helper_is_ended(self):
        owner = subprocess.Popen(["sleep", "600"])
        a, _ = self.start("FAKE:sleep=60", env={**self.env, "CRUCIBLE_HELPER_ANCHOR": str(owner.pid)})
        self.assertTrue(self.until(lambda: self.rec(a)["status"] == "running"))
        owner.kill(); owner.wait()
        self.assertTrue(self.until(lambda: self.rec(a)["status"] == "orphaned"))

    def test_stopping_a_helper_stops_the_one_it_started(self):
        a, _ = self.start("FAKE:nest=FAKE:sleep=60")
        self.assertTrue(self.until(lambda: (self.rec("h002") or {}).get("status") == "running"))
        self.call("close", "--run", str(self.run_dir), "--owner", "solver:s1:r1")
        self.assertEqual((self.rec("h001")["status"], self.rec("h002")["status"]), ("stopped", "stopped"))

    def test_a_helper_whose_supervisor_died_is_found_and_ended(self):
        a, _ = self.start("FAKE:sleep=60")
        self.assertTrue(self.until(lambda: self.rec(a)["status"] == "running"))
        rec = self.rec(a)
        os.kill(rec["sup_pid"], signal.SIGKILL)
        self.assertTrue(self.until(lambda: not alive(rec["sup_pid"])))
        time.sleep(3.2)
        json.loads(self.call("status", str(self.run_dir)).stdout)
        self.assertEqual(self.rec(a)["status"], "orphaned")
        self.assertTrue(self.until(lambda: not alive(rec["pid"]), 10))


class Failures(Base):
    cfg = {"per_owner": 9}

    def test_a_failed_session_is_reported_and_charged_what_it_used(self):
        r = self.call("run", "--run", str(self.run_dir), "--owner", "solver:s1:r1", "--task-file", self.task("FAKE:fail"))
        self.assertIn("helper h001: failed", r.stdout); self.assertIn("something broke", r.stdout)
        r = self.call("run", "--run", str(self.run_dir), "--owner", "solver:s1:r1", "--task-file", self.task("FAKE:turns"))
        self.assertIn("helper h002: out_of_turns", r.stdout)
        self.assertAlmostEqual(self.rec("h002")["eq"], 0.1, places=3)

    def test_after_a_usage_limit_no_helper_starts_for_a_while(self):
        r = self.call("run", "--run", str(self.run_dir), "--owner", "solver:s1:r1", "--task-file", self.task("FAKE:limit"))
        self.assertIn("helper h001: limit", r.stdout)
        _, r = self.start("FAKE:ok"); self.assertIn("helper refused (limit)", r.stdout)

    def test_a_killed_session_is_charged_from_its_transcript(self):
        a, _ = self.start("FAKE:sleep=60", "solver:s1:r1", "--model", "sonnet")
        self.assertTrue(self.until(lambda: self.rec(a)["status"] == "running"))
        t = Path(self.tmp.name) / "projects" / "some-folder"; t.mkdir(parents=True)
        line = {"type": "assistant", "message": {"id": "m1", "model": "claude-sonnet-5-5", "usage": {"input_tokens": 0, "output_tokens": 20000, "cache_read_input_tokens": 4000000, "cache_creation_input_tokens": 400000}}}
        (t / f"{self.rec(a)['session']}.jsonl").write_text(json.dumps(line) + "\n" + json.dumps(line) + "\n")   # the same message twice counts once
        self.call("close", "--run", str(self.run_dir), "--owner", "solver:s1:r1")
        rec = self.rec(a)
        self.assertEqual(rec["status"], "stopped")
        self.assertAlmostEqual(rec["cost_usd"], (100000 + 400000 + 500000) / 1e6 * 3.1, places=3)
        self.assertTrue(rec["transcript"].endswith(".jsonl"))


class InTheRun(Base):
    """The run's own bookkeeping (scripts/crucible_run.py) opens, closes and counts helpers."""
    cfg = {"per_owner": 9}

    def run_py(self, *args, env=None):
        return subprocess.run([sys.executable, str(REPO / "scripts" / "crucible_run.py"), *args], capture_output=True, text=True, env=env or self.env, timeout=120)

    def test_staging_a_launch_passes_the_launcher_and_lifts_an_earlier_stop(self):
        bindir = Path(self.tmp.name) / "bin"; bindir.mkdir(); os.symlink(FAKE, bindir / "claude")
        env = {**self.env, "PATH": f"{bindir}:{self.env['PATH']}"}
        os.remove(self.run_dir / "helpers" / "config.json")
        h.reap(self.run_dir, "an earlier stop")
        self.assertTrue((self.run_dir / "helpers" / "STOP").exists())
        out = json.loads(self.run_py("stage", str(self.run_dir), env=env).stdout)
        self.assertTrue(out["helpers"]["cmd"].endswith("crucible_helper.py"))
        self.assertNotIn("depthMax", out["helpers"])
        self.assertFalse((self.run_dir / "helpers" / "STOP").exists())
        self.assertEqual(json.loads(self.run_py("stage", str(self.run_dir), "--helper-depth", "4", env=env).stdout)["helpers"]["depthMax"], 4)
        self.assertNotIn("helpers", json.loads(self.run_py("stage", str(self.run_dir), "--no-helpers", env=env).stdout))
        self.assertNotIn("helpers", json.loads(self.run_py("stage", str(self.run_dir), "crucible-evolve.js", env=env).stdout))

    def test_a_machine_without_the_command_gets_no_helpers(self):
        os.remove(self.run_dir / "helpers" / "config.json")
        env = {**self.env, "PATH": "/usr/bin:/bin"}
        out = json.loads(subprocess.run([sys.executable, str(REPO / "scripts" / "crucible_run.py"), "stage", str(self.run_dir)], capture_output=True, text=True, env=env).stdout)
        self.assertNotIn("helpers", out)

    def test_the_checkpoint_of_a_stopped_run_ends_its_helpers(self):
        a, _ = self.start("FAKE:sleep=60")
        self.assertTrue(self.until(lambda: self.rec(a)["status"] == "running"))
        pid = self.rec(a)["pid"]
        r = self.run_py("checkpoint", str(self.run_dir))
        self.assertIn("helper sessions stopped: 1", r.stdout, r.stdout + r.stderr)
        self.assertEqual(self.rec(a)["status"], "stopped")
        self.assertTrue(self.until(lambda: not alive(pid), 10))

    def test_the_efficiency_log_and_the_digest_count_them(self):
        import crucible_run as cr, crucible_review as rv
        self.call("run", "--run", str(self.run_dir), "--owner", "solver:s1:r1", "--task-file", self.task("FAKE:nest=FAKE:ok"))
        self.start("FAKE:ok", "critic:s1:r1")
        hs = h.summary(self.run_dir)
        self.assertEqual((hs["count"], hs["max_depth"], hs["refused"], hs["unread"], hs["still_alive"], hs["done_share"]), (2, 2, 1, 0, 0, 1.0))
        d = {"name": "x", "run": "r", "helpers": {**hs, "share_of_agents": 0.02}}
        md = rv.digest_md(d)
        self.assertIn("## Helpers", md); self.assertIn("2 helper session(s) under 1 solver(s), deepest level 2", md)
        self.assertIn("none started", rv.digest_md({"name": "x", "run": "r"}))
        self.assertEqual((rv.METRICS["helpers.done_share"](d), rv.METRICS["helpers.unread"](d), rv.METRICS["helpers.still_alive"](d)), (1.0, 0, 0))
        self.assertIsNone(rv.METRICS["helpers.done_share"]({}))
        self.assertIn("crucible_helper", cr.build_efficiency.__code__.co_names + cr.save.__code__.co_names)


if __name__ == "__main__":
    unittest.main(verbosity=1)
