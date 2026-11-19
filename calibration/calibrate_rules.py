#!/usr/bin/env python3
"""calibrate_rules.py: test the engine's own prompts on small cases with a known right answer.

  python3 calibrate_rules.py --out <dir> [--engine <engine.js>[,<older-engine.js>]] [--only attacker,contract,referee,planner]
                             [--cases b1-extra-mutant,...] [--routes sonnet@high,opus@high] [--provider claude|codex] [--jobs 4] [--timeout 900]

calibrate.py asks "which model can fill a role". This file asks "does the prompt make a model follow the rule", for the
rules added in v5.1 after the first real v5.0 run:
  attacker   one more mutant beyond the contract's list must not send correct work back (b1); a real defect that no
             listed test catches must still block (b2); a listed check that fails for a cause in another part must be
             passed to its owner, not block (b3); a contract clause over an open set ("every mutant the checker
             writes") is read as its listed instances, so correct work is not sent back for one more mutant (b4)
  contract   the contract writer must use closed thresholds, also for a part that invites "cannot be evaded" (sandbox)
  referee    one more instance of a sampled class is a caveat; a real defect is upheld
  planner    a small build is planned with owners, a skeleton, an early end-to-end proof and a chosen critical set
Each prompt is rendered by the engine itself (render_prompt.mjs), so what is tested is what a run would send. Pass two
engines to compare versions on the same cases. Runs are real agents on the Claude subscription: about 20 small ones.
"""
import hashlib, json, re, shutil, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "scripts"))
import crucible_agent as agent  # noqa: E402

SLUG_GOOD = '''import re
import unicodedata


def slugify(text):
    """Lower-case slug: ASCII letters and digits are kept, a letter with a combining accent loses the accent, every run
    of other characters becomes one hyphen, and the result has no leading or trailing hyphen."""
    t = unicodedata.normalize("NFD", text.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")
'''
SLUG_BUG = SLUG_GOOD.replace('r"[^a-z0-9]+"', 'r"[^a-z0-9_]+"')   # keeps underscores: wrong under the statement, caught by no listed test
TESTS = '''import unittest
from slugify import slugify


class T(unittest.TestCase):
    def test_words(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_trim(self):
        self.assertEqual(slugify("  Trim me  "), "trim-me")

    def test_accents(self):
        self.assertEqual(slugify("Crème Brûlée"), "creme-brulee")

    def test_digits(self):
        self.assertEqual(slugify("Version 2 beta"), "version-2-beta")

    def test_empty(self):
        self.assertEqual(slugify(""), "")


if __name__ == "__main__":
    unittest.main()
'''
MUTANTS = '''#!/usr/bin/env python3
"""Contract check T2: each listed mutant of slugify.py must make the suite fail.  usage: mutants.py <artifacts dir>"""
import pathlib, shutil, subprocess, sys, tempfile
src = pathlib.Path(sys.argv[1])
M = {"M1 no lower-casing": (".lower()", ""), "M2 no trimming of hyphens": ('.strip("-")', ""), "M3 no accent folding": ("if not unicodedata.combining(c)", "if True")}
bad = 0
for name, (a, b) in M.items():
    d = pathlib.Path(tempfile.mkdtemp())
    for f in src.glob("*.py"):
        shutil.copy(f, d / f.name)
    code = (d / "slugify.py").read_text()
    if a not in code:
        print(f"{name}: cannot be applied (the code has no {a!r})"); bad += 1; continue
    (d / "slugify.py").write_text(code.replace(a, b, 1))
    r = subprocess.run([sys.executable, "-m", "unittest", "test_slugify"], cwd=d, capture_output=True, text=True)
    print(f"{name}: {'killed' if r.returncode else 'SURVIVED'}"); bad += 0 if r.returncode else 1
sys.exit(1 if bad else 0)
'''
EXPORT = '''import json
from slugify import slugify


def export_slugs(titles, path):
    """Write the catalog's slug records: one {"title", "slug"} object per title."""
    with open(path, "w") as fh:
        json.dump([{"title": t, "slug": slugify(t)} for t in titles], fh)
'''
CHECK_EXPORT = '''#!/usr/bin/env python3
"""Contract check T3: the records export_slugs() writes load with the catalog's own loader.  usage: check_export.py <artifacts dir>"""
import sys, tempfile, pathlib
sys.path.insert(0, sys.argv[1])
from export import export_slugs
from catalog.records import load   # the catalog part's loader
p = pathlib.Path(tempfile.mkdtemp()) / "slugs.json"
export_slugs(["Hello World"], p)
assert load(p)[0].slug == "hello-world"
'''
STATEMENT = ("Implement slugify(text) in slugify.py. The text is lower-cased and letters with a combining accent lose it (é becomes e, ü becomes u, "
             "ç becomes c; canonical decomposition, NFD). Then ASCII letters and digits are kept, and every run of other characters becomes a "
             "single hyphen: spaces, punctuation, underscores, symbols, and any character that is still not an ASCII letter or digit (ß, ø, "
             "non-ASCII punctuation, letters of other scripts). The result has no leading or trailing hyphen. Empty input, or input with no "
             "ASCII letter or digit after these steps, gives the empty string.")


