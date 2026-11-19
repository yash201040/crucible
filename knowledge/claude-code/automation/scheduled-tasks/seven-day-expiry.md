---
type: "Limit"
title: "Seven-day expiry of recurring tasks"
description: "Recurring session-scoped tasks fire a final time and delete themselves 7 days after creation."
resource: "https://code.claude.com/docs/en/scheduled-tasks"
tags: [expiry, limits, scheduling, loop]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers: []
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "scheduled-tasks"
    resource: "https://code.claude.com/docs/en/scheduled-tasks"
    title: "Run prompts on a schedule"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Recurring tasks expire 7 days after creation. The task fires one final time, then deletes itself. This bounds how long a forgotten loop can run. It applies to dynamic `/loop` schedules too.

# How to use it

For a longer life, cancel and recreate the task before it expires, or use cloud scheduled tasks or Desktop scheduled tasks for durable scheduling.

# Notes

On `--resume` or `--continue`, expired recurring tasks are not restored.
