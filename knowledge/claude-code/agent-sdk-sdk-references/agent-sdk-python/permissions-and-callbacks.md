---
type: "Feature"
title: "Permission modes, can_use_tool and hooks"
description: "Python types for permission modes, the can_use_tool callback and results, permission updates, and the hook system with its input and output types."
resource: "https://code.claude.com/docs/en/agent-sdk/python"
tags: [permissions, hooks, can-use-tool, python, unattended]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "PermissionMode"
  - "default"
  - "acceptEdits"
  - "plan"
  - "dontAsk"
  - "bypassPermissions"
  - "auto"
  - "can_use_tool"
  - "CanUseTool"
  - "ToolPermissionContext"
  - "PermissionResultAllow"
  - "PermissionResultDeny"
  - "PermissionUpdate"
  - "PermissionRuleValue"
  - "updated_input"
  - "updated_permissions"
  - "interrupt"
  - "HookEvent"
  - "PreToolUse"
  - "PostToolUse"
  - "PostToolUseFailure"
  - "UserPromptSubmit"
  - "Stop"
  - "SubagentStop"
  - "PreCompact"
  - "Notification"
  - "SubagentStart"
  - "PermissionRequest"
  - "HookMatcher"
  - "HookCallback"
  - "HookContext"
  - "BaseHookInput"
  - "SyncHookJSONOutput"
  - "AsyncHookJSONOutput"
  - "continue_"
  - "async_"
  - "asyncTimeout"
  - "permissionDecision"
  - "permissionDecisionReason"
  - "updatedInput"
  - "additionalContext"
  - "updatedToolOutput"
  - "updatedMCPToolOutput"
  - "on_failure"
  - "dangerouslyDisableSandbox"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-python"
    resource: "https://code.claude.com/docs/en/agent-sdk/python"
    title: "Agent SDK reference - Python"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Python-side controls for tool authorization and event interception in unattended runs.

# How to use it

`PermissionMode` values: `"default"` (standard), `"acceptEdits"` (auto-accept file edits), `"plan"` (explore and plan), `"dontAsk"` (deny anything not pre-approved instead of prompting), `"bypassPermissions"` (skip checks; explicit ask rules still prompt), `"auto"` (a model classifier reviews actions such as shell commands and network requests).

`can_use_tool(tool_name, input_data, context) -> PermissionResultAllow | PermissionResultDeny`. It replaces the interactive prompt and runs only when the permission flow falls through to a prompt. It is NOT invoked for calls approved by `allowed_tools`, settings allow rules or the permission mode (so do not also list gated tools in `allowed_tools`); use a `PreToolUse` hook to see those. An allow rule does not pre-approve actions no mode auto-approves.
- `PermissionResultAllow(updated_input=None, updated_permissions=None)`; `PermissionResultDeny(message="", interrupt=False)`.
- `ToolPermissionContext`: `signal` (reserved), `suggestions`, `tool_use_id`, `agent_id` (set for subagent calls), `blocked_path`, `decision_reason`, `title`, `display_name`, `description`.
- `PermissionUpdate.type`: `addRules`, `replaceRules`, `removeRules`, `setMode`, `addDirectories`, `removeDirectories`; `destination`: `userSettings`, `projectSettings`, `localSettings`, `session`; `behavior`: `allow`, `deny`, `ask`. `PermissionRuleValue(tool_name, rule_content)`.

Hooks: `ClaudeAgentOptions(hooks={event: [HookMatcher(matcher=..., hooks=[callback], timeout=..., on_failure=...)]})`. Python `HookEvent` values: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `UserPromptSubmit`, `Stop`, `SubagentStop`, `PreCompact`, `Notification`, `SubagentStart`, `PermissionRequest`. The TypeScript SDK supports more events than Python.
- Callback signature `(input, tool_use_id, context: HookContext) -> HookJSONOutput`. Inputs share `session_id`, `transcript_path`, `cwd`, optional `permission_mode`; tool hooks add `tool_name`, `tool_input`, `tool_use_id`, and optional `agent_id` and `agent_type` inside subagents. `PostToolUse` adds `tool_response`; `PostToolUseFailure` adds `error`, `is_interrupt`; `UserPromptSubmit` adds `prompt`; `Stop` adds `stop_hook_active`; `SubagentStop` adds `stop_hook_active`, `agent_id`, `agent_transcript_path`, `agent_type`; `PreCompact` adds `trigger` (`manual` or `auto`) and `custom_instructions`; `Notification` adds `message`, `title`, `notification_type`; `SubagentStart` adds `agent_id`, `agent_type`; `PermissionRequest` adds `permission_suggestions`.
- Output `SyncHookJSONOutput`: `continue_` (sent as `continue`, default True), `suppressOutput` (no effect), `stopReason`, `decision` (`"block"`), `systemMessage`, `reason`, `hookSpecificOutput`. Specific outputs: `PreToolUse` has `permissionDecision` (`allow`, `deny`, `ask`, `defer`), `permissionDecisionReason`, `updatedInput`, `additionalContext`; `PostToolUse` has `additionalContext`, `updatedToolOutput` (all tools), `updatedMCPToolOutput` (MCP only, prefer the former); `PermissionRequest` has `decision`. `AsyncHookJSONOutput`: `async_` (True, sent as `async`) and `asyncTimeout` in ms.

# Limits and defaults

- `HookMatcher.timeout` is in seconds; default 600 for most events, 30 for `UserPromptSubmit`. `matcher` is a tool name or pattern such as `"Write|Edit"`; no matcher matches every tool. `on_failure="block"` blocks the action if a callback fails.
- More than 4,096 items in `updated_permissions` (each update, rule and directory counts) makes Claude Code deny the call with a message ending `updatedPermissions may hold at most 4096 updates, rules and directories in all.`
- `interrupt()` does not fire `PostToolUseFailure`.
- To route `dangerouslyDisableSandbox` requests through `can_use_tool` in `query()`, the prompt must be a stream and a dummy `PreToolUse` hook returning `{"continue_": True}` keeps the stream open.