def scope(i, title, statement, owns, critical=False, deps=(), difficulty="moderate", criterion="The behaviour matches the statement for every input it covers, and the contract's tests pass."):
    return {"id": i, "title": title, "statement": statement, "in_scope": "this module and its tests", "out_of_scope": "everything the other scope owns",
            "success_criterion": criterion, "verification_oracles": ["the unit tests", "independent checks of the stated behaviour"], "domain_checks": ["boundary inputs", "tests that do not test the claim"],
            "debunk_lenses": ["counterexample hunt"], "starting_angle": "the direct implementation", "depends_on": list(deps), "priority": 1, "difficulty": difficulty, "owns": owns, "critical": critical}


def plan(scopes, items):
    return {"problem_restatement": "A small catalog tool needs URL slugs for its titles and a record format for its entries.", "deliverable": "the two modules with tests",
            "complexity_tier": "M", "strategy": "exhaustive", "strategy_rationale": "both parts are needed", "horizon": "single_pass",
            "success_definition": "titles get correct slugs and the catalog can load the records", "success_items": items, "scopes": scopes,
            "integration_notes": "the catalog loads what the slug module exports", "shared_data": [], "assumptions": [], "risks": []}


SLUG = scope("slug", "URL slugs for titles", STATEMENT, ["slugify.py and its tests", "the slug rules"], True)
CATALOG = scope("catalog", "Catalog records", "Define the catalog record format and its loader in catalog/records.py.", ["the catalog record format", "the loader catalog/records.py"], False)
PLAN = plan([SLUG, CATALOG], [{"id": "S1", "item": "every title gets a correct slug", "owner": "slug"}, {"id": "S2", "item": "the catalog loads exported records", "owner": "catalog"}])
SUB = {"status": "claim", "claim": "slugify.py implements the slug rules as stated; all 5 unit tests pass and the three listed mutants are killed.",
       "assertions": ["letters and digits are kept and lower-cased; accented letters lose their accents", "every run of other characters becomes one hyphen", "no leading or trailing hyphen; empty input gives the empty string", "the 5 tests pass and mutants M1, M2 and M3 are killed"],
       "provenance": "Implemented with unicodedata NFKD folding and one regular expression. Verified with python3 -m unittest test_slugify and the contract's mutants.py.",
       "evidence": [{"kind": "executed", "detail": "5 tests pass", "where": "artifacts/test_slugify.py"}, {"kind": "executed", "detail": "M1, M2, M3 killed", "where": "contract/mutants.py"}],
       "acceptance": [{"id": "T1", "result": "pass", "note": "5/5"}, {"id": "T2", "result": "pass", "note": "3/3 killed"}], "objection_responses": [], "avenues": [], "confidence": 0.9, "boundary_issues": [], "contract_disputes": []}


def contract(cdir, t3=False, open_clause=False):
    # open_clause: the wording that made two parts of a real run loop for ten rounds each: a threshold over a set nobody can finish
    t2 = ("exit code 0, and every mutant of slugify.py that the checker writes must also be killed by the suite" if open_clause
          else "exit code 0: mutants M1, M2 and M3 are each killed by the suite")
    tests = [{"id": "T1", "test": "python3 -m unittest test_slugify -v, run in the artifacts folder", "threshold": "all tests pass", "kind": "executable"},
             {"id": "T2", "test": f"python3 {cdir}/mutants.py <artifacts folder>", "threshold": t2, "kind": "executable"}]
    if t3:
        tests.append({"id": "T3", "test": f"python3 {cdir}/check_export.py <artifacts folder>", "threshold": "exit code 0: the records export_slugs() writes load with catalog.records.load", "kind": "executable"})
    return {"pinned_statement": STATEMENT, "acceptance_tests": tests, "negative_tests": ["a slugify that keeps upper case fails a test (M1)"],
            "forbidden_shortcuts": ["editing test_slugify.py to match the implementation", "special-casing the test inputs"],
            "open_classes": [] if open_clause else ["mutants of slugify.py: M1 (no lower-casing), M2 (no trimming of hyphens) and M3 (no accent folding) must be killed"], "outside_control": []}


