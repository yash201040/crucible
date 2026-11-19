---
type: "Reference"
title: "Cron tools and task management"
description: "CronCreate, CronList and CronDelete tools for session-scoped scheduled tasks, with ID format and the 50-task cap."
resource: "https://code.claude.com/docs/en/scheduled-tasks"
tags: [cron, tools, scheduling, limits]
kind: "tool"
maturity: "unlabelled"
since: "2.1.299"
surfaces: [cli]
requires: "Next-run times in CronList rows need v2.1.299 or later"
identifiers:
  - "CronCreate"
  - "CronList"
  - "CronDelete"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "scheduled-tasks"
    resource: "https://code.claude.com/docs/en/scheduled-tasks"
    title: "Run prompts on a schedule"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude manages session-scoped tasks through three tools. You can ask in natural language ("what scheduled tasks do I have?", "cancel the deploy check job") or name the tools.

# How to use it

| Tool | Purpose |
| :- | :- |
| `CronCreate` | Schedule a task: a 5-field cron expression, the prompt, and whether it recurs or fires once |
| `CronList` | List tasks with IDs, schedules, next run times and prompts |
| `CronDelete` | Cancel a task by ID |

# Limits and defaults

- Each task has an 8-character ID for `CronDelete`.
- A session holds at most 50 scheduled tasks at once.
- The scheduler checks every second and enqueues due tasks at low priority; a prompt fires between turns, never mid-response. If Claude is busy, it waits until the turn ends.
- All times use your local timezone (`0 9 * * *` is 9am local, not UTC).

# Notes

Disabling: see [disable scheduler](./disable-session-scheduling.md). Cron syntax: [cron reference](./cron-expression-reference.md).
