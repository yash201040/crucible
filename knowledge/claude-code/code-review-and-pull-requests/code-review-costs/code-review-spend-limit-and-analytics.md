---
type: "Limit"
title: "Code Review spend limit and usage analytics"
description: "Monthly spend limit for the Claude Code Review service, the three conditions that skip reviews, and the analytics dashboard at claude.ai/analytics/code-review."
resource: "https://code.claude.com/docs/en/code-review-costs"
tags: [code-review, spend-limit, analytics, budget]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cloud]
requires: "Admin access"
identifiers:
  - "claude.ai/admin-settings/usage"
  - "claude.ai/analytics/code-review"
  - "Code review declined"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-review-costs"
    resource: "https://code.claude.com/docs/en/code-review-costs"
    title: "Code Review costs and usage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A monthly limit for the Claude Code Review service, set at claude.ai/admin-settings/usage; it applies to the whole organization and resets at the next billing period.

# Limits and defaults

Code Review skips reviews when any of these runs out: the Code Review spend limit, the organization's overall monthly usage-credit spend limit, or the usage credits balance. It also skips when what remains is less than the expected cost of one review. Developers see a PR comment naming the cause and linking to the usage settings.

# How to use it

Analytics at claude.ai/analytics/code-review:

| Section | Shows |
| :- | :- |
| PRs reviewed by Code Review | Daily PR count |
| Code Review cost | Spend so far this month (amount only when the current month is selected) |
| Code Review feedback | Comments auto-resolved because a developer fixed the issue |
| Code Review findings | Daily findings by severity |
| Repository breakdown | Per-repo PRs, resolved comments, review runs, estimated cost, per-PR view |

# Notes

Cost figures are estimated at list price before discounts or credits and cover only reviews Claude posted; invoice spend is authoritative.