M4 = {"id": "F1", "severity": "major", "blocks_acceptance": True, "status": "confirmed", "where": "contract T2 / test_slugify.py", "class": "listed_check",
      "issue": "When the + is removed from the regular expression (each character replaced on its own, so runs are not collapsed), all 5 tests still pass. The contract says mutants must be killed by the suite, and this one survives.",
      "evidence": "mutant M4: re.sub(r\"[^a-z0-9]\", \"-\", t) -> 5 tests pass, 0 fail", "failing_check": "apply M4 to a copy of slugify.py and run python3 -m unittest test_slugify: it passes, it should fail", "origin": "new"}
USC = {"id": "F2", "severity": "major", "blocks_acceptance": True, "status": "confirmed", "where": "slugify.py, the regular expression", "class": "behaviour",
       "issue": "When the text contains an underscore, slugify keeps it: slugify('a_b') returns 'a_b'. The statement says underscores are among the other characters that become a hyphen, so the result must be 'a-b'.",
       "evidence": "python3 -c \"from slugify import slugify; print(slugify('a_b'))\" prints a_b", "failing_check": "python3 -c \"from slugify import slugify; assert slugify('a_b') == 'a-b'\"", "origin": "new"}
CRITIC_2 = {"verdict": "major_issues", "attack_surfaces": ["A1", "A2", "A4"], "objections": [M4, USC], "checks_run": [{"check": "ran the tests and two probes", "kind": "ran", "executed": True, "independent_method": True, "result": "see findings"}],
            "integrity_ok": True, "integrity_violation": "", "exhaustion": {"accept": False, "untried_avenues": []}}

SANDBOX = scope("sandbox", "Confined command runner", "Implement run_confined(cmd, root) in confine.py for this machine (macOS, sandbox-exec is available). It runs cmd with root as the working directory so that the command cannot read any file outside root and cannot open a network connection. Reads and writes inside root, and the command's exit code and output, work as they do without confinement.",
                ["confine.py", "the confinement profile"], True, criterion="A command run through run_confined cannot read outside root or reach the network, and ordinary work inside root still succeeds.")
BUILD_PROBLEM = """Build "doclinks", a small tool for a team's documentation folder (a few hundred Markdown files in a git repository).
What it must do:
1. Scan the folder and find broken links: links to files or headings inside the folder that do not exist, and external links that return an error.
2. For a broken internal link, propose the most likely intended target (the file was renamed or the heading reworded).
3. Write the findings as a report: a JSON file for scripts and one HTML page for people, grouped by file, with the proposed fix next to each broken link.
4. Apply the proposed fixes on request, as a patch the user reviews before it is applied.
5. Run as a command line tool, and as a watch mode that re-checks changed files.
6. External link checks must be polite: cached for a day, rate-limited per host, and skippable offline.
The user's main point: the proposed fixes must be right. A wrong fix that is applied silently is worse than a broken link, so nothing is applied without review, and the tool must show how sure it is.
Done means: on the team's real folder, the tool finds the broken links, the proposals for renamed files and reworded headings are right in the cases checked by hand, and the report page opens and reads well.
There is no existing code. Python 3.12, standard library plus requests. Do not research the web for this; plan from the description."""
MINI_PLAN = plan([scope("all", "everything", "build it", ["everything"], True)], [])
from crucible_review import OPEN_SET  # noqa: E402  (the same pattern the engine uses)
UNBOUNDED = re.compile(r"\b(?:any|every|all|no|never|whatever|arbitrary)\b[^.|;]{0,60}\b(?:path|file|way|method|technique|means|input|command|form|variant|encoding|trick)s?\b", re.I)   # looser: wording to read by hand


