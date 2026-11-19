---
type: "Guide"
title: "Display todo progress in real time"
description: "Pair TaskCreate tool_use with its tool_result by tool_use_id to read the assigned task id from tool_use_result."
resource: "https://code.claude.com/docs/en/agent-sdk/todo-tracking"
tags: [todo, progress, tool-result, tracker]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "tool_use_result"
  - "TaskCreateOutput"
  - "tool_use_id"
  - "TaskList"
  - "TaskGet"
  - "activeForm"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-todo-tracking"
    resource: "https://code.claude.com/docs/en/agent-sdk/todo-tracking"
    title: "Track todos"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A `TaskTracker` pattern keeps a map of tasks by ID and re-renders a progress summary (completed count, in-progress count, each active item's `activeForm` label in place of `subject`).

# How to use it

- The assigned task ID is not in the `TaskCreate` input. Claude Code delivers each tool's structured output on the user message carrying the `tool_result` block, in the `tool_use_result` field. For `TaskCreate` that is `TaskCreateOutput` (TypeScript, `{ task: { id, subject } }`), a plain dict in Python.
- Pair each `tool_result` with its `tool_use` by `tool_use_id`, read `task.id`, skip when `is_error`.
- Handle `status: "deleted"` by removing the task.
- Claude can read the list with `TaskList` and one task with `TaskGet`.
- The example uses `maxTurns: 20`, `permissionMode: "acceptEdits"` and `CLAUDE_CODE_ENABLE_TODO_TOOLS: "1"`.
