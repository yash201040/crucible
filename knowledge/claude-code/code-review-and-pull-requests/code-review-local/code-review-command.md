---
type: "Feature"
title: "/code-review local command"
description: "/code-review reviews your branch, a PR, path or commit range in your session as a background subagent; flags --fix, --comment, --post, --max-findings."
resource: "https://code.claude.com/docs/en/code-review-local"
tags: [code-review, slash-command, subagent, flags]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk, desktop]
requires: "Any plan"
identifiers:
  - "/code-review"
  - "/review"
  - "--fix"
  - "--comment"
  - "--post"
  - "--max-findings"
  - "ReportFindings"
  - "CLAUDE_CODE_DISABLE_BACKGROUND_TASKS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-review-local"
    resource: "https://code.claude.com/docs/en/code-review-local"
    title: "Review locally with /code-review"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A command typed in a session. Claude reviews the changes, looks for correctness bugs (and, depending on model and effort, reuse, simplification and efficiency cleanups) and reports in the conversation. It counts toward plan usage or API billing like the rest of the session. `/review` is an alias. It was named `/simplify` before v2.1.147, when it applied fixes by default; script `/code-review --fix` instead.

# How to use it

| Target | Type |
| :- | :- |
| Current branch plus uncommitted changes (commits ahead of upstream, else `main`, else previous commit) | `/code-review` |
| Last 15 commits | `/code-review HEAD~15..HEAD` |
| Branch vs branch | `/code-review main...my-feature` |
| Single commit | `/code-review abc1234^..abc1234` |
| Pull request | `/code-review 1234` |
| Path | `/code-review src/auth` |

| Flag | Effect |
| :- | :- |
| `--fix` | Also apply findings to the working tree (goes through permission mode) |
| `--comment` | Post findings as inline comments on a GitHub PR, or a single note on a GitLab MR (needs v2.1.257+, `glab`; else prints findings) |
| `--post` | On an `ultra` cloud review of a github.com PR, preselect posting to the PR in the launch dialog (v2.1.227+) |
| `--max-findings <n>` / `all` / `default` | Cap findings; findings-tool limit is 32; value is remembered for later reviews except in `-p` runs (v2.1.288+) |

An effort level can be typed (`low` through `max`, plus `ultra`); `low` reports only most confident findings. With no level typed, the last typed level is reused (even across sessions) with a notice; levels passed in `-p` runs are not remembered; `ultra` neither uses nor updates it; if none ever typed, session effort is used.

# Limits and defaults

- Terminal session: runs as a background forked subagent with its own context window; findings arrive when done. Foreground runs: non-interactive `-p` or Agent SDK (waits and includes findings, except `ultra`), `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1` (also disables other background task features), or running `/code-review` again while one is in progress.
- Reports findings as text in terminal and `-p` text/JSON runs; in a host that requests a findings list (such as the desktop app) it uses the `ReportFindings` tool and later re-reports each finding as fixed, skipped or no change needed.
- Follows `CLAUDE.md` (also in `-p`), not `REVIEW.md`.
- Background `--fix` edits fall outside session checkpoints, so `/rewind` does not undo them for files not already edited; use git. In the foreground `/rewind` works as usual.

# Notes

- Without `ultra`, all text after level and flags is the review target, even if it starts with another command name. With `ultra`, one word is a base branch or PR number; longer text becomes a note attached to the review.
- Claude can start it itself (plain-language request, or a session-scoped scheduled task, never `ultra`). Block that with `"skillOverrides": {"code-review": "user-invocable-only"}`. Before v2.1.246, autonomous start depended on a fetched feature flag.
- It is a bundled skill, so no `SKILL.md` to edit; a project or personal skill named `code-review` replaces it while `/review` keeps the bundled one. Neighbors: `/simplify` (cleanup only, applies fixes), `/verify`.
