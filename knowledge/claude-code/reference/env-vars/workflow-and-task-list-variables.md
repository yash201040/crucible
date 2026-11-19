---
type: "Reference"
title: "Workflow and task list variables"
description: "Variables for workflow concurrency, same-prefix staggering for cache reuse, disabling workflows and the shared task list tools."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [workflows, concurrency, task-list, caching]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.269"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "CLAUDE_CODE_DISABLE_WORKFLOWS"
  - "CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS"
  - "CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS"
  - "CLAUDE_CODE_ENABLE_TASKS"
  - "CLAUDE_CODE_ENABLE_TODO_TOOLS"
  - "CLAUDE_CODE_TASK_LIST_ID"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Controls for workflow runs (fan-out of many agents) and the task-tracking tools.

# How to use it

| Variable | What it does |
| :- | :- |
| `CLAUDE_CODE_DISABLE_WORKFLOWS` | `1` disables workflows; same as the `disableWorkflows` setting. |
| `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` | Agents one workflow run executes at once, `1` to `256`. Default up to 16, fewer when fewer CPUs are available; queued `agent()` calls wait for a slot. Every running agent's transcript stays in memory, so higher values raise memory use. Plain digits only; out-of-range keeps default. Requires v2.1.269+. |
| `CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS` | Upper bound on how long a workflow agent waits for a same-prefix sibling's first response before sending its own first request, so siblings read the cached prefix. Default `5000`; `0` disables; never waits when `DISABLE_PROMPT_CACHING` is set. Requires v2.1.229+. |
| `CLAUDE_CODE_ENABLE_TASKS` | Selects task tools. Default provides `TaskCreate`, `TaskUpdate`, `TaskGet`, `TaskList`; `0` gives legacy `TodoWrite`. |
| `CLAUDE_CODE_ENABLE_TODO_TOOLS` | `1` provides the task tools on every model (otherwise only on listed models). `CLAUDE_CODE_ENABLE_TASKS` still picks Task tools vs `TodoWrite`. Requires v2.1.233+. |
| `CLAUDE_CODE_TASK_LIST_ID` | Same ID across Claude Code instances shares one task list, in sessions that have the Task tools. |
