#!/usr/bin/env python3
"""crucible_okf.py: the knowledge bundle about the host (Claude Code), in Open Knowledge Format 0.2.

The bundle lives in knowledge/claude-code/: one markdown file per concept, YAML frontmatter, `index.md` per folder.
It records what the host can do, from its official documentation, pinned to one release, so that a review of crucible
can ask "what does the host offer that we do not use" and, after an update, "what changed since the pin".

  crucible_okf.py find <words...> [--high]      concepts whose title, names, tags or description match every word
  crucible_okf.py list [--orchestration high] [--category C] [--maturity M] [--crucible S]
  crucible_okf.py show <concept path>            print one concept
  crucible_okf.py check                          conformance with OKF 0.2 and this bundle's own rules
  crucible_okf.py stats
  crucible_okf.py index                          write every folder's index.md again (after adding concepts by hand)
  crucible_okf.py refresh [--cache DIR]          download the documentation again, say which pages changed since the
                                                 pin and which releases are new (changes nothing in the bundle)
  crucible_okf.py build <stage dir> --docs DIR   (maintainer) turn readers' staging files into the bundle

Needs no package. `build` uses PyYAML when it is installed, because readers' files are less regular than the bundle.
The documentation text itself is never stored in the bundle: only our own notes on it, with a link and a hash per page.
"""
import hashlib, json, os, re, sys, time, urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BUNDLE = Path(os.environ.get("CRUCIBLE_OKF") or REPO / "knowledge" / "claude-code")
CACHE = Path(os.environ.get("CRUCIBLE_OKF_CACHE") or Path.home() / ".crucible" / "cache" / "claude-code-docs")
INDEX_URL = "https://code.claude.com/docs/llms.txt"
FULL_URL = "https://code.claude.com/docs/llms-full.txt"
RESERVED = {"index.md", "log.md"}
TYPES = ["Feature", "Reference", "Limit", "Concept", "Guide", "Release Digest", "Release Pin", "Experiment", "Playbook"]
KINDS = ["env_var", "setting", "cli_flag", "slash_command", "tool", "hook", "frontmatter", "file", "api", "ui", "behavior", "limit", "mixed"]
MATURITY = ["experimental", "beta", "preview", "research-preview", "deprecated", "unlabelled"]
RELEVANCE = ["high", "medium", "low", "none"]
ORDER = ["type", "title", "description", "resource", "tags", "kind", "maturity", "since", "surfaces", "requires", "identifiers", "orchestration",
         "crucible", "status", "generated", "verified", "sources", "stale_after"]


# ---------- frontmatter: a small reader for the regular form this script writes, and the writer ----------

def _scalar(s: str):
    s = s.strip()
    if s.startswith('"'):
        return json.loads(s)
    if s.startswith("[") or s.startswith("{"):
        return _flow(s)
    return s


def _flow(s: str):
    """Flow lists and mappings as this script writes them: JSON, except that mapping keys and plain words are bare."""
    j = re.sub(r'([{,]\s*)([A-Za-z_][A-Za-z0-9_]*)\s*:', r'\1"\2":', s)
    try:
        return json.loads(j)
    except ValueError:
        inner = s.strip()[1:-1].strip()
        return [x.strip().strip('"') for x in inner.split(",") if x.strip()] if s.strip().startswith("[") else {}


