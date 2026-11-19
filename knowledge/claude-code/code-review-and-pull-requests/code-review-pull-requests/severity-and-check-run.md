---
type: "Reference"
title: "Code Review severities, responding and check run"
description: "Severity markers, how to dismiss or answer findings, and what the Claude Code Review check run shows, including when an earlier result is kept."
resource: "https://code.claude.com/docs/en/code-review-pull-requests"
tags: [code-review, severity, check-run, pull-requests]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cloud]
requires: "Code Review enabled for the repository"
identifiers:
  - "Claude Code Review"
  - "Code review skipped — no new changes"
  - "Code review not repeated — earlier findings still open"
  - "Code review queued..."
  - "Code review in progress..."
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-review-pull-requests"
    resource: "https://code.claude.com/docs/en/code-review-pull-requests"
    title: "Read and request reviews on a pull request"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Marker | Severity | Meaning |
| :- | :- | :- |
| 🔴 | Important | A bug to fix before merging |
| 🟡 | Nit | Minor, not blocking |
| 🟣 | Pre-existing | Bug already in the codebase, not introduced by the PR |

A finding may have a collapsed **Why this was flagged** section.

# How to use it

- Dismiss without a change: resolve the thread yourself; replying alone does not dismiss. Merge needs no response unless branch protection requires conversation resolution.
- Fix: push; the next review resolves its earlier thread if it judges the issue fixed.
- Disagree: reply; the reply does not start a review, but the next review reads replies and may resolve or post one follow-up. Recurring wrong findings belong in `REVIEW.md`.
- Check run Details: one table sorted by severity (file:line, issue), including findings GitHub did not accept inline. A finding with a line but no inline comment shows as an annotation in Files changed (Important red, nit yellow, pre-existing gray). The check run concludes neutral, or skipped after pushes that keep the earlier result; never failure.

# Limits and defaults

A push keeps the earlier result (titles **Code review skipped — no new changes** or **Code review not repeated — earlier findings still open**) when, on github.com, the PR still adds and removes the same lines (empty commit, clean merge of base, clean rebase) and nobody resolved an Important finding's thread since. To force a review: `@claude review` or **Re-run**.

A later automatic review focuses on changes since the last review and posts fewer nits and pre-existing findings; the review body sentence ends "outside the scope of this re-review and not posted" or "found and not posted". `@claude review` covers the whole PR again.
