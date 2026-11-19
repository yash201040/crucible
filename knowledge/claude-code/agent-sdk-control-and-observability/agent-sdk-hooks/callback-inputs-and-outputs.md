---
type: "Reference"
title: "Hook callback inputs and output fields"
description: "The three callback arguments, shared input fields, and top-level and hookSpecificOutput return fields including permission decisions."
resource: "https://code.claude.com/docs/en/agent-sdk/hooks"
tags: [hooks, outputs, permission-decision, updated-input]
kind: "api"
maturity: "unlabelled"
since: "0.3.236"
surfaces: [sdk]
requires: "classifierContext needs TypeScript Agent SDK v0.3.236 or later"
identifiers:
  - "session_id"
  - "cwd"
  - "hook_event_name"
  - "agent_id"
  - "agent_type"
  - "tool_name"
  - "tool_input"
  - "systemMessage"
  - "continue"
  - "continue_"
  - "hookSpecificOutput"
  - "hookEventName"
  - "permissionDecision"
  - "permissionDecisionReason"
  - "updatedInput"
  - "additionalContext"
  - "updatedToolOutput"
  - "updatedMCPToolOutput"
  - "classifierContext"
  - "tool_deferred"
  - "PreToolUseHookInput"
  - "NotificationHookInput"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-hooks"
    resource: "https://code.claude.com/docs/en/agent-sdk/hooks"
    title: "Intercept and control agent behavior with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Every callback receives three arguments: (1) a typed input object (e.g. `PreToolUseHookInput` has `tool_name` and `tool_input`; `NotificationHookInput` has `message`); (2) the tool use ID (`str | None` / `string | undefined`) that correlates `PreToolUse` and `PostToolUse` for one call; (3) a context: in TypeScript it holds `signal` (`AbortSignal`), in Python it is reserved.

All inputs share `session_id`, `cwd`, `hook_event_name`. `agent_id` and `agent_type` are set when the hook fires inside a subagent: on the base input in TypeScript; in Python optional on `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest` and required on `SubagentStart`, `SubagentStop`.

# How to use it

Return `{}` to allow without changes. Output has two kinds of fields:

| Field | Where | Effect |
| - | - | - |
| `systemMessage` | top level | message shown to the user (not the model) |
| `continue` / `continue_` | top level | whether the agent keeps running |
| `permissionDecision` | `hookSpecificOutput`, `PreToolUse` | `"allow"`, `"deny"`, `"ask"`, `"defer"` |
| `permissionDecisionReason` | `hookSpecificOutput` | reason given to the model |
| `updatedInput` | `hookSpecificOutput`, `PreToolUse` | replaces the whole tool input |
| `additionalContext` | `hookSpecificOutput`, `PostToolUse` | appended to the tool result |
| `updatedToolOutput` | `hookSpecificOutput`, `PostToolUse` | replaces tool output before Claude sees it; built-in and MCP tools, both SDKs |
| `updatedMCPToolOutput` | `hookSpecificOutput` | older field; MCP tool output only |
| `classifierContext` | `hookSpecificOutput`, `PostToolUse`, TypeScript only | short note for the auto mode permission classifier |

Include `hookEventName` in `hookSpecificOutput`. Same JSON format as shell command hooks. Some events discard top-level fields; see each event's section on the hooks page.

# Limits and defaults

- `"defer"` ends the turn with a result whose `stop_reason` is `"tool_deferred"`, so the call can be resumed later; `updatedInput` is ignored with `"defer"`.
- With several `PreToolUse` hooks, precedence is `deny` over `defer` over `ask` over `allow`.
- `classifierContext` can be weighed as user intent by the classifier; the hooks page covers its length cap and synchronous-only rule.
- Pair `updatedInput` with `allow` to auto-approve or `ask` to show it to the user; omitted `permissionDecision` still applies the input via normal permission evaluation. Always return a new object; do not mutate `tool_input`.