def parse_frontmatter(text: str):
    """(frontmatter dict, body) or (None, text). Reads the regular form only: `key: value`, flow values, and block lists
    of quoted strings or of flow mappings / `- key: value` groups."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, text
    fm, body = {}, text[end + 5:]
    key = None
    for line in text[4:end].split("\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2)
            fm[key] = [] if val == "" else _scalar(val)
            continue
        m = re.match(r"^\s+-\s+(.*)$", line)
        if m and key is not None and isinstance(fm.get(key), list):
            item = m.group(1).strip()
            km = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", item)
            fm[key].append({km.group(1): _scalar(km.group(2))} if km and not item.startswith('"') else _scalar(item))
            continue
        m = re.match(r"^\s+([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if m and key is not None and isinstance(fm.get(key), list) and fm[key] and isinstance(fm[key][-1], dict):
            fm[key][-1][m.group(1)] = _scalar(m.group(2))
    return fm, body


def _q(v) -> str:
    return json.dumps("" if v is None else str(v), ensure_ascii=False)


def _flowmap(d: dict) -> str:
    return "{ " + ", ".join(f"{k}: {_q(v)}" for k, v in d.items()) + " }"


def dump_frontmatter(fm: dict) -> str:
    out = ["---"]
    keys = [k for k in ORDER if k in fm] + sorted(k for k in fm if k not in ORDER)
    for k in keys:
        v = fm[k]
        if k in ("tags", "surfaces"):
            out.append(f"{k}: [{', '.join(str(x) for x in v)}]")
        elif k == "identifiers":
            out.append("identifiers: []" if not v else "identifiers:\n" + "\n".join(f"  - {_q(x)}" for x in v))
        elif k == "generated" and isinstance(v, dict):
            out.append(f"generated: {_flowmap(v)}")
        elif k == "verified":
            vs = v if isinstance(v, list) else [v]
            out.append("verified:\n" + "\n".join(f"  - {_flowmap(x)}" for x in vs))
        elif k == "sources":
            lines = ["sources:"]
            for s in v:
                items = list(s.items())
                lines.append(f"  - {items[0][0]}: {_q(items[0][1])}")
                lines += [f"    {a}: {_q(b)}" for a, b in items[1:]]
            out.append("\n".join(lines))
        elif isinstance(v, (list, dict)):
            out.append(f"{k}: {json.dumps(v, ensure_ascii=False)}")
        else:
            out.append(f"{k}: {_q(v)}")
    return "\n".join(out) + "\n---\n"


# ---------- reading the bundle ----------

def concepts(bundle: Path = None):
    bundle = bundle or BUNDLE
    for f in sorted(bundle.rglob("*.md")):
        if f.name in RESERVED:
            continue
        fm, body = parse_frontmatter(f.read_text())
        yield f.relative_to(bundle).as_posix(), fm, body


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9.]+", "-", str(s).lower()).strip("-")


def check(bundle: Path = None) -> list:
    """OKF 0.2 conformance (every concept has parseable frontmatter with a type; index files have none, except
    okf_version at the root) and this bundle's own rules. Returns a list of problems."""
    bundle = bundle or BUNDLE
    bad, seen = [], 0
    for rel, fm, body in concepts(bundle):
        seen += 1
        if fm is None:
            bad.append(f"{rel}: no parseable frontmatter"); continue
        if not str(fm.get("type") or "").strip():
            bad.append(f"{rel}: no type")
        if fm.get("type") not in TYPES:
            bad.append(f"{rel}: type {fm.get('type')!r} is not one this bundle uses")
        for k in ("title", "description"):
            if not str(fm.get(k) or "").strip():
                bad.append(f"{rel}: no {k}")
        if fm.get("orchestration") not in RELEVANCE:
            bad.append(f"{rel}: orchestration {fm.get('orchestration')!r}")
        if not isinstance(fm.get("generated"), dict) or not fm["generated"].get("by"):
            bad.append(f"{rel}: generated.by missing")
        for s in fm.get("sources") or []:
            if not isinstance(s, dict) or not s.get("resource"):
                bad.append(f"{rel}: a source without a resource")
        if not body.strip():
            bad.append(f"{rel}: empty body")
    for f in bundle.rglob("index.md"):
        t = f.read_text()
        if t.startswith("---\n") and f.parent != bundle:
            bad.append(f"{f.relative_to(bundle)}: only the root index may carry frontmatter")
    if not seen:
        bad.append("the bundle holds no concept")
    return bad


