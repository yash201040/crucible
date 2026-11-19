---
type: "Reference"
title: "Workspace trust and ultrareview errors"
description: "claude ultrareview and /code-review ultra refusals: untrusted folder, --trust-workspace, diff size limits, merge-base, no branches, GitHub access."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, ultrareview, workspace-trust, ci]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.309"
surfaces: [cli, headless, cloud]
requires: ""
identifiers:
  - "claude ultrareview"
  - "/ultrareview"
  - "/code-review ultra"
  - "--trust-workspace"
  - "IS_DEMO"
  - "git remote set-head origin"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Refusals that stop `claude ultrareview` or `/code-review ultra` (cloud review) before the cloud session starts. A refused launch does not use a free run and does not bill usage credits.

# How to use it

Trust: in a folder that is not trusted and cannot ask (stdin/stdout not a terminal, e.g. `claude ultrareview --json > findings.json`), the run exits 1 with `Error: Workspace not trusted ...`. In a script or CI job append `--trust-workspace` to trust the folder for that run only (added v2.1.309; takes no value, so put a PR number or base branch first: `claude ultrareview 1234 --trust-workspace`). Use it only for trusted code because git and project settings can then run programs.

| Message | Meaning |
|---|---|
| `Error: Workspace not trusted. This terminal ...` | terminal reports no size or too small |
| `... is your home directory` | home trust is never saved |
| `No answer in time.` then `Workspace not trusted` | `Trust <folder>? [y/N]` unanswered for 5 minutes |
| `Ultrareview did not start: <folder> is not trusted` | answered `n` / Enter |
| `Ultrareview did not start: --trust-workspace takes no value` | extra token after the flag |
| `Ultrareview did not start: "<folder>" is not trusted, and this session started without asking` | in-session `/ultrareview`; start `claude` without `IS_DEMO`, accept dialog |
| `Diff is too large for ultrareview` | limits 500 files and 8,000 lines changed (PRs: `PR #<N> is too large`); pass a closer base: `/code-review ultra <branch>` |
| `Could not find merge-base with <base>` | falls back to reviewing all tracked files on a verifiably complete clone; otherwise refuses. Fix: pass base explicitly or `git fetch --unshallow origin` |
| `Your checkout has no branches` | detached HEAD with no refs cannot be bundled; `git checkout -b <name>` (before v2.1.221 the upload failed) |
| `Ultrareview clones <owner>/<repo> ... none is connected` | no GitHub account connected to the Claude account (preflight since v2.1.248); `/web-setup` or claude.ai/connect-github |
| `Your connected GitHub account can't see <owner>/<repo>` | Claude GitHub app not installed/granted; install at github.com/apps/claude/installations/new (since v2.1.248) |

# Limits and defaults

- Diff limits: 500 files, 8,000 lines.
- Trust question timeout: 5 minutes.

# Notes

Before v2.1.309, `claude ultrareview` did not accept `--trust-workspace`. Sibling cloud errors are in [cloud session and GitHub errors](./p3-cloud-session-and-github-errors.md).
