---
type: "Concept"
title: "Todo lifecycle and when Claude creates todos"
description: "Statuses pending, in_progress, completed, deleted, and the situations in which Claude creates todos."
resource: "https://code.claude.com/docs/en/agent-sdk/todo-tracking"
tags: [todo, lifecycle, status, tasks]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "pending"
  - "in_progress"
  - "completed"
  - "deleted"
  - "TaskUpdate"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-todo-tracking"
    resource: "https://code.claude.com/docs/en/agent-sdk/todo-tracking"
    title: "Track todos"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

In a session that has the task tools, Claude keeps a written todo list and updates each item's status; changes appear in the stream as structured tool calls. Opt in only when your application reads those calls.

# How to use it

Lifecycle: created as `pending`; set `in_progress` when work starts; `completed` when done; removed by `TaskUpdate` with `status: "deleted"`.

Claude creates todos for: multi-step tasks of three or more actions, user-provided task lists, longer operations, explicit requests. It may skip very short or single-step requests.

# Notes

Task system messages (`SDKTaskNotificationMessage` in TypeScript, `TaskNotificationMessage` in Python) report background tasks such as backgrounded commands and subagents, not todos. Todo activity shows as `tool_use` blocks in assistant messages.
