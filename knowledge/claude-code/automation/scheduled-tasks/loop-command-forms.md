---
type: "Feature"
title: "The /loop command"
description: "The /loop bundled skill reruns a prompt on a fixed interval, a Claude-chosen interval, or a built-in maintenance prompt."
resource: "https://code.claude.com/docs/en/scheduled-tasks"
tags: [loop, scheduling, polling, skills]
kind: "slash_command"
maturity: "unlabelled"
since: "2.1.248"
surfaces: [cli]
requires: "Dynamic intervals and the built-in maintenance prompt need v2.1.248 or later on Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform, Microsoft Foundry, or with feature-flag fetching off"
identifiers:
  - "/loop"
  - "/loop 5m"
  - "/loop 20m /review-pr 1234"
  - "ScheduleWakeup"
  - "disable-model-invocation"
  - "skillOverrides"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "scheduled-tasks"
    resource: "https://code.claude.com/docs/en/scheduled-tasks"
    title: "Run prompts on a schedule"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/loop` is a bundled skill that reruns a prompt while the session stays open. Interval and prompt are both optional; what you give decides the behavior.

# How to use it

| You provide | Example | Result |
| :- | :- | :- |
| Interval and prompt | `/loop 5m check the deploy` | Fixed schedule |
| Prompt only | `/loop check the deploy` | Claude picks the interval each iteration |
| Interval only, or nothing | `/loop` | Built-in maintenance prompt, or `loop.md` if present |

- Interval can lead as a bare token (`30m`) or trail as a clause (`every 2 hours`). Units: `s`, `m`, `h`, `d`.
- Fixed interval: Claude converts it to a cron expression, schedules it and confirms cadence and job ID. Seconds round up to the nearest minute (cron granularity). Intervals without a clean cron step (`7m`, `90m`) round to the nearest one that has, and Claude says which.
- Dynamic interval: after each iteration Claude picks a delay between 1 minute and 1 hour from what it observed and prints the delay and reason. The loop shows in the task list as a one-shot wakeup (which can run slightly early on `:00`/`:30`), and the 7-day expiry applies.
- With the Monitor tool available, Claude may use it directly for a dynamic loop request; it streams a background script's output and can be more token-efficient than polling.
- A skill can be the prompt, e.g. `/loop 20m /review-pr 1234`.

# Limits and defaults

A scheduled fire only runs skills Claude may invoke itself. These arrive as plain text instead of executing: built-in commands (`/permissions`, `/model`, `/clear`), skills with `disable-model-invocation: true` (including bundled `/verify`), skills hidden by a `skillOverrides` setting or a `Skill` deny rule, and MCP prompts such as `/mcp__github__list_prs`.

# Notes

The built-in maintenance prompt, in order: continue unfinished work from the conversation; tend the current branch's PR (review comments, failed CI, merge conflicts); run cleanup passes (bug hunts, simplification) when nothing is pending. Each run goes through the session's permission checks before pushing or deleting. See [loop.md](./loop-md-default-prompt.md) and [stopping loops](./stop-a-loop.md).
