---
type: "Concept"
title: "Session scope and resume"
description: "Scheduled tasks belong to the session; --resume and --continue restore unexpired ones."
resource: "https://code.claude.com/docs/en/scheduled-tasks"
tags: [sessions, resume, scheduling]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "--resume"
  - "--continue"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "scheduled-tasks"
    resource: "https://code.claude.com/docs/en/scheduled-tasks"
    title: "Run prompts on a schedule"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Scheduled tasks created with `/loop` or the cron tools are scoped to a session. They are not durable scheduling: for scheduling that survives independently of any session, the page points to cloud scheduled tasks (Routines), Desktop scheduled tasks, or GitHub Actions.

# How to use it

Resume with `claude --resume` or `claude --continue` to get back tasks that have not [expired](./seven-day-expiry.md), apart from the cases in [limitations](./scheduling-limitations.md).

# Notes

Inheritance: a `/loop` task inherits MCP servers and permission prompts from its session.
