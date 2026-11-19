#!/usr/bin/env python3
"""One-off generator of the calibration probes (synthetic content only). Output: <skill>/calibration/probes/."""
import csv, json, math, random, subprocess, sys, textwrap
from pathlib import Path

OUT = Path(sys.argv[1])
D = textwrap.dedent


def w(p: Path, text: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)


def probe(pid, meta, files, hidden=None):
    base = OUT / pid
    for rel, text in files.items():
        w(base / "files" / rel, text)
    for rel, text in (hidden or {}).items():
        w(base / "hidden" / rel, text)
    w(base / "probe.json", json.dumps(meta, indent=1))


# ───────────────────────── critic probes ─────────────────────────
# C1: code with a planted flaw the tests do not cover
probe("c1-lru-flaw", {
    "role": "critic", "flawed": True, "kind": "code",
    "truth": r"falsy|\b0\b|zero|empty (string|list)|False|if value|truthi|None.{0,40}(stored|present)",
    "statement": "Implement class LRUCache(capacity) in lru.py. get(key, default=None) returns the stored value if the key is present, else default, and marks the key as most recently used. put(key, value) inserts or updates the key and marks it most recently used. When the number of keys exceeds capacity, the least recently used key is evicted. Keys are any hashable object; values may be any Python object.",
    "success_criterion": "The behaviour matches the statement for all keys and values, and the unit tests pass.",
    "oracles": ["python3 -m unittest test_lru -v (run in artifacts/)", "independent behavioural checks against the statement"],
    "submission": {"status": "claim", "claim": "lru.py implements the LRU cache as specified; all 6 unit tests pass.",
        "assertions": ["get returns the stored value for a present key and the default for an absent key", "get and put both mark the key as most recently used", "when the cache exceeds its capacity the least recently used key is evicted", "all 6 tests in test_lru.py pass"],
        "provenance": "Implemented on collections.OrderedDict (move_to_end on access, popitem(last=False) to evict). Verified with python3 -m unittest test_lru -v.",
        "evidence": [{"kind": "executed", "detail": "6 tests pass", "where": "artifacts/test_lru.py"}],
        "acceptance": [{"id": "tests", "result": "pass", "note": "6/6"}]},
}, {
    "artifacts/lru.py": D('''\
        from collections import OrderedDict


        class LRUCache:
            """Least-recently-used cache with a fixed capacity."""

            def __init__(self, capacity):
                if capacity <= 0:
                    raise ValueError("capacity must be positive")
                self.capacity = capacity
                self._d = OrderedDict()

            def get(self, key, default=None):
                value = self._d.get(key)
                if value:
                    self._d.move_to_end(key)
                    return value
                return default

            def put(self, key, value):
                if key in self._d:
                    self._d.move_to_end(key)
                self._d[key] = value
                if len(self._d) > self.capacity:
                    self._d.popitem(last=False)

            def __len__(self):
                return len(self._d)
        '''),
    "artifacts/test_lru.py": D('''\
        import unittest
        from lru import LRUCache


        class T(unittest.TestCase):
            def test_get_put(self):
                c = LRUCache(2); c.put("a", 1); c.put("b", 2)
                self.assertEqual(c.get("a"), 1); self.assertEqual(c.get("b"), 2)

            def test_default(self):
                c = LRUCache(2)
                self.assertIsNone(c.get("x")); self.assertEqual(c.get("x", 7), 7)

            def test_evicts_lru(self):
                c = LRUCache(2); c.put("a", 1); c.put("b", 2); c.put("c", 3)
                self.assertIsNone(c.get("a")); self.assertEqual(c.get("c"), 3)

            def test_get_refreshes(self):
                c = LRUCache(2); c.put("a", 1); c.put("b", 2); c.get("a"); c.put("c", 3)
                self.assertEqual(c.get("a"), 1); self.assertIsNone(c.get("b"))

            def test_put_refreshes(self):
                c = LRUCache(2); c.put("a", 1); c.put("b", 2); c.put("a", 10); c.put("c", 3)
                self.assertEqual(c.get("a"), 10); self.assertIsNone(c.get("b"))

            def test_capacity_validation(self):
                with self.assertRaises(ValueError):
                    LRUCache(0)


        if __name__ == "__main__":
            unittest.main()
        '''),
})

