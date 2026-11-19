---
type: "Reference"
title: "AgentDefinition fields"
description: "All fields of an SDK subagent definition: description, prompt, tools, model, skills, memory, mcpServers, maxTurns, effort, background and more."
resource: "https://code.claude.com/docs/en/agent-sdk/subagents"
tags: [subagents, agentdefinition, fields, model]
kind: "api"
maturity: "unlabelled"
since: "2.1.246"
surfaces: [sdk]
requires: ""
identifiers:
  - "description"
  - "prompt"
  - "tools"
  - "disallowedTools"
  - "model"
  - "skills"
  - "memory"
  - "mcpServers"
  - "initialPrompt"
  - "maxTurns"
  - "autoCompactWindow"
  - "background"
  - "omitClaudeMd"
  - "effort"
  - "permissionMode"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-subagents"
    resource: "https://code.claude.com/docs/en/agent-sdk/subagents"
    title: "Subagents in the SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The fields of an `AgentDefinition`. In Python, multi-word names such as `disallowedTools` and `mcpServers` keep camelCase to match the wire format.

# How to use it

| Field | Type | Required | What it does |
| --- | --- | --- | --- |
| `description` | string | Yes | When to use this agent |
| `prompt` | string | Yes | System prompt defining role and behavior |
| `tools` | string[] | No | Allowed tool names; if omitted, inherits every tool available to subagents |
| `disallowedTools` | string[] | No | Tools to remove; accepts MCP patterns `mcp__server`, `mcp__server__*`, `mcp__*` (every MCP tool) |
| `model` | string | No | Alias `'fable'`, `'opus'`, `'sonnet'`, `'haiku'`, `'inherit'` (model of the spawning agent) or full model ID; if omitted follows the subagent model order in the Claude Code docs |
| `skills` | string[] | No | Skill names preloaded at startup; at most the first 32 distinct names; unlisted skills remain invocable via the Skill tool |
| `memory` | `'user'`, `'project'`, `'local'` | No | Memory source |
| `mcpServers` | (string or object)[] | No | MCP servers by name or inline config |
| `initialPrompt` | string | No | Auto-submitted first user turn when the agent runs as the main thread agent; ignored as a subagent |
| `maxTurns` | number | No | Max agentic turns; at the limit output is marked partial and the agent can be resumed (partial marking needs Claude Code v2.1.246 or later) |
| `autoCompactWindow` | number | No | Lowers the auto-compact window for this subagent to a token count of 100000 or more; needs TypeScript Agent SDK v0.3.296 or later; not in Python |
| `background` | boolean | No | Run as a non-blocking background task |
| `omitClaudeMd` | boolean | No | Leave user, project, local CLAUDE.md out of initial context (managed policy files still load); ignored for main thread agent; needs TypeScript SDK v0.3.271 or later; not in Python |
| `effort` | `'low'`, `'medium'`, `'high'`, `'xhigh'`, `'max'` or number | No | Reasoning effort |
| `permissionMode` | PermissionMode | No | Permission mode for tool execution; subagent inheritance rules decide when it applies |

# Notes

Tool restriction: a tool omitted from `tools` is not in the subagent's session at all, so Claude works without it and there is no prompt or error. Common combinations: read-only analysis `Read`, `Grep`, `Glob`; test execution `Bash`, `Read`, `Grep`; code modification `Read`, `Edit`, `Write`, `Grep`, `Glob`; full access = omit `tools`.
