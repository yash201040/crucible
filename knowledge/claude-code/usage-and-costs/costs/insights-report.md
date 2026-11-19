---
type: "Feature"
title: "/insights usage report"
description: "/insights analyzes up to 200 recent sessions and writes an HTML report on how you work, to ~/.claude/usage-data/report.html."
resource: "https://code.claude.com/docs/en/costs"
tags: [insights, report, sessions, usage, auto-mode]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/insights"
  - "~/.claude/usage-data/report.html"
  - "cleanupPeriodDays"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "costs"
    resource: "https://code.claude.com/docs/en/costs"
    title: "Manage costs effectively"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/insights` reports on how you work rather than token counts: what you work on, friction points (misunderstood requests, buggy code) and suggestions. It analyzes recent sessions on this machine.

# How to use it

Run `/insights`. A run analyzes up to 200 sessions it has not seen before and skips very short ones; the header then shows e.g. `200 sessions (412 total)`. If auto mode is available and recent sessions mostly ran without it, the report may estimate how many permission prompts auto mode could have handled.

# Limits and defaults

- Latest report: `~/.claude/usage-data/report.html`; a timestamped copy of each run is saved alongside.
- Reports are deleted at startup when older than `cleanupPeriodDays` (30 days by default).
- Works on any plan and any provider; analysis runs through the same provider/account and its tokens count against your plan or API usage. Sessions from other devices and claude.ai are excluded.
