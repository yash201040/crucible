---
type: "Reference"
title: "Analytics dashboards by plan"
description: "Which Claude Code analytics dashboard each plan uses, who can open it, and what it shows."
resource: "https://code.claude.com/docs/en/analytics"
tags: [analytics, dashboard, teams, enterprise, console]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [web]
requires: "Claude for Teams or Enterprise (Admin or Owner), or Claude Console with UsageView permission"
identifiers:
  - "claude.ai/analytics/claude-code"
  - "platform.claude.com/claude-code"
  - "claude.ai/admin-settings/claude-code"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "analytics"
    resource: "https://code.claude.com/docs/en/analytics"
    title: "Track team usage with analytics"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code has two analytics dashboards that show usage patterns, contribution metrics and engineering velocity. Which one you use depends on how your organization pays for Claude Code. Code Review has its own separate dashboard (see code-review-costs, "View usage").

# How to use it

| Plan | URL | Includes |
| - | - | - |
| Claude for Teams / Enterprise | claude.ai/analytics/claude-code | Usage metrics, contribution metrics with GitHub integration, leaderboard, CSV data export |
| API (Claude Console) | platform.claude.com/claude-code | Usage metrics, spend tracking, team insights |

Teams/Enterprise: Admins and Owners can view it. Usage metrics there are lines of code accepted, suggestion accept rate, daily active users and sessions.

For per-user token counts and cost estimates, use OpenTelemetry export (monitoring-usage) or the spend report from the organization's analytics settings (token usage and estimated usage-credit spend per user and per model).

# Notes

- Usage and adoption data is available to all Teams and Enterprise accounts; contribution metrics need extra setup (see [contribution metrics setup](./contribution-metrics-setup.md)).
