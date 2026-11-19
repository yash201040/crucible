#!/usr/bin/env python3
"""crucible run bookkeeping.

  crucible_run.py save  <workflow-output-file> <runDir> [--transcript DIR] [--run-id wf_...]
                                                          record a finished run: result.json, atlas.md, index.md, registry
  crucible_run.py index <runDir>                          rebuild index.md from result.json + the files on disk
  crucible_run.py list  [N]                               list the last N runs from ~/.crucible/registry.jsonl
  crucible_run.py atlases [cwd]                           print atlas.md paths of earlier runs (for priorAtlases)
  crucible_run.py metrics <runDir> [--transcript DIR]     write metrics.json for a run (finds the journal itself)
  crucible_run.py proposals [all]                         list self-improvement proposals (pending by default)
  crucible_run.py evolve-save <workflow-output-file> <dir>  record a periodic crucible-evolve result
  crucible_run.py install [--host codex]                  Claude Code: copy engine/*.js to ~/.claude/workflows/.
                                                          Codex: write the Codex front desk to ~/.agents/skills/crucible/SKILL.md
  crucible_run.py stage <runDir> [workflow.js] [--profile P]  copy the installed workflow into the run dir; prints {scriptPath, expectVersion, routing}
  crucible_run.py rsi <repoDir>                           the product's improvement file (RSI.md) and its open feedback items, as JSON
  crucible_run.py rsi-init <repoDir>                      create RSI.md and feedback/ in a product repo from the template
  crucible_run.py efficiency [n]                          efficiency of the last n runs (time, parallelism, loops, routes)
  crucible_run.py version                                 the engine version the front desk must pass as expectVersion
  crucible_run.py repo                                    print the framework folder's real path (symlinks resolved)
  crucible_run.py code-mode                               can Claude Code's Code Mode be on in this session, and how to start one with it
  crucible_run.py local                                   this installation's own front-desk notes (~/.crucible/local/front-desk.md), if any
  crucible_run.py history [N]                             runs with metrics and evolve outcomes
  crucible_run.py review-due                              is a periodic self-review due?
  crucible_run.py review-pack [--runs <runDir | file in it | part of its name> ...] [--feedback FILE]
                                                          build the pack for a self-review: the runs named, else every run on the
                                                          current engine version; per run a digest and what the user typed afterwards
  crucible_run.py digest <runDir | name>                  print one run's digest (time, budget, attempts, findings, loops, context)
  crucible_run.py probe-check <pack> [--routes R] [--provider claude|codex] [--dry]
                                                          after a review changed the engine: the probe cases whose prompt changed, on
                                                          the engine before and after; a case that turned wrong is reverted
  crucible_run.py checkpoint <runDir> [--transcript DIR]  write checkpoint.json (every scope's stage) from the journal;
                                                          used to close a stopped run and to continue it later
  crucible_run.py continue-info <handoff.md | runDir>     everything the front desk needs to continue a run

index.md is the address map of a run: every scope's contract, round files (claim / critique /
worklog / artifacts), debunk reviews, appeal and repair, plus the workflow transcript directory
(journal.jsonl + per-agent transcripts). Nothing here is fed back into agents automatically.
Stdlib only.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from pathlib import Path

REGISTRY = Path(os.environ.get("CRUCIBLE_REGISTRY", Path.home() / ".crucible" / "registry.jsonl"))
REPO = Path(__file__).resolve().parent.parent
WORKFLOWS = Path.home() / ".claude" / "workflows"
# This installation's own additions (optional; never in the framework folder): ~/.crucible/local/
#   front-desk.md   extra rules for the front desk (own flags, a paid data tool); printed by `crucible_run.py local`
#   local.json      {"paid_ledger": "<jsonl of paid calls: session, at, cost_usd, status, endpoint>", "fetch_cache": "<dir with <session>/hits.jsonl>",
#                    "data_flags": ["/name"]}   flags that survive stop and continue
LOCAL_DIR = Path(os.environ.get("CRUCIBLE_LOCAL", Path.home() / ".crucible" / "local"))
try:
    LOCAL = json.loads((LOCAL_DIR / "local.json").read_text())
except Exception:
    LOCAL = {}
LEDGER = Path(LOCAL["paid_ledger"]).expanduser() if LOCAL.get("paid_ledger") else None
CACHE = Path(LOCAL["fetch_cache"]).expanduser() if LOCAL.get("fetch_cache") else None
REVIEW_EVERY_DAYS = 7
REVIEW_PENDING_MAX = 10
PROPOSALS = Path(os.environ.get("CRUCIBLE_PROPOSALS", Path.home() / ".crucible" / "proposals"))


def _find_result(obj, depth=0):
    """Find the crucible-engine return object (has runDir + results) anywhere inside obj."""
    if depth > 12:
        return None
    if isinstance(obj, dict):
        if "runDir" in obj and ("results" in obj or obj.get("planOnly")):
            return obj
        for v in obj.values():
            r = _find_result(v, depth + 1)
            if r is not None:
                return r
    elif isinstance(obj, list):
        for v in reversed(obj):
            r = _find_result(v, depth + 1)
            if r is not None:
                return r
    elif isinstance(obj, str) and "runDir" in obj and len(obj) > 20:
        s = obj.strip()
        start = s.find("{")
        if start >= 0:
            try:
                return _find_result(json.loads(s[start:]), depth + 1)
            except Exception:
                # try to cut at the last closing brace
                end = s.rfind("}")
                if end > start:
                    try:
                        return _find_result(json.loads(s[start:end + 1]), depth + 1)
                    except Exception:
                        return None
    return None


def parse_output(path: Path):
    text = path.read_text(errors="replace")
    candidates = []
    try:
        candidates.append(json.loads(text))
    except Exception:
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                candidates.append(json.loads(line))
            except Exception:
                continue
    if not candidates:
        candidates.append(text)
    result = None
    for c in reversed(candidates):
        result = _find_result(c)
        if result is not None:
            break
    m = re.search(r"(~?/[^\s\"']*/subagents/workflows/wf_[A-Za-z0-9_-]+)", text)
    transcript = m.group(1) if m else None
    m2 = re.search(r"\b(wf_[A-Za-z0-9-]{6,})\b", text)
    run_id = m2.group(1) if m2 else None
    return result, transcript, run_id


def _rel(p: Path, base: Path) -> str:
    try:
        return str(p.relative_to(base))
    except ValueError:
        return str(p)


def build_index(run_dir: Path) -> Path:
    res_path = run_dir / "result.json"
    result = json.loads(res_path.read_text()) if res_path.exists() else {}
    meta = json.loads((run_dir / "run-meta.json").read_text()) if (run_dir / "run-meta.json").exists() else {}
    by_id = {r["id"]: r for r in result.get("results", [])}
    lines = [f"# crucible run index", "", f"- run dir: `{run_dir}`"]
    if meta.get("transcriptDir"):
        lines.append(f"- workflow transcripts: `{meta['transcriptDir']}` (journal.jsonl = every agent's return value)")
    if meta.get("workflowRunId"):
        lines.append(f"- workflow run id: `{meta['workflowRunId']}`")
    for name in ("problem.md", "report.md", "atlas.md"):
        if (run_dir / name).exists():
            lines.append(f"- {name}: `{name}`")
    plan_dir = run_dir / "plan"
    if plan_dir.exists():
        lines.append("- plan files: " + ", ".join(f"`{_rel(p, run_dir)}`" for p in sorted(plan_dir.rglob("*")) if p.is_file()))
    for lay in result.get("layers", []) if len(result.get("layers", [])) > 1 else []:
        lines.append(f"- layer {lay.get('layer')} report: `{_rel(Path(lay['report']), run_dir)}` (scopes: {', '.join(lay.get('scopes', []))})")
    plan = result.get("plan", {})
    if plan:
        lines += ["", f"strategy **{plan.get('strategy')}**, tier {plan.get('tier')}, horizon {plan.get('horizon', 'single_pass')}, depth {result.get('depth')}, "
                  f"satisfied={result.get('satisfied')}, stoppedForBudget={result.get('stoppedForBudget')}"]
        if result.get("skipped"):
            lines.append(f"skipped scopes: {', '.join(result['skipped'])}")
    counts = {}
    for r in result.get("results", []):
        counts[r["final"]] = counts.get(r["final"], 0) + 1
    if counts:
        lines.append("status counts: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    lines += ["", "| scope | difficulty | final | pair outcome | rounds | attacker verdicts | debunk | best claim |", "|---|---|---|---|---|---|---|---|"]
    for r in result.get("results", []):
        lines.append(f"| {r['id']} | {r.get('difficulty', '-')} | **{r['final']}** | {r.get('pairOutcome')} | {r.get('rounds')} | "
                     f"{' → '.join(r.get('verdicts', []))} | {', '.join(r.get('debunk', []))}{' (appeal ' + r['appeal'] + ')' if r.get('appeal') else ''} | "
                     f"`{_rel(Path(r['claimPath']), run_dir) if r.get('claimPath') else '-'}` |")
    scopes_dir = run_dir / "scopes"
    if scopes_dir.exists():
        lines += ["", "## Files per scope"]
        for sd in sorted(p for p in scopes_dir.iterdir() if p.is_dir()):
            r = by_id.get(sd.name, {})
            lines += ["", f"### {sd.name}" + (f" [{r.get('final')}]: {r.get('title', '')}" if r else "")]
            if r.get("claim"):
                lines.append(f"> {r['claim'][:400]}")
            for f in sorted(sd.rglob("*")):
                if f.is_file() and "artifacts" not in f.parts:
                    lines.append(f"- `{_rel(f, run_dir)}`")
            arts = [f for f in sd.rglob("*") if f.is_file() and "artifacts" in f.parts]
            if arts:
                lines.append(f"- artifacts: {len(arts)} files under `{_rel(sd, run_dir)}/**/artifacts/`")
    syn = result.get("synthesis") or {}
    if syn:
        lines += ["", "## Synthesis", f"**{syn.get('headline', '')}** (confidence: {syn.get('confidence')})"]
        for item in syn.get("human_review_items", []):
            lines.append(f"- review: {item}")
        for c in syn.get("contradictions", []):
            lines.append(f"- contradiction: {c}")
    out = run_dir / "index.md"
    out.write_text("\n".join(lines) + "\n")
    return out


def _transcripts(meta: dict) -> dict:
    """scope id -> [(label, transcript path)] from the workflow journal."""
    out = {}
    td = meta.get("transcriptDir")
    if not td or not (Path(td) / "journal.jsonl").exists():
        return out
    for line in (Path(td) / "journal.jsonl").read_text(errors="replace").splitlines():
        try:
            e = json.loads(line)
        except Exception:
            continue
        if e.get("type") != "started" or not e.get("label"):
            continue
        parts = e["label"].split(":")
        sid = parts[1] if len(parts) > 1 and parts[0] in {"contract", "solver", "critic", "debunk", "appeal", "repair", "repair-check"} else "_run"
        out.setdefault(sid, []).append((e["label"], str(Path(td) / f"agent-{e.get('agentId')}.jsonl")))
    return out


def _set_aside(f: Path):
    """Keep an earlier session's file (e.g. a closed run's answer) instead of overwriting it."""
    if f.exists():
        stamp = time.strftime("%Y%m%d-%H%M", time.localtime(f.stat().st_mtime))
        dest, n = f.with_name(f"{f.stem}.{stamp}{f.suffix}"), 1
        while dest.exists():
            n += 1
            dest = f.with_name(f"{f.stem}.{stamp}-{n}{f.suffix}")
        f.rename(dest)


def _v43(result: dict) -> bool:
    """Did engine v4.3 or later return this result? Compared as numbers ('v4.10' and 'v5' are later than 'v4.3')."""
    m = re.match(r"v?(\d+)(?:\.(\d+))?", str(result.get("engineVersion") or ""))
    return bool(m) and (int(m.group(1)), int(m.group(2) or 0)) >= (4, 3)


def _before_results(f: Path, result: dict) -> bool:
    """Before v4.3 the synthesizer wrote report.md / crucible-handoff.md itself, after every part's claim file, and the
    closer after the --stop checkpoint (SKILL.md :136-:137). One older than the newest of these was not written by this
    session (e.g. the harness refused the write)."""
    ts = [Path(r["claimPath"]).stat().st_mtime for r in result.get("results") or [] if r.get("claimPath") and Path(r["claimPath"]).is_file()]
    if result.get("closed") and (f.parent / "checkpoint.json").is_file():  # a closer result has results: [] (engine :993)
        ts.append((f.parent / "checkpoint.json").stat().st_mtime)
    return f.exists() and bool(ts) and f.stat().st_mtime < max(ts)


def open_items_appendix(run_dir: Path, result: dict) -> str:
    """Everything the run left open, listed from its records: every blocking finding, every flaw left after a repair, every
    issue between parts, every request nobody answered. A synthesizer chooses what to say; on one run its handoff carried
    about half of the open findings. This list is complete by construction and is appended below its text."""
    res = [r for r in result.get("results") or [] if not r.get("supersededBy")]
    lines = []
    items = (result.get("plan") or {}).get("successItems") or []
    got = {x.get("id"): x for x in (result.get("synthesis") or {}).get("success_items") or [] if isinstance(x, dict)}
    if items:
        lines.append("### Items of the success definition, by owner")
        for it in items:
            g = got.get(it.get("id")) or {}
            lines.append(f"- {it.get('id')} (owner: {it.get('owner')}): {it.get('item')}  -> {g.get('status', 'not judged')}{(': ' + str(g.get('basis'))) if g.get('basis') else ''}")
    per = []
    for r in res:
        blk = [o for o in r.get("open") or [] if o.get("blocking")]
        rest = [o for o in r.get("open") or [] if not o.get("blocking")]
        left = r.get("repairLeft") or {}
        if not (blk or rest or left.get("all") or r.get("caveats") or r.get("final") in ("unconverged", "contested", "flawed", "unreviewed", "failed", "blocked", "not_started")):
            continue
        k = r.get("kept") or {}
        per.append(f"#### {r.get('id')} [{r.get('final')}{', critical' if r.get('critical') else ''}]"
                   + (f" kept version: round {k.get('round')} ({k.get('attempt')})" if k.get("round") else "") + (f"; claim file: {r.get('claimPath')}" if r.get("claimPath") else ""))
        if blk:
            per.append(f"Blocking findings still open ({len(blk)}):")
            per += [f"- {o.get('id')} [{o.get('severity')}{', ' + o['class'] if o.get('class') else ''}] {o.get('issue')} (check: {o.get('check')})" for o in blk]
        if left.get("all"):
            mat = set(left.get("material") or [])
            per.append(f"Flaws left after the repair ({len(left['all'])}, of which material: {len(mat)}):")
            per += [f"- {'[material] ' if f in mat else ''}{f}" for f in left["all"]]
        if rest:
            per.append(f"Findings that do not block ({len(rest)}):")
            per += [f"- {o.get('id')} [{o.get('class') or o.get('severity')}] {o.get('issue')}" for o in rest]
        if r.get("caveats"):
            per.append(f"Review caveats ({len(r['caveats'])}):")
            per += [f"- {c}" for c in r["caveats"]]
    if per:
        lines += ["### Open items per part"] + per
    bnd = [(r.get("id"), b) for r in res for b in r.get("boundaryIssues") or []]
    if bnd:
        lines.append(f"### Issues between parts ({len(bnd)})")
        lines += [f"- {rid} -> {', '.join(b.get('other') or []) or '(no part named)'} [{b.get('kind')}{', found by its check' if b.get('from') == 'check' else ''}]: {b.get('detail')}" for rid, b in bnd]
    board = run_dir / "board"
    if board.is_dir():
        names = {f.name for f in board.glob("*.md")}
        unanswered = sorted(n for n in names if n.startswith("to-") and f"reply--{n}" not in names)
        if unanswered:
            lines.append(f"### Requests between parts that nobody answered ({len(unanswered)}; folder {board})")
            lines += [f"- {n}" for n in unanswered]
    never = list(result.get("skipped") or [])
    if never:
        lines.append("### Parts that never started")
        lines.append("- " + ", ".join(never))
    if not lines:
        return ""
    return "\n\n---\n\n## Complete list of open items (generated from the run's records)\n\nThe text above is the judgment; this list is the full record behind it.\n\n" + "\n".join(lines) + "\n"


def write_outputs(run_dir: Path, result: dict) -> list:
    """v4.3+: the synthesizer and closer return report, user_answer and handoff (the harness refuses subagent writes
    of these files); write them here. Earlier sessions' versions are kept next to them under a dated name."""
    syn = result.get("synthesis") or {}
    written = []
    handoff = syn.get("handoff")
    if handoff and str(handoff).strip():
        try:
            handoff = str(handoff).strip() + open_items_appendix(run_dir, result)
        except Exception as e:  # bookkeeping must never block giving the user their answer
            print(f"the generated list of open items was not appended: {e}")
    outs = [(run_dir / "report.md", syn.get("report")), (run_dir / "answer.md", syn.get("user_answer")), (run_dir / "crucible-handoff.md", handoff)]
    if len(result.get("layers") or []) > 1:
        outs += [(run_dir / "layers" / f"L{lay['layer']}" / "report.md", lay.get("reportText")) for lay in result["layers"]]
    if _v43(result):  # layer reports an earlier session left that this one does not rewrite
        outs += [(f, None) for f in sorted(run_dir.glob("layers/L*/report.md")) if f not in [o[0] for o in outs]]
    for f, text in outs:
        text = str(text).strip() + "\n" if text and str(text).strip() else None
        if text and f.exists() and f.read_text(errors="replace") == text:
            written.append(f)  # save run again on the same output: already this session's
        elif text:
            _set_aside(f)
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(text)
            written.append(f)
        elif f != run_dir / "report.md" and (_v43(result) or (syn.get("inline") and f.name == "answer.md") or _before_results(f, result)):  # report.md: write_inline_report
            # nothing returned for it (no handoff, single-part run, failed or empty synthesizer / closer): since v4.3 only
            # save writes these files, so one that is here is an earlier session's; never leave it under the current name
            _set_aside(f)
    return written


