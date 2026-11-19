---
type: "Feature"
title: "canUseTool callback for approvals"
description: "A canUseTool callback pauses execution when a tool needs approval or Claude asks a question, and can stay pending indefinitely."
resource: "https://code.claude.com/docs/en/agent-sdk/user-input"
tags: [agent-sdk, permissions, approvals, callback]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "canUseTool"
  - "can_use_tool"
  - "CanUseTool"
  - "PermissionRequest"
  - "PreToolUse"
  - "defer"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-user-input"
    resource: "https://code.claude.com/docs/en/agent-sdk/user-input"
    title: "Handle approvals and user input"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude requests user input in two situations: it needs permission to use a tool, or it has clarifying questions via the `AskUserQuestion` tool. Both trigger the `canUseTool` callback, which pauses execution until it returns. This differs from normal turns where Claude finishes and waits for the next message.

# How to use it

Pass `canUseTool` (TypeScript option, type `CanUseTool`) or `can_use_tool=` (Python `ClaudeAgentOptions`). It fires when (1) a tool is not auto-approved by a permission rule or permission mode, with the tool name such as `"Bash"` or `"Write"`; (2) Claude calls `AskUserQuestion`. If you set a `tools` array, include `AskUserQuestion` for questions to work.

The callback may stay pending indefinitely. If a user may take longer than your process can stay running, register a `PreToolUse` hook that returns the `defer` decision, so the process can exit and resume later from the persisted session. The `PermissionRequest` hook can send external notifications (Slack, email, push) while Claude waits.

# Limits and defaults

- An earlier step can allow or deny a call before `canUseTool` runs: the permission evaluation flow checks deny rules, the permission mode, then allow rules first. To run checks on calls a rule or mode already allowed, use a `PreToolUse` hook, which can allow, deny or modify them.
- In some configurations, such as `dontAsk` mode, Claude Code does not call the callback; the last step of "How permissions are evaluated" says what happens instead.
- Python quirk shown in the examples: a dummy `PreToolUse` hook (`{"continue_": True}`) is a "required workaround" that keeps the stream open for `can_use_tool`, and the prompt must be an async generator.
