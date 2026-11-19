---
type: "Limit"
title: "Scheduled task usage and hourly limits"
description: "Hourly run caps per account and per task for scheduled, Run now and API-fired runs, and behavior at subscription limits."
resource: "https://code.claude.com/docs/en/routines"
tags: [limits, rate-limits, usage, scheduled-tasks, cost]
kind: "limit"
maturity: "research-preview"
since: ""
surfaces: [cloud]
requires: ""
identifiers: []
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "routines"
    resource: "https://code.claude.com/docs/en/routines"
    title: "Automate work with scheduled tasks"
stale_after: "2027-01-19T00:00:00Z"
---

# Limits and defaults

Scheduled task runs draw down subscription usage like interactive sessions. Separate hourly limits per start method (no overage on any):

| Action | Limit | Counted for | Over the limit |
|---|---|---|---|
| Scheduled runs, including one-off | 100 per hour | account | run waits until reset |
| Run now, API fires, re-running a one-off | 30 per hour | each task (one shared count) | action fails until reset |
| Run now and re-running a one-off | 100 per hour | account | action fails |
| API fires | 100 per hour | account (separate from Run now) | action fails |
| GitHub events | per-task and per-account hourly caps | | events dropped until reset |

When the subscription usage limit is hit, orgs with usage credits can continue on metered overage; otherwise further runs are rejected until the window resets. While the subscription is paused, tasks are on hold and must be turned back on afterwards.