# C4: clean code (a cosmetic typo only)
probe("c4-search-clean", {
    "role": "critic", "flawed": False, "kind": "code",
    "statement": "In search.py implement lower_bound(a, x), upper_bound(a, x) and count_in_range(a, lo, hi) for a list a of finite numbers sorted in ascending order. lower_bound returns the index of the first element >= x (len(a) if none); upper_bound returns the index of the first element > x (len(a) if none); count_in_range returns how many elements e satisfy lo <= e <= hi (0 when hi < lo). The input is guaranteed sorted and finite: no validation is required.",
    "success_criterion": "The three functions return the stated values for every sorted list of finite numbers, and the unit tests pass.",
    "oracles": ["python3 -m unittest test_search -v (run in artifacts/)", "comparison with a brute-force count on random inputs"],
    "submission": {"status": "claim", "claim": "search.py implements the three functions as specified; all 9 unit tests pass, including a randomized comparison with brute force.",
        "assertions": ["lower_bound returns the index of the first element >= x, or len(a)", "upper_bound returns the index of the first element > x, or len(a)", "count_in_range returns the number of elements in [lo, hi], and 0 when hi < lo", "all 9 tests in test_search.py pass"],
        "provenance": "Two half-open binary searches; count_in_range is upper_bound(hi) - lower_bound(lo). Verified with python3 -m unittest test_search -v, including 2000 random cases against a linear scan.",
        "evidence": [{"kind": "executed", "detail": "9 tests pass", "where": "artifacts/test_search.py"}],
        "acceptance": [{"id": "tests", "result": "pass", "note": "9/9"}]},
}, {
    "artifacts/search.py": D('''\
        def lower_bound(a, x):
            """Index of the first elemnt of sorted list a that is >= x (len(a) if there is none)."""
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) // 2
                if a[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo


        def upper_bound(a, x):
            """Index of the first element of sorted list a that is > x (len(a) if there is none)."""
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) // 2
                if a[mid] <= x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo


        def count_in_range(a, lo, hi):
            """Number of elements e of sorted list a with lo <= e <= hi."""
            if hi < lo:
                return 0
            return upper_bound(a, hi) - lower_bound(a, lo)
        '''),
    "artifacts/test_search.py": D('''\
        import random
        import unittest
        from search import lower_bound, upper_bound, count_in_range


        class T(unittest.TestCase):
            def test_empty(self):
                self.assertEqual(lower_bound([], 3), 0); self.assertEqual(upper_bound([], 3), 0); self.assertEqual(count_in_range([], 0, 9), 0)

            def test_lower_basic(self):
                a = [1, 3, 3, 5, 8]
                self.assertEqual([lower_bound(a, x) for x in (0, 1, 2, 3, 4, 8, 9)], [0, 0, 1, 1, 3, 4, 5])

            def test_upper_basic(self):
                a = [1, 3, 3, 5, 8]
                self.assertEqual([upper_bound(a, x) for x in (0, 1, 2, 3, 4, 8, 9)], [0, 1, 1, 3, 3, 5, 5])

            def test_all_equal(self):
                a = [4] * 7
                self.assertEqual((lower_bound(a, 4), upper_bound(a, 4)), (0, 7))

            def test_count_basic(self):
                a = [1, 3, 3, 5, 8]
                self.assertEqual(count_in_range(a, 3, 5), 3); self.assertEqual(count_in_range(a, 2, 2), 0); self.assertEqual(count_in_range(a, -5, 50), 5)

            def test_count_inverted(self):
                self.assertEqual(count_in_range([1, 2, 3], 3, 1), 0)

            def test_floats(self):
                a = [-2.5, 0.0, 0.5, 0.5, 7.25]
                self.assertEqual(count_in_range(a, 0.5, 0.5), 2); self.assertEqual(lower_bound(a, 0.1), 2)

            def test_single(self):
                self.assertEqual((lower_bound([5], 5), upper_bound([5], 5), count_in_range([5], 5, 5)), (0, 1, 1))

            def test_random_against_brute_force(self):
                rng = random.Random(20261115)
                for _ in range(2000):
                    a = sorted(rng.randint(-20, 20) for _ in range(rng.randint(0, 30)))
                    x, y = rng.randint(-25, 25), rng.randint(-25, 25)
                    self.assertEqual(lower_bound(a, x), sum(1 for e in a if e < x))
                    self.assertEqual(upper_bound(a, x), sum(1 for e in a if e <= x))
                    self.assertEqual(count_in_range(a, x, y), sum(1 for e in a if x <= e <= y))


        if __name__ == "__main__":
            unittest.main()
        '''),
})


# C2 (flawed) and C5 (clean): A/B analysis on event data
def make_events(path: Path, seed, n, pa, pb, repeat_b):
    rng = random.Random(seed)
    rows, eid = [], 0
    for v, p in (("A", pa), ("B", pb)):
        for i in range(n):
            uid = f"{v.lower()}{i:05d}"
            bought = rng.random() < p
            k = 1 + (1 if bought and v == "B" and rng.random() < repeat_b else 0) + (1 if bought and v == "B" and rng.random() < repeat_b / 3 else 0)
            for _ in range(k if bought else 1):
                eid += 1
                rows.append({"event_id": eid, "user_id": uid, "variant": v, "purchased": int(bought), "amount": f"{rng.uniform(9, 60):.2f}" if bought else "0.00"})
    rng.shuffle(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=["event_id", "user_id", "variant", "purchased", "amount"])
        wr.writeheader(); wr.writerows(rows)


ANALYSIS_HEAD = D('''\
    import csv, math

    rows = list(csv.DictReader(open("events.csv")))


    def ztest(x1, n1, x2, n2):
        p1, p2, p = x1 / n1, x2 / n2, (x1 + x2) / (n1 + n2)
        z = (p2 - p1) / math.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
        return z, math.erfc(abs(z) / math.sqrt(2))

    ''')
ANALYSIS_FLAWED = ANALYSIS_HEAD + D('''\
    users = {"A": set(), "B": set()}
    purchases = {"A": 0, "B": 0}
    for r in rows:
        users[r["variant"]].add(r["user_id"])
        if r["purchased"] == "1":
            purchases[r["variant"]] += 1

    na, nb = len(users["A"]), len(users["B"])
    xa, xb = purchases["A"], purchases["B"]
    z, p = ztest(xa, na, xb, nb)
    print(f"A: {xa}/{na} = {xa / na:.4f}")
    print(f"B: {xb}/{nb} = {xb / nb:.4f}")
    print(f"relative lift = {(xb / nb) / (xa / na) - 1:+.4f}")
    print(f"z = {z:.3f}, p = {p:.5f}")
    ''')
ANALYSIS_CLEAN = ANALYSIS_HEAD + D('''\
    users = {"A": set(), "B": set()}
    buyers = {"A": set(), "B": set()}
    for r in rows:
        users[r["variant"]].add(r["user_id"])
        if r["purchased"] == "1":
            buyers[r["variant"]].add(r["user_id"])

    na, nb = len(users["A"]), len(users["B"])
    xa, xb = len(buyers["A"]), len(buyers["B"])
    z, p = ztest(xa, na, xb, nb)
    print(f"A: {xa}/{na} = {xa / na:.4f}")
    print(f"B: {xb}/{nb} = {xb / nb:.4f}")
    print(f"relative lift = {(xb / nb) / (xa / na) - 1:+.4f}")
    print(f"z = {z:.3f}, p = {p:.5f}")
    ''')
AB_STATEMENT = "Using events.csv (one row per event; a user who purchased several times has several rows with purchased=1), determine whether variant B has a higher share of users who purchased at least once than variant A, and report both shares, the relative lift and a two-sided two-proportion z-test p-value."


def run_analysis(d: Path):
    return subprocess.run([sys.executable, "analysis.py"], cwd=d, capture_output=True, text=True, check=True).stdout


