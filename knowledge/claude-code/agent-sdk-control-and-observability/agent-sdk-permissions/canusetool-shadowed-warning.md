---
type: "Concept"
title: "canUseTool shadowed warning"
description: "TypeScript SDK emits a process warning when a configuration makes auto-approval run before the canUseTool callback."
resource: "https://code.claude.com/docs/en/agent-sdk/permissions"
tags: [permissions, warning, canusetool, typescript]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: "TypeScript SDK"
identifiers:
  - "CLAUDE_SDK_CAN_USE_TOOL_SHADOWED"
  - "permissionMode: 'bypassPermissions'"
  - "allowedTools"
  - "process.on('warning', ...)"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-permissions"
    resource: "https://code.claude.com/docs/en/agent-sdk/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When you pass a `canUseTool` callback in a configuration where calls are auto-approved before the callback is consulted, the TypeScript SDK emits a Node.js process warning once, when the query is constructed. The warning code is `CLAUDE_SDK_CAN_USE_TOOL_SHADOWED`.

# How to use it

Two triggers:
- `permissionMode: 'bypassPermissions'`: text starts with `canUseTool will not be invoked: permissionMode 'bypassPermissions'`. Move checks into a `PreToolUse` hook to see approved calls too.
- An `allowedTools` entry that is only a bare tool name such as `"Read"`: the warning lists each after `canUseTool will not be invoked for:`. Remove the entry so the callback runs for calls needing approval.

Entries with a specifier such as `Bash(ls *)`, the `acceptEdits` mode, and allow rules from settings files do not trigger it (settings rules are invisible to the check).

Log it with `process.on('warning', ...)` and match the code.

# Notes

The warning blocks nothing and changes no option.
