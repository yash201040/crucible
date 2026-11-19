---
type: "Feature"
title: "Plan usage breakdown and recommendations"
description: "On subscription plans /usage attributes usage to skills, subagents, plugins and MCP servers, recommends changes, and lists heavy loops."
resource: "https://code.claude.com/docs/en/costs"
tags: [usage, attribution, recommendations, loops, subscription]
kind: "ui"
maturity: "unlabelled"
since: "2.1.242"
surfaces: [cli, ide]
requires: "Pro, Max, Ultra, Team or Enterprise plan; Loops rows need v2.1.242+"
identifiers:
  - "/usage"
  - "/loop"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "costs"
    resource: "https://code.claude.com/docs/en/costs"
    title: "Manage costs effectively"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

On Pro, Max, Ultra, Team or Enterprise, `/usage` also shows what counts against plan limits.

# How to use it

- **Attribution**: recent usage attributed to skills, subagents, plugins and individual MCP servers, as a percentage of total. An MCP server's share counts only requests that consumed one of its tool results (before v2.1.222, every request after one call was attributed to it).
- **Recommendations**: one per row, each starting with a share of recent usage of at least 10%, e.g. `25%  Trim ~/code/api/CLAUDE.md · 49k tokens per request`. The share says how much of your usage the row applies to, not savings; one request can count toward several rows, so shares can exceed 100%.
- **Loops**: a row per heaviest `/loop` or other session-scoped scheduled task, ordered by total tokens, plus a count of the rest. Each row reports firing frequency, run count, total and per-run tokens, last run. Rows are keyed by the task's prompt, so a stopped and re-created loop stays one row.

Press `d` or `w` to switch between last 24 hours and last 7 days.

# Limits and defaults

- Figures are approximate and computed from local session history on this machine; other devices and claude.ai are excluded.
- In the VS Code extension, attribution and recommendations appear in the Account & usage dialog with a Day and Week toggle, without Loops rows.
