---
type: "Reference"
title: "Task-tracking tools and model availability"
description: "TodoWrite and Task tools are default only on older models; how to opt in on newer ones."
resource: "https://code.claude.com/docs/en/agent-sdk/todo-tracking"
tags: [todo, task-tools, models, opt-in]
kind: "tool"
maturity: "unlabelled"
since: "2.1.268"
surfaces: [sdk]
requires: "Claude Opus 4.7, Sonnet 4.6, Haiku 4.5 or earlier for default availability"
identifiers:
  - "TodoWrite"
  - "TaskCreate"
  - "TaskGet"
  - "TaskUpdate"
  - "TaskList"
  - "CLAUDE_CODE_ENABLE_TASKS"
  - "CLAUDE_CODE_ENABLE_TODO_TOOLS"
  - "allowedTools"
  - "allowed_tools"
  - "tools"
  - "pathToClaudeCodeExecutable"
  - "cli_path"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-todo-tracking"
    resource: "https://code.claude.com/docs/en/agent-sdk/todo-tracking"
    title: "Track todos"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Five tools: `TodoWrite`, `TaskCreate`, `TaskGet`, `TaskUpdate`, `TaskList`. They are available by default only on Claude Opus 4.7, Claude Sonnet 4.6, Claude Haiku 4.5 and earlier models. On every other model, including unrecognized model IDs, they are absent unless you opt in. Newer models track multi-step work without a written todo list. This default set applies in Claude Code v2.1.268 and later (TypeScript Agent SDK bundles it from v0.3.268).

# How to use it

Where available, Claude Code provides the four Task tools, or `TodoWrite` instead when `CLAUDE_CODE_ENABLE_TASKS=0`. Opt a session in by one of:
- naming one of the tools in `allowedTools` / `allowed_tools`
- listing them in the `tools` option (restricts built-ins to those named; include others you need)
- setting `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` in `env`. In TypeScript `env` replaces the subprocess environment, so spread `...process.env`; in Python `env` is merged on the inherited one.

# Limits and defaults

Without opt-in on such a model there are no `tool_use` blocks for them in the stream. If you point `pathToClaudeCodeExecutable` (TypeScript) or `cli_path` (Python) at your own install, that install's defaults apply.
