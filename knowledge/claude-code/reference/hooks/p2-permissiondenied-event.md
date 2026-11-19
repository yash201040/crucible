---
type: "Feature"
title: "PermissionDenied hook event"
description: "Fires when auto mode denies a tool call; a hook can set retry to tell the model it may try again."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, permissiondenied, auto-mode, retry]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: "auto mode"
identifiers:
  - "PermissionDenied"
  - "retry"
  - "reason"
  - "Classifier unavailable"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs when auto mode denies a tool call, including a denial with no classifier verdict (a separate safety check refused the classifier's request, or its response did not parse). Fires only in auto mode: not for a manual dialog denial, a PreToolUse block, or a `deny` rule. Matches tool name like PreToolUse. Use it to log denials, adjust config or let the model retry.

# How to use it

Input adds `tool_name`, `tool_input`, `tool_use_id`, `reason`, and `mcp_server` for MCP tools. `reason` text forms: the matched policy in brackets, such as `[Destructive or Unwanted Actions]` or `[Irreversible Local Destruction]`; text starting `Auto mode could not evaluate this action and is blocking it for safety` (no verdict); or `Classifier unavailable` (classifier model unavailable, or a server check failed or timed out).

Return `{"hookSpecificOutput": {"hookEventName": "PermissionDenied", "retry": true}}` to add a message telling the model it may retry.

# Limits and defaults

- Claude Code does not reverse the denial itself; without JSON or with `retry: false` the denial stands.
- `retry: true` is ignored when the classifier produced no verdict; Claude Code already tells the model in the rejection message whether to retry later or move on.
- Supports all five hook types, but prompt and agent hook output is discarded here (they cannot set `retry`).
