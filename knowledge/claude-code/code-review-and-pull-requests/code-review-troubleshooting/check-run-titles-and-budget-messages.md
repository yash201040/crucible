---
type: "Reference"
title: "Code Review check run titles and budget messages"
description: "What each Claude Code Review check run title means, why a review did not start, budget-skip comment wording, and how to retrigger a failed review."
resource: "https://code.claude.com/docs/en/code-review-troubleshooting"
tags: [code-review, troubleshooting, check-run, budget]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cloud]
requires: ""
identifiers:
  - "Code review queued..."
  - "Code review in progress..."
  - "Code review found no issues"
  - "Code review skipped — no new changes"
  - "Code review not repeated — earlier findings still open"
  - "Code review failed"
  - "Code review timed out"
  - "Code review declined"
  - "⚠️ Code review skipped"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-review-troubleshooting"
    resource: "https://code.claude.com/docs/en/code-review-troubleshooting"
    title: "Troubleshoot Code Review"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Start from the **Claude Code Review** check run; its title says how far the review got.

# How to use it

| Title | Meaning / action |
| :- | :- |
| Queued / in progress | Wait |
| Found no issues | Finished with none; on a later review look in the body for a count of left-out findings |
| A title saying issues were found | Look in Details, Files changed annotations, whole-file comments on Conversation, or an **Additional findings** heading in the review body if no inline comments |
| Skipped — no new changes | Automatic review did not run on the push; `@claude review` to force |
| Not repeated — earlier findings still open | Push a fix or `@claude review` |
| Failed / timed out | See retrigger below |
| Declined | Read the summary; budget or spend limit |
| No check run | Comment `@claude review`; if still none, check causes below |

No check run after a command: Code Review is not on for the repository (no comment either; ask an Owner to add it); comment not top-level or not at start or edited; no write access (tip says "No review was started: manual reviews can only be requested by someone with write access to this repository."); budget ran out.

Budget skip comment begins "⚠️ Code review skipped" and links claude.ai/admin-settings/usage; wording: "has reached its monthly code review spending cap" (resumes next billing period or raise limit), "has no extra usage available to pay for this review" (credits balance empty or overall monthly spend limit reached), "is too low to start another review" (remaining below expected cost of one). After restoring budget, comment `@claude review` (needs write access).

# Notes

Retrigger: if the summary says "The review session was interrupted before it could finish. A new review of this commit has been queued automatically." do nothing (retried once). Otherwise comment `@claude review` (fresh review, no subscription) or click **Re-run** in the Checks tab for non-fork PRs (covers current head, no subscription).
