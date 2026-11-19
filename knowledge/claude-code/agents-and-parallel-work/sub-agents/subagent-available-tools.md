---
type: "Reference"
title: "Tools available to subagents"
description: "Which tools every subagent loses, and the smaller built-in tool set of background subagents."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, tools, background, filters]
kind: "tool"
maturity: "unlabelled"
since: "2.1.280"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "Agent"
  - "AskUserQuestion"
  - "EndConversation"
  - "EnterPlanMode"
  - "ExitPlanMode"
  - "ScheduleWakeup"
  - "WaitForMcpServers"
  - "Workflow"
  - "LSP"
  - "SubagentHandback"
  - "ListAgents"
  - "TaskCreate"
  - "TaskGet"
  - "TaskList"
  - "TaskUpdate"
  - "CronCreate"
  - "CronDelete"
  - "CronList"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Subagents inherit built-in tools and MCP tools of the main conversation, narrowed by two filters. Forks skip both filters and get the parent's exact tool pool. On macOS, Linux and WSL a subagent can also receive Glob and Grep when the main conversation lacks them.

# How to use it

Filter 1 removes these from every subagent, even when listed in `tools`:

| Tool | Condition |
| :- | :- |
| `Agent` | When at the depth limit (in a fork it stays listed but errors) |
| `AskUserQuestion`, `EnterPlanMode`, `ScheduleWakeup`, `WaitForMcpServers`, `Workflow` | Always |
| `EndConversation` | Always (can end only main conversation) |
| `ExitPlanMode` | Unless `permissionMode` is `plan` |

Filter 2 applies to background subagents (the default). Apart from `Agent` and `ExitPlanMode`, a background subagent keeps every MCP tool but only these built-ins: `Read`, `Grep`, `Glob`, `LSP`, `Bash`, `PowerShell`, `Edit`, `Write`, `NotebookEdit`, `WebFetch`, `WebSearch`, `TodoWrite`, `Skill`, `ToolSearch`, `EnterWorktree`, `ExitWorktree`, `Monitor`, `TaskStop`, `SendMessage`, `Artifact`, plus `SubagentHandback` for one that reports through it. Everything else is removed silently unless the `tools` list then resolves to nothing.

# Notes

- Before v2.1.280, background subagents could not use `LSP`.
- `ListAgents`: foreground subagents inherit it where cross-session messaging is enabled; background ones do not.
- Agent team teammates additionally keep `TaskCreate`, `TaskGet`, `TaskList`, `TaskUpdate`, `CronCreate`, `CronDelete`, `CronList`. Without the Task tools in the session, subagents do not get task tools either.