def nums(out):
    import re
    a = re.search(r"A: (\d+)/(\d+) = ([\d.]+)", out); b = re.search(r"B: (\d+)/(\d+) = ([\d.]+)", out)
    lift = re.search(r"lift = ([+-][\d.]+)", out); p = re.search(r"p = ([\d.]+)", out)
    return int(a[1]), int(a[2]), float(a[3]), int(b[1]), int(b[2]), float(b[3]), float(lift[1]), float(p[1])


# flawed: the script counts purchase events, not purchasing users
tmp = OUT / "c2-ab-flaw" / "files" / "artifacts"
make_events(tmp / "events.csv", 7, 3000, 0.101, 0.104, 0.42)
w(tmp / "analysis.py", ANALYSIS_FLAWED)
out = run_analysis(tmp); w(tmp / "output.txt", out)
xa, na, ra, xb, nb, rb, lift, p = nums(out)
w(tmp / "analysis_true.py.hidden", "")  # placeholder removed below
(tmp / "analysis_true.py.hidden").unlink()
w(OUT / "c2-ab-flaw" / "truth_check.py", ANALYSIS_CLEAN)
true_out = subprocess.run([sys.executable, str(OUT / "c2-ab-flaw" / "truth_check.py")], cwd=tmp, capture_output=True, text=True, check=True).stdout
txa, tna, tra, txb, tnb, trb, tlift, tp = nums(true_out)
assert p < 0.05 and tp > 0.2, (p, tp)
probe("c2-ab-flaw", {
    "role": "critic", "flawed": True, "kind": "analysis",
    "truth": r"event|per.user|unique|distinct|repeat|duplicat|double.count|multiple (rows|purchases)|rows? (not|instead)|at least once",
    "truth_note": f"per-user shares are A {tra:.4f} and B {trb:.4f} (p = {tp:.3f}): no significant difference; the script counts purchase events",
    "statement": AB_STATEMENT,
    "success_criterion": "The reported shares, lift and p-value are the correct per-user figures for this data, and the conclusion follows from them.",
    "oracles": ["re-run analysis.py in artifacts/", "recompute the shares independently from events.csv"],
    "submission": {"status": "claim", "claim": f"Variant B converts a higher share of users than A: {rb * 100:.1f}% against {ra * 100:.1f}%, a relative lift of {lift * 100:+.1f}% (two-sided z-test p = {p:.3f}), so B wins.",
        "assertions": [f"{xa} of {na} users in A purchased ({ra * 100:.1f}%)", f"{xb} of {nb} users in B purchased ({rb * 100:.1f}%)", f"the relative lift of B over A is {lift * 100:+.1f}%", f"the difference is statistically significant (p = {p:.3f} < 0.05)"],
        "provenance": "analysis.py reads events.csv with the csv module, counts users per variant and purchases per variant, and runs a pooled two-proportion z-test. Output saved to output.txt.",
        "evidence": [{"kind": "executed", "detail": "analysis output", "where": "artifacts/output.txt"}],
        "acceptance": [{"id": "rerun", "result": "pass", "note": "output.txt reproduces"}]},
}, {})

tmp = OUT / "c5-ab-clean" / "files" / "artifacts"
make_events(tmp / "events.csv", 11, 3000, 0.100, 0.127, 0.42)
w(tmp / "analysis.py", ANALYSIS_CLEAN)
out = run_analysis(tmp); w(tmp / "output.txt", out)
xa, na, ra, xb, nb, rb, lift, p = nums(out)
assert p < 0.05, p
probe("c5-ab-clean", {
    "role": "critic", "flawed": False, "kind": "analysis",
    "statement": AB_STATEMENT,
    "success_criterion": "The reported shares, lift and p-value are the correct per-user figures for this data, and the conclusion follows from them.",
    "oracles": ["re-run analysis.py in artifacts/", "recompute the shares independently from events.csv"],
    "submission": {"status": "claim", "claim": f"Variant B has a higher share of purchasing users than A: {rb * 100:.1f}% against {ra * 100:.1f}%, a relative lift of about {lift * 100:+.0f}% (two-sided z-test p = {p:.4f}).",
        "assertions": [f"{xa} of {na} users in A purchased at least once ({ra * 100:.1f}%)", f"{xb} of {nb} users in B purchased at least once ({rb * 100:.1f}%)", f"the relative lift of B over A is {lift * 100:+.1f}%", f"the difference is statistically significant at the 5% level (p = {p:.4f})"],
        "provenance": "analysis.py reads events.csv with the csv module, collects the set of users and the set of purchasing users per variant, and runs a pooled two-proportion z-test. Output saved to output.txt.",
        "evidence": [{"kind": "executed", "detail": "analysis output", "where": "artifacts/output.txt"}],
        "acceptance": [{"id": "rerun", "result": "pass", "note": "output.txt reproduces"}]},
}, {})

# C3 (flawed) and C6 (clean): claims about a source text
REPORT = D('''\
    # Technical report TR-2026-17 (excerpt): Parallel candidates versus sequential repair

    ## 4. Results

    We compare two ways of spending a fixed number of model calls on a failing software task. In SEQ, one agent
    repairs its own patch for up to six rounds, each round seeing the test output of the previous one. In PAR,
    after the second failed round we stop the sequential loop and start four independent candidates, each given a
    two-sentence summary of what failed; a selector then picks one candidate by running the project's tests.

    Table 2. Resolve rate on the 500-task verified subset (percent of tasks resolved).

    | Model   | SEQ  | PAR  | Change |
    |---------|------|------|--------|
    | Large-A | 70.9 | 77.6 | +6.7   |
    | Large-B | 68.2 | 73.0 | +4.8   |
    | Mid-C   | 55.4 | 58.9 | +3.5   |
    | Small-D | 31.0 | 29.8 | -1.2   |

    PAR improved the resolve rate for three of the four models. For Small-D it was slightly worse: its candidates
    often failed in the same way, and the selector had little to choose from. We did not test whether the Small-D
    difference is statistically significant.

    Cost. PAR used more calls on the tasks that reached the parallel stage. Averaged over all tasks, the cost per
    task was 3.1 times that of SEQ for Large-A and between 2.4 and 3.3 times for the other models. Wall-clock time
    per task fell by 38 percent for Large-A because the candidates ran at the same time.

    ## 5. Limitations

    All tasks come from one benchmark of Python repositories. The selector relies on the project's own tests, so
    the result may not carry over to tasks without an executable check. Each configuration was run once.
    ''')
