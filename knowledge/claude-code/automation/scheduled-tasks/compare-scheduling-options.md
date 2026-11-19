---
type: "Concept"
title: "Compare scheduling options"
description: "Cloud, Desktop and /loop scheduling differ in where they run, persistence, file access, permissions and minimum interval."
resource: "https://code.claude.com/docs/en/scheduled-tasks"
tags: [scheduling, cloud, desktop, loop]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, cloud]
requires: ""
identifiers:
  - "/loop"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "scheduled-tasks"
    resource: "https://code.claude.com/docs/en/scheduled-tasks"
    title: "Run prompts on a schedule"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code has three ways to schedule recurring or one-off work. `/loop` tasks are session-scoped; cloud and Desktop tasks outlive any session.

# How to use it

| | Cloud | Desktop | `/loop` |
| :- | :- | :- | :- |
| Runs on | Cloud, Anthropic-managed by default | Your machine | Your machine |
| Requires machine on | No | Yes | Yes |
| Requires open session | No | No | Yes |
| Persistent across restarts | Yes | Yes | Restored on `--resume`, with exceptions |
| Access to local files | No (fresh clone) | Yes | Yes |
| MCP servers | Connectors configured per task | Config files and connectors | Inherits from session |
| Permission prompts | Auto mode by default | Configurable per task | Inherits from session |
| Minimum interval | 1 hour | 1 minute when Claude sets it, 1 hour in the forms | 1 minute |

Guidance from the page: cloud tasks for reliable work without your machine, Desktop tasks for local files and tools, `/loop` for quick polling during a session. GitHub Actions with a `schedule` trigger is another durable option.

# Notes

Two related needs are covered elsewhere: Channels (react to events instead of polling) and `/goal` (keep working turn after turn toward a condition rather than on an interval). Session-scoped tasks come back on `--resume` or `--continue` unless expired or otherwise excluded; see [limitations](./scheduling-limitations.md).