def data_flag(run_dir: Path):
    """Which of this installation's own flags (local.json: data_flags) did the user type for this run? Read only the flag
    lines of problem.md, never the problem or context text. Returns the flag, or None."""
    pf = run_dir / "problem.md"
    if not pf.exists():
        return None
    t = pf.read_text(errors="replace")
    lines = re.findall(r"^# Flags[^\n]*\n([^\n]*)", t, re.M) + re.findall(r"^# Continuation[^\n]*", t, re.M)
    for flag in LOCAL.get("data_flags") or []:
        if any(re.search(r"(?<![\w/-])" + re.escape(flag) + r"\b", l) for l in lines):
            return flag
    return None


def write_inline_report(run_dir: Path, result: dict):
    """Single-scope runs skip the synthesizer agent; write report.md from the result instead."""
    out = run_dir / "report.md"
    syn = result.get("synthesis") or {}
    if str(syn.get("report") or "").strip():
        return None
    if out.exists() and not _v43(result) and not _before_results(out, result):  # old engines had the synthesizer write report.md itself
        return None
    if not result.get("results"):
        _set_aside(out)  # e.g. the closer failed: no report from this session; one that is here is an earlier session's
        return None
    note = ("_Single-scope run: no synthesizer agent; written from the run result._" if syn.get("inline")
            else "_Fallback: the synthesizer did not write report.md; this summary is built from the run result. There is no integrated answer: read the claim files of every part before relying on any of it._")
    head = (syn.get("headline") or result["results"][0].get("claim", "")) if syn.get("inline") else (syn.get("headline") or "(no integrated answer: the synthesizer failed)")
    lines = ["# crucible report", "", note, "",
             f"**Answer:** {head}", "",
             f"Confidence: {syn.get('confidence', '-')}", "",
             "| scope | difficulty | status | rounds | attacker verdicts | debunk | claim file |", "|---|---|---|---|---|---|---|"]
    for r in result["results"]:
        lines.append(f"| {r['id']} | {r.get('difficulty', '-')} | **{r['final']}** | {r.get('rounds')} | {' → '.join(r.get('verdicts', []))} | "
                     f"{', '.join(r.get('debunk', [])) or ('none (trivial: attacker checks only)' if r.get('difficulty') == 'trivial' else '-')} | "
                     f"`{_rel(Path(r['claimPath']), run_dir) if r.get('claimPath') else '-'}` |")
    for item in syn.get("human_review_items", []):
        lines.append(f"- review: {item}")
    text = "\n".join(lines) + "\n"
    if not (out.exists() and out.read_text(errors="replace") == text):  # save run again: this session's report stays
        _set_aside(out)  # v4.3+: a report.md already here is an earlier session's
        out.write_text(text)
    return out


