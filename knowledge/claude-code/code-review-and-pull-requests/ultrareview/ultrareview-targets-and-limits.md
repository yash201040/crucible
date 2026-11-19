---
type: "Feature"
title: "Ultrareview targets, scope and diff limits"
description: "How to point ultrareview at a branch, base, commit, PR or plain-words note, and the diff size limits and fallbacks."
resource: "https://code.claude.com/docs/en/ultrareview"
tags: [code-review, diff, pull-request, limits]
kind: "behavior"
maturity: "research-preview"
since: ""
surfaces: [cli, cloud]
requires: "github.com for PR mode; GitHub account connected to Claude account with read access"
identifiers:
  - "/code-review ultra <base>"
  - "/code-review ultra <PR-number>"
  - "/web-setup"
  - "CCR_FORCE_BUNDLE"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "ultrareview"
    resource: "https://code.claude.com/docs/en/ultrareview"
    title: "Find bugs with ultrareview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Rules for what ultrareview reviews and when it refuses or falls back.

# How to use it

| Command | Reviews |
| - | - |
| `/code-review ultra` | current branch vs default branch, including uncommitted and staged changes |
| `/code-review ultra develop` | current branch vs another base; base need not exist locally (fetched from `origin`); a commit id or tag also works |
| `/code-review ultra 1234` | a github.com PR; also accepts `#1234`, `PR 1234`, pasted URL (must be the current repo) |
| `/code-review ultra check my auth changes` | current branch, with the text kept as a note shown in the launch dialog |

A launch dialog shows scope (file and line count for branches), remaining free runs and estimated cost before starting. Branch review bundles and uploads the repo (same rules as uploading a local repo to a cloud session); PR mode uploads nothing and the cloud sandbox clones from github.com using the connected GitHub account (connect with `/web-setup`). GitHub Enterprise Server repos: run without a PR number. Text counts as a note only when it has more than one word and is not a branch or PR reference; a single word is read as a branch or PR; text mixing a PR reference with other words (such as `check PR 123 again`) launches nothing. If the repo is too large to bundle, use PR mode.

# Limits and defaults

- Diff too large: by default up to 500 changed files and 8,000 changed lines (values can change; the refusal names the ones in effect).
- Empty diff: refuses, names what it compared against and suggests a way out.
- First commit: whole repo reviewed after dialog confirmation; untracked files cause refusal (`git add` them). `claude ultrareview` and `claude -p` refuse it. Requires Claude Code v2.1.277 or later.
- No merge base (or no base branch): reviews every tracked file; needs a full clone; launches only after dialog confirmation or when running the `claude ultrareview` subcommand; `claude -p` refuses. A checkout with no branches or refs (such as detached HEAD after fetching a URL) is refused: create a branch first.
