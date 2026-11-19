---
type: "Guide"
title: "Scan, results files and patches"
description: "Run /claude-security scans at low, medium or high effort, read the CLAUDE-SECURITY results files, and turn findings into reviewed patches you apply yourself."
resource: "https://code.claude.com/docs/en/claude-security"
tags: [security, scan, sarif, patches]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "claude-security plugin installed"
identifiers:
  - "/claude-security"
  - "CLAUDE-SECURITY-<timestamp>/"
  - "CLAUDE-SECURITY-RESULTS.md"
  - "CLAUDE-SECURITY-RESULTS.jsonl"
  - "CLAUDE-SECURITY-RESULTS.sarif"
  - "CLAUDE-SECURITY-REVISION-<commit>.json"
  - "patches/F<n>.patch"
  - "git apply"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-security"
    resource: "https://code.claude.com/docs/en/claude-security"
    title: "Scan your codebase for vulnerabilities"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/claude-security` opens a menu of three jobs: scan codebase, scan changes, suggest patches. You can also pass arguments (`/claude-security scan my branch`, `/claude-security scan my public API code at high`) or ask in plain language ("scan commit abc1234", "fix finding F3").

# How to use it

Scan effort (findings get the same independent verification at all three):

| Effort | Behavior |
| :- | :- |
| `low` | Quick first look; skips architecture map and threat model on codebase scans |
| `medium` | Default |
| `high` | `medium` plus more hunting in the same code |

Change scans offer the branch diff, one of your open pull requests (only if `gh` is signed in and permitted), or a single commit; only committed changes are scanned. Large repositories: scan one focused area at a time; the coverage section states what was examined.

Results go into a timestamped `CLAUDE-SECURITY-<timestamp>/` directory in the repo (the only change a scan makes), with its own `.gitignore` (delete it to commit reports):

| File | Content |
| :- | :- |
| `CLAUDE-SECURITY-RESULTS.md` | Report: finding ID (`F1`), impact, exploit scenario, severity, confidence, recommendation |
| `CLAUDE-SECURITY-RESULTS.jsonl` | Same findings, one JSON object per line |
| `CLAUDE-SECURITY-RESULTS.sarif` | SARIF 2.1.0 log with CWE categories |
| `CLAUDE-SECURITY-REVISION-<commit>.json` | Commit scanned (`UNVERSIONED` outside version control), effort, whether uncommitted changes were included, verification thoroughness |

# Limits and defaults

- Scans are nondeterministic; a second scan or `high` effort can find more.
- Patches: drafted in a scratch copy of the repo against committed code; skipped with a note if the code has changed since the report. Each patch is reviewed by an independent agent that runs project tests where they exist; it is written only if it vouches the patch fixes the one finding, adds no vulnerability and keeps behavior. Output is `patches/F<n>.patch` plus a note (which says if there were no tests).
- Patches are never applied automatically; apply with `git apply CLAUDE-SECURITY-<timestamp>/patches/F1.patch`, one pull request per patch.
