---
type: "Feature"
title: "Task tool availability"
description: "Which models get TaskCreate/TaskGet/TaskList/TaskUpdate by default, how to opt in, and behavior in subagents and agent teams."
resource: "https://code.claude.com/docs/en/tools-reference#task-tool-availability"
tags: [tasks, models, agent-teams, subagents, opt-in]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.268"
surfaces: [cli, sdk, cloud]
requires: ""
identifiers:
  - "CLAUDE_CODE_ENABLE_TASKS"
  - "CLAUDE_CODE_ENABLE_TODO_TOOLS"
  - "--allowedTools"
  - "--tools"
  - "--settings"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`TaskCreate`, `TaskGet`, `TaskUpdate`, `TaskList` and `TodoWrite` are provided by default only on Opus 4.7, Sonnet 4.6, Haiku 4.5 and earlier models (default set applies from v2.1.268). Where available you get the four Task tools, or `TodoWrite` when `CLAUDE_CODE_ENABLE_TASKS=0`. Other models, and unrecognized model IDs such as a custom name via an LLM gateway, omit them because newer models track multi-step work without a checklist and the tool definitions cost context.

# How to use it

Opt in on other models by: exporting `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` (same tools on every model and provider); naming a tool in `--allowedTools` (e.g. `claude --allowedTools TaskCreate`); listing tools in `--tools`; or in the Agent SDK using `allowedTools` and `tools` options. Background sessions and cloud sessions provide the tools on every model.

Subagents and teams:
- A subagent has the task tools only when your session does, whatever model it runs. An in-process agent team teammate has them when the session does.
- A split-pane teammate is a separate process that inherits your `--tools` list and deny rules, not `--allowedTools`. With no `--tools` or deny rule and the variable unset, it gets its own model's defaults. An exported `CLAUDE_CODE_ENABLE_TODO_TOOLS` is not passed to it (it receives a fixed set of env variables); start with `claude --settings '{"env":{"CLAUDE_CODE_ENABLE_TODO_TOOLS":"1"}}'` so the teammate gets it too. `--tools` naming them gives them on any model; a tool missing from `--tools` or in a deny rule is lacking.
- Without the Task tools an agent coordinates through messages instead of the shared task list.
