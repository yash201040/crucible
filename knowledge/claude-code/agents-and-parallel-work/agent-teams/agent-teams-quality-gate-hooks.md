---
type: "Reference"
title: "Hooks for agent team quality gates"
description: "TeammateIdle, TaskCreated and TaskCompleted hooks that can block with exit code 2 and send feedback."
resource: "https://code.claude.com/docs/en/agent-teams"
tags: [agent-teams, hooks, quality-gates, tasks]
kind: "hook"
maturity: "experimental"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "TeammateIdle"
  - "TaskCreated"
  - "TaskCompleted"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-teams"
    resource: "https://code.claude.com/docs/en/agent-teams"
    title: "Orchestrate teams of Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Hooks that enforce rules when teammates finish work or tasks change.

# How to use it

| Hook | Runs when | Exit code 2 does |
| - | - | - |
| `TeammateIdle` | a teammate is about to go idle | sends feedback and keeps the teammate working |
| `TaskCreated` | a task is being created | prevents creation and sends feedback |
| `TaskCompleted` | a task is being marked complete | prevents completion and sends feedback |

# Notes

Full hook semantics are on the hooks page.
