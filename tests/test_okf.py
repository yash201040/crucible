#!/usr/bin/env python3
"""Tests of the knowledge bundle about the host and of its tool (scripts/crucible_okf.py). No network, no model.
    python3 tests/test_okf.py"""
import hashlib, io, json, contextlib, sys, tempfile, unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import crucible_okf as k          # noqa: E402

REAL = REPO / "knowledge" / "claude-code"
FM = {"type": "Feature", "title": 'A "quoted" title: with a colon', "description": "One sentence.", "resource": "https://example.invalid/docs/en/page#part",
      "tags": ["agents", "limits"], "kind": "env_var", "maturity": "experimental", "since": "2.1.300", "surfaces": ["cli", "headless"], "requires": "",
      "identifiers": ["SOME_VAR", "--some-flag", "a\\b"], "orchestration": "high", "generated": {"by": "tool/1", "at": "2026-11-19T20:00:00Z"},
      "verified": [{"by": "process:probe", "at": "2026-11-20T00:00:00Z"}],
      "sources": [{"id": "page", "resource": "https://example.invalid/docs/en/page", "title": "A page: its title"}], "stale_after": "2027-01-19T00:00:00Z"}


class Frontmatter(unittest.TestCase):
    def test_what_is_written_is_read_back_the_same(self):
        fm, body = k.parse_frontmatter(k.dump_frontmatter(FM) + "\n# What it is\n\ntext\n")
        self.assertEqual(fm, FM)
        self.assertEqual(body.strip(), "# What it is\n\ntext")

    def test_a_file_without_frontmatter_is_not_a_concept(self):
        self.assertEqual(k.parse_frontmatter("# just a heading\n")[0], None)


class TheBundle(unittest.TestCase):
    """The bundle in the repository follows OKF 0.2 and this bundle's own rules."""
    def test_it_is_conformant(self):
        self.assertEqual(k.check(REAL), [])

    def test_the_root_index_declares_the_version_and_every_folder_has_an_index(self):
        self.assertTrue((REAL / "index.md").read_text().startswith('---\nokf_version: "0.2"\n---\n'))
        for d in {p.parent for p in REAL.rglob("*.md") if p.name not in k.RESERVED}:
            self.assertTrue((d / "index.md").exists(), d)
            self.assertFalse((d / "index.md").read_text().startswith("---") and d != REAL, d)

    def test_nothing_in_it_names_a_machine(self):
        import getpass
        me = getpass.getuser()      # the documentation's own examples use made-up users; this machine's user must not appear
        for f in list(REAL.rglob("*.md")) + [REAL / "manifest.json"]:
            t = f.read_text()
            self.assertNotIn(f"/Users/{me}", t, f)
            self.assertNotIn(f"/home/{me}", t, f)

    def test_a_name_finds_its_concept(self):
        rels = [r for r, _ in k.find(["CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH"], bundle=REAL)]
        self.assertIn("agents-and-parallel-work/sub-agents/nested-subagents.md", rels)

    def test_the_pin_names_a_release_and_a_hash_per_page(self):
        man = json.loads((REAL / "manifest.json").read_text())
        self.assertRegex(man["documented_release"], r"^\d+\.\d+\.\d+$")
        self.assertTrue(len(man["pages"]) > 150 and all(len(p["sha256"]) == 64 for p in man["pages"]))
        self.assertTrue((REAL / "release" / "pin.md").exists())

    def test_experiments_say_who_confirmed_them(self):
        seen = 0
        for rel, fm, _ in k.concepts(REAL):
            if fm.get("type") == "Experiment":
                seen += 1
                self.assertTrue(fm.get("verified"), rel)
        self.assertTrue(seen >= 5, seen)