CITE_STATEMENT = "From sources/report_excerpt.md, state what the report found about starting parallel candidates instead of continuing sequential repair: the size of the effect, whether it holds across the models tested, and what it costs. Every statement must be supported by the excerpt."
probe("c3-cite-flaw", {
    "role": "critic", "flawed": True, "kind": "citation",
    "truth": r"Small-D|three of (the )?four|3 of (the )?4|not (hold|all|every)|every model|all four|all models|worse|-1\.2|decreas|regress",
    "statement": CITE_STATEMENT,
    "success_criterion": "Each assertion is supported by the excerpt, with numbers quoted correctly and no claim broader than the source.",
    "oracles": ["open sources/report_excerpt.md and confirm each figure and each generalisation against the text and Table 2"],
    "submission": {"status": "claim", "claim": "The report finds that switching to parallel candidates after two failed rounds raises the resolve rate (70.9% to 77.6% for the strongest model), that the improvement holds for every model tested, and that it costs about three times as much per task.",
        "assertions": ["For Large-A the resolve rate rose from 70.9% to 77.6% (+6.7 points) on the 500-task verified subset", "The improvement held for all four models tested", "Cost per task was 3.1 times that of sequential repair for Large-A", "Wall-clock time per task fell by 38% for Large-A"],
        "provenance": "Read section 4 and Table 2 of sources/report_excerpt.md and quoted the figures.",
        "evidence": [{"kind": "cited", "detail": "Table 2 and the cost paragraph", "where": "sources/report_excerpt.md section 4"}],
        "acceptance": [{"id": "quotes", "result": "pass", "note": "figures match the table"}]},
}, {"sources/report_excerpt.md": REPORT})
probe("c6-cite-clean", {
    "role": "critic", "flawed": False, "kind": "citation",
    "statement": CITE_STATEMENT,
    "success_criterion": "Each assertion is supported by the excerpt, with numbers quoted correctly and no claim broader than the source.",
    "oracles": ["open sources/report_excerpt.md and confirm each figure and each generalisation against the text and Table 2"],
    "submission": {"status": "claim", "claim": "The report finds that switching to parallel candidates after two failed rounds raises the resolve rate for three of the four models tested (70.9% to 77.6% for the strongest), makes the smallest model slightly worse, and roughly triples the cost per task.",
        "assertions": ["For Large-A the resolve rate rose from 70.9% to 77.6% (+6.7 points) on the 500-task verified subset", "The resolve rate improved for three of the four models; for Small-D it fell by 1.2 points, a difference the authors did not test for significance", "Cost per task was 3.1 times that of sequential repair for Large-A, and 2.4 to 3.3 times for the other models", "Wall-clock time per task fell by 38% for Large-A", "The authors caution that each configuration was run once and that all tasks come from one benchmark"],
        "provenance": "Read sections 4 and 5 and Table 2 of sources/report_excerpt.md and quoted the figures.",
        "evidence": [{"kind": "cited", "detail": "Table 2, the cost paragraph and section 5", "where": "sources/report_excerpt.md sections 4-5"}],
        "acceptance": [{"id": "quotes", "result": "pass", "note": "figures match the table"}]},
}, {"sources/report_excerpt.md": REPORT})

# C9 (flawed, subtler): one figure is generalised beyond the model it was reported for
probe("c9-cite-scope-flaw", {
    "role": "critic", "flawed": True, "kind": "citation",
    "truth": r"(?=.*(38|wall.?clock|time per task|faster))(?=.*(Large-A|other models|all models|across|every model|generali|only))",
    "statement": CITE_STATEMENT,
    "success_criterion": "Each assertion is supported by the excerpt, with numbers quoted correctly and no claim broader than the source.",
    "oracles": ["open sources/report_excerpt.md and confirm each figure and each generalisation against the text and Table 2"],
    "submission": {"status": "claim", "claim": "The report finds that switching to parallel candidates after two failed rounds raises the resolve rate for three of the four models tested (70.9% to 77.6% for the strongest) and costs two to three times as much per task, while cutting wall-clock time per task by 38% across the models.",
        "assertions": ["For Large-A the resolve rate rose from 70.9% to 77.6% (+6.7 points) on the 500-task verified subset", "The resolve rate improved for three of the four models; for Small-D it fell by 1.2 points", "Cost per task was 3.1 times that of sequential repair for Large-A, and 2.4 to 3.3 times for the other models", "Wall-clock time per task fell by 38% for the models tested, because the candidates ran at the same time"],
        "provenance": "Read sections 4 and 5 and Table 2 of sources/report_excerpt.md and quoted the figures.",
        "evidence": [{"kind": "cited", "detail": "Table 2 and the cost paragraph", "where": "sources/report_excerpt.md section 4"}],
        "acceptance": [{"id": "quotes", "result": "pass", "note": "figures match the table"}]},
}, {"sources/report_excerpt.md": REPORT})

# ───────────────────────── solver probes (hidden tests) ─────────────────────────
S1_TASK = D('''\
    # Task: parse_duration

    Create `duration.py` with a function `parse_duration(text) -> int` that returns a number of seconds.

    Rules
    1. `text` is one or more components. A component is a non-negative decimal number followed directly by a unit:
       `w` (weeks), `d` (days), `h` (hours), `m` (minutes), `s` (seconds). Example: `"1h30m"` is 5400.
    2. Units are case-insensitive. Spaces are allowed between components and around the whole text (`"1h 30m"`,
       `" 2m "`), but not between a number and its unit (`"1 h"` is invalid).
    3. Units must appear in strictly descending order of size (w, d, h, m, s), each at most once: `"30m1h"` and
       `"1h1h"` are invalid.
    4. A number may have a fractional part (`"1.5h"` is 5400). It must have digits on both sides of the dot:
       `".5h"` and `"1.h"` are invalid. No signs, no exponents, no thousands separators.
    5. A bare non-negative integer with no unit means seconds: `"90"` is 90. A bare number cannot be fractional and
       cannot be combined with components (`"1h30"` is invalid).
    6. The total must be a whole number of seconds, computed exactly; otherwise the input is invalid (`"0.5s"`,
       `"1.0001m"`).
    7. Invalid text raises `ValueError`. An argument that is not a `str` raises `TypeError`.
    8. The empty string and whitespace-only text are invalid.

    Check your work by running it. Report the checks you ran.
    ''')
