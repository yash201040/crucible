#!/usr/bin/env python3
"""Tests of the review pack (scripts/crucible_review.py) on made-up runs. No model is called and nothing outside a temp
folder is written.   python3 tests/test_review.py"""
import json, os, sys, tempfile, unittest
from pathlib import Path

TMP = Path(tempfile.mkdtemp(prefix="crucible-review-test-"))
os.environ["CRUCIBLE_REGISTRY"] = str(TMP / "state" / "registry.jsonl")
os.environ["CRUCIBLE_PROPOSALS"] = str(TMP / "state" / "proposals")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import crucible_run as cr          # noqa: E402
import crucible_review as rv       # noqa: E402

rv.engine_version = lambda: "v5.1"
rv.EXPECT = TMP / "expectations.json"


def obj(i, sev="major", cls=None, blocks=True):
    o = {"id": i, "severity": sev, "blocks_acceptance": blocks, "issue": "x", "evidence": "e", "failing_check": "f"}
    if cls:
        o["class"] = cls
    return o


def make_run(name, engine="v5.1", saved="2026-11-18T10:00:00", register=True, agents=4, session=True):
    rd = TMP / "runs" / name
    td = TMP / "projects" / "proj" / f"sess-{name}" / "subagents" / "workflows" / "wf_x"
    (rd / "board").mkdir(parents=True); td.mkdir(parents=True)
    labels = {"contract:p1": {"acceptance_tests": [{"id": "T1", "test": "run the suite", "threshold": "every mutant the checker writes must be killed"},
                                                    {"id": "T2", "test": "mutants", "threshold": "every mutant M1-M3 is killed"}], "negative_tests": ["a wrong sort fails"]},
              "solver:p1:r1": {"status": "claim", "claim": "c", "assertions": ["a"], "evidence": [{"kind": "executed"}]},
              "critic:p1:r1": {"verdict": "major_issues", "objections": [obj("o1", cls="behaviour"), obj("o2", cls="test_strength"), obj("o3", "minor", "evidence")]},
              "solver:p1:r2": {"status": "progress", "claim": "", "assertions": [], "evidence": []},
              "critic:p1:r2": {"verdict": "major_issues", "objections": [obj("o4", cls="behaviour"), obj("o5", cls="out_of_part")]}}
    lines = []
    for n, (label, result) in enumerate(list(labels.items())[:max(agents, 1)] if agents < 5 else labels.items()):
        lines += [json.dumps({"type": "started", "agentId": f"a{n}", "label": label, "phase": "Solve"}), json.dumps({"type": "result", "agentId": f"a{n}", "result": result})]
        (td / f"agent-a{n}.jsonl").write_text("\n".join(json.dumps({"type": "assistant", "timestamp": f"2026-11-18T0{4 + n}:0{k}:00Z", "message": {"id": f"m{n}{k}", "model": "claude-sonnet", "content": [],
                                              "usage": {"input_tokens": 1000, "cache_read_input_tokens": 400000 if label.startswith("solver") else 10, "output_tokens": 500}}}) for k in range(2)) + "\n")
    (td / "journal.jsonl").write_text("\n".join(lines) + "\n")
    res = {"runDir": str(rd), "engineVersion": engine, "depth": "standard", "routing": {"profile": "balanced"}, "budget": {"agents": 40, "estimate": 20, "ceiling": 24, "wrapped": True}, "skipped": ["proof"],
           "plan": {"scopes": [{"id": "p1", "critical": False}, {"id": "proof", "critical": True}]},
           "results": [{"id": "p1", "difficulty": "hard", "final": "flawed", "pairOutcome": "open", "rounds": 2, "route": "sonnet@high",
                        "roundLog": [{"round": 1, "attempt": "main", "blocking": 1}, {"round": 2, "attempt": "main", "blocking": 1}],
                        "boundaryIssues": [{"kind": "missing_input", "other": ["proof"], "detail": "d"}, {"kind": "coupled", "other": ["proof"], "detail": "d2"}], "fanout": None}],
           "synthesis": {"solved": "partly", "confidence": "medium", "contradictions": [1], "human_review_items": [], "success_items": [{"id": "S1", "status": "met"}, {"id": "S2", "status": "open"}]}}
    (rd / "result.json").write_text(json.dumps(res))
    (rd / "run-meta.json").write_text(json.dumps({"transcriptDir": str(td), "savedAt": saved}))
    (rd / "problem.md").write_text(f"problem of {name}\n")
    (rd / "answer.md").write_text("a\n")
    (rd / "board" / "to-proof--from-p1--field.md").write_text("ask")
    (rd / "board" / "to-p1--from-proof--x.md").write_text("ask"); (rd / "board" / "reply--to-p1--from-proof--x.md").write_text("done")
    st = td.parents[2].with_suffix(".jsonl")
    if session:
        u = lambda ts, content, **k: json.dumps({"type": "user", "timestamp": ts, "message": {"role": "user", "content": content}, **k})
        st.write_text("\n".join([
            u("2026-11-18T03:00:00Z", "start the run"),                                    # before the save (local time is later than UTC here or equal)
            u("2026-11-19T08:00:00Z", "the tabs are confusing and I cannot import my tasks"),
            u("2026-11-19T08:01:00Z", [{"type": "tool_result", "content": "x"}]),
            u("2026-11-19T08:02:00Z", "<task-notification>\n<task-id>1</task-id>"),
            u("2026-11-19T08:03:00Z", "This session is being continued from a previous conversation that ran out of context.", isCompactSummary=True),
            u("2026-11-19T08:04:00Z", "hidden", isMeta=True),
            u("2026-11-19T08:05:00Z", "<command-message>search</command-message>\n<command-name>/search</command-name>\n<command-args>find who else built this</command-args>"),
            u("2026-11-19T08:06:00Z", "<command-name>/compact</command-name>\n<command-args></command-args>"),
            u("2026-11-19T08:07:00Z", [{"type": "text", "text": "it never ran end to end before you gave it to me"}]),
            u("2026-11-19T08:08:00Z", "<system-reminder>internal</system-reminder>"),
        ]) + "\n")
    row = {"runDir": str(rd), "kind": "run", "problem": f"problem of {name}", "savedAt": saved, "transcriptDir": str(td), "sessionTranscript": str(st) if session else None, "planOnly": False, "engine": engine, "counts": {"flawed": 1}}
    if register:
        cr.REGISTRY.parent.mkdir(parents=True, exist_ok=True)
        with cr.REGISTRY.open("a") as fh:
            fh.write(json.dumps(row) + "\n")
    return rd, row