class Build(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="crucible-okf-test-"))
        self.stage = self.tmp / "stage"; self.stage.mkdir()
        self.old, k.BUNDLE = k.BUNDLE, self.tmp / "bundle"
        block = lambda path, title: f"=====FILE: {path}=====\n---\ntype: \"Feature\"\ntitle: \"{title}\"\ndescription: \"d\"\norchestration: \"HIGH\"\nmaturity: \"Research Preview\"\nidentifiers:\n  - \"X_VAR\"\nsources:\n  - id: \"p\"\n    resource: \"https://example.invalid/p\"\n---\n\n# What it is\n\nbody\n"
        (self.stage / "a.okf.txt").write_text(block("Cat One/page/first thing.md", "First") + block("cat-one/page/first-thing.md", "Same name again")
                                              + block("too/short.md", "Bad path") + "=====FILE: cat-one/page/no-front.md=====\nno frontmatter here\n")

    def tearDown(self):
        k.BUNDLE = self.old

    def test_staging_files_become_concepts_with_indexes_and_problems_are_listed(self):
        (k.BUNDLE / "experiments").mkdir(parents=True)
        (k.BUNDLE / "experiments" / "mine.md").write_text(k.dump_frontmatter({**FM, "type": "Experiment"}) + "\nkept\n")
        with contextlib.redirect_stdout(io.StringIO()) as out:
            k.build(self.stage, self.tmp, "2026-11-19T20:00:00Z", "2027-01-19T00:00:00Z")
        rep = json.loads(out.getvalue())
        self.assertEqual(rep["concepts"], 2)
        self.assertEqual(len(rep["problems"]), 2)
        fm, _ = k.parse_frontmatter((k.BUNDLE / "cat-one" / "page" / "first-thing.md").read_text())
        self.assertEqual((fm["orchestration"], fm["maturity"], fm["generated"]["at"]), ("high", "research-preview", "2026-11-19T20:00:00Z"))
        self.assertTrue((k.BUNDLE / "cat-one" / "page" / "first-thing-2.md").exists())      # the same name twice: both kept
        self.assertTrue((k.BUNDLE / "experiments" / "mine.md").exists())                     # our own folders survive a build
        self.assertIn("[First](first-thing.md) - d **[high]**", (k.BUNDLE / "cat-one" / "page" / "index.md").read_text())
        self.assertEqual(k.check(k.BUNDLE), [])


class Refresh(unittest.TestCase):
    """What changed since the pin: found from hashes and release numbers, without touching the bundle."""
    PAGE = lambda self, name, text: f"# {name}\nSource: https://example.invalid/docs/en/{name}\n\n{text}\n"

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="crucible-okf-refresh-"))
        self.old, k.BUNDLE = k.BUNDLE, self.tmp / "bundle"
        (k.BUNDLE / "cat" / "alpha").mkdir(parents=True)
        (k.BUNDLE / "cat" / "alpha" / "c.md").write_text(k.dump_frontmatter(FM) + "\nbody\n")
        a, b = self.PAGE("alpha", "old text"), self.PAGE("beta", "same")
        h = lambda s: hashlib.sha256(s.encode()).hexdigest()
        (k.BUNDLE / "manifest.json").write_text(json.dumps({"documented_release": "2.1.10", "fetched_at": "t", "pages": [
            {"url": "https://example.invalid/docs/en/alpha", "page": "alpha", "sha256": h(a)}, {"url": "https://example.invalid/docs/en/beta", "page": "beta", "sha256": h(b)},
            {"url": "https://example.invalid/docs/en/gone", "page": "gone", "sha256": "0" * 64}]}))
        self.live = (self.PAGE("alpha", "new text") + b + self.PAGE("gamma", "a new page")
                     + "# Changelog\nSource: https://example.invalid/docs/en/changelog\n\n**2.1.12**\n\nNovember 2, 2026\n\n* Added x\n\n**2.1.11**\n\nNovember 1, 2026\n\n* Added y\n\n**2.1.10**\n\nOctober 30, 2026\n\n* Added z\n")
        self.get, k._get = k._get, lambda url: self.live

    def tearDown(self):
        k.BUNDLE, k._get = self.old, self.get

    def test_changed_new_and_removed_pages_and_newer_releases(self):
        before = (k.BUNDLE / "manifest.json").read_text()
        with contextlib.redirect_stdout(io.StringIO()) as out:
            k.refresh(self.tmp / "cache")
        r = json.loads(out.getvalue())
        self.assertEqual((r["pages_changed"], r["pages_new"], r["pages_removed"]), (["alpha"], ["en/changelog", "en/gamma"], ["gone"]))
        self.assertEqual(r["releases_since_pin"], ["2.1.12", "2.1.11"])
        self.assertEqual(r["concepts_of_changed_pages"], 1)
        self.assertIn("Added x", Path(r["release_notes_since_pin"]).read_text())
        self.assertEqual((k.BUNDLE / "manifest.json").read_text(), before)                    # the bundle is not touched


if __name__ == "__main__":
    unittest.main(verbosity=1)
