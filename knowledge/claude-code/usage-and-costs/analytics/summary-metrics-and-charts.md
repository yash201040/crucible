---
type: "Reference"
title: "Summary metrics and charts"
description: "Definitions of the dashboard's summary metrics, PRs-per-user chart, PR breakdown chart and leaderboard."
resource: "https://code.claude.com/docs/en/analytics"
tags: [analytics, metrics, leaderboard, pull-requests, csv]
kind: "ui"
maturity: "beta"
since: ""
surfaces: [web]
requires: "Claude for Teams or Enterprise"
identifiers:
  - "PRs with Claude Code"
  - "LOC with Claude Code"
  - "Suggestion accept rate"
  - "Lines of code accepted"
  - "Total PRs per user"
  - "Export all users"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "analytics"
    resource: "https://code.claude.com/docs/en/analytics"
    title: "Track team usage with analytics"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The metrics are deliberately conservative: only lines and PRs with high confidence of Claude Code involvement are counted, so they underestimate real impact.

# How to use it

| Metric / chart | Meaning |
| - | - |
| PRs with Claude Code | Merged PRs with at least one line written with Claude Code; one card shows the count, one the share of all merged PRs |
| LOC with Claude Code | Lines across merged PRs written with Claude Code; only "effective lines" (more than 3 characters after normalization) |
| Suggestion accept rate | Percent of times users accept edit suggestions (Edit, Write, NotebookEdit tool usage) |
| Lines of code accepted | Lines the Edit and Write tools added or removed in accepted edits; rejected suggestions excluded; later deletions do not reduce it |
| Total PRs per user | PRs merged per day divided by daily active users |
| PRs with Claude Code chart | Each day's merged PRs with Claude Code vs All PRs; toggle to Lines of code view |
| Leaderboard | Top 10 users by contribution volume; toggle Pull requests or Lines of code |
| Users and Sessions charts | Adoption trends and usage dips |

Click Export all users to download CSV for all users, not just the top 10.

# Notes

Suggested uses: demonstrate ROI (compare with DORA metrics, sprint velocity), find power users to onboard others.