def build_atlas(run_dir: Path) -> Path:
    result = json.loads((run_dir / "result.json").read_text()) if (run_dir / "result.json").exists() else {}
    meta = json.loads((run_dir / "run-meta.json").read_text()) if (run_dir / "run-meta.json").exists() else {}
    tr = _transcripts(meta)
    lines = ["# crucible atlas: explored surfaces", "",
             "Every trajectory of this run, whatever its outcome. Later runs and reviewers read this to avoid",
             "re-exploring settled ground: verified results can be reused, dead ends and debunked claims should not",
             "be retried without a concrete new angle. Full logs: the scope dir files and the raw agent transcripts.",
             f"", f"run: `{run_dir}`", ""]
    for e in result.get("atlas", []):
        lines += [f"## {e['id']} [{e['final']}{', ' + e['difficulty'] if e.get('difficulty') else ''}] {e.get('title', '')}", "",
                  f"- statement: {e.get('statement', '')}", f"- rounds: {e.get('rounds')}",
                  f"- best claim: {e.get('claim') or '(none)'}", f"- dir: `{e.get('dir')}`"]
        if e.get("tried"):
            lines.append("- avenues tried:")
            lines += [f"  - {t}" for t in e["tried"]]
        if e.get("untried"):
            lines.append("- known untried avenues:")
            lines += [f"  - {t}" for t in e["untried"]]
        if e.get("defects"):
            lines.append("- substantive defects raised by critics:")
            lines += [f"  - {t}" for t in e["defects"]]
        if e.get("refutations"):
            lines.append("- debunk refutations:")
            lines += [f"  - {t}" for t in e["refutations"]]
        if tr.get(e["id"]):
            lines.append("- agent transcripts:")
            lines += [f"  - {lab}: `{path}`" for lab, path in tr[e["id"]]]
        lines.append("")
    if tr.get("_run"):
        lines += ["## run-level agents", ""] + [f"- {lab}: `{path}`" for lab, path in tr["_run"]]
    out = run_dir / "atlas.md"
    out.write_text("\n".join(lines) + "\n")
    return out


def prior_atlases(cwd: str | None) -> int:
    if not REGISTRY.exists():
        return 0
    cwd = str(Path(cwd or os.getcwd()).resolve())
    for l in REGISTRY.read_text().splitlines():
        try:
            r = json.loads(l)
        except Exception:
            continue
        a = Path(r["runDir"]) / "atlas.md"
        if a.exists() and (r["runDir"].startswith(cwd) or os.environ.get("CRUCIBLE_HOME", "\0") in r["runDir"]):
            print(f"{a}\t{r.get('savedAt')}\t{r.get('problem', '')}")
    return 0


