---
type: "Guide"
title: "Monitor todo changes from the stream"
description: "Watch TaskCreate and TaskUpdate tool_use blocks to log task activity, handling repaired key names defensively."
resource: "https://code.claude.com/docs/en/agent-sdk/todo-tracking"
tags: [todo, monitoring, stream, tool-use]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "TaskCreate"
  - "TaskUpdate"
  - "taskId"
  - "id"
  - "task_id"
  - "activeForm"
  - "active_form"
  - "error_max_turns"
  - "maxTurns"
  - "max_turns"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-todo-tracking"
    resource: "https://code.claude.com/docs/en/agent-sdk/todo-tracking"
    title: "Track todos"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Scan assistant messages for `tool_use` blocks named `TaskCreate` (input has `subject`) and `TaskUpdate` (input has task ID and `status`) to log task activity.

# How to use it

- The example sets `permissionMode: "acceptEdits"`, `maxTurns: 15` and `CLAUDE_CODE_ENABLE_TODO_TOOLS: "1"` in `env`.
- The streamed `tool_use` input is the raw model output. Claude Code repairs close-but-wrong keys before execution (`id` or `task_id` become `taskId`; `active_form` becomes `activeForm`), but the repair is not shown in the stream, so read `taskId ?? id ?? task_id` defensively.
- The `+` log lines carry no assigned IDs, so updates cannot be matched to creates; use the [real-time display pattern](./display-progress-in-real-time.md) for that.

# Limits and defaults

A single-shot `query()` that hits its turn limit yields a result with subtype `error_max_turns`, then raises an error containing `Reached maximum number of turns`; wrap the loop in try.
