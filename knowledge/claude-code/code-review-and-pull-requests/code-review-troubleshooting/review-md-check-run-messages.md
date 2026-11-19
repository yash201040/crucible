---
type: "Reference"
title: "REVIEW.md check run messages and setup problems"
description: "Meaning of REVIEW.md-related check run messages (unprotected branch, unconfirmed protection, link limits, skipped includes) and Owner setup fixes."
resource: "https://code.claude.com/docs/en/code-review-troubleshooting"
tags: [code-review, review-md, troubleshooting, setup]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cloud]
requires: ""
identifiers:
  - "REVIEW.md"
  - "Install GitHub App"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-review-troubleshooting"
    resource: "https://code.claude.com/docs/en/code-review-troubleshooting"
    title: "Troubleshoot Code Review"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Four check run messages about `REVIEW.md`:

| Message fragment | Meaning |
| :- | :- |
| "applied the repository's review instructions (REVIEW.md) from its default branch, which is not protected against direct pushes" | Only the root file was read |
| "were not applied to this review: branch protection could not be confirmed" | No `REVIEW.md` read |
| "they link to a file this pull request modifies, or carry more links than the review checks" | Root or the stated number of subdirectory files skipped: more than 64 Markdown links, a malformed link, or a link to a file or folder the PR changes |
| "include line(s) in the root REVIEW.md were skipped on this review" | Root applied but named files (or skill files) did not |

# How to use it

Setup problems for Owners: a repository missing from **Add a repository** (search by name; click **Install GitHub App** and grant access); no check run on a test PR (confirm **Allow code review** is on, the repository is listed, the App has access, the PR is not a draft, Manual repos need `@claude review`).
