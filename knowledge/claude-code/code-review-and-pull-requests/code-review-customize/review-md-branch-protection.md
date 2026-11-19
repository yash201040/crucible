---
type: "Concept"
title: "Which branch REVIEW.md is read from"
description: "Code Review reads REVIEW.md from the base or default branch, never the PR's changes, and honors severity cuts and exclusions only from a protected branch."
resource: "https://code.claude.com/docs/en/code-review-customize"
tags: [code-review, branch-protection, review-md, security]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cloud]
requires: ""
identifiers:
  - "REVIEW.md"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-review-customize"
    resource: "https://code.claude.com/docs/en/code-review-customize"
    title: "Customize Code Review"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Rules for which copy of `REVIEW.md` applies. From a protected default branch the root file's severity lowering, path/issue exclusions and nit caps are honored.

# How to use it

What counts as protection: default branch, a classic branch protection rule or a ruleset; any other branch, a ruleset only. A ruleset counts when it restricts updates or requires PRs with at least one approval; if it requires PRs it must also dismiss approval on new push or require approval after the last push.

| Situation | Copy read | Files read |
| :- | :- | :- |
| Default branch protected; PR targets it or a branch no ruleset protects | Default branch | Root, included files, most subdirectory files |
| PR targets another branch protected by a ruleset | That base branch | Root, included files, most subdirectory files |
| Default branch unprotected and base branch has no rule of either kind | Default branch | Root file only |
| Protection cannot be confirmed (includes unprotected default with a base branch that has only a classic rule) | None | None |

# Notes

Check-run messages report which case applied (see [troubleshooting](../code-review-troubleshooting/review-md-check-run-messages.md)).
