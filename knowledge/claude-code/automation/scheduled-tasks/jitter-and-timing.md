---
type: "Concept"
title: "Jitter and run timing"
description: "Claude Code offsets scheduled run times: recurring tasks run late by up to half the gap (max 30 min), one-shots on :00/:30 up to 90 s early."
resource: "https://code.claude.com/docs/en/scheduled-tasks"
tags: [jitter, scheduling, cron, timing]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.299"
surfaces: [cli]
requires: "Next-run times in CronCreate/CronList rows need v2.1.299 or later"
identifiers:
  - "*/5 * * * *"
  - "next run"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "scheduled-tasks"
    resource: "https://code.claude.com/docs/en/scheduled-tasks"
    title: "Run prompts on a schedule"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

So that many sessions do not hit the API at the same instant, Claude Code shifts each task's run time. Recurring tasks run late (except every-5-minutes); one-shot tasks scheduled on the hour or half hour run slightly early.

# How to use it

Find the next due time in the row under the `CronCreate` call (for example `next run 10:21 AM`), or ask Claude to list tasks and read `next run` under `CronList`.

| Schedule | When each run starts |
| :- | :- |
| Every 5 minutes (`*/5 * * * *`, what `/loop 5m` creates) | 4 min 45 s after the previous run |
| Every 10 minutes | 0 to 5 minutes late |
| Every 30 minutes | 0 to 15 minutes late |
| Hourly or less often | 0 to 30 minutes late |

# Limits and defaults

- Other recurring tasks: late by up to half the gap to the next run, at most 30 minutes.
- Evenly spaced tasks run the same number of minutes late every time; unevenly spaced ones (e.g. `:00` and `:15`) can differ per run.
- The 5-minute case starts 15 s sooner because a run exactly five minutes later would find the 5-minute prompt cache expired.
- One-shot on `:00` or `:30`: up to 90 seconds early. Other minutes are not shifted, so when timing matters use `3 9 * * *` instead of `0 9 * * *`.
- Example: `7,37 * * * *` has a 0 to 15 minute delay; at 14 minutes it runs at `:21` and `:51`. Changing the minute moves the run, and delay is added on top.
