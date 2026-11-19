---
type: "Feature"
title: "Task list (Claude's checklist)"
description: "Claude's to-do checklist toggled with Ctrl+T, shared across sessions with CLAUDE_CODE_TASK_LIST_ID."
resource: "https://code.claude.com/docs/en/interactive-mode#task-list"
tags: [tasks, checklist, sessions, persistence]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "A model with task-tracking tools, or opt-in"
identifiers:
  - "CLAUDE_CODE_TASK_LIST_ID"
  - "CLAUDE_CODE_ENABLE_TODO_TOOLS"
  - "~/.claude/tasks/"
  - "Ctrl+T"
  - "/tasks"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "interactive-mode"
    resource: "https://code.claude.com/docs/en/interactive-mode"
    title: "Interactive mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Items Claude creates to plan multi-step work, shown as pending, in progress or complete. Separate from the background-task view (`/tasks`).

# How to use it

- `Ctrl+T` toggles the view (up to five tasks shown). Ask Claude "show me all tasks" or "clear all tasks".
- Tasks persist across context compactions. An expanded list is restored on `--resume` or `--continue` if tasks remain.
- Share a list across sessions: `CLAUDE_CODE_TASK_LIST_ID=my-project claude` uses a named directory under `~/.claude/tasks/`.

# Limits and defaults

The list fills only where task-tracking tools exist: by default Opus 4.7, Sonnet 4.6, Haiku 4.5 and earlier. On other models (including unrecognized model IDs) it stays empty unless `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` or another opt-in; see [Task tool availability](../tools-reference/task-tool-availability.md).