def _match(fm, rel, words) -> bool:
    hay = " ".join([rel, str(fm.get("title", "")), str(fm.get("description", "")), " ".join(map(str, fm.get("tags") or [])),
                    " ".join(map(str, fm.get("identifiers") or []))]).lower()
    return all(w.lower() in hay for w in words)


def find(words, high=False, bundle=None) -> list:
    rows = []
    for rel, fm, _ in concepts(bundle):
        if fm and _match(fm, rel, words) and (not high or fm.get("orchestration") == "high"):
            rows.append((rel, fm))
    return rows


def _line(rel, fm) -> str:
    flags = [fm.get("orchestration", "?")]
    if fm.get("maturity") not in (None, "", "unlabelled"):
        flags.append(fm["maturity"])
    if fm.get("crucible"):
        flags.append("crucible:" + fm["crucible"])
    if fm.get("verified"):
        flags.append("tested")
    return f"{rel}  [{', '.join(flags)}]\n    {fm.get('title', '')}: {fm.get('description', '')}"


# ---------- building it from readers' staging files ----------

def _yaml_load(text: str):
    try:
        import yaml
        return yaml.safe_load(text)
    except ImportError:
        return parse_frontmatter("---\n" + text + "\n---\n")[0]
    except Exception:
        return None


def _as_list(v):
    if v is None or v == "":
        return []
    return [str(x) for x in v] if isinstance(v, list) else [str(v)]


def _pick(v, allowed, default):
    v = str(v or "").strip().lower().replace(" ", "-").replace("_", "-")
    alias = {"research-preview": "research-preview", "ga": "unlabelled", "stable": "unlabelled", "none": "unlabelled", "": default}
    v = alias.get(v, v)
    for a in allowed:
        if v == a.lower().replace("_", "-"):
            return a
    return default


def split_stage(stage: Path) -> tuple:
    """Every `=====FILE: path=====` block of every staging file -> {path: (frontmatter, body, staging file)}, and problems."""
    out, bad = {}, []
    for f in sorted(stage.glob("*.okf.txt")):
        parts = re.split(r"(?m)^=====FILE:\s*(.+?)\s*=====\s*$", f.read_text())
        for i in range(1, len(parts), 2):
            rel, block = parts[i].strip().lstrip("/"), parts[i + 1].strip("\n") + "\n"
            m = re.match(r"(?s)^---\n(.*?)\n---\n?(.*)$", block)
            if not m:
                bad.append(f"{f.name}: {rel}: no frontmatter block"); continue
            fm = _yaml_load(m.group(1))
            if not isinstance(fm, dict):
                bad.append(f"{f.name}: {rel}: frontmatter does not parse"); continue
            segs = [_slug(s) for s in rel[:-3].split("/")] if rel.endswith(".md") else []
            if len(segs) != 3 or not all(segs) or segs[-1] in ("index", "log"):
                bad.append(f"{f.name}: {rel}: path is not <category>/<page>/<concept>.md"); continue
            rel = "/".join(segs) + ".md"
            n = 2
            while rel in out:
                rel = "/".join(segs[:-1] + [f"{segs[-1]}-{n}"]) + ".md"; n += 1
            out[rel] = (fm, m.group(2).strip() + "\n", f.name)
    return out, bad