def _locate_transcript(run_dir: Path):
    """Fallback: find the workflow transcript dir whose journal mentions this run dir (newest first)."""
    base = Path.home() / ".claude" / "projects"
    needle = str(run_dir)
    hits = sorted(base.glob("*/*/subagents/workflows/wf_*/journal.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)
    for j in hits[:200]:
        try:
            if needle in j.read_text(errors="replace"):
                return str(j.parent), j.parent.name
        except Exception:
            continue
    return None, None


SCRIPT_TOOLS = ("REPL",)      # Claude Code's Code Mode: the tool that runs a script which calls the other tools


def _agent_stats(path: Path) -> dict:
    """Token usage (deduplicated per API message), tool calls and wall time of one agent transcript."""
    seen, st = set(), {"input": 0, "cache_write": 0, "cache_read": 0, "output": 0, "tool_calls": 0, "script_calls": 0, "turns": 0, "first": None, "last": None, "model": None, "ctx_peak": 0}
    if not path.exists():
        return st
    for line in path.read_text(errors="replace").splitlines():
        try:
            r = json.loads(line)
        except Exception:
            continue
        ts = r.get("timestamp")
        if ts:
            st["first"] = st["first"] or ts
            st["last"] = ts
        m = r.get("message")
        if r.get("type") != "assistant" or not isinstance(m, dict):
            continue
        for b in m.get("content") or []:
            if isinstance(b, dict) and b.get("type") == "tool_use":
                st["tool_calls"] += 1
                st["script_calls"] += 1 if b.get("name") in SCRIPT_TOOLS else 0   # one script can stand for many tool calls
        mid, u = m.get("id"), m.get("usage") or {}
        if not u or mid in seen:
            continue
        seen.add(mid)
        st["turns"] += 0 if r.get("aggregate") else 1     # one model call: each re-reads the whole context so far
        st["model"] = m.get("model") or st["model"]
        st["input"] += u.get("input_tokens") or 0
        st["cache_write"] += u.get("cache_creation_input_tokens") or 0
        st["cache_read"] += u.get("cache_read_input_tokens") or 0
        st["output"] += u.get("output_tokens") or 0
        # the context this call carried: a solver that grows far past what one session holds had too large a part
        # (a record written by the standalone runner holds totals over the whole agent, which say nothing about that)
        if not r.get("aggregate"):
            st["ctx_peak"] = max(st["ctx_peak"], (u.get("input_tokens") or 0) + (u.get("cache_creation_input_tokens") or 0) + (u.get("cache_read_input_tokens") or 0))
    return st


def _utc_to_local(ts: str) -> str:
    import datetime as dt
    try:
        return dt.datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone().strftime("%Y-%m-%dT%H:%M:%S")
    except Exception:
        return ts or ""


def build_metrics(run_dir: Path, meta: dict, write: bool = True) -> dict:
    """metrics.json: per-agent tokens / tool calls / time, totals by role and phase, failures, paid calls, cache hits."""
    td = meta.get("transcriptDir")
    agents, results, returned = [], {}, {}
    if td and (Path(td) / "journal.jsonl").exists():
        started = []
        for line in (Path(td) / "journal.jsonl").read_text(errors="replace").splitlines():
            try:
                e = json.loads(line)
            except Exception:
                continue
            if e.get("type") == "started":
                started.append(e)
            elif e.get("type") == "result":
                results[e.get("agentId")] = e.get("result") is not None
                returned[e.get("agentId")] = e.get("result")
        for e in started:
            st = _agent_stats(Path(td) / f"agent-{e.get('agentId')}.jsonl")
            label = e.get("label") or "?"
            role = re.sub(r"^L\d+:", "", label).split(":")[0]
            agents.append({"label": label, "role": role, "phase": e.get("phase"), "agentId": e.get("agentId"),
                           "returned": results.get(e.get("agentId"), False), **st})
    tot = lambda xs, k: sum(a[k] for a in xs)
    by = lambda key: {k: {"agents": len(v), "output": tot(v, "output"), "context": tot(v, "input") + tot(v, "cache_write") + tot(v, "cache_read"), "tool_calls": tot(v, "tool_calls")}
                      for k, v in _group(agents, key).items()}
    firsts = [a["first"] for a in agents if a["first"]]
    lasts = [a["last"] for a in agents if a["last"]]
    window = (_utc_to_local(min(firsts)), _utc_to_local(max(lasts))) if firsts else None
    session = Path(td).parts[-4] if td and len(Path(td).parts) >= 4 else None
    paid = {"calls": 0, "cost_usd": 0.0, "failed": 0, "endpoints": {}}
    hits = {"count": 0, "saved_usd": 0.0}
    if window and session:
        if LEDGER and LEDGER.exists():
            for line in LEDGER.read_text(errors="replace").splitlines():
                try:
                    r = json.loads(line)
                except Exception:
                    continue
                if r.get("session") == session and window[0] <= r.get("at", "") <= window[1]:
                    paid["calls"] += 1
                    paid["cost_usd"] += float(r.get("cost_usd") or 0)
                    paid["failed"] += 1 if (r.get("status") or 200) >= 400 else 0
                    paid["endpoints"][r.get("endpoint")] = paid["endpoints"].get(r.get("endpoint"), 0) + 1
        hf = CACHE / session / "hits.jsonl" if CACHE else None
        if hf and hf.exists():
            for line in hf.read_text(errors="replace").splitlines():
                try:
                    r = json.loads(line)
                except Exception:
                    continue
                if window[0] <= r.get("at", "") <= window[1]:
                    hits["count"] += 1
                    hits["saved_usd"] += float(r.get("saved_usd") or 0)
    m = {"agents": agents, "totals": {"agents": len(agents), "returned_nothing": sum(1 for a in agents if not a["returned"]),
                                      "output": tot(agents, "output"), "context": tot(agents, "input") + tot(agents, "cache_write") + tot(agents, "cache_read"),
                                      "tool_calls": tot(agents, "tool_calls"), "window": window},
         "by_role": by("role"), "by_phase": by("phase"), "paid_calls": paid, "cache_hits": hits}
    if write:
        (run_dir / "metrics.json").write_text(json.dumps(m, indent=1))
    if not write:   # a review reads what each agent returned
        m["returned"] = {a["label"]: returned.get(a["agentId"]) for a in agents}
    try:
        m["efficiency"] = build_efficiency(run_dir, agents, {a["label"]: returned.get(a["agentId"]) for a in agents}, write)
    except Exception as e:  # bookkeeping must never block a save
        m["efficiency"] = {"error": str(e)}
    return m


def _epoch(ts):
    import datetime as dt
    try:
        return dt.datetime.fromisoformat(str(ts).replace("Z", "+00:00")).timestamp()
    except Exception:
        return None


SCOPE_ROLES = {"contract", "solver", "critic", "critic2", "referee", "debunk", "appeal", "repair", "repair-check"}


def build_efficiency(run_dir: Path, agents: list, returned: dict, write: bool = True) -> dict:
    """efficiency.json: where the run's time and agent calls went. Three questions: did agents run side by side or wait
    in a chain (time), did parts loop (cost), and did each role run on a model that fit (rework, speed).
    Definitions (each computable from an agent's start, end, tokens, role, part and round):
      wall_s            last end - first start;  stalled_s = time with no agent alive (pause, outage);  active_s = wall_s - stalled_s
      busy_s            sum of agent durations;  mean_live = busy_s / active_s;  peak_live = most agents alive at once
      low_live_share    share of active time with only one or two agents alive (the tail the user sees as a slow run)
      part.span_s       first start to last end of a part's agents;  part.chain_s = sum of its agents' durations
      part.idle_s       time inside the span when none of its agents was alive (waiting for a slot or a prerequisite)
      loop_out_tokens   output tokens of solver and attacker agents after a part's first round (what looping cost)
      first_round_ok    parts whose first attack found no blocking finding, per solver model and per attacker model
      attempts          the solver and attacker agents of the attempts after the serial rounds; "kept" = those of the attempt
                        whose submission became the part's result (the rest of that work was discarded)
      budget            the estimate shown at approval against what was used; parts that never started, critical ones named
      context           the largest context a solver carried (tokens), and the cached tokens re-read over the run
    """
    rows = []
    for a in agents:
        t0, t1 = _epoch(a.get("first")), _epoch(a.get("last"))
        if t0 is None or t1 is None:
            continue
        p = re.sub(r"^L\d+:", "", a["label"]).split(":")
        m = re.search(r"(haiku|sonnet|opus|fable)", a.get("model") or "")
        rows.append({**a, "t0": t0, "t1": max(t1, t0), "part": p[1] if p[0] in SCOPE_ROLES and len(p) > 1 else None,
                     "round": int(p[2][1:]) if len(p) > 2 and re.fullmatch(r"r\d+", p[2]) else None, "m": m.group(1) if m else (a.get("model") or "?")})
    if not rows:
        return {}
    start, end = min(r["t0"] for r in rows), max(r["t1"] for r in rows)
    wall = max(end - start, 1e-9)
    ev = sorted([(r["t0"], 1) for r in rows] + [(r["t1"], -1) for r in rows], key=lambda x: (x[0], x[1]))
    live, peak, last, at = 0, 0, start, {}
    for t, d in ev:
        at[min(live, 3)] = at.get(min(live, 3), 0) + (t - last)
        live += d; peak = max(peak, live); last = t
    busy = sum(r["t1"] - r["t0"] for r in rows)
    # the second half of the run by time: is the tail thin?
    half = start + wall / 2
    tail_busy = sum(max(0, r["t1"] - max(r["t0"], half)) for r in rows)
    active = max(wall - at.get(0, 0), 1e-9)   # time with no agent alive (a pause, an outage, the gap before a resume) is not the run's doing
    tail_stalled, live, last = 0.0, 0, start
    for t, d in ev:
        if live == 0 and t > half:
            tail_stalled += t - max(last, half)
        live += d; last = t
    parts = {}
    for r in rows:
        if r["part"]:
            parts.setdefault(r["part"], []).append(r)
    part_rows = []
    for pid, rs in parts.items():
        s0, s1 = min(r["t0"] for r in rs), max(r["t1"] for r in rs)
        cover, cur = 0.0, None
        for r in sorted(rs, key=lambda x: x["t0"]):   # union of the part's live intervals
            if cur is None or r["t0"] > cur[1]:
                if cur:
                    cover += cur[1] - cur[0]
                cur = [r["t0"], r["t1"]]
            else:
                cur[1] = max(cur[1], r["t1"])
        cover += (cur[1] - cur[0]) if cur else 0
        rounds = sorted({r["round"] for r in rs if r["role"] == "solver" and r["round"]})
        first = min(rounds) if rounds else None
        c1 = returned.get(f"critic:{pid}:r{first}") if first else None
        ok1 = None
        if isinstance(c1, dict):
            ok1 = not any(_blocking(o) for o in c1.get("objections") or []) and c1.get("verdict") not in ("refuted",)
        part_rows.append({"part": pid, "span_s": round(s1 - s0), "chain_s": round(sum(r["t1"] - r["t0"] for r in rs)), "idle_s": round((s1 - s0) - cover),
                          "agents": len(rs), "rounds": len(rounds), "referee": any(r["role"] == "referee" for r in rs), "first_round_ok": ok1,
                          "solver_model": next((r["m"] for r in rs if r["role"] == "solver" and r["round"] == first), None),
                          "critic_model": next((r["m"] for r in rs if r["role"] == "critic" and r["round"] == first), None),
                          "loop_out_tokens": sum(r["output"] for r in rs if r["role"] in ("solver", "critic", "critic2") and r["round"] and r["round"] != first),
                          "ends_at_share": round((s1 - start) / wall, 2)})
    part_rows.sort(key=lambda x: -x["span_s"])
    by = {}
    for r in rows:
        k = f"{r['role']} {r['m']}"
        b = by.setdefault(k, {"agents": 0, "seconds": [], "output": 0, "returned_nothing": 0})
        b["agents"] += 1; b["seconds"].append(r["t1"] - r["t0"]); b["output"] += r["output"]; b["returned_nothing"] += 0 if r.get("returned") else 1
    for k, b in by.items():
        xs = sorted(b.pop("seconds"))
        b.update({"mean_s": round(sum(xs) / len(xs)), "median_s": round(xs[len(xs) // 2]), "max_s": round(xs[-1]), "mean_output": round(b["output"] / b["agents"])})
    fr = {}
    for x in part_rows:
        for role, mk in (("solver", "solver_model"), ("attacker", "critic_model")):
            if x["first_round_ok"] is not None and x[mk]:
                f = fr.setdefault(f"{role} {x[mk]}", {"parts": 0, "first_round_ok": 0})
                f["parts"] += 1; f["first_round_ok"] += 1 if x["first_round_ok"] else 0
    out_total = sum(r["output"] for r in rows) or 1
    loop = sum(x["loop_out_tokens"] for x in part_rows)
    extra = {}
    try:   # what the engine recorded: which attempt was kept, the budget, what never started
        res = json.loads((run_dir / "result.json").read_text()) if (run_dir / "result.json").exists() else {}
    except Exception:
        res = {}
    att = {"parts": 0, "agents": 0, "agents_kept": 0, "seconds": 0, "seconds_kept": 0, "repair_alone_enough": 0, "no_winner": 0, "by_strategy": {}}
    for pr in res.get("results") or []:
        fo = pr.get("fanout")
        if not fo:
            continue
        att["parts"] += 1
        which = {x.get("round"): x.get("attempt") for x in pr.get("roundLog") or []}
        kept = which.get(pr.get("bestRound")) if fo.get("winner") else None
        outs = {a.get("strategy"): a.get("outcome") for a in fo.get("attempts") or []}
        att["no_winner"] += 0 if fo.get("winner") else 1
        att["repair_alone_enough"] += 1 if outs.get("repair") == "survived" else 0
        for st_id, oc in outs.items():
            b = att["by_strategy"].setdefault(st_id, {"parts": 0, "survived": 0})
            b["parts"] += 1; b["survived"] += 1 if oc == "survived" else 0
        for r in parts.get(pr.get("id"), []):
            a = which.get(r["round"]) if r["role"] in ("solver", "critic", "critic2") else None
            if not a or a == "main":
                continue
            d = r["t1"] - r["t0"]
            att["agents"] += 1; att["seconds"] += d
            if a == kept:
                att["agents_kept"] += 1; att["seconds_kept"] += d
    if att["parts"]:
        att["seconds"], att["seconds_kept"] = round(att["seconds"]), round(att["seconds_kept"])
        att["share_of_busy"] = round(att["seconds"] / max(busy, 1e-9), 2)
        att["discarded_share_of_busy"] = round((att["seconds"] - att["seconds_kept"]) / max(busy, 1e-9), 2)
        extra["attempts"] = att
    if res.get("budget"):
        b = res["budget"]
        crit = {x.get("id") for x in (res.get("plan") or {}).get("scopes") or [] if x.get("critical")}
        skipped = list(res.get("skipped") or []) + [x.get("id") for x in res.get("results") or [] if x.get("final") == "not_started"]
        extra["budget"] = {"estimate": b.get("estimate"), "ceiling": b.get("ceiling"), "used": b.get("agents"), "wrapped": bool(b.get("wrapped")),
                           "used_over_estimate": round(b["agents"] / b["estimate"], 2) if b.get("estimate") else None,
                           "not_started": skipped, "critical_not_started": [x for x in skipped if x in crit]}
        fin = {}
        for x in res.get("results") or []:
            fin[x.get("final")] = fin.get(x.get("final"), 0) + 1
        extra["finals"] = fin
    sol = sorted(r.get("ctx_peak") or 0 for r in rows if r["role"] == "solver")
    if sol and sol[-1]:
        extra["context"] = {"solver_ctx_peak_median": sol[len(sol) // 2], "solver_ctx_peak_max": sol[-1], "solvers_over_300k": sum(1 for x in sol if x > 300000),
                            "cache_read_tokens": sum(r.get("cache_read") or 0 for r in rows)}
    turns = [r.get("turns") or 0 for r in rows]
    if sum(turns):   # how many model calls an agent needed, and how much of that went through scripts (Code Mode)
        extra["steps"] = {"turns": sum(turns), "turns_per_agent": round(sum(turns) / len(rows), 1), "turns_median": sorted(turns)[len(turns) // 2],
                          "tool_calls": sum(r.get("tool_calls") or 0 for r in rows), "script_calls": sum(r.get("script_calls") or 0 for r in rows),
                          "agents_using_scripts": sum(1 for r in rows if r.get("script_calls")),
                          "cache_read_per_agent_m": round(sum(r.get("cache_read") or 0 for r in rows) / len(rows) / 1e6, 2), "code_mode": res.get("codeMode")}
    eff = {
        "wall_s": round(wall), "stalled_s": round(at.get(0, 0)), "active_s": round(active), "busy_s": round(busy), "agents": len(rows),
        "mean_live": round(busy / active, 2), "peak_live": peak,
        "low_live_share": round((at.get(1, 0) + at.get(2, 0)) / active, 2), "single_live_share": round(at.get(1, 0) / active, 2),
        "second_half_mean_live": round(tail_busy / max(1e-9, (wall / 2) - tail_stalled), 2),
        "loop_out_tokens": loop, "loop_share_of_output": round(loop / out_total, 2),
        "parts_over_two_rounds": sum(1 for x in part_rows if x["rounds"] > 2), "parts": part_rows[:40],
        "slowest_part": part_rows[0]["part"] if part_rows else None, "slowest_part_span_share": round(part_rows[0]["span_s"] / wall, 2) if part_rows else None,
        "by_role_model": by, "first_round": fr, **extra,
        "how_to_read": "mean_live far below peak_live, or a high low_live_share, means the run waited on serial chains: look at the parts with the longest span_s and at idle_s. "
                       "loop_share_of_output is what rounds after the first cost. first_round shows, per model, how often a part's first attack found nothing blocking. "
                       "attempts.discarded_share_of_busy is agent time spent on versions that were not kept; attempts.repair_alone_enough against attempts.parts shows how often the first, cheap attempt settled it. "
                       "budget.used_over_estimate far from 1 means the approval-time estimate was wrong; budget.critical_not_started should always be empty. "
                       "context.solvers_over_300k counts solvers whose part was too large for one session. "
                       "steps.turns_per_agent is model calls per agent (each re-reads the context so far); steps.agents_using_scripts above 0 means agents ran scripts that call tools (Code Mode), which should lower turns and cached tokens per agent.",
    }
    if write:
        (run_dir / "efficiency.json").write_text(json.dumps(eff, indent=1))
    return eff


def _group(xs, key):
    out = {}
    for x in xs:
        out.setdefault(x.get(key) or "?", []).append(x)
    return out


def _registry_rows():
    rows = []
    if REGISTRY.exists():
        for l in REGISTRY.read_text().splitlines():
            try:
                rows.append(json.loads(l))
            except Exception:
                pass
    return rows


def _registry_update(run_dir: str, **fields):
    rows = _registry_rows()
    for r in rows:
        if r.get("runDir") == run_dir:
            r.update(fields)
    REGISTRY.write_text("".join(json.dumps(r) + "\n" for r in rows))


def _proposals(status=None):
    out = []
    if PROPOSALS.exists():
        for f in sorted(PROPOSALS.glob("*.json")):
            try:
                d = json.loads(f.read_text())
            except Exception:
                continue
            if status is None or d.get("status") == status:
                d["_path"] = str(f)
                out.append(d)
    return out


def write_proposal(run_dir: Path, result: dict, meta: dict, session_transcript):
    """One dated proposal record per run: the reflector's findings, linked to the run. Never applied here."""
    ref = result.get("reflection") or {}
    if not ref.get("findings"):
        return None
    PROPOSALS.mkdir(parents=True, exist_ok=True)
    pid = f"{time.strftime('%Y%m%d-%H%M%S')}-{meta.get('workflowRunId') or run_dir.name}"
    rec = {"id": pid, "created": time.strftime("%Y-%m-%dT%H:%M:%S"), "status": "pending", "workflowRunId": meta.get("workflowRunId"),
           "runDir": str(run_dir), "sessionTranscript": session_transcript, "transcriptDir": meta.get("transcriptDir"),
           "reflection": str(run_dir / "evolve" / "reflection.md"), "findings": ref.get("findings"), "notes": ref.get("notes", "")}
    (PROPOSALS / f"{pid}.json").write_text(json.dumps(rec, indent=1))
    lines = [f"# proposal {pid}", "", f"- run: `{run_dir}` (workflow {meta.get('workflowRunId')})", f"- status: pending", ""]
    for f in ref["findings"]:
        lines += [f"## {f.get('id')}: {f.get('title')} ({f.get('category')}){' [touches protected]' if f.get('touches_protected') else ''}",
                  f"- impact: {f.get('impact')}", f"- root cause: {f.get('root_cause')}", f"- proposed fix: {f.get('proposed_fix')}",
                  "- evidence: " + "; ".join(f"{e.get('path')} ({e.get('locator')})" for e in f.get("evidence") or []), ""]
    (PROPOSALS / f"{pid}.md").write_text("\n".join(lines) + "\n")
    return pid


def list_proposals(all_=False) -> int:
    ps = _proposals(None if all_ else "pending")
    for d in ps:
        print(f"{d['id']}  {d.get('status'):9}  {len(d.get('findings') or [])} finding(s)  " + "; ".join(f.get("title", "")[:60] for f in d.get("findings") or [])[:160])
    print(f"{len(ps)} proposal record(s){'' if all_ else ' pending'} in {PROPOSALS}")
    return 0


def metrics_cmd(run_dir: Path, transcript=None) -> int:
    if not transcript:
        transcript, _ = _locate_transcript(run_dir)
    if not transcript:
        print("journal not found for this run dir"); return 1
    m = build_metrics(run_dir, {"transcriptDir": transcript})
    print(f"metrics: {run_dir / 'metrics.json'} ({m['totals']['agents']} agents, {m['totals']['output']} output tokens)")
    e = m.get("efficiency") or {}
    if e.get("wall_s"):
        print(f"efficiency: {run_dir / 'efficiency.json'} (active {e['active_s'] // 60} min, {e['mean_live']} agents alive on average, peak {e['peak_live']}, "
              f"{round(100 * e['low_live_share'])}% of the time with two or fewer alive, {round(100 * e['loop_share_of_output'])}% of output spent after first rounds)")
    print(f"journal: {Path(transcript) / 'journal.jsonl'}")
    return 0


def evolve_save(output_file: Path, out_dir: Path) -> int:
    raw = output_file.read_text(errors="replace")
    res = None
    try:
        d = json.loads(raw)
        res = d.get("result") if isinstance(d, dict) and "result" in d else d
        if isinstance(res, str):
            res = json.loads(res)
    except Exception:
        i = raw.find('{"mode"')
        if i >= 0:
            try:
                res = json.loads(raw[i:raw.rfind("}") + 1])
            except Exception:
                res = None
    if not isinstance(res, dict) or "mode" not in res:
        print(f"could not parse the evolve result in {output_file}"); return 1
    ed = out_dir / "evolve"
    ed.mkdir(parents=True, exist_ok=True)
    (ed / "result.json").write_text(json.dumps(res, indent=1))
    props = res.get("proposals") or []
    if props:
        pf = REPO / "PROPOSALS.md"
        head, _, rest = pf.read_text().partition("\n\n")
        entry = "".join(f"\n## {time.strftime('%Y-%m-%d')} {p['id']}: {p['title']} ({p.get('category')})\n- impact: {p.get('impact')}\n- proposed fix: {p.get('fix')}\n"
                        f"- evidence: {'; '.join(e.get('path', '') + ' (' + e.get('locator', '') + ')' for e in p.get('evidence') or [])}\n- verifier: {p.get('reason')}\n- from: {out_dir}\n" for p in props)
        pf.write_text(head + "\n\n" + entry.lstrip("\n") + ("\n" + rest if rest else ""))
        os.system(f"cd '{REPO}' && git add -- PROPOSALS.md && git commit -qm 'crucible proposals: {len(props)} new' -- PROPOSALS.md >/dev/null 2>&1")
    summary = {"mode": res.get("mode"), "findings": len(res.get("findings") or []), "confirmed": sum(1 for f in res.get("findings") or [] if f.get("verdict") == "confirmed"),
               "applied": [a.get("id") for a in res.get("applied") or []], "reverted": [a.get("id") for a in res.get("reverted") or []],
               "proposals": [p.get("id") for p in props], "deferred": res.get("deferred") or [], "at": time.strftime("%Y-%m-%dT%H:%M:%S")}
    _registry_update(str(out_dir), evolve=summary)
    pk = out_dir / "proposals.json"
    if res.get("mode") == "periodic" and pk.exists():
        adopted = {pid for f in res.get("findings") or [] for pid in (f.get("from_proposals") or []) if f.get("id") in summary["applied"]}
        for pid in json.loads(pk.read_text()):
            f = PROPOSALS / f"{pid}.json"
            if f.exists():
                d = json.loads(f.read_text())
                d["status"] = "adopted" if pid in adopted else "reviewed"
                d["reviewedAt"] = summary["at"]
                d["review"] = str(out_dir)
                f.write_text(json.dumps(d, indent=1))
        summary["proposals_marked"] = len(json.loads(pk.read_text()))
    try:
        import crucible_review as rv
        summary["expectations"] = rv.record_expectations(res, out_dir)
    except Exception as e:      # bookkeeping must never lose the review's result
        summary["expectations"] = {"error": str(e)}
    try:
        g = rv.guard_owner_file(out_dir)
        if g:
            summary["expectationFile"] = {**g, "say": "this review changed expectation.md, which only the owner edits: tell the user first"
                                          + (" (the file was put back)" if g.get("restored") else " (it was NOT put back: show them `git log -- expectation.md`)")}
    except Exception as e:
        summary["expectationFile"] = {"error": str(e)}
    summary["engineChanged"] = bool(res.get("engineChanged"))
    if not any(r.get("runDir") == str(out_dir) for r in _registry_rows()):   # a review without its own crucible run still counts as the last review
        REGISTRY.parent.mkdir(parents=True, exist_ok=True)
        with REGISTRY.open("a") as fh:
            fh.write(json.dumps({"runDir": str(out_dir), "kind": "review", "problem": "periodic self-review", "savedAt": summary["at"], "planOnly": False, "counts": {}}) + "\n")
    summary["next"] = (f"the engine changed: run `crucible_run.py probe-check {out_dir}` in the background and report its verdict" if summary["engineChanged"]
                       else "the engine did not change: no probes needed")
    _registry_update(str(out_dir), evolve=summary)
    print(json.dumps(summary, indent=1))
    return 0


def install(host: str = "claude") -> int:
    import shutil, subprocess
    if host == "codex":   # Codex reads skills from ~/.agents/skills/<name>/SKILL.md; its front desk drives the standalone runner
        src = REPO / "hosts" / "codex" / "SKILL.md"
        dst = Path(os.environ.get("CRUCIBLE_CODEX_SKILLS", Path.home() / ".agents" / "skills")) / "crucible"
        dst.mkdir(parents=True, exist_ok=True)
        (dst / "SKILL.md").write_text(src.read_text().replace("{{CRUCIBLE_DIR}}", str(REPO)))
        print(f"installed the Codex front desk -> {dst / 'SKILL.md'} (framework folder: {REPO})")
        return 0
    WORKFLOWS.mkdir(parents=True, exist_ok=True)
    ok = True
    for js in sorted((REPO / "engine").glob("*.js")):
        chk = subprocess.run(["node", "-e", "const fs=require('fs');new Function('args','budget','agent','parallel','pipeline','phase','log','workflow','return (async()=>{'+fs.readFileSync(process.argv[1],'utf8').replace(/^export const meta/m,'const meta')+'})')", str(js)], capture_output=True, text=True)
        if chk.returncode:
            print(f"NOT installed {js.name}: does not parse\n{chk.stderr[:400]}"); ok = False; continue
        shutil.copy2(js, WORKFLOWS / js.name)
        print(f"installed {js.name} -> {WORKFLOWS / js.name}")
    return 0 if ok else 1


def history(n: int) -> int:
    rows = _registry_rows()[-n:]
    for r in rows:
        ev = r.get("evolve") or {}
        mt = r.get("metrics") or {}
        print(f"{r.get('savedAt', '')[:16]}  {r.get('kind', 'run'):6}  {json.dumps(r.get('counts', {}))[:60]:60}  agents={mt.get('agents', '?')}  out={mt.get('output', '?')}  "
              f"paid=${mt.get('paid_usd', '?')}  notes={'yes' if r.get('proposal') else '-'}{(' review-applied ' + ','.join(ev['applied'])) if ev.get('applied') else ''}  {r.get('problem', '')[:60]}")
        print(f"    {r.get('runDir')}")
    return 0


def _last_review():
    revs = [r for r in _registry_rows() if r.get("kind") == "review"]
    return revs[-1] if revs else None


def review_due() -> int:
    last = _last_review()
    since = last.get("savedAt", "") if last else ""
    runs = [r for r in _registry_rows() if r.get("kind", "run") == "run" and r.get("savedAt", "") > since and not r.get("planOnly")]
    import datetime as dt
    days = (dt.datetime.now() - dt.datetime.fromisoformat(since)).days if since else None
    pending = _proposals("pending")
    oldest = min((p.get("created", "") for p in pending), default="")
    age = (dt.datetime.now() - dt.datetime.fromisoformat(oldest)).days if oldest else 0
    due = len(pending) >= REVIEW_PENDING_MAX or (pending and age >= REVIEW_EVERY_DAYS)
    print(f"review: {'due' if due else 'not due'} ({len(pending)} pending proposal record(s), oldest {age} day(s); {len(runs)} run(s) since {'last review ' + since[:10] if since else 'the start'})")
    return 0


RANK = {"refuted": 0, "major_issues": 1, "unverified": 1.5, "minor_issues": 2, "unrefuted": 3}
ROLES = {"contract", "solver", "critic", "critic2", "referee", "debunk", "appeal", "repair", "repair-check"}


def _blocking(o: dict) -> bool:
    return o.get("severity") == "fatal" or (o.get("severity") == "major" and o.get("blocks_acceptance") is not False)


def _revision_failed(f: Path, td) -> bool:
    """plan-vN.json (N >= 2) whose revision agent wrote it and then failed, so v(N-1) was launched (engine :399-:402): in
    the plan-only journal of the session that wrote it (a workflow of the same Claude session, not older than the file,
    whose planner returned the plan-v(N-1).json beside it), planner:vN started and returned nothing."""
    n = int(re.sub(r"\D", "", f.stem) or 0)
    prev, lab, ids = f.with_name(f"plan-v{n - 1}.json"), "planner" if n == 2 else f"planner:v{n - 1}", lambda p: [s.get("id") for s in p.get("scopes", [])] if isinstance(p, dict) else None
    for j in sorted(Path(td).parent.glob("wf_*/journal.jsonl"), key=lambda p: p.stat().st_mtime_ns) if n >= 2 and td and prev.is_file() else []:
        st, done = {}, {}
        for line in j.read_text(errors="replace").splitlines() if j.stat().st_mtime_ns >= f.stat().st_mtime_ns else []:
            try:
                e = json.loads(line)
            except Exception:
                continue
            if e.get("type") == "started":
                st[e.get("agentId")] = e.get("label")
            elif e.get("type") == "result" and e.get("agentId") in st:
                done[st[e["agentId"]]] = e.get("result")
        if f"planner:v{n}" in st.values() and ids(done.get(lab)) == ids(json.loads(prev.read_text())):
            return f"planner:v{n}" not in done
    return False


def _latest_plan(run_dir: Path, td=None):
    """The plan the run executed: the layer-1 plan written last. A plan-only run writes plan[/continue]/plan-vN.json
    (engine :346, :360, :399) and the desk launches the version it returned (the last one, unless a revision failed:
    :401), or writes approved-plan.json after it on a change (SKILL.md :102, :104); earlier sessions' plan files are older."""
    vs = [p for p in [run_dir / "approved-plan.json", *(run_dir / "plan").glob("plan-v*.json"), *(run_dir / "plan" / "continue").glob("plan-v*.json")] if p.is_file() and not _revision_failed(p, td)]
    if vs:  # same time (a copied run dir): approved-plan.json, then plan/continue/, then the highest version
        f = max(vs, key=lambda p: (p.stat().st_mtime_ns, p.name == "approved-plan.json", p.parent.name == "continue", int(re.sub(r"\D", "", p.stem) or 0)))
        d = json.loads(f.read_text())
        return d.get("plan", d), str(f)
    return {}, None


def build_checkpoint(run_dir: Path, transcript=None) -> Path:
    """checkpoint.json: where every scope stands, from the workflow journal (every finished agent's return value).
    Agents that were still running when the run stopped are lost; everything they built on is kept."""
    meta = json.loads((run_dir / "run-meta.json").read_text()) if (run_dir / "run-meta.json").exists() else {}
    td = transcript or meta.get("transcriptDir") or _locate_transcript(run_dir)[0]
    res, started = {}, {}
    if td and (Path(td) / "journal.jsonl").exists():
        for line in (Path(td) / "journal.jsonl").read_text(errors="replace").splitlines():
            try:
                e = json.loads(line)
            except Exception:
                continue
            if e.get("type") == "started" and e.get("label"):
                started[e["label"]] = e.get("agentId")
            elif e.get("type") == "result" and e.get("agentId"):
                lab = next((l for l, a in started.items() if a == e["agentId"]), None)
                if lab:
                    res[lab] = e.get("result")
    final = {}
    rj = run_dir / "result.json"
    plan, plan_path = _latest_plan(run_dir, td)
    if rj.exists() and not (plan_path and rj.stat().st_mtime < Path(plan_path).stat().st_mtime):  # an older result.json is an earlier session's
        try:
            final = {r["id"]: r for r in json.loads(rj.read_text()).get("results", [])}
        except Exception:
            final = {}
    scopes_all, layer_plans = list(plan.get("scopes", [])), {}
    for lab, lp in res.items():  # later layers' plans, as their planners returned them (last revision wins)
        m = re.match(r"^L(\d+):planner(?::v(\d+))?$", lab)
        if m and isinstance(lp, dict) and int(m.group(2) or 1) >= layer_plans.get(int(m.group(1)), (0,))[0]:
            layer_plans[int(m.group(1))] = (int(m.group(2) or 1), lp)
    for k, (_, lp) in sorted(layer_plans.items()):  # ids as the engine runs them (engine :405-:409)
        pre, own = (lambda i, k=k: i if str(i).startswith(f"L{k}-") else f"L{k}-{i}"), {s.get("id") for s in lp.get("scopes", [])}
        scopes_all += [dict(s, id=pre(s["id"]), depends_on=[pre(d) for d in s.get("depends_on") or [] if d in own]) for s in lp.get("scopes", [])]
    ids = [s["id"] for s in scopes_all]
    for lab in list(started):
        p = lab.split(":")
        if p[0] in ROLES and len(p) > 1 and p[1] not in ids:
            ids.append(p[1])   # gap, restructured and escalated scopes
    ids += [i for i in final if i not in ids]   # established results of this session
    by_plan = {s["id"]: s for s in scopes_all}
    worked = {lab.split(":")[1] for lab in started if lab.split(":")[0] in ROLES and ":" in lab}
    scopes = []
    for sid in ids:
        sd = run_dir / "scopes" / sid
        rounds = sorted({int(m.group(1)) for l in res for m in [re.match(rf"^solver:{re.escape(sid)}:r(\d+)$", l)] if m and f"critic:{sid}:r{m.group(1)}" in res})
        rec = {"id": sid, "title": by_plan.get(sid, {}).get("title", sid), "difficulty": by_plan.get(sid, {}).get("difficulty"),
               "depends_on": by_plan.get(sid, {}).get("depends_on", []), "dir": str(sd), "rounds": [], "contract_path": None}
        if f"contract:{sid}" in res or (sd / "contract.md").exists():
            rec["contract_path"] = str(sd / "contract.md")
        best, best_rank, avenues, untried = None, -1, {}, []
        for r in rounds:
            sv, cr = res[f"solver:{sid}:r{r}"] or {}, res[f"critic:{sid}:r{r}"] or {}
            obs = (cr.get("objections") or []) + ((res.get(f"critic2:{sid}:r{r}") or {}).get("objections") or [])
            rec["rounds"].append({"round": r, "solver_status": sv.get("status"), "claim": (sv.get("claim") or "")[:600], "verdict": cr.get("verdict"),
                                  "blocking": sum(map(_blocking, obs)), "non_blocking": len(obs) - sum(map(_blocking, obs)),
                                  "claim_file": str(sd / f"round-{r:02d}" / "claim.md"), "critique_file": str(sd / f"round-{r:02d}" / "critique.md")})
            for a in sv.get("avenues") or []:
                avenues[a.get("avenue")] = a
            if sv.get("status") == "claim" and RANK.get(cr.get("verdict"), 1) >= best_rank:
                best_rank, best = RANK.get(cr.get("verdict"), 1), r
            untried = (cr.get("exhaustion") or {}).get("untried_avenues") or []
        # the attack that stands is the best round's (after parallel attempts the last round is not the best one)
        last_c = res.get(f"critic:{sid}:r{best or rounds[-1]}") if rounds else None
        ruled = {x.get("id"): x for x in ((res.get(f"referee:{sid}") or {}).get("rulings") or []) if isinstance(x, dict)}
        cleared = lambda o: (ruled.get(o.get("id")) or {}).get("ruling") == "caveat" or ((ruled.get(o.get("id")) or {}).get("ruling") == "rejected" and (ruled.get(o.get("id")) or {}).get("check_executed"))
        rec["open_findings"] = [{"id": o.get("id"), "blocking": _blocking(o) and not cleared(o), "severity": o.get("severity"), "issue": o.get("issue"), "failing_check": o.get("failing_check")}
                                for o in (last_c or {}).get("objections") or []]
        if ruled:
            rec["referee"] = {"upheld": sum(1 for o in rec["open_findings"] if o["blocking"]), "ruled": len(ruled)}
        rec["untried_avenues"] = [a["avenue"] for a in avenues.values() if a.get("outcome") == "next"] + list(untried)
        if best:
            rec["best_round"], rec["best_claim_file"] = best, str(sd / f"round-{best:02d}" / "claim.md")
        if rounds:
            rec["latest_claim_file"] = str(sd / f"round-{rounds[-1]:02d}" / "claim.md")
        votes = [res[l] for l in sorted(res) if l.startswith(f"debunk:{sid}:") and res[l]]
        deb_started = [l for l in started if l.startswith(f"debunk:{sid}:")]
        rec["review"] = [{"core_verdict": v.get("core_verdict"), "material_flaws": v.get("material_flaws", []), "fixable_flaws": (v.get("fixable_flaws") or [])[:8]} for v in votes]
        repair_started, repair_done = f"repair:{sid}" in started, f"repair-check:{sid}" in res
        if repair_done and (res.get(f"repair-check:{sid}") or {}).get("repaired") and res.get(f"repair:{sid}"):
            rec["best_claim_file"] = str(sd / "debunk" / "repair" / "claim.md")
        if sid in final:
            rec["stage"], rec["final"] = "finished", final[sid].get("final")
        elif votes and len(votes) == len(deb_started) and (not repair_started or repair_done):
            rec["stage"] = "reviewed"
            rec["final"] = "debunked" if any(v.get("core_verdict") == "core_refuted" for v in votes) and f"appeal:{sid}" not in res else (
                "verified" if all(v.get("core_verdict") == "core_holds" for v in votes) else "contested")
        elif deb_started:
            rec["stage"] = "in_review"
        elif rounds:
            rec["stage"] = "in_rounds"
            last = rec["rounds"][-1]
            rec["last_attack_blocking"] = last["blocking"]
        elif rec["contract_path"]:
            rec["stage"] = "contract_only"
        else:
            rec["stage"] = "not_started"
        scopes.append(rec)
    # a continuation reuses the run dir: keep what earlier sessions recorded for scopes this journal does not cover
    old_path = run_dir / "checkpoint.json"
    if old_path.exists():
        try:
            old = {x["id"]: x for x in json.loads(old_path.read_text()).get("scopes", [])}
        except Exception:
            old = {}
        merged = []
        for rec in scopes:
            o = old.pop(rec["id"], None)
            if o and rec["id"] not in worked:  # no agent of this session worked on it: the earlier record stands, with this plan's
                # title / difficulty / depends_on and this session's final; an earlier "finished" of a re-planned scope is not one
                new = {k: rec[k] for k in ("title", "difficulty", "depends_on")} if rec["id"] in by_plan else {}
                new.update({k: rec[k] for k in ("stage", "final")} if rec["id"] in final else {})
                rec = {**o, **new}
                if rec.get("stage") == "finished" and rec["id"] not in final:
                    rec["earlier_final"], rec["stage"] = rec.pop("final", None), "in_rounds" if rec.get("rounds") else "contract_only" if rec.get("contract_path") else "not_started"
            elif o:
                have = {x["round"] for x in rec["rounds"]}
                rec["rounds"] = [x for x in o.get("rounds", []) if x["round"] not in have] + rec["rounds"]
                rec["contract_path"] = rec["contract_path"] or o.get("contract_path")
                for k in ("best_round", "best_claim_file", "latest_claim_file"):  # an earlier best claim stands while this session has none
                    if k not in rec and o.get(k):
                        rec[k] = o[k]
                cl = [x for x in rec["rounds"] if x.get("solver_status") == "claim" and x.get("claim_file")]
                if have and cl and "/debunk/repair/" not in str(rec.get("best_claim_file")):  # ranked over every session's rounds, as one session does
                    top = max(cl, key=lambda x: (RANK.get(x.get("verdict"), 1), x["round"]))
                    rec["best_round"], rec["best_claim_file"] = top["round"], top["claim_file"]
                if not have:  # its agents of this session finished no round (resumed scope stopped in flight): the earlier attack still stands
                    rec.update({k: o[k] for k in ("open_findings", "untried_avenues", "last_attack_blocking") if o.get(k) is not None})
                    if rec["stage"] in ("not_started", "contract_only") and rec["rounds"]:
                        rec["stage"] = "in_rounds"
            merged.append(rec)
        scopes = merged + list(old.values())
    lost = [l for l, a in started.items() if l not in res]
    ck = {"runDir": str(run_dir), "problem_file": str(run_dir / "problem.md"), "plan_file": plan_path, "transcriptDir": td,
          "built": time.strftime("%Y-%m-%dT%H:%M:%S"), "agents_finished": len(res), "agents_lost_in_flight": lost,
          "stages": {k: sum(1 for x in scopes if x["stage"] == k) for k in ("finished", "reviewed", "in_review", "in_rounds", "contract_only", "not_started")},
          "scopes": scopes,
          "how_to_read": "stage: finished (the run ended normally; final = its status), reviewed (attacker and review panel done), in_review (survived the attacker; review incomplete), "
                         "in_rounds (best attempt so far; open_findings are from the last attack), contract_only, not_started. Blocking findings are what kept a scope from being accepted."}
    out = run_dir / "checkpoint.json"
    out.write_text(json.dumps(ck, indent=1))
    return out


def _problem_text(run_dir: Path) -> str:
    pf = run_dir / "problem.md"
    if not pf.exists():
        return ""
    t = pf.read_text(errors="replace")
    m = re.search(r"^# Problem[^\n]*\n(.*?)(?=^# )", t, re.S | re.M)
    return (m.group(1) if m else t).strip()


def continue_info(path: Path) -> int:
    run_dir = path if path.is_dir() else path.parent  # <runDir>/crucible-handoff.md also after save set it aside
    if not (run_dir / "problem.md").exists():
        print(json.dumps({"error": f"no crucible run at {run_dir} (problem.md missing)"}))
        return 1
    ck = run_dir / "checkpoint.json"
    if not ck.exists():
        ck = build_checkpoint(run_dir)
    d = json.loads(ck.read_text())
    ho = run_dir / "crucible-handoff.md"
    flags = (run_dir / "problem.md").read_text(errors="replace")
    depth = (re.search(r"depth chosen: (\w+)", flags) or re.search(r"--depth (\w+)", flags))
    print(json.dumps({"runDir": str(run_dir), "problem": _problem_text(run_dir), "checkpoint": str(ck), "handoff": str(ho) if ho.exists() else None,
                      "depth": depth.group(1) if depth else "standard", "stages": d.get("stages"), "dataFlag": data_flag(run_dir),
                      "context_file": str(run_dir / "context.txt") if (run_dir / "context.txt").exists() else None,
                      # context.txt, then each continuation's context-continue.txt, context-continue2.txt, ...: oldest first
                      "context_files": [str(p) for p in sorted(run_dir.glob("context*.txt"), key=lambda p: (p.name != "context.txt", int(re.sub(r"\D", "", p.stem) or 1), p.name))]}, indent=1))
    return 0


def save(output_file: Path, run_dir: Path, transcript_arg=None, run_id_arg=None, session_arg=None, kind="run") -> int:
    run_dir.mkdir(parents=True, exist_ok=True)
    result, transcript, wf_id = parse_output(output_file)
    if not transcript_arg:  # a path in the output text may be an agent quoting another session's transcript (or none that
        # exists): the newest journal that names this run dir is this session's; the quoted path only if there is none
        quoted = transcript if transcript and (Path(transcript).expanduser() / "journal.jsonl").exists() else None
        transcript = _locate_transcript(run_dir)[0] or (str(Path(quoted).expanduser()) if quoted else None)
    else:
        transcript = transcript_arg
    wf_id = run_id_arg or (Path(transcript).name if transcript else wf_id)  # the transcript dir is named after its run
    if result is None:
        print(f"could not find the crucible result in {output_file}; write it to {run_dir}/result.json and run: crucible_run.py index {run_dir}")
        return 1
    (run_dir / "result.json").write_text(json.dumps(result, indent=1))
    meta = {"transcriptDir": transcript, "workflowRunId": wf_id, "outputFile": str(output_file), "savedAt": time.strftime("%Y-%m-%dT%H:%M:%S")}
    old_meta = run_dir / "run-meta.json"
    if old_meta.exists():  # a close or continuation keeps the trail of the earlier workflow runs of this run dir
        try:
            om = json.loads(old_meta.read_text())
            meta["earlierRuns"] = om.get("earlierRuns", []) + [{k: om.get(k) for k in ("transcriptDir", "workflowRunId", "savedAt")}]
        except Exception:
            pass
    elif (run_dir / "checkpoint.json").exists():
        try:
            meta["earlierRuns"] = [{"transcriptDir": json.loads((run_dir / "checkpoint.json").read_text()).get("transcriptDir")}]
        except Exception:
            pass
    (run_dir / "run-meta.json").write_text(json.dumps(meta, indent=1))
    metrics = build_metrics(run_dir, meta) if not result.get("planOnly") else {}
    if result.get("closed"):
        print(f"closed run: the checkpoint it was closed from is kept: {run_dir / 'checkpoint.json'}")
    elif not result.get("planOnly"):
        try:
            print(f"checkpoint: {build_checkpoint(run_dir, transcript)}")
        except Exception as e:  # bookkeeping must never block giving the user their answer
            print(f"checkpoint not written: {e}")
    st_path = None
    if session_arg:
        _h = sorted(Path.home().glob(f".claude/projects/*/{session_arg}.jsonl"))
        st_path = str(_h[0]) if _h else None
    pid = write_proposal(run_dir, result, meta, st_path)
    if pid:
        print(f"self-review notes recorded: {PROPOSALS / (pid + '.md')}")
    if result.get("atlas") is not None:
        print(f"atlas: {build_atlas(run_dir)}")
    if not result.get("planOnly"):
        for f in write_outputs(run_dir, result):
            print(f"written from the result: {f}")
        rep_path = write_inline_report(run_dir, result)
        if rep_path:
            print(f"report written from the result (no synthesizer report found): {rep_path}")
    idx = build_index(run_dir)
    problem = ""
    pf = run_dir / "problem.md"
    if pf.exists():
        problem = pf.read_text(errors="replace").strip().splitlines()[0][:200] if pf.read_text().strip() else ""
    REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    counts = {}
    for r in result.get("results", []):
        counts[r["final"]] = counts.get(r["final"], 0) + 1
    keep = []
    if REGISTRY.exists():  # upsert: one line per run dir
        for l in REGISTRY.read_text().splitlines():
            try:
                if json.loads(l).get("runDir") != str(run_dir):
                    keep.append(l)
            except Exception:
                keep.append(l)
    REGISTRY.write_text("".join(k + "\n" for k in keep))
    with REGISTRY.open("a") as fh:
        st = st_path
        t = (metrics or {}).get("totals", {})
        fh.write(json.dumps({"runDir": str(run_dir), "kind": kind, "problem": problem, "savedAt": meta["savedAt"], "transcriptDir": transcript,
                             "workflowRunId": wf_id, "sessionTranscript": st, "planOnly": bool(result.get("planOnly")), "counts": counts, "proposal": pid,
                             "metrics": {"agents": t.get("agents"), "output": t.get("output"), "context": t.get("context"),
                                         "paid_usd": round((metrics or {}).get("paid_calls", {}).get("cost_usd", 0), 4),
                                         "cache_hits": (metrics or {}).get("cache_hits", {}).get("count")} if metrics else None,
                             "efficiency": {k: ((metrics or {}).get("efficiency") or {}).get(k) for k in ("wall_s", "active_s", "mean_live", "peak_live", "low_live_share", "second_half_mean_live", "attempts", "budget", "loop_share_of_output", "parts_over_two_rounds", "slowest_part_span_share")} if (metrics or {}).get("efficiency", {}).get("wall_s") else None,
                             "routing": (result.get("routing") or {}).get("profile"), "engine": result.get("engineVersion")}) + "\n")
    print(f"saved {run_dir}/result.json and {idx}")
    print("status counts: " + (", ".join(f"{k}={v}" for k, v in sorted(counts.items())) or ("closed from checkpoint" if result.get("closed") else "plan only")))
    # the user gets answer.md (written for them); report.md is the internal record and is never presented
    if metrics and not result.get("planOnly"):
        pc = metrics.get("paid_calls", {})
        if LEDGER:
            print(f"paid data calls in this run: {pc.get('calls', 0)}, ${pc.get('cost_usd', 0):.4f}, {pc.get('failed', 0)} failed")
    ans, syn, r0 = run_dir / "answer.md", result.get("synthesis") or {}, (result.get("results") or [{}])[0]
    if ans.exists():
        print(f"next: read {ans} and give it to the user (SKILL.md section 5)")
    elif result.get("planOnly") or (syn.get("inline") and r0.get("claimPath") and Path(r0["claimPath"]).exists()):
        print("next: no answer.md; for a single-part run write the answer from the claim file (SKILL.md section 5)")
    elif syn.get("inline"):  # the part failed before any round, or its claim file was never written (engine :817)
        print(f"next: no answer.md, and the single part (ended {r0.get('final')}) left no claim file: it was not solved; answer from {run_dir / 'report.md'} and {r0.get('dir')} (SKILL.md section 5)")
    else:  # the synthesizer or closer failed or returned nothing
        print(f"next: this session returned no answer (answer.md was not written): say so first, then answer from {run_dir / ('report.md' if result.get('results') else 'checkpoint.json')} and the claim files it lists (SKILL.md section 5)")
    return 0


def rsi(repo: Path, init=False) -> int:
    """RSI.md: a product's own improvement policy and feedback log (references/RSI-template.md). The front desk reads it
    before a run on that product; nothing here changes the product."""
    f, fb = repo / "RSI.md", repo / "feedback"
    if init:
        if not repo.is_dir():
            print(json.dumps({"error": f"{repo} is not a directory"})); return 1
        made = []
        if not f.exists():
            f.write_text((REPO / "references" / "RSI-template.md").read_text().replace("<PRODUCT>", repo.resolve().name)); made.append(str(f))
        for d in ("open", "done", "declined"):
            (fb / d).mkdir(parents=True, exist_ok=True)
        if not (fb / "README.md").exists():
            (fb / "README.md").write_text((REPO / "references" / "RSI-feedback-readme.md").read_text()); made.append(str(fb / "README.md"))
        print(json.dumps({"created": made, "rsi": str(f), "feedback": str(fb)}, indent=1)); return 0
    items = []
    for x in sorted((fb / "open").glob("*.md")) if (fb / "open").is_dir() else []:
        t = x.read_text(errors="replace")
        items.append({"file": str(x), "title": next((l.lstrip("# ").strip() for l in t.splitlines() if l.strip()), x.stem), "chars": len(t)})
    print(json.dumps({"rsi": str(f) if f.exists() else None, "feedback_dir": str(fb) if fb.is_dir() else None, "open_feedback": items,
                      "hint": None if f.exists() else "no RSI.md here: `crucible_run.py rsi-init <repo>` creates one"}, indent=1))
    return 0


def efficiency_cmd(n: int) -> int:
    rows = [r for r in _registry_rows() if r.get("efficiency")][-n:]
    if not rows:
        print("no run with efficiency numbers yet (they are recorded from engine v5 on, at save)"); return 0
    print("saved             engine routing    wall  live(mean/peak) <=2-live  2nd-half-live  loop-out  >2-round parts  problem")
    for r in rows:
        e = r["efficiency"]
        print(f"{r.get('savedAt', '')[:16]}  {r.get('engine') or '?':6} {r.get('routing') or '?':9} {(e.get('active_s') or e['wall_s']) // 60:4}m  {e['mean_live']:5}/{e['peak_live']:<3}       {round(100 * e['low_live_share']):3}%  {e['second_half_mean_live']:13}  {round(100 * e['loop_share_of_output']):6}%  {e['parts_over_two_rounds']:14}  {r.get('problem', '')[:50]}")
    return 0


def list_runs(n: int) -> int:
    if not REGISTRY.exists():
        print("no runs recorded")
        return 0
    rows = [json.loads(l) for l in REGISTRY.read_text().splitlines() if l.strip()][-n:]
    for r in rows:
        print(f"{r['savedAt']}  {r.get('counts')}  {r['runDir']}\n    {r.get('problem', '')}")
    return 0


def main(argv):
    if len(argv) >= 3 and argv[0] == "save":
        opts = {argv[i]: argv[i + 1] for i in range(3, len(argv) - 1) if argv[i].startswith("--")}
        return save(Path(argv[1]).expanduser(), Path(argv[2]).expanduser(), opts.get("--transcript"), opts.get("--run-id"), opts.get("--session"), opts.get("--kind", "run"))
    if len(argv) >= 2 and argv[0] == "metrics":
        o = {argv[i]: argv[i + 1] for i in range(2, len(argv) - 1) if argv[i].startswith("--")}
        return metrics_cmd(Path(argv[1]).expanduser(), o.get("--transcript"))
    if argv and argv[0] == "proposals":
        return list_proposals(len(argv) > 1 and argv[1] == "all")
    if len(argv) >= 3 and argv[0] == "evolve-save":
        return evolve_save(Path(argv[1]).expanduser(), Path(argv[2]).expanduser())
    if len(argv) >= 2 and argv[0] == "stage":
        # Workflow launches by name can resolve to a stale registry snapshot, and scriptPath must be readable by the
        # session (inside the working directory): copy the installed engine into the run dir and launch that file.
        rd = Path(argv[1]).expanduser()
        rd.mkdir(parents=True, exist_ok=True)
        so = {argv[i]: argv[i + 1] for i in range(2, len(argv) - 1) if argv[i].startswith("--")}
        name = argv[2] if len(argv) > 2 and not argv[2].startswith("--") else "crucible-engine.js"
        src = WORKFLOWS / name
        if not src.exists() or "--source" in argv:   # no Claude Code install on this machine (a Codex host): the framework's own copy
            src = REPO / "engine" / name
        dst = rd / name
        dst.write_text(src.read_text())
        m = re.search(r"const ENGINE_VERSION = '([^']+)'", dst.read_text())
        out = {"scriptPath": str(dst), "expectVersion": m.group(1) if m else None}
        rj = REPO / "routing.json"
        if name == "crucible-engine.js" and rj.exists():   # pass `routing` to the engine as args.routing
            table = json.loads(rj.read_text())
            prof = so.get("--profile") or table.get("default")
            if prof not in table["profiles"]:
                print(json.dumps({"error": f"unknown routing profile {prof!r}; choose one of {sorted(table['profiles'])}"})); return 1
            out["routing"] = {k: v for k, v in table["profiles"][prof].items() if k != "about"}
            # a profile with Codex or OpenRouter routes needs args.sessionId, so their relay agents can find their specs
            out["externalRoutes"] = bool(re.search(r'"(codex|openrouter):', json.dumps(out["routing"]["roles"])))
        print(json.dumps(out))
        return 0
    if argv and argv[0] == "version":
        m = re.search(r"const ENGINE_VERSION = '([^']+)'", (REPO / "engine" / "crucible-engine.js").read_text())
        inst = WORKFLOWS / "crucible-engine.js"
        mi = re.search(r"const ENGINE_VERSION = '([^']+)'", inst.read_text()) if inst.exists() else None
        print(m.group(1) if m else "unknown", "" if mi and m and mi.group(1) == m.group(1) else "(installed copy differs: run crucible_run.py install)")
        return 0
    if len(argv) >= 2 and argv[0] in ("rsi", "rsi-init"):
        return rsi(Path(argv[1]).expanduser(), init=argv[0] == "rsi-init")
    if argv and argv[0] == "efficiency":
        return efficiency_cmd(int(argv[1]) if len(argv) > 1 else 10)
    if argv and argv[0] == "code-mode":   # what the front desk needs to know about Claude Code's Code Mode in this session
        surface, asked = os.environ.get("CLAUDE_CODE_ENTRYPOINT") or "unknown", os.environ.get("CLAUDE_CODE_EXPERIMENTAL_CODE_MODE") == "1"
        terminal = surface == "cli"
        print(f"surface: {surface}; Code Mode asked for at start: {'yes' if asked else 'no'}; "
              + ("it is on only if you have the REPL tool." if asked and terminal else
                 "it can be on here: start Claude with `crucible-claude` (or CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1 claude) and confirm once." if terminal else
                 "it cannot be on in this app: Code Mode works only in a terminal session started with `crucible-claude` (or CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1 claude)."))
        return 0
    if argv and argv[0] == "local":      # this installation's own front-desk notes, if any (SKILL.md prints them at the top)
        f = LOCAL_DIR / "front-desk.md"
        print(f.read_text().strip() if f.exists() else "(none)")
        return 0
    if argv and argv[0] == "repo":
        print(REPO); return 0
    if argv and argv[0] == "install":
        return install(argv[argv.index("--host") + 1] if "--host" in argv and argv.index("--host") + 1 < len(argv) else "claude")
    if argv and argv[0] == "history":
        return history(int(argv[1]) if len(argv) > 1 else 20)
    if argv and argv[0] == "review-due":
        return review_due()
    if argv and argv[0] == "review-pack":
        import crucible_review as rv
        refs, fb, i = [], None, 1
        while i < len(argv):
            if argv[i] == "--feedback" and i + 1 < len(argv):
                fb = argv[i + 1]; i += 2
            elif argv[i] == "--runs":
                i += 1
            else:
                refs.append(argv[i]); i += 1
        return rv.review_pack(refs or None, fb)
    if len(argv) >= 2 and argv[0] == "probe-check":
        import crucible_review as rv
        o = {argv[i]: argv[i + 1] for i in range(2, len(argv) - 1) if argv[i].startswith("--")}
        prov = o.get("--provider", "claude")
        return rv.probe_check(Path(argv[1]).expanduser(), o.get("--routes", "sonnet@high,opus@high" if prov == "claude" else "@high"), "--dry" in argv, prov)
    if len(argv) >= 2 and argv[0] == "digest":
        import crucible_review as rv
        d, err = rv.resolve_run(argv[1])
        if err:
            print(err); return 1
        print(rv.digest_md(rv.run_digest(d, next((r for r in _registry_rows() if r.get("runDir") == str(d)), None))))
        return 0
    if len(argv) >= 2 and argv[0] == "index":
        print(build_index(Path(argv[1]).expanduser()))
        return 0
    if argv and argv[0] == "atlases":
        return prior_atlases(argv[1] if len(argv) > 1 else None)
    if len(argv) >= 2 and argv[0] == "checkpoint":
        o = {argv[i]: argv[i + 1] for i in range(2, len(argv) - 1) if argv[i].startswith("--")}
        print(build_checkpoint(Path(argv[1]).expanduser(), o.get("--transcript")))
        return 0
    if len(argv) >= 2 and argv[0] == "continue-info":
        return continue_info(Path(argv[1]).expanduser())
    if argv and argv[0] == "list":
        return list_runs(int(argv[1]) if len(argv) > 1 else 20)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
