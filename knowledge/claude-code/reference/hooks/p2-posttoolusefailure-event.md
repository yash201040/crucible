---
type: "Feature"
title: "PostToolUseFailure hook event"
description: "Fires when a started tool fails; gives error and is_interrupt and can add context for Claude."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, posttoolusefailure, errors, tool-calls]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "PostToolUseFailure"
  - "error"
  - "is_interrupt"
  - "duration_ms"
  - "tool_use_error"
  - "additionalContext"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs when a tool that started executing fails: it threw, or an MCP tool returned an error result. Matches tool name like PreToolUse. Does not fire for calls rejected before execution (unknown tool, schema or validation failure returned as `tool_use_error`, or permission denial; denials fire PreToolUse, see PermissionDenied).

# How to use it

Input: `tool_name`, `tool_input`, `tool_use_id`, `mcp_server` for MCP tools, plus `error`, optional `is_interrupt`, optional `duration_ms`.

- `error`: string, generally the text Claude gets as the tool result; format varies. Key on `tool_name`, `is_interrupt` and the first line `Exit code N` (Bash and PowerShell, followed by interleaved output); treat the rest as display text. A bare failure message with no exit line appears if the shell could not start. Long strings are middle-truncated around `... [N characters truncated] ...`; lines like `Command timed out after 2m 0s` may be inserted.
- `is_interrupt`: true when the failure reached Claude Code as an abort. Cancelling a running tool does not fire this hook.

Output: `hookSpecificOutput.additionalContext` added alongside the error.