def fingerprint(d: Path):
    """The engine's own fingerprint command (fpCmd), so the attacker's recomputation matches."""
    out = subprocess.run(f'find "{d}" -type f -print0 | sort -z | xargs -0 shasum -a 256 | shasum -a 256', shell=True, capture_output=True, text=True).stdout.strip()
    return out, sum(1 for f in d.rglob("*") if f.is_file())


def setup(run: Path, case):
    """Lay out a run directory the way the engine expects it and return the spec for render_prompt.mjs."""
    if run.exists():
        shutil.rmtree(run)
    run.mkdir(parents=True)
    kind, name = case["kind"], case["name"]
    spec = {"runDir": str(run), "problem": case.get("problem") or PLAN["problem_restatement"], "plan": PLAN}
    (run / "problem.md").write_text(spec["problem"] + "\n")
    if kind in ("attacker", "referee"):
        art, cdir = run / "scopes/slug/round-01/artifacts", run / "scopes/slug/contract"
        art.mkdir(parents=True); cdir.mkdir(parents=True)
        (art / "slugify.py").write_text(SLUG_BUG if case.get("bug") else SLUG_GOOD)
        (art / "test_slugify.py").write_text(TESTS)
        (cdir / "mutants.py").write_text(MUTANTS)
        sub = json.loads(json.dumps(SUB))
        if case.get("t3"):
            (art / "export.py").write_text(EXPORT)
            (cdir / "check_export.py").write_text(CHECK_EXPORT)
            sub["acceptance"].append({"id": "T3", "result": "not_run", "note": "catalog.records does not exist yet (the catalog part owns it), so the check cannot import it"})
            sub["boundary_issues"] = [{"kind": "missing_input", "blocks_correctness": False, "other_scopes": ["catalog"], "detail": "T3 needs catalog.records.load, which the catalog part has not delivered; a request is on the board"}]
            sub["assertions"].append("export_slugs() writes one {title, slug} record per title")
        if kind == "referee":   # the engine asks the referee about round 2's submission
            shutil.copytree(run / "scopes/slug/round-01", run / "scopes/slug/round-02")
        c = contract(str(cdir), case.get("t3"), case.get("open_clause"))
        c["frozen_dir"] = str(cdir); c["frozen_sha256"], c["frozen_files"] = fingerprint(cdir)
        spec.update({"contract": c, "submission": sub, "label": "critic:slug:r1" if kind == "attacker" else "referee:slug"})
        if kind == "referee":
            spec["critic"] = CRITIC_2
    elif kind == "contract":
        sc = SANDBOX if name.startswith("sandbox") else SLUG
        sc = {**sc, "difficulty": case.get("difficulty", "moderate")}
        spec.update({"plan": plan([sc, CATALOG], PLAN["success_items"]), "label": f"contract:{sc['id']}"})
    elif kind == "planner":
        spec.update({"plan": MINI_PLAN, "label": "planner", "problem": BUILD_PROBLEM})
    return spec


def render(engine, spec, run: Path):
    f = run / "spec.json"
    f.write_text(json.dumps(spec))
    out = subprocess.run(["node", str(HERE / "render_prompt.mjs"), str(engine), str(f)], capture_output=True, text=True)
    if out.returncode:
        raise RuntimeError(out.stderr.strip()[:400])
    return json.loads(out.stdout)


NEVER = ("test_strength", "out_of_part")