def normalise(fm: dict, at: str, stale: str) -> dict:
    g = fm.get("generated") if isinstance(fm.get("generated"), dict) else {}
    src = [s for s in (fm.get("sources") or []) if isinstance(s, dict) and s.get("resource")]
    d = {"type": fm.get("type") if fm.get("type") in TYPES else "Feature",
         "title": str(fm.get("title") or "").strip(), "description": " ".join(str(fm.get("description") or "").split()),
         "resource": str(fm.get("resource") or (src[0]["resource"] if src else "")),
         "tags": [_slug(t) for t in _as_list(fm.get("tags")) if _slug(t)][:8],
         "kind": _pick(fm.get("kind"), KINDS, "mixed"), "maturity": _pick(fm.get("maturity"), MATURITY, "unlabelled"),
         "since": str(fm.get("since") or "").strip(), "surfaces": [_slug(s) for s in _as_list(fm.get("surfaces")) if _slug(s)],
         "requires": " ".join(str(fm.get("requires") or "").split()), "identifiers": list(dict.fromkeys(_as_list(fm.get("identifiers")))),
         "orchestration": _pick(fm.get("orchestration"), RELEVANCE, "low"),
         "generated": {"by": str(g.get("by") or "claude-code/sonnet-5.5"), "at": str(g.get("at") or at)},
         "sources": [{k: str(v) for k, v in s.items()} for s in src], "stale_after": str(fm.get("stale_after") or stale)}
    return d


IDENT = [("env_var", re.compile(r"`([A-Z][A-Z0-9]+(?:_[A-Z0-9]+)+)`")), ("cli_flag", re.compile(r"`(--[a-z][a-z0-9-]+)")),
         ("slash_command", re.compile(r"`(/[a-z][a-z0-9-]{2,})`"))]


def page_identifiers(text: str) -> dict:
    return {k: sorted(set(rx.findall(text))) for k, rx in IDENT}


def write_indexes(bundle: Path, okf_version="0.2"):
    """`index.md` in every folder: its concepts with their descriptions, and its subfolders with a count."""
    info = {}
    for rel, fm, _ in concepts(bundle):
        info[rel] = fm or {}
    dirs = sorted({p.parent for p in bundle.rglob("*.md") if p.name not in RESERVED} | {bundle}, key=lambda p: len(p.parts), reverse=True)
    count = {}
    for d in dirs:
        count[d] = sum(1 for r in info if (bundle / r).is_relative_to(d))
    for d in dirs:
        L = []
        subs = sorted(x for x in d.iterdir() if x.is_dir() and count.get(x))
        files = sorted(x for x in d.glob("*.md") if x.name not in RESERVED)
        rel = d.relative_to(bundle).as_posix()
        head = "Claude Code knowledge bundle" if d == bundle else rel
        if d == bundle:
            L += ["---", f'okf_version: "{okf_version}"', "---", ""]
        L += [f"# {head}", ""]
        for s in subs:
            high = sum(1 for r, fm in info.items() if (bundle / r).is_relative_to(s) and fm.get("orchestration") == "high")
            L.append(f"* [{s.name}]({s.name}/) - {count[s]} concept(s), {high} of high relevance to orchestration")
        if subs and files:
            L += ["", "# Concepts", ""]
        for f in files:
            fm = info.get(f.relative_to(bundle).as_posix(), {})
            mark = "" if fm.get("orchestration") != "high" else " **[high]**"
            L.append(f"* [{fm.get('title') or f.stem}]({f.name}) - {fm.get('description', '')}{mark}")
        (d / "index.md").write_text("\n".join(L) + "\n")