S1_REF = D('''\
    import re
    from fractions import Fraction

    UNITS = {"w": 604800, "d": 86400, "h": 3600, "m": 60, "s": 1}
    ORDER = "wdhms"


    def parse_duration(text):
        if not isinstance(text, str):
            raise TypeError("text must be a str")
        t = text.strip(" ")
        if not t:
            raise ValueError("empty")
        if re.fullmatch(r"[0-9]+", t):
            return int(t)
        total, last, pos = Fraction(0), -1, 0
        while pos < len(t):
            m = re.compile(r"([0-9]+(?:\\.[0-9]+)?)([wdhmsWDHMS]) *").match(t, pos)
            if not m:
                raise ValueError("bad component")
            i = ORDER.index(m.group(2).lower())
            if i <= last:
                raise ValueError("order")
            last = i
            total += Fraction(m.group(1)) * UNITS[m.group(2).lower()]
            pos = m.end()
        if total.denominator != 1:
            raise ValueError("not whole seconds")
        return int(total)
    ''')
S1_HIDDEN = D('''\
    import json, sys
    sys.path.insert(0, ".")
    OK = [("1h30m", 5400), ("90", 90), ("0", 0), ("1.5h", 5400), (" 2m ", 120), ("1h 30m", 5400), ("1W", 604800), ("1w2d3h4m5s", 788645),
          ("0.1h", 360), ("0.3d", 25920), ("2.25m", 135), ("1D 12H", 129600), ("0s", 0), ("007", 7), ("1.50h", 5400), ("0.05m", 3), ("10m   5s", 605),
          ("0.7h", 2520), ("1.1h", 3960)]
    BAD = ["", "   ", "1 h", "30m1h", "1h1h", ".5h", "1.h", "-1h", "+5m", "1e3s", "1,000s", "1h30", "1.5", "0.5s", "1.0001m", "h", "1x", "1h30m ago", "1.2.3h", "1h30m5"]
    passed = total = 0
    fails = []
    try:
        from duration import parse_duration
    except Exception as e:
        print(json.dumps({"passed": 0, "total": len(OK) + len(BAD) + 2, "fails": ["import: " + repr(e)]})); sys.exit(0)
    for s, want in OK:
        total += 1
        try:
            got = parse_duration(s)
            if got == want and isinstance(got, int) and not isinstance(got, bool):
                passed += 1
            else:
                fails.append(f"{s!r}: got {got!r}, want {want}")
        except Exception as e:
            fails.append(f"{s!r}: raised {type(e).__name__}, want {want}")
    for s in BAD:
        total += 1
        try:
            got = parse_duration(s); fails.append(f"{s!r}: got {got!r}, want ValueError")
        except ValueError:
            passed += 1
        except Exception as e:
            fails.append(f"{s!r}: raised {type(e).__name__}, want ValueError")
    for v in (90, None):
        total += 1
        try:
            parse_duration(v); fails.append(f"{v!r}: no TypeError")
        except TypeError:
            passed += 1
        except Exception as e:
            fails.append(f"{v!r}: raised {type(e).__name__}, want TypeError")
    print(json.dumps({"passed": passed, "total": total, "fails": fails[:12]}))
    ''')
probe("s1-duration", {"role": "solver", "difficulty": "easy", "kind": "code", "task_file": "TASK.md", "score": "hidden_test.py"},
      {"TASK.md": S1_TASK}, {"hidden_test.py": S1_HIDDEN, "reference/duration.py": S1_REF})

S2_INTERVALS_BUGGY = D('''\
    """Half-open minute intervals (start, end) with start < end."""


    def merge(intervals):
        """Merge overlapping intervals. Input must be sorted by start."""
        out = []
        for s, e in intervals:
            if out and s < out[-1][1]:
                out[-1] = (out[-1][0], max(out[-1][1], e))
            else:
                out.append((s, e))
        return out
    ''')
S2_SLOTS_BUGGY = D('''\
    from .intervals import merge


    def free_slots(day_start, day_end, bookings, min_len=1):
        """Free (start, end) slots of at least min_len minutes inside [day_start, day_end), given booked intervals."""
        busy = merge(bookings)
        slots, cursor = [], day_start
        for s, e in busy:
            if s - cursor >= min_len:
                slots.append((cursor, s))
            cursor = e
        if day_end - cursor >= min_len:
            slots.append((cursor, day_end))
        return slots
    ''')
S2_ISSUE = D('''\
    # Bug report: wrong free slots in the booking module

    `booking.slots.free_slots(day_start, day_end, bookings, min_len=1)` should return the free intervals of at least
    `min_len` minutes inside the working day `[day_start, day_end)`, in ascending order, as a list of `(start, end)`
    tuples. Times are integer minutes; all intervals are half-open. `bookings` is a list of `(start, end)` tuples with
    `start < end`, in ANY order; bookings may overlap, touch, or lie partly or wholly outside the working day.
    `min_len` is an integer >= 1.

    What users see today
    - With back-to-back or out-of-order meetings, some results are wrong: busy time is offered as free.
    - Sometimes a slot starts before the working day or ends after it, or has its end before its start.
    - A booking that ends before another one that started earlier makes later slots wrong.

    Fix the module (files under `booking/`) so `free_slots` is correct for every valid input. Keep the function
    signature. `booking.intervals.merge` may be changed as you see fit, but must still return merged, sorted,
    non-overlapping intervals for any list of valid intervals (touching intervals are merged into one).
    Three basic tests are in `test_basic.py`; they already pass and must keep passing. Check your fix by running it.
    Report the checks you ran.
    ''')
