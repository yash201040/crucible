---
type: "Feature"
title: "AgentDefinition and Agent tool"
description: "Programmatic subagents via AgentDefinition, the Agent tool's input and output shapes, and background task messages."
resource: "https://code.claude.com/docs/en/agent-sdk/python"
tags: [subagents, agent-tool, background-tasks, worktree, python]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "AgentDefinition"
  - "agents"
  - "Agent"
  - "Task"
  - "disallowedTools"
  - "initialPrompt"
  - "maxTurns"
  - "background"
  - "permissionMode"
  - "mcpServers"
  - "memory"
  - "subagent_type"
  - "run_in_background"
  - "isolation"
  - "TaskStartedMessage"
  - "TaskProgressMessage"
  - "TaskNotificationMessage"
  - "TaskUsage"
  - "async_launched"
  - "remote_launched"
  - "TaskStop"
  - "KillShell"
  - "KillBash"
  - "TaskOutput"
  - "Monitor"
  - "forward_subagent_text"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-python"
    resource: "https://code.claude.com/docs/en/agent-sdk/python"
    title: "Agent SDK reference - Python"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Subagents can be defined in code with `AgentDefinition` (passed as `ClaudeAgentOptions.agents`, a dict of name to definition) and are launched by Claude through the `Agent` tool. `Task` is the old tool name, still accepted as an alias; the init `SystemMessage` `tools` list still reports it as `Task`.

# How to use it

`AgentDefinition` is a dataclass with camelCase field names (snake_case keywords raise `TypeError`):

| Field | Required | What it does |
| :- | :- | :- |
| `description` | yes | when to use the agent |
| `prompt` | yes | the agent's system prompt |
| `tools` | no | allowed tools; omitted inherits all tools available to subagents |
| `disallowedTools` | no | tools to remove; accepts `mcp__server`, `mcp__server__*`, `mcp__*` |
| `model` | no | `"sonnet"`, `"opus"`, `"haiku"`, `"inherit"` or full id |
| `skills` | no | skills preloaded at startup; others remain invocable via Skill |
| `memory` | no | `"user"`, `"project"` or `"local"` |
| `mcpServers` | no | server names or inline `{name: config}` dicts |
| `initialPrompt` | no | auto-submitted as first turn when the agent is the main thread agent |
| `maxTurns` | no | turn cap |
| `background` | no | run as a non-blocking background task |
| `effort` | no | named level or integer |
| `permissionMode` | no | mode inside the agent; subagent inheritance rules decide when it applies |

`Agent` tool input: `description`, `prompt`, `subagent_type`, `model` (`"sonnet"`, `"opus"`, `"haiku"`, `"fable"`), `effort`, `run_in_background`, `name`, `isolation` (`"worktree"` or `"remote"`); `team_name` and `mode` are deprecated and ignored.

Output is discriminated on `status`:
- `"completed"`: `agentId`, `agentType`, `content`, `resolvedModel` (Claude Code 2.1.174+), `modelsUsed` (2.1.212+, set only when the model was swapped mid-run), `totalToolUseCount`, `totalDurationMs`, `totalTokens`, `usage`, `toolStats`, `prompt`, `worktreePath`, `worktreeBranch`.
- `"async_launched"`: `isAsync`, `agentId`, `description`, `resolvedModel`, `modelsUsed`, `prompt`, `outputFile`, `canReadOutputFile`.
- `"remote_launched"`: `taskId`, `sessionUrl`, `description`, `prompt`, `outputFile`.

Background task stream messages (all `SystemMessage` subclasses): `TaskStartedMessage` (`task_id`, `description`, `task_type` of `"local_bash"`, `"local_agent"`, `"mcp_task"`, `"remote_agent"`), `TaskProgressMessage` (`usage` as `TaskUsage` with `total_tokens`, `tool_uses`, `duration_ms`; `last_tool_name`), `TaskNotificationMessage` (`status` of `"completed"`, `"failed"`, `"stopped"`, plus `output_file`, `summary`, `usage`). Stop a task with `ClaudeSDKClient.stop_task()` or the `TaskStop` tool.

# Limits and defaults

- `run_in_background` omitted: a call from your main agent runs the new agent in the background (`status: "async_launched"`); a call from a subagent waits for it, unless the definition sets `background` to `True`. Before Python SDK v0.2.169 (first to bundle Claude Code 2.1.302+) agents started by subagents also ran in the background by default.
- `usage` and `totalTokens` come from the subagent's final API request only, not the whole run. `output_tokens_details` needs SDK 0.2.136+ (Claude Code 2.1.228); `fallback_credit` needs SDK 0.2.162+ (Claude Code 2.1.285).
- Subagent text/thinking blocks of foreground subagents are omitted unless `forward_subagent_text=True`.
- `TaskOutput` (alias `BashOutput`) was removed in Claude Code 2.1.277; Claude reads a background task's output file with `Read`. Old `disallowed_tools` or deny entries naming them are ignored silently.
- `TaskStop` accepts `task_id` (`shell_id` deprecated); previous names `KillShell` and `KillBash` still work in permission rules, hook matchers and `tools`, `allowed_tools`, `disallowed_tools`.
