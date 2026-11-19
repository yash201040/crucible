---
type: "Feature"
title: "Asynchronous hook output"
description: "Return async true so the agent continues without waiting; usable only for side effects like logging."
resource: "https://code.claude.com/docs/en/agent-sdk/hooks"
tags: [hooks, async, logging, side-effects]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "async"
  - "async_"
  - "asyncTimeout"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-hooks"
    resource: "https://code.claude.com/docs/en/agent-sdk/hooks"
    title: "Intercept and control agent behavior with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

By default the agent waits for a hook to return. An async output tells the agent to continue immediately.

# How to use it

Start a background task, then return `{"async_": True, "asyncTimeout": 30000}` (Python) or `{ async: true, asyncTimeout: 30000 }` (TypeScript).

| Field | Type | Description |
| - | - | - |
| `async` | `true` | async mode; in Python use `async_` (reserved keyword) |
| `asyncTimeout` | number | optional timeout in milliseconds for the background operation |

# Limits and defaults

Async outputs cannot block, modify or inject context because the agent has already moved on; use them only for logging, metrics or notifications.