def build(stage: Path, docs: Path, at: str, stale: str, keep=("release", "experiments", "playbooks")) -> int:
    """Readers' staging files -> the bundle. Folders named in `keep` are ours and are never replaced by a build."""
    found, bad = split_stage(stage)
    BUNDLE.mkdir(parents=True, exist_ok=True)
    for d in BUNDLE.iterdir():      # replace what a build owns
        if d.is_dir() and d.name not in keep:
            import shutil
            shutil.rmtree(d)
    for rel, (fm, body, _) in found.items():
        f = BUNDLE / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(dump_frontmatter(normalise(fm, at, stale)) + "\n" + body)
    write_indexes(BUNDLE)
    report = {"concepts": len(found), "problems": bad, "from_staging_files": len(list(stage.glob("*.okf.txt")))}
    tree = docs / "tree.json"
    if tree.exists():      # coverage: names in a page that no concept of that page lists
        pages = [t for t in json.loads(tree.read_text()) if t.get("bytes")]
        names = {}
        for rel, (fm, body, _) in found.items():
            names.setdefault(rel.split("/")[1], set()).update(_as_list(fm.get("identifiers")))
            names[rel.split("/")[1]].update(re.findall(r"`([^`\n]+)`", body))
        allnames = set().union(*names.values()) if names else set()
        miss, nopage = {}, []
        for t in pages:
            page = t["slug"].replace("__", "-")
            if t["slug"] == "changelog":
                continue
            if page not in names:
                nopage.append(page); continue
            ids = page_identifiers((docs / "pages" / f"{t['slug']}.md").read_text())
            have = " ".join(names[page])
            m = [x for k in ids for x in ids[k] if x not in have]
            if m:
                miss[page] = {"missing": m, "of": sum(len(v) for v in ids.values()), "nowhere": [x for x in m if not any(x in n for n in allnames)]}
        report["pages_without_concepts"] = nopage
        report["names_missing_from_their_page"] = {p: f"{len(v['missing'])} of {v['of']}" for p, v in sorted(miss.items(), key=lambda kv: -len(kv[1]["missing"]))}
        report["names_in_no_concept"] = sorted({x for v in miss.values() for x in v["nowhere"]})
        (stage / "coverage.json").write_text(json.dumps(miss, indent=1))
    print(json.dumps(report, indent=1)[:6000])
    return 0


# ---------- the pin, and what changed since ----------

def _get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "docs-indexer"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read().decode("utf-8", "replace")


def split_pages(full: str) -> dict:
    ms = list(re.finditer(r"(?m)^# (.+)\nSource: (https://\S+)\n", full))
    return {m.group(2): full[m.start(): ms[i + 1].start() if i + 1 < len(ms) else len(full)] for i, m in enumerate(ms)}


def versions(changelog: str) -> list:
    ms = list(re.finditer(r"(?m)^\*\*(\d+\.\d+\.\d+)\*\*\s*$", changelog))
    out = []
    for i, m in enumerate(ms):
        blk = changelog[m.end(): ms[i + 1].start() if i + 1 < len(ms) else len(changelog)]
        d = re.search(r"(?m)^([A-Z][a-z]+ \d{1,2}, \d{4})\s*$", blk)
        out.append({"version": m.group(1), "date": d.group(1) if d else "", "text": blk.strip()})
    return out


def make_manifest(docs: Path, extra: dict) -> dict:
    """The pin: per documentation page its URL, official place in the documentation's own index, size and hash."""
    tree = [t for t in json.loads((docs / "tree.json").read_text()) if t.get("bytes")]
    vs = versions((docs / "pages" / "changelog.md").read_text())
    return {"about": "The documentation the bundle was built from. `crucible_okf.py refresh` compares the live documentation with this.",
            "index": INDEX_URL, "full": FULL_URL, **extra, "documented_release": vs[0]["version"], "documented_release_date": vs[0]["date"],
            "pages": [{"url": (t["url"][:-3] if t["url"].endswith(".md") else t["url"]), "page": t["slug"].replace("__", "-"), "title": t["title"],
                       "official": t["path"], "bytes": t["bytes"], "sha256": t["sha256"]} for t in tree]}