def score(case, r, new_rules):
    kind = case["kind"]
    if kind == "attacker":
        objs = [o for o in r.get("objections") or [] if str(o.get("evidence") or "").strip() and str(o.get("failing_check") or "").strip()]
        blk = lambda o: (not new_rules or o.get("class") not in NEVER) and (o.get("severity") == "fatal" or (o.get("severity") == "major" and o.get("blocks_acceptance") is not False))
        block = [o for o in objs if blk(o)]
        ex = sum(1 for c in r.get("checks_run") or [] if c.get("executed") and c.get("kind") != "inspected")
        integ = r.get("integrity_ok") is False
        accepted = not block and ex > 0 and not integ and r.get("verdict") != "refuted"
        text = lambda o: f"{o.get('issue')} {o.get('evidence')}".lower()
        usc = [o for o in objs if re.search(r"underscore|a_b|'_'|\"_\"|_\b", text(o))]
        mut = [o for o in objs if re.search(r"mutant|surviv|collaps|\bruns?\b|consecutive|repeated|test (?:suite|coverage)|not tested|no test", text(o))]
        oop = [o for o in objs if o.get("class") == "out_of_part" or re.search(r"catalog", text(o))]
        s = {"accepted": accepted, "blocking": len(block), "findings": len(objs), "executed": ex, "classes": sorted({str(o.get("class")) for o in objs}),
             "blocking_ids": [f"{o.get('id')}[{o.get('class')}]" for o in block],
             "marked_blocking_by_model": sum(1 for o in objs if o.get("severity") in ("fatal", "major") and o.get("blocks_acceptance") is not False)}
        if case["name"] in ("b1-extra-mutant", "b4-open-clause"):
            s.update({"right": accepted, "raised_test_gap": len(mut), "test_gap_classes": sorted({str(o.get("class")) for o in mut})})
        elif case["name"] == "b2-real-defect":
            s.update({"right": any(blk(o) for o in usc), "found_defect": bool(usc), "defect_class": sorted({str(o.get("class")) for o in usc})})
        else:
            s.update({"right": accepted and (bool(oop) or not new_rules), "raised_outside_cause": len(oop), "outside_classes": sorted({str(o.get("class")) for o in oop}), "owner_named": sorted({str(o.get("owner")) for o in oop if o.get("owner")})})
        return s
    if kind == "contract":
        tests = r.get("acceptance_tests") or []
        texts = [f"{t.get('id')}: {t.get('test')} [{t.get('threshold')}]" for t in tests] + [f"negative: {t}" for t in r.get("negative_tests") or []]
        hard = [t[:200] for t in texts if OPEN_SET.search(t)]
        return {"right": not hard, "tests": len(tests), "negative_tests": len(r.get("negative_tests") or []), "open_set_clauses": hard,
                "wording_to_read": [t[:200] for t in texts if UNBOUNDED.search(t) and not OPEN_SET.search(t)],
                "open_classes": r.get("open_classes"), "outside_control": r.get("outside_control"), "frozen_files": r.get("frozen_files")}
    if kind == "referee":
        rul = {x.get("id"): x for x in r.get("rulings") or []}
        f1, f2 = (rul.get("F1") or {}), (rul.get("F2") or {})
        return {"right": f1.get("ruling") in ("caveat", "rejected") and f2.get("ruling") == "upheld", "extra_mutant": f1.get("ruling"), "real_defect": f2.get("ruling"),
                "checks_executed": [f1.get("check_executed"), f2.get("check_executed")], "repairable": r.get("repairable")}
    if kind == "planner":
        ids = {s["id"] for s in r.get("scopes") or []}
        items = r.get("success_items") or []
        crit = [s["id"] for s in r.get("scopes") or [] if s.get("critical") is True]
        deps = {s["id"]: [d for d in s.get("depends_on") or [] if d in ids] for s in r.get("scopes") or []}
        return {"scopes": len(ids), "items": len(items), "items_with_valid_owner": sum(1 for it in items if it.get("owner") in ids), "scopes_with_owns": sum(1 for s in r.get("scopes") or [] if s.get("owns")),
                "critical": crit, "difficulties": sorted(s.get("difficulty") for s in r.get("scopes") or []), "depends": deps,
                "right": bool(items) and all(it.get("owner") in ids for it in items) and 0 < len(crit) * 2 <= len(ids) + 1 and all(s.get("owns") for s in r.get("scopes") or [])}
    return {}


CASES = [
    {"kind": "attacker", "name": "b1-extra-mutant"}, {"kind": "attacker", "name": "b2-real-defect", "bug": True}, {"kind": "attacker", "name": "b3-outside-cause", "t3": True},
    {"kind": "attacker", "name": "b4-open-clause", "open_clause": True},
    {"kind": "contract", "name": "slug-contract"}, {"kind": "contract", "name": "sandbox-contract"},
    {"kind": "referee", "name": "referee-mixed", "bug": True}, {"kind": "planner", "name": "planner-build"},
]


def labels_of(engines):
    """One label per engine: its version, or version-new / version-old when two engines carry the same version."""
    vs = [re.search(r"ENGINE_VERSION = '([^']+)'", Path(e).read_text()).group(1) for e in engines]
    return [v if vs.count(v) == 1 else f"{v}-{'new' if i == 0 else 'old' + (str(i) if i > 1 else '')}" for i, v in enumerate(vs)]


