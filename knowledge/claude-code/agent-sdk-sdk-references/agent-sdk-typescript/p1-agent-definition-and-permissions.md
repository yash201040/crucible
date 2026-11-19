---
type: "Reference"
title: "AgentDefinition, permission modes and canUseTool"
description: "Programmatic subagent fields, PermissionMode values, the canUseTool callback options, PermissionResult and setting sources."
resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
tags: [subagents, permissions, canusetool, settings-sources]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "AgentDefinition"
  - "initialPrompt"
  - "autoCompactWindow"
  - "background"
  - "omitClaudeMd"
  - "memory"
  - "criticalSystemReminder_EXPERIMENTAL"
  - "disallowedTools"
  - "PermissionMode"
  - "default"
  - "acceptEdits"
  - "bypassPermissions"
  - "plan"
  - "dontAsk"
  - "auto"
  - "CanUseTool"
  - "PermissionResult"
  - "PermissionUpdate"
  - "requestId"
  - "defaultToNo"
  - "suppressAlwaysAllowRule"
  - "updatedPermissions"
  - "SettingSource"
  - "ToolConfig"
  - "askUserQuestion.previewFormat"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-typescript"
    resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
    title: "Agent SDK reference - TypeScript"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`AgentDefinition` defines a subagent in the `agents` option. `PermissionMode` and `canUseTool` control approvals for unattended or hosted runs.

# How to use it

`AgentDefinition` fields:

| Field | Required | Notes |
| :- | :- | :- |
| `description` | yes | When to use the agent |
| `prompt` | yes | System prompt |
| `tools` | no | Allowed tools; omitted inherits all subagent tools; use `skills` to preload skills, not `'Skill'` |
| `disallowedTools` | no | Also accepts `mcp__server`, `mcp__server__*`, `mcp__*` |
| `model` | no | `'fable'`, `'opus'`, `'sonnet'`, `'haiku'`, `'inherit'` or full ID |
| `mcpServers`, `skills` | no | Per-agent MCP and preloaded skills |
| `initialPrompt` | no | First user turn when run as main-thread agent |
| `maxTurns` | no | API round-trip cap |
| `autoCompactWindow` | no | Token count of `100000` or more; v0.3.296+ |
| `background` | no | Non-blocking background task |
| `omitClaudeMd` | no | Skip user/project/local CLAUDE.md (managed still loads); ignored for main-thread agent; v0.3.271+ |
| `memory` | no | `'user'|'project'|'local'` |
| `effort` | no | Named level or integer |
| `permissionMode` | no | Subagent inheritance rules decide when it applies |
| `criticalSystemReminder_EXPERIMENTAL` | no | Experimental reminder in system prompt |

`PermissionMode`: `default`, `acceptEdits`, `bypassPermissions` (explicit ask rules still prompt), `plan`, `dontAsk` (deny if not pre-approved), `auto` (model classifier reviews actions).

`canUseTool(toolName, input, options)` runs only when the flow falls through to a prompt (not for `allowedTools`, allow rules or mode approvals; use a `PreToolUse` hook to check those). Options: `signal`, `suggestions`, `blockedPath`, `mcpServer` (v0.3.274+), `decisionReason`, `defaultToNo` and `suppressAlwaysAllowRule` (v0.3.268+), `toolUseID`, `agentID`, `requestId`. Return `{ behavior: "allow", updatedInput?, updatedPermissions?, toolUseID? }` or `{ behavior: "deny", message, interrupt?, toolUseID? }`. Return `null` only if you already sent the `control_response` yourself echoing `requestId` (v2.1.199+); otherwise the tool call blocks indefinitely, because prompts do not time out.

# Limits and defaults

- More than 4,096 items in `updatedPermissions` makes the result invalid and the call is denied.
- `SettingSource`: `'user'` (`~/.claude/settings.json`), `'project'` (`.claude/settings.json`), `'local'` (`.claude/settings.local.json`). Omitted means all three. Precedence local > project > user; programmatic options override them; a managed policy value wins over a programmatic option (except e.g. `effortLevel` via `applyFlagSettings()`). Include `"project"` to load CLAUDE.md.
- `PermissionUpdate` types: `addRules`, `replaceRules`, `removeRules`, `setMode`, `addDirectories`, `removeDirectories`; destinations `userSettings`, `projectSettings`, `localSettings`, `session`, `cliArg`; behaviors `allow|deny|ask`.
