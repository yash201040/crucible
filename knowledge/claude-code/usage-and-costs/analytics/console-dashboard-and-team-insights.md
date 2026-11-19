---
type: "Feature"
title: "Console dashboard and team insights"
description: "The Claude Console analytics page for API customers: metrics, per-user team insights table, permissions and the Analytics API."
resource: "https://code.claude.com/docs/en/analytics"
tags: [analytics, console, api, spend, team-insights]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [web]
requires: "Claude Console account with UsageView permission (Developer, Billing, Admin, Owner, Primary Owner roles)"
identifiers:
  - "UsageView"
  - "platform.claude.com/claude-code"
  - "Claude Code Analytics API"
  - "read:analytics"
  - "claude.ai/analytics/api-keys"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "analytics"
    resource: "https://code.claude.com/docs/en/analytics"
    title: "Track team usage with analytics"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

API customers on the Claude Console see usage and spend metrics at platform.claude.com/claude-code. It needs the UsageView permission, held by the Developer, Billing, Admin, Owner and Primary Owner roles.

# How to use it

Dashboard shows: Lines of code accepted, Suggestion accept rate, Active users and Sessions (daily counts), and Spend (daily API costs in dollars).

Team insights table (date range selectable at top, default last 30 days):

| Column | Meaning |
| - | - |
| Members | Users and API keys with reported usage; API keys by key name, OAuth users by email |
| Spend | Per-user total API costs |
| Lines accepted | Per-user lines added or removed by Edit and Write in accepted edits |

Programmatic access:
- API customers: the Claude Code Analytics API returns daily per-user metrics, using an Admin API key.
- Enterprise plan: the Claude Enterprise Analytics API returns per-user engagement, usage and cost reports across Claude surfaces including Claude Code. A Primary Owner creates a key with the `read:analytics` scope at claude.ai/analytics/api-keys. Not available on the Teams plan.

# Limits and defaults

- Contribution metrics with GitHub integration are not currently available for API customers.
- Console spend figures are estimates; actual costs are on the Cost page (platform.claude.com/cost).
