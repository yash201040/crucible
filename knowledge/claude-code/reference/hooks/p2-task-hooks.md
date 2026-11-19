---
type: "Feature"
title: "TaskCreated and TaskCompleted hook events"
description: "Hooks that can block creating or completing a task; no matchers; also drive teammate behavior."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, tasks, agent-teams, quality-gates]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Task tools available in the session"
identifiers:
  - "TaskCreated"
  - "TaskCompleted"
  - "TaskCreate"
  - "TaskUpdate"
  - "task_id"
  - "task_subject"
  - "task_description"
  - "teammate_name"
  - "team_name"
  - "agent_id"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`TaskCreated` runs when a task is being created via `TaskCreate` (enforce naming, require descriptions); it does not fire in a session without the Task tools. `TaskCompleted` runs when a task is being marked completed: when any agent marks it via `TaskUpdate`, or when an agent team teammate finishes its turn with in-progress tasks (enforce passing tests or lint). Neither supports matchers.

# How to use it

Input for both: `task_id`, `task_subject`, optional `task_description`, `teammate_name`, `team_name` (deprecated, to be removed), and `agent_id` (the common field identifying the subagent or in-process teammate creating or completing the task; may be absent; v2.1.290 or later).

TaskCreated blocks with exit 2 (stderr is the message) or `{"decision": "block", "reason": "..."}`; Claude Code deletes the task and returns the message as the tool error. `continue: false` is ignored and Claude keeps working.

TaskCompleted:
- Exit 2: task not completed; stderr fed back to the model.
- `{"decision": "block", "reason": "..."}`: task stays open; Claude gets `reason`.
- `{"continue": false, "stopReason": "..."}`: at the end of a teammate's turn the teammate goes idle with the task in progress, even if another TaskCompleted hook blocks; `stopReason` shows in the teammate transcript. On a `TaskUpdate` call `continue: false` is ignored.

Both support all five hook types; prompt-hook behavior on `ok: false` is described in [prompt hooks](./p2-prompt-hooks.md).