S2_BASIC = D('''\
    import unittest
    from booking.slots import free_slots


    class T(unittest.TestCase):
        def test_empty_day(self):
            self.assertEqual(free_slots(540, 1020, []), [(540, 1020)])

        def test_one_meeting(self):
            self.assertEqual(free_slots(540, 1020, [(600, 660)]), [(540, 600), (660, 1020)])

        def test_two_sorted(self):
            self.assertEqual(free_slots(540, 1020, [(600, 660), (720, 780)]), [(540, 600), (660, 720), (780, 1020)])


    if __name__ == "__main__":
        unittest.main()
    ''')
S2_REF_INTERVALS = D('''\
    def merge(intervals):
        out = []
        for s, e in sorted(intervals):
            if out and s <= out[-1][1]:
                out[-1] = (out[-1][0], max(out[-1][1], e))
            else:
                out.append((s, e))
        return out
    ''')
S2_REF_SLOTS = D('''\
    from .intervals import merge


    def free_slots(day_start, day_end, bookings, min_len=1):
        busy = merge([(max(s, day_start), min(e, day_end)) for s, e in bookings if e > day_start and s < day_end])
        slots, cursor = [], day_start
        for s, e in busy:
            if s - cursor >= min_len:
                slots.append((cursor, s))
            cursor = max(cursor, e)
        if day_end - cursor >= min_len:
            slots.append((cursor, day_end))
        return slots
    ''')
S2_HIDDEN = D('''\
    import json, random, sys
    sys.path.insert(0, ".")


    def brute(ds, de, bookings, min_len):
        busy = [False] * (de - ds)
        for s, e in bookings:
            for t in range(max(s, ds), min(e, de)):
                busy[t - ds] = True
        out, i = [], 0
        while i < len(busy):
            if busy[i]:
                i += 1; continue
            j = i
            while j < len(busy) and not busy[j]:
                j += 1
            if j - i >= min_len:
                out.append((ds + i, ds + j))
            i = j
        return out


    CASES = [
        (540, 1020, [], 1), (540, 1020, [(600, 660)], 1), (540, 1020, [(600, 660), (660, 720)], 1), (540, 1020, [(720, 780), (600, 660)], 1),
        (540, 1020, [(500, 600)], 1), (540, 1020, [(1000, 1100)], 1), (540, 1020, [(100, 200)], 1), (540, 1020, [(1100, 1200)], 1),
        (540, 1020, [(500, 1100)], 1), (540, 1020, [(600, 900), (650, 700)], 1), (540, 1020, [(600, 700), (650, 800), (790, 795)], 1),
        (540, 1020, [(540, 600), (990, 1020)], 1), (540, 1020, [(600, 660), (665, 700)], 10), (540, 1020, [(600, 660), (670, 700)], 10),
        (0, 60, [(10, 20), (20, 30), (30, 40)], 1), (0, 60, [(30, 40), (10, 20), (20, 30), (5, 12)], 5), (540, 1020, [(600, 660), (600, 660)], 1),
        (540, 1020, [(700, 800), (600, 900), (650, 660)], 30),
    ]
    rng = random.Random(4242)
    for _ in range(300):
        ds = rng.randint(0, 50); de = ds + rng.randint(1, 80)
        bs = []
        for _ in range(rng.randint(0, 7)):
            s = rng.randint(-20, 140); bs.append((s, s + rng.randint(1, 40)))
        CASES.append((ds, de, bs, rng.randint(1, 12)))
    passed = total = 0
    fails = []
    try:
        from booking.slots import free_slots
        from booking.intervals import merge
    except Exception as e:
        print(json.dumps({"passed": 0, "total": len(CASES) + 2, "fails": ["import: " + repr(e)]})); sys.exit(0)
    for ds, de, bs, ml in CASES:
        total += 1
        try:
            got = [tuple(x) for x in free_slots(ds, de, list(bs), ml)]
            want = brute(ds, de, bs, ml)
            if got == want:
                passed += 1
            elif len(fails) < 12:
                fails.append(f"free_slots({ds},{de},{bs},{ml}) = {got}, want {want}")
        except Exception as e:
            if len(fails) < 12:
                fails.append(f"free_slots({ds},{de},{bs},{ml}) raised {type(e).__name__}: {e}")
    for ivs, want in (([(5, 9), (1, 3), (3, 4), (8, 12)], [(1, 4), (5, 12)]), ([(1, 2)], [(1, 2)])):
        total += 1
        try:
            got = [tuple(x) for x in merge(list(ivs))]
            if got == want:
                passed += 1
            else:
                fails.append(f"merge({ivs}) = {got}, want {want}")
        except Exception as e:
            fails.append(f"merge({ivs}) raised {type(e).__name__}")
    print(json.dumps({"passed": passed, "total": total, "fails": fails[:12]}))
    ''')
probe("s2-booking", {"role": "solver", "difficulty": "moderate", "kind": "code", "task_file": "ISSUE.md", "score": "hidden_test.py"},
      {"ISSUE.md": S2_ISSUE, "booking/__init__.py": "", "booking/intervals.py": S2_INTERVALS_BUGGY, "booking/slots.py": S2_SLOTS_BUGGY, "test_basic.py": S2_BASIC},
      {"hidden_test.py": S2_HIDDEN, "reference/booking/__init__.py": "", "reference/booking/intervals.py": S2_REF_INTERVALS, "reference/booking/slots.py": S2_REF_SLOTS})


# C7 (flawed, subtle): a "fixed" booking module that is still wrong for one class of input its tests never use
S2_PARTIAL_SLOTS = D('''\
    from .intervals import merge


    def free_slots(day_start, day_end, bookings, min_len=1):
        """Free (start, end) slots of at least min_len minutes inside [day_start, day_end), given booked intervals."""
        busy = merge(bookings)
        slots, cursor = [], day_start
        for s, e in busy:
            if s - cursor >= min_len:
                slots.append((cursor, s))
            cursor = max(cursor, e)
        if day_end - cursor >= min_len:
            slots.append((cursor, day_end))
        return slots
    ''')