def refresh(cache: Path = None) -> int:
    cache = cache or CACHE
    man = json.loads((BUNDLE / "manifest.json").read_text())
    cache.mkdir(parents=True, exist_ok=True)
    full = _get(FULL_URL)
    (cache / "llms-full.txt").write_text(full)
    (cache / "llms.txt").write_text(_get(INDEX_URL))
    live = {(u[:-3] if u.endswith(".md") else u): b for u, b in split_pages(full).items()}
    old = {p["url"]: p for p in man["pages"]}
    changed = [u for u in old if u in live and hashlib.sha256(live[u].encode()).hexdigest() != old[u]["sha256"]]
    cl = next((b for u, b in live.items() if u.endswith("/changelog")), "")
    tup = lambda v: tuple(int(x) for x in v.split("."))
    newer = [v for v in versions(cl) if tup(v["version"]) > tup(man["documented_release"])]
    (cache / "releases-since-pin.md").write_text("\n\n".join(f"**{v['version']}** ({v['date']})\n\n{v['text']}" for v in newer))
    print(json.dumps({"pinned_release": man["documented_release"], "pinned_at": man.get("fetched_at"), "live_release": versions(cl)[0]["version"] if cl else None,
                      "releases_since_pin": [v["version"] for v in newer], "release_notes_since_pin": str(cache / "releases-since-pin.md"),
                      "pages_changed": sorted(old[u]["page"] for u in changed if not u.endswith("/changelog")),
                      "pages_new": sorted(u.rsplit("/docs/", 1)[-1] for u in live if u not in old),
                      "pages_removed": sorted(old[u]["page"] for u in old if u not in live),
                      "concepts_of_changed_pages": sum(1 for rel, fm, _ in concepts() if rel.split("/")[1] in {old[u]["page"] for u in changed}),
                      "live_text": str(cache / "llms-full.txt"),
                      "next": "read the release notes since the pin first; then re-read only the changed and new pages and update their concepts"}, indent=1))
    return 0


def main(argv) -> int:
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__); return 0
    global BUNDLE
    if "--bundle" in argv:      # work on another bundle folder (tests, a trial build)
        i = argv.index("--bundle"); BUNDLE = Path(argv[i + 1]); argv = argv[:i] + argv[i + 2:]
    cmd, rest = argv[1], argv[2:]
    opt = lambda name, d=None: (rest[rest.index(name) + 1] if name in rest and rest.index(name) + 1 < len(rest) else d)
    if cmd == "find":
        words = [w for w in rest if not w.startswith("--")]
        rows = find(words, "--high" in rest)
        print("\n".join(_line(r, fm) for r, fm in rows) or "(nothing matches)")
        return 0
    if cmd == "list":
        want = {"orchestration": opt("--orchestration"), "maturity": opt("--maturity"), "crucible": opt("--crucible")}
        cat = opt("--category")
        for rel, fm, _ in concepts():
            if fm and all(v is None or fm.get(k) == v for k, v in want.items()) and (not cat or rel.startswith(cat.rstrip("/") + "/")):
                print(_line(rel, fm))
        return 0
    if cmd == "show":
        print((BUNDLE / rest[0]).read_text()); return 0
    if cmd == "check":
        bad = check()
        print("\n".join(bad) if bad else f"conformant: {sum(1 for _ in concepts())} concepts"); return 1 if bad else 0
    if cmd == "stats":
        from collections import Counter
        c, o, m, t, s = Counter(), Counter(), Counter(), Counter(), Counter()
        for rel, fm, _ in concepts():
            fm = fm or {}
            c[rel.split("/")[0]] += 1; o[fm.get("orchestration")] += 1; m[fm.get("maturity")] += 1; t[fm.get("type")] += 1; s[fm.get("crucible") or "-"] += 1
        print(json.dumps({"concepts": sum(c.values()), "by_category": dict(c.most_common()), "by_relevance": dict(o), "by_maturity": dict(m),
                          "by_type": dict(t), "by_crucible": dict(s)}, indent=1)); return 0
    if cmd == "index":      # write every folder's index.md again (after adding concepts by hand)
        write_indexes(BUNDLE); print(f"indexes written: {sum(1 for _ in BUNDLE.rglob('index.md'))}"); return 0
    if cmd == "refresh":
        return refresh(Path(opt("--cache")) if opt("--cache") else None)
    if cmd == "build":
        return build(Path(rest[0]), Path(opt("--docs")), opt("--at", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())), opt("--stale", ""))
    print(f"unknown command {cmd}"); return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