OLD, _ = make_run("20261115-old-run-alpha", engine="v5.0", saved="2026-11-15T10:00:00")
NEW, NEWROW = make_run("20261118-new-run-beta", agents=5)
NEW2, _ = make_run("20261119-new-run-gamma", saved="2026-11-19T10:00:00", agents=5)
LOOSE, _ = make_run("20261119-loose-run-delta", register=False)


class Select(unittest.TestCase):
    def test_default_is_every_run_on_the_current_version(self):
        primary, older, text, errors = rv.select()
        self.assertEqual({Path(r["runDir"]).name for r in primary}, {NEW.name, NEW2.name})
        self.assertEqual([Path(r["runDir"]).name for r in older], [OLD.name])
        self.assertIn("current engine version v5.1", text); self.assertFalse(errors)

    def test_no_run_on_the_current_version_falls_back_to_runs_since_the_last_review(self):
        rv.engine_version = lambda: "v9.9"
        try:
            primary, older, text, _ = rv.select()
            self.assertEqual(len(primary), 3); self.assertEqual(older, []); self.assertIn("no run on the current engine version v9.9 yet", text)
        finally:
            rv.engine_version = lambda: "v5.1"

    def test_named_runs_by_folder_by_file_inside_and_by_part_of_the_name(self):
        primary, _, text, errors = rv.select([str(OLD), str(NEW / "answer.md"), "loose-run", str(OLD)])
        self.assertEqual([Path(r["runDir"]).name for r in primary], [OLD.name, NEW.name]); self.assertEqual(len(errors), 1)   # a loose run is not in the registry: name it by path
        primary, _, _, errors = rv.select([str(LOOSE)])
        self.assertEqual(primary[0]["engine"], "v5.1"); self.assertTrue(primary[0]["unregistered"]); self.assertFalse(errors)
        primary, older, _, _ = rv.select([str(NEW)])     # a named run is the registry's own record, and is not listed twice
        self.assertEqual(primary[0].get("sessionTranscript"), NEWROW["sessionTranscript"]); self.assertNotIn(NEW.name, [Path(r["runDir"]).name for r in older])
        primary, _, _, errors = rv.select(["old-run-alpha"])
        self.assertEqual(Path(primary[0]["runDir"]), OLD)

    def test_a_name_that_fits_several_runs_or_none_is_an_error_not_a_guess(self):
        self.assertIn("several", rv.select(["new-run"])[3][0])
        self.assertIn("matches no recorded run", rv.select(["nothing-like-this"])[3][0])
        self.assertIn("no saved crucible run", rv.select([str(TMP)])[3][0])

    def test_versions_order_by_number(self):
        self.assertTrue(rv.ver("v5.1") < rv.ver("v5.1.1") < rv.ver("v5.2") < rv.ver("v5.10")); self.assertEqual(rv.ver(None), (0,))


