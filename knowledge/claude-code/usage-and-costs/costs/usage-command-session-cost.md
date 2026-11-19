---
type: "Feature"
title: "/usage session cost block"
description: "The /usage Session block shows locally computed token usage and estimated dollar cost for the current session."
resource: "https://code.claude.com/docs/en/costs"
tags: [usage, cost, session, modelpricing, budget]
kind: "slash_command"
maturity: "unlabelled"
since: "2.1.211"
surfaces: [cli]
requires: ""
identifiers:
  - "/usage"
  - "modelPricing"
  - "--max-budget-usd"
  - "/clear"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "costs"
    resource: "https://code.claude.com/docs/en/costs"
    title: "Manage costs effectively"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Running `/usage` shows, under the Session heading, the current session's tokens and cost. Claude Code computes the dollar figure locally from token counts at list price, unless a `modelPricing` table is in effect (set by an admin in managed settings); then the `Total cost` line carries the note `at your organization's configured rates`. The figure is an estimate.

# How to use it

Output fields: `Total cost`, `Total duration (API)`, `Total duration (wall)`, `Total code changes` (lines added/removed), and `Usage by model` (input, output, cache read, cache write tokens and dollars per model).

The Session block is meant for API users. Pro, Max and Ultra subscribers have usage included, so the cost figure is not relevant for billing; they see plan usage bars, activity stats and a usage breakdown.

# Limits and defaults

- Totals reset when `/clear` starts a new session (next total starts at $0). Before v2.1.211 they accumulated across `/clear` for the life of the process.
- Responses billed at the 1.1x data residency rate are multiplied by 1.1 in the session cost. The same total appears in the status line cost field and counts toward `--max-budget-usd`.
