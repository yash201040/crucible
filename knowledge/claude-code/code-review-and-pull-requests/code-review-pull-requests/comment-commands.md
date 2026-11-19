---
type: "Reference"
title: "@claude review comment commands"
description: "PR comment commands to start a single review, subscribe to push reviews, or stop; conditions, draft and fork behavior, and overlap with the GitHub Action."
resource: "https://code.claude.com/docs/en/code-review-pull-requests"
tags: [code-review, comment-commands, github, pull-requests]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cloud]
requires: "Write, maintain or admin permission on the repository"
identifiers:
  - "@claude review"
  - "@claude review always"
  - "@claude review once"
  - "@claude review stop"
  - "@claude review off"
  - "@claude review pause"
  - "trigger_phrase"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-review-pull-requests"
    resource: "https://code.claude.com/docs/en/code-review-pull-requests"
    title: "Read and request reviews on a pull request"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Command | Effect |
| :- | :- |
| `@claude review` | One review, no subscription to future pushes |
| `@claude review once` | Same as `@claude review` |
| `@claude review always` | Review now and subscribe the PR to push-triggered reviews |
| `@claude review stop` / `off` / `pause` | End the push subscription without starting or canceling a review; Claude replies with a comment, not a check run |

Before a July 2026 update, `@claude review` subscribed the PR to push reviews; use `always` for that.

# How to use it

Conditions: new top-level PR comment (not inline, not a review body, edits do not count); whole command on one line at the start (misspelled `always`/`stop` or later line is read as plain `@claude review`; capitalization ignored); commenter has write/maintain/admin checked via GitHub (bot comments ignored); PR open. Accepted commands create a check run titled **Code review queued...** then **Code review in progress...**. An eyes reaction alone does not confirm. A review already running on the latest commit blocks a second one.

# Limits and defaults

- Repositories set to **After every push** cannot be stopped by comment; convert the PR to a draft (a review starts when marked ready again).
- Drafts: command works, pushes to a draft do not start reviews even after `always` until ready. Forks: no automatic review regardless of setting; `@claude review` works (write access on the base repo); `always` does not subscribe later pushes; **Re-run** does not start a review.
- Other ways to start: opening, reopening or marking ready (Once/After every push), a push (After every push or subscribed PR), **Re-run** on a failed or timed-out review for non-fork PRs, or an automatic single retry for an interrupted session.

# Notes

If the Claude Code GitHub Action runs in interactive mode with the default `@claude` trigger phrase, an `@claude review` comment starts it too; set the Action's `trigger_phrase` input to a different phrase.