class AfterRun(unittest.TestCase):
    def test_only_what_the_user_typed_after_the_save(self):
        msgs = rv.after_run_messages(NEWROW["sessionTranscript"], "2026-11-18T10:00:00")
        self.assertEqual([m["text"] for m in msgs], ["the tabs are confusing and I cannot import my tasks", "/search find who else built this", "it never ran end to end before you gave it to me"])

    def test_no_transcript_gives_nothing(self):
        self.assertEqual(rv.after_run_messages(None, ""), []); self.assertEqual(rv.after_run_messages(str(TMP / "nope.jsonl"), ""), [])

    def test_the_conversation_is_found_from_where_the_agent_transcripts_lie(self):
        self.assertEqual(rv.session_transcript({"runDir": str(LOOSE), "sessionTranscript": None}), str(TMP / "projects" / "proj" / f"sess-{LOOSE.name}.jsonl"))

    def test_a_long_tail_is_cut_and_said_so(self):
        msgs = rv.after_run_messages(NEWROW["sessionTranscript"], "2026-11-18T10:00:00", limit=1)
        self.assertEqual(len(msgs), 2); self.assertIn("more messages follow", msgs[1]["text"])


class Digest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.before = sorted(f.name for f in NEW.rglob("*"))
        cls.d = rv.run_digest(NEW, NEWROW)

    def test_the_run_folder_is_not_changed(self):
        self.assertEqual(sorted(f.name for f in NEW.rglob("*")), self.before)

    def test_findings_by_kind_and_the_two_kinds_that_never_block(self):
        f = self.d["findings"]
        self.assertEqual((f["total"], f["blocking"]), (5, 2)); self.assertEqual(f["by_class"], {"behaviour": 2, "test_strength": 1, "evidence": 1, "out_of_part": 1}); self.assertEqual(f["never_blocking_share"], 0.4)

    def test_open_clause_is_found_and_a_named_list_is_not(self):
        self.assertEqual(list(self.d["open_clauses"]), ["p1"]); self.assertEqual(len(self.d["open_clauses"]["p1"]), 1); self.assertIn("checker writes", self.d["open_clauses"]["p1"][0])

    def test_rounds_that_did_not_shrink_the_open_findings(self):
        self.assertEqual(self.d["loops"]["parts_with_rounds_not_shrinking"], ["p1"])

    def test_empty_hand_back_budget_and_essential_part_not_started(self):
        self.assertEqual(self.d["empty_handbacks"], ["solver:p1:r2"]); self.assertEqual(self.d["budget"]["critical_not_started"], ["proof"]); self.assertEqual(self.d["budget"]["used_over_estimate"], 2.0)

    def test_between_parts(self):
        b = self.d["between_parts"]
        self.assertEqual((b["issues_raised"], b["by_pair"], b["requests"], b["requests_unanswered"]), (2, {"p1 -> proof": 2}, 2, ["to-proof--from-p1--field.md"]))

    def test_context_and_answer(self):
        self.assertEqual(self.d["context"]["solvers_over_300k"], 2); self.assertEqual(self.d["answer"]["success_items"], {"met": 1, "open": 1}); self.assertEqual(self.d["finals"], {"flawed": 1})

    def test_the_text_form_carries_the_figures(self):
        md = rv.digest_md(self.d)
        for piece in ("used / estimate 2.0", "essential parts never started: ['proof']", "{'p1': 1}", "| p1 | hard |"):
            self.assertIn(piece, md)

    def test_a_run_from_before_finding_kinds_says_so(self):
        d = json.loads(json.dumps(self.d)); d["findings"].update({"classified": 0, "by_class": {"unclassified": 5}})
        self.assertIn("predates finding kinds", rv.digest_md(d))