def prompt_sha(engine, case, work: Path):
    """What the engine would send for this case (prompt and reply format), as a hash. No model is called."""
    run = work / case["name"]
    p = render(engine, setup(run, case), run)   # the same folder for every engine, so only the engine can make a difference
    return hashlib.sha256(json.dumps([p["prompt"], p["schema"]], sort_keys=True).encode()).hexdigest()


def changed_cases(new, old, work: Path, only=None):
    """The cases whose prompt or reply format differs between two engines: the only ones worth running on both."""
    out = []
    for case in CASES:
        if only and case["name"] not in only:
            continue
        try:
            if prompt_sha(new, case, work) != prompt_sha(old, case, work):
                out.append(case["name"])
        except Exception:
            out.append(case["name"])   # an engine that cannot render the case is a difference
    return out


def run_cases(out: Path, engines, routes="", only=None, cases=None, timeout=900, jobs_n=4, provider="claude"):
    """Run the cases on each engine; returns the engines' labels. Results: <out>/summary.json."""
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    engines = [Path(e) for e in engines]
    only = set(only or ("attacker", "contract", "referee", "planner"))
    routes = [x for x in (routes or "").split(",") if x]
    labels = labels_of(engines)
    jobs = []
    for e, ver in zip(engines, labels):
        for case in CASES:
            if case["kind"] not in only or (cases and case["name"] not in cases):
                continue
            if case["kind"] == "planner" and "success_items" not in e.read_text():
                continue   # an engine from before v5.1 has no ownership rules to test
            for rt in (routes if case["kind"] in ("attacker", "contract") and routes else [None]):
                jobs.append((e, ver, case, rt))

    def one(job):
        e, ver, case, rt = job
        tag = f"{case['name']}--{ver}--{(rt or 'engine-route').replace('@', '-')}"
        run = out / tag
        done = run / "result.json"
        if done.exists():
            return json.loads(done.read_text())
        spec = setup(run, case)
        p = render(e, spec, run)
        model, effort = (rt.split("@") if rt else (p["model"] or ("sonnet" if provider == "claude" else ""), p["effort"] or "high"))   # "@high": the provider's default model
        (run / "prompt.txt").write_text(p["prompt"])
        t0 = time.time()
        res = agent.run_agent(provider, model or None, effort, p["prompt"], p["schema"], run, timeout, 60, lean=True)
        rec = {"case": case["name"], "kind": case["kind"], "engine": ver, "route": f"{model}@{effort}", "ok": bool(res.get("ok")), "seconds": round(time.time() - t0),
               "turns": res.get("turns"), "tokens_in": (res.get("usage") or {}).get("in"), "tokens_out": (res.get("usage") or {}).get("out"),   # what the prompt cost, to compare two engines
               "error": None if res.get("ok") else str(res.get("error"))[:300]}
        if res.get("ok") and isinstance(res.get("result"), dict):
            rec["score"] = score(case, res["result"], new_rules="class: {" in json.dumps(p["schema"]) or '"class"' in json.dumps(p["schema"]))
            (run / "returned.json").write_text(json.dumps(res["result"], indent=1))
        done.write_text(json.dumps(rec, indent=1))
        print(f"{tag}: {'ok' if rec['ok'] else 'FAILED'} in {rec['seconds']} s {json.dumps(rec.get('score') or rec['error'])[:300]}", file=sys.stderr, flush=True)
        return rec

    with ThreadPoolExecutor(max_workers=jobs_n) as ex:
        recs = list(ex.map(one, jobs))
    (out / "summary.json").write_text(json.dumps(recs, indent=1))
    print(f"{sum(1 for r in recs if (r.get('score') or {}).get('right'))} of {len(recs)} right; summary: {out / 'summary.json'}", file=sys.stderr)
    return labels


def main(argv):
    o = dict(zip(argv[::2], argv[1::2]))
    engines = (o.get("--engine") or str(HERE.parent / "engine" / "crucible-engine.js")).split(",")
    run_cases(o["--out"], engines, o.get("--routes") or "", (o.get("--only") or "attacker,contract,referee,planner").split(","),
              [c for c in (o.get("--cases") or "").split(",") if c] or None, int(o.get("--timeout", 900)), int(o.get("--jobs", 4)), o.get("--provider", "claude"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
