---
type: "Concept"
title: "Code Review billing and review frequency"
description: "Code Review is billed on token usage through usage credits to the organization; cost scales with review level, change size and how often reviews run."
resource: "https://code.claude.com/docs/en/code-review-costs"
tags: [code-review, billing, usage-credits, cost]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cloud]
requires: "Team or Enterprise plan"
identifiers:
  - "Review runs"
  - "Once after PR creation"
  - "After every push"
  - "Manual (@claude review)"
  - "@claude review always"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-review-costs"
    resource: "https://code.claude.com/docs/en/code-review-costs"
    title: "Code Review costs and usage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

No flat per-review price. Spend = cost of each review (review level, change size, surrounding code complexity, candidate issues to verify) times number of reviews. Billing is on token usage through usage credits, separately from the plan's included usage, to the organization (not the developer), and appears on the Anthropic bill even if the org uses Bedrock, Google Cloud's Agent Platform or Foundry otherwise.

# How to use it

Each repository's **Review runs** setting decides count:

| Setting | Effect |
| :- | :- |
| Once after PR creation | Review when opened, reopened or marked ready |
| After every push | Review each push; cost multiplies by pushes (default for newly added repositories) |
| Manual (@claude review) | No reviews on open or push |

Comment effects: `@claude review always` in Once/Manual mode opts the PR into push reviews (added cost per push); in After every push mode it changes nothing; `@claude review` runs one review without subscribing. Drafts and fork PRs get no automatic reviews, so pushes there add none.

# Notes

Estimate: set a monthly spend limit, pilot on a few repos with Once or Manual, read each repository's **Average cost** column (Admin settings > Claude Code > Code review), then multiply by PRs per month (and by pushes per PR for After every push).