class Expectations(unittest.TestCase):
    def setUp(self):
        rv.EXPECT.write_text(json.dumps({"expectations": [
            {"id": "e-over", "since": "v5.1", "change": "c", "metric": "budget.used_over_estimate", "baseline": 1.63, "op": "<=", "target": 1.25, "status": "open"},
            {"id": "e-crit", "since": "v5.1", "change": "c", "metric": "budget.critical_not_started", "baseline": 2, "op": "==", "target": 0, "status": "open"},
            {"id": "e-later", "since": "v5.2", "change": "c", "metric": "finals.verified_share", "baseline": 0, "op": ">=", "target": 0.5, "status": "open"},
            {"id": "e-closed", "since": "v5.0", "change": "c", "metric": "finals.verified_share", "baseline": 0, "op": ">=", "target": 0.5, "status": "met"}]}))
        self.d = {"name": "r", "engine": "v5.1", "agents": 40, "budget": {"used_over_estimate": 1.1, "critical_not_started": ["proof"]}, "finals": {"verified": 1, "flawed": 1}}

    def test_measured_only_on_runs_of_that_version_or_later_and_of_some_size(self):
        rows = {e["id"]: e for e in rv.check_expectations([self.d, {**self.d, "name": "old", "engine": "v5.0"}, {**self.d, "name": "tiny", "agents": 5}])}
        self.assertEqual(set(rows), {"e-over", "e-crit", "e-later"})
        self.assertEqual([o["run"] for o in rows["e-over"]["observed"]], ["r"]); self.assertEqual(rows["e-over"]["verdict"], "met on every run")
        self.assertEqual(rows["e-crit"]["verdict"], "not met on 1 of 1 run(s)"); self.assertEqual(rows["e-later"]["verdict"], "no run to measure it on yet")
        self.assertIn("| e-crit | v5.1 |", rv.expectations_md(list(rows.values())))

    def test_a_review_records_new_expectations_for_applied_changes_only_and_sets_statuses(self):
        pack = TMP / "pack-x"; pack.mkdir(exist_ok=True)
        (pack / "expectations.json").write_text(json.dumps(rv.check_expectations([self.d])))
        res = {"version": "v5.1.1", "applied": [{"id": "fix-a"}], "expectations": [{"id": "e-over", "status": "met", "reason": "1.1 on one run"}, {"id": "nope", "status": "met"}, {"id": "e-crit", "status": "bogus"}],
               "newExpectations": [{"finding": "fix-a", "change": "c", "metric": "loops.open_clause_parts", "baseline": 6, "op": "==", "target": 0, "why": "w"},
                                   {"finding": "fix-b", "change": "c", "metric": "loops.open_clause_parts", "baseline": 6, "op": "==", "target": 0},
                                   {"finding": "fix-a", "change": "c", "metric": "made.up", "baseline": 1, "op": "<=", "target": 0}]}
        out = rv.record_expectations(res, pack)
        self.assertEqual(out, {"added": ["v5.1.1-fix-a"], "status": ["e-over: met"]})
        data = {e["id"]: e for e in json.loads(rv.EXPECT.read_text())["expectations"]}
        self.assertEqual(data["e-over"]["status"], "met"); self.assertEqual(data["e-over"]["checked"][0]["value"], 1.1); self.assertEqual(data["e-crit"]["status"], "open")
        self.assertEqual((data["v5.1.1-fix-a"]["since"], data["v5.1.1-fix-a"]["status"]), ("v5.1.1", "open"))
        self.assertEqual(rv.record_expectations(res, pack)["added"], [])    # twice is once

    def test_every_number_an_expectation_may_use_is_also_offered_to_the_selector(self):
        src = (cr.REPO / "engine" / "crucible-evolve.js").read_text()
        import re
        listed = set(re.findall(r"'([a-z_]+\.[a-z0-9_]+)'", src[src.index("const METRICS"):src.index("]", src.index("const METRICS"))]))
        self.assertEqual(listed, set(rv.METRICS))
        shipped = json.loads((cr.REPO / "references" / "expectations.json").read_text())["expectations"]
        self.assertTrue(shipped and all(e["metric"] in rv.METRICS and e["op"] in rv.OPS for e in shipped))