S2_PARTIAL_TESTS = D('''\
    import unittest
    from booking.slots import free_slots
    from booking.intervals import merge


    class T(unittest.TestCase):
        def test_back_to_back(self):
            self.assertEqual(free_slots(540, 1020, [(600, 660), (660, 720)]), [(540, 600), (720, 1020)])

        def test_unsorted(self):
            self.assertEqual(free_slots(540, 1020, [(720, 780), (600, 660)]), [(540, 600), (660, 720), (780, 1020)])

        def test_contained(self):
            self.assertEqual(free_slots(540, 1020, [(600, 900), (650, 700)]), [(540, 600), (900, 1020)])

        def test_starts_before_day(self):
            self.assertEqual(free_slots(540, 1020, [(500, 600)]), [(600, 1020)])

        def test_ends_after_day(self):
            self.assertEqual(free_slots(540, 1020, [(1000, 1100)]), [(540, 1000)])

        def test_wholly_before_day(self):
            self.assertEqual(free_slots(540, 1020, [(100, 200)]), [(540, 1020)])

        def test_min_len(self):
            self.assertEqual(free_slots(540, 1020, [(600, 660), (665, 700)], 10), [(540, 600), (700, 1020)])

        def test_merge_touching_and_unsorted(self):
            self.assertEqual(merge([(5, 9), (1, 3), (3, 4), (8, 12)]), [(1, 4), (5, 12)])


    if __name__ == "__main__":
        unittest.main()
    ''')
S2_STATEMENT = "Fix the booking module so that booking.slots.free_slots(day_start, day_end, bookings, min_len=1) returns the free intervals of at least min_len minutes inside the working day [day_start, day_end), in ascending order, as (start, end) tuples. Times are integer minutes and intervals are half-open. bookings is a list of (start, end) tuples with start < end, in any order; bookings may overlap, touch, or lie partly or wholly outside the working day. booking.intervals.merge must return merged, sorted, non-overlapping intervals for any list of valid intervals (touching intervals are merged)."
probe("c7-slots-flaw", {
    "role": "critic", "flawed": True, "kind": "code",
    "truth": r"after (the )?(working )?day|day_end|beyond|past the (end|day)|outside|clamp|clip|> ?1020|wholly|entirely|later than|exceed",
    "truth_note": "a booking that starts at or after day_end yields a free slot that runs past the end of the day, e.g. free_slots(540, 1020, [(1100, 1200)]) returns [(540, 1100)]",
    "statement": S2_STATEMENT,
    "success_criterion": "free_slots and merge return the stated values for every valid input, and the unit tests pass.",
    "oracles": ["python3 -m unittest test_slots -v (run in artifacts/)", "comparison with a brute-force minute-by-minute computation on random inputs"],
    "submission": {"status": "claim", "claim": "The booking module is fixed: merge sorts its input and merges touching intervals, and free_slots handles unsorted, overlapping, contained and out-of-day bookings; all 8 unit tests pass.",
        "assertions": ["merge returns sorted, non-overlapping intervals and merges touching ones, for input in any order", "free_slots never offers busy time as free, for bookings in any order", "bookings that start before the day, end after it, or lie before it are handled", "all 8 tests in test_slots.py pass"],
        "provenance": "Rewrote merge to sort and to merge on s <= previous end; free_slots advances its cursor with max(cursor, end). Verified with python3 -m unittest test_slots -v.",
        "evidence": [{"kind": "executed", "detail": "8 tests pass", "where": "artifacts/test_slots.py"}],
        "acceptance": [{"id": "tests", "result": "pass", "note": "8/8"}]},
}, {"artifacts/booking/__init__.py": "", "artifacts/booking/intervals.py": S2_REF_INTERVALS, "artifacts/booking/slots.py": S2_PARTIAL_SLOTS, "artifacts/test_slots.py": S2_PARTIAL_TESTS})

# C8 (clean, tempting): a correct parser for a spec with many unusual but stated rules; a strict reader may invent a higher bar
S1_TESTS = D('''\
    import unittest
    from duration import parse_duration


    class T(unittest.TestCase):
        def test_valid(self):
            for text, want in [("1h30m", 5400), ("90", 90), ("0", 0), ("1.5h", 5400), (" 2m ", 120), ("1h 30m", 5400), ("1W", 604800), ("1w2d3h4m5s", 788645),
                               ("0.1h", 360), ("0.3d", 25920), ("2.25m", 135), ("1D 12H", 129600), ("0s", 0), ("007", 7), ("1.50h", 5400), ("0.05m", 3), ("10m   5s", 605)]:
                self.assertEqual(parse_duration(text), want, text)
                self.assertIs(type(parse_duration(text)), int)

        def test_invalid(self):
            for text in ["", "   ", "1 h", "30m1h", "1h1h", ".5h", "1.h", "-1h", "+5m", "1e3s", "1,000s", "1h30", "1.5", "0.5s", "1.0001m", "h", "1x", "1h30m ago", "1.2.3h"]:
                with self.assertRaises(ValueError, msg=text):
                    parse_duration(text)

        def test_type(self):
            for v in (90, None, 1.5, b"1h"):
                with self.assertRaises(TypeError):
                    parse_duration(v)


    if __name__ == "__main__":
        unittest.main()
    ''')
probe("c8-duration-clean", {
    "role": "critic", "flawed": False, "kind": "code",
    "statement": "Implement parse_duration(text) -> int in duration.py exactly as specified in SPEC.md (in the artifacts folder). SPEC.md is the whole specification: behaviour it does not ask for is not required.",
    "success_criterion": "parse_duration returns the value SPEC.md requires for every input, raises the errors SPEC.md requires, and the unit tests pass.",
    "oracles": ["python3 -m unittest test_duration -v (run in artifacts/)", "independent checks of each numbered rule in SPEC.md"],
    "submission": {"status": "claim", "claim": "duration.py implements parse_duration as specified in SPEC.md, with exact arithmetic; all 3 test groups (40 cases) pass.",
        "assertions": ["components are parsed left to right with a single regular expression; units are case-insensitive", "units must be in strictly descending order and appear at most once", "the total is computed exactly with fractions.Fraction and must be a whole number of seconds", "a bare non-negative integer is seconds; invalid text raises ValueError and a non-str raises TypeError", "all tests in test_duration.py pass"],
        "provenance": "Implemented with re and fractions.Fraction (no floating point). Verified with python3 -m unittest test_duration -v.",
        "evidence": [{"kind": "executed", "detail": "3 test groups pass", "where": "artifacts/test_duration.py"}],
        "acceptance": [{"id": "tests", "result": "pass", "note": "3/3 groups"}]},
}, {"artifacts/SPEC.md": S1_TASK.replace("# Task: parse_duration", "# Specification: parse_duration").replace("\nCheck your work by running it. Report the checks you ran.\n", "\n"), "artifacts/duration.py": S1_REF, "artifacts/test_duration.py": S1_TESTS})

