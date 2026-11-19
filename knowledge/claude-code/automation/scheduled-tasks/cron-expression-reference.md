---
type: "Reference"
title: "Cron expression syntax"
description: "Standard 5-field cron syntax accepted by CronCreate, with examples and unsupported extensions."
resource: "https://code.claude.com/docs/en/scheduled-tasks"
tags: [cron, syntax, scheduling]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CronCreate"
  - "*/5 * * * *"
  - "0 * * * *"
  - "7 * * * *"
  - "0 9 * * *"
  - "0 9 * * 1-5"
  - "30 14 15 3 *"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "scheduled-tasks"
    resource: "https://code.claude.com/docs/en/scheduled-tasks"
    title: "Run prompts on a schedule"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`CronCreate` takes `minute hour day-of-month month day-of-week`. Every field supports `*`, single values (`5`), steps (`*/15`), ranges (`1-5`) and lists (`1,15,30`).

# How to use it

| Example | Meaning |
| :- | :- |
| `*/5 * * * *` | Every 5 minutes |
| `0 * * * *` | Every hour on the hour |
| `7 * * * *` | Every hour at 7 minutes past |
| `0 9 * * *` | Daily 9am local |
| `0 9 * * 1-5` | Weekdays 9am local |
| `30 14 15 3 *` | March 15, 2:30pm local |

# Limits and defaults

- Day-of-week: `0` or `7` is Sunday through `6` Saturday.
- Not supported: `L`, `W`, `?`, and name aliases such as `MON` or `JAN`.
- If both day-of-month and day-of-week are constrained, a date matches when either matches (vixie-cron semantics).