class Probes(unittest.TestCase):
    def test_verdict_compares_case_by_case_where_both_sides_were_judged(self):
        R = lambda case, engine, right, ok=True, route="sonnet@high": {"case": case, "engine": engine, "route": route, "ok": ok, "score": {"right": right}}
        v = rv.probe_verdict([R("a", "old", True), R("a", "new", False), R("b", "old", False), R("b", "new", True), R("c", "old", True), R("c", "new", True),
                              R("d", "old", False), R("d", "new", False), R("e", "old", True), R("e", "new", True, ok=False), R("a", "old", True, route="opus@high"), R("a", "new", True, route="opus@high")], "new", "old")
        self.assertEqual(v["regressed"], [{"case": "a", "route": "sonnet@high"}]); self.assertEqual(v["improved"], [{"case": "b", "route": "sonnet@high"}])
        self.assertEqual(v["same_right"], 2); self.assertEqual(v["same_wrong"], [{"case": "d", "route": "sonnet@high"}]); self.assertEqual(v["not_judged"][0]["case"], "e")

    def test_the_pattern_for_an_open_set_is_the_engines_own(self):
        import re
        js = re.search(r"const OPEN_SET = /(.+)/i\n", (cr.REPO / "engine" / "crucible-engine.js").read_text()).group(1)
        self.assertEqual(js, rv.OPEN_SET.pattern)


class Pack(unittest.TestCase):
    def test_the_pack_for_the_named_run(self):
        import contextlib, io
        fb = TMP / "fb.md"; fb.write_text("the last run never assembled the parts\n")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.assertEqual(rv.review_pack([str(NEW)], str(fb)), 0)
        info = json.loads(buf.getvalue())
        pack = Path(info["pack"])
        self.assertEqual([p["name"] for p in info["primary"]], [NEW.name]); self.assertEqual(sorted(info["older"]), sorted([str(OLD), str(NEW2)]))
        for f in ("history.md", "pack.json", "expectations.md", "run-audit.md", "user-feedback.md", f"runs/{NEW.name}/digest.md", f"runs/{NEW.name}/digest.json", f"runs/{NEW.name}/after-run.md"):
            self.assertTrue((pack / f).exists(), f)
        self.assertIn("never assembled the parts", (pack / "user-feedback.md").read_text()); self.assertIn("the tabs are confusing", (pack / f"runs/{NEW.name}/after-run.md").read_text())
        self.assertIn("the 1 run(s) the user named", (pack / "history.md").read_text()); self.assertFalse(info["nothingToReview"])
        self.assertTrue(pack.is_relative_to(cr.REGISTRY.parent / "reviews"))

    def test_only_the_most_recent_runs_are_marked_for_a_full_audit(self):
        import contextlib, io
        buf, keep = io.StringIO(), rv.AUDIT_MAX_RUNS
        rv.AUDIT_MAX_RUNS = 1
        try:
            with contextlib.redirect_stdout(buf):
                rv.review_pack([str(NEW2), str(NEW)])
        finally:
            rv.AUDIT_MAX_RUNS = keep
        info = json.loads(buf.getvalue())
        self.assertEqual([(p["name"], p["audit"]) for p in info["primary"]], [(NEW.name, False), (NEW2.name, True)])
        self.assertIn("not audited in full", (Path(info["pack"]) / "history.md").read_text())

    def test_a_wrong_name_stops_before_a_pack_is_built(self):
        import contextlib, io
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.assertEqual(rv.review_pack(["nothing-like-this"]), 1)
        self.assertIn("matches no recorded run", json.loads(buf.getvalue())["error"])