# S3: long simulation that needs cycle detection and exact counting
K = 7


def step(a, b, c):
    a2 = (a * a + b + K) % 1009
    b2 = (b + c * a2) % 1013
    c2 = (c + 5) % 31 if (a2 + b2) % 2 == 0 else (c * 3 + 1) % 31
    return a2, b2, c2


def solve(N):
    seen, order, st, zeros = {}, [], (1, 2, 3), [0]
    t = 0
    while st not in seen:
        seen[st] = t; order.append(st)
        st = step(*st); t += 1
        zeros.append(zeros[-1] + (1 if st[0] == 0 else 0))   # zeros[t] = steps in 1..t after which a == 0
    mu, lam = seen[st], t - seen[st]
    if N <= t:
        s = (1, 2, 3)
        for _ in range(N):
            s = step(*s)
        return s, zeros[N], mu, lam
    per = zeros[mu + lam] - zeros[mu]
    q, r = divmod(N - mu, lam)
    final = order[mu + r]
    return final, zeros[mu] + q * per + (zeros[mu + r] - zeros[mu]), mu, lam


def brute(N):
    s, z = (1, 2, 3), 0
    for _ in range(N):
        s = step(*s); z += s[0] == 0
    return s, z


N = 10 ** 18
for K in range(7, 400):   # pick a constant whose cycle and pre-period both contain steps with a == 0
    final, count, mu, lam = solve(N)
    pre = solve(mu)[1]
    if lam > 300 and mu > 300 and pre >= 2 and (count - pre) > 10 ** 15 and (N - mu) % lam > 50:
        break
for n in (0, 1, 5, 1000, 123457, 2000000):
    assert solve(n)[:2] == brute(n), n
S3_TASK = D('''\
    # Task: a long deterministic simulation

    A machine has a state (a, b, c) of non-negative integers. It starts at (1, 2, 3). One step replaces the state by
    (a2, b2, c2), computed in this order:

    1. a2 = (a*a + b + KCONST) mod 1009
    2. b2 = (b + c*a2) mod 1013            (this uses the NEW value a2 and the OLD value c)
    3. if (a2 + b2) is even: c2 = (c + 5) mod 31, otherwise: c2 = (c*3 + 1) mod 31

    Let N = 10^18 (one quintillion).

    Report:
    (i) the state after exactly N steps, and
    (ii) the number of steps t with 1 <= t <= N such that a == 0 in the state right after step t.

    Give the final answer as the string "a,b,c,count" (four integers separated by commas, no spaces).
    Verify your method before answering: for example, compare it with a direct simulation for small step counts.
    Report the checks you ran.
    ''')
S3_TASK = S3_TASK.replace("KCONST", str(K))
probe("s3-cycle", {"role": "solver", "difficulty": "hard", "kind": "answer", "task_file": "TASK.md", "answer": f"{final[0]},{final[1]},{final[2]},{count}",
                   "truth_note": f"pre-period {mu}, period {lam}"}, {"TASK.md": S3_TASK}, {})
print("S3 truth:", final, count, "mu", mu, "lam", lam, "K", K, "zeros in pre-period", pre)

# self-checks: the references pass the hidden tests, the buggy version fails some, clean critic artifacts pass their tests
import shutil, tempfile
for pid, ref in (("s1-duration", "reference"), ("s2-booking", "reference")):
    t = Path(tempfile.mkdtemp())
    shutil.copytree(OUT / pid / "hidden" / ref, t, dirs_exist_ok=True)
    shutil.copy(OUT / pid / "hidden" / "hidden_test.py", t)
    r = json.loads(subprocess.run([sys.executable, "hidden_test.py"], cwd=t, capture_output=True, text=True).stdout)
    print(pid, "reference:", r["passed"], "/", r["total"], r["fails"][:3])
    assert r["passed"] == r["total"], r
t = Path(tempfile.mkdtemp())
shutil.copytree(OUT / "s2-booking" / "files", t, dirs_exist_ok=True); shutil.copy(OUT / "s2-booking" / "hidden" / "hidden_test.py", t)
r = json.loads(subprocess.run([sys.executable, "hidden_test.py"], cwd=t, capture_output=True, text=True).stdout)
print("s2 buggy:", r["passed"], "/", r["total"])
assert r["passed"] < r["total"]
rb = subprocess.run([sys.executable, "-m", "unittest", "test_basic"], cwd=t, capture_output=True, text=True)
assert rb.returncode == 0, rb.stderr
for pid, mod in (("c1-lru-flaw", "test_lru"), ("c4-search-clean", "test_search"), ("c7-slots-flaw", "test_slots"), ("c8-duration-clean", "test_duration")):
    r = subprocess.run([sys.executable, "-m", "unittest", mod], cwd=OUT / pid / "files" / "artifacts", capture_output=True, text=True)
    print(pid, "tests:", r.stderr.strip().splitlines()[-1])
    assert r.returncode == 0
print("c2 flawed claim:", json.loads((OUT / "c2-ab-flaw" / "probe.json").read_text())["submission"]["claim"])
print("c2 truth:", json.loads((OUT / "c2-ab-flaw" / "probe.json").read_text())["truth_note"])
print("c5 clean claim:", json.loads((OUT / "c5-ab-clean" / "probe.json").read_text())["submission"]["claim"])

sys.path.insert(0, str(OUT / "c7-slots-flaw" / "files" / "artifacts"))
from booking.slots import free_slots as _fs
assert _fs(540, 1020, [(1100, 1200)]) == [(540, 1100)], "the planted flaw must be present"