class OwnerFile(unittest.TestCase):
    """expectation.md is the owner's: a review's commit that changes it is undone, the owner's own change is left alone."""
    def setUp(self):
        import subprocess
        self.repo = Path(tempfile.mkdtemp(prefix="crucible-owner-test-"))
        self.git = lambda *a: subprocess.run(["git", "-C", str(self.repo), "-c", "user.name=t", "-c", "user.email=t@example.invalid", *a], capture_output=True, text=True)
        self.git("init", "-q")
        (self.repo / "expectation.md").write_text("only the owner edits this\n"); (self.repo / "code.txt").write_text("a\n")
        self.git("add", "-A"); self.git("commit", "-qm", "start")
        self.base = self.git("rev-parse", "HEAD").stdout.strip()
        self.pack = self.repo / "pack"; self.pack.mkdir(); (self.pack / "pack.json").write_text(json.dumps({"repoHead": self.base}))
        (self.repo / ".git" / "info" / "exclude").write_text("pack/\n")
        self.old = (cr.REPO, os.environ.get("GIT_AUTHOR_NAME"))
        cr.REPO = self.repo
        for k, v in (("GIT_AUTHOR_NAME", "t"), ("GIT_AUTHOR_EMAIL", "t@example.invalid"), ("GIT_COMMITTER_NAME", "t"), ("GIT_COMMITTER_EMAIL", "t@example.invalid")):
            os.environ[k] = v

    def tearDown(self):
        cr.REPO = self.old[0]
        for k in ("GIT_AUTHOR_NAME", "GIT_AUTHOR_EMAIL", "GIT_COMMITTER_NAME", "GIT_COMMITTER_EMAIL"):
            os.environ.pop(k, None)

    def commit(self, msg, text=None, code=None):
        if text is not None:
            (self.repo / "expectation.md").write_text(text)
        if code is not None:
            (self.repo / "code.txt").write_text(code)
        self.git("add", "-A"); self.git("commit", "-qm", msg)

    def test_a_review_that_left_the_file_alone_reports_nothing(self):
        self.commit("crucible evolve(periodic): a fix", code="b\n")
        self.assertEqual(rv.guard_owner_file(self.pack), {})

    def test_a_review_commit_that_changed_it_is_undone_for_that_file_only(self):
        self.commit("crucible evolve(periodic): a fix", text="an agent rewrote this\n", code="b\n")
        g = rv.guard_owner_file(self.pack)
        self.assertEqual(len(g["changed_by_review"]), 1)
        self.assertTrue(g["restored"])
        self.assertEqual((self.repo / "expectation.md").read_text(), "only the owner edits this\n")
        self.assertEqual((self.repo / "code.txt").read_text(), "b\n")
        self.assertEqual(self.git("status", "--porcelain").stdout.strip(), "")

    def test_the_owners_own_change_is_never_put_back(self):
        self.commit("my own edit", text="the owner changed a line\n")
        self.assertEqual(rv.guard_owner_file(self.pack), {})
        self.commit("crucible evolve(periodic): a fix", text="an agent rewrote this\n")
        g = rv.guard_owner_file(self.pack)
        self.assertFalse(g["restored"])
        self.assertEqual((self.repo / "expectation.md").read_text(), "an agent rewrote this\n")


class TheFileItself(unittest.TestCase):
    def test_it_says_who_edits_it_and_names_nothing_of_one_machine(self):
        f = Path(__file__).resolve().parent.parent / "expectation.md"
        s = f.read_text()
        self.assertTrue(s.split("\n")[2].startswith("Only I, the owner of this repository, edit this file."))
        self.assertNotIn("/Users/", s)
        for i in ["U1", "U10", "R1", "R12", "I1", "I6", "L1", "L4"]:
            self.assertIn(f"**{i}.", s)


if __name__ == "__main__":
    unittest.main(verbosity=1)
