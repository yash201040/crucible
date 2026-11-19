---
type: "Reference"
title: "SDK permission modes and setting them"
description: "The six SDK permission modes, default mode from v2.1.302, changing mode mid-session, and subagent inheritance."
resource: "https://code.claude.com/docs/en/agent-sdk/permissions"
tags: [permission-modes, subagents, set-permission-mode, defaults]
kind: "setting"
maturity: "unlabelled"
since: "2.1.302"
surfaces: [sdk]
requires: ""
identifiers:
  - "permission_mode"
  - "permissionMode"
  - "set_permission_mode()"
  - "setPermissionMode()"
  - "default"
  - "dontAsk"
  - "acceptEdits"
  - "bypassPermissions"
  - "plan"
  - "auto"
  - "permissions.defaultMode"
  - "AgentDefinition"
  - "allowDangerouslySkipPermissions"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-permissions"
    resource: "https://code.claude.com/docs/en/agent-sdk/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Permission modes give global control over tool use. Set at `query()` time with `permission_mode` (Python) / `permissionMode` (TypeScript), or change mid-session with `set_permission_mode()` / `setPermissionMode()`; the new mode applies immediately to later requests.

# How to use it

| Mode | Tool behavior |
| :- | :- |
| `default` | No mode-based auto-approval; calls needing approval with no allow rule go to `canUseTool`. |
| `dontAsk` | Any call that would prompt is denied without calling `canUseTool`. |
| `acceptEdits` | File edits and filesystem ops (`mkdir`, `rm`, `mv`, etc.) in working directories auto-approved. |
| `bypassPermissions` | No prompts, except actions no mode auto-approves and (outside a cloud session) custom tools marked `always_ask`. |
| `plan` | Claude explores and plans; file-tool edits go to `canUseTool` even if an allow rule matches. |
| `auto` | A model classifier reviews actions such as shell commands and network requests. |

Streaming example: `await q.setPermissionMode("acceptEdits")` (TypeScript) or `await client.set_permission_mode("acceptEdits")` (Python).

# Limits and defaults

- With Claude Code v2.1.302 or later, an app starts in `default` mode unless a mode is set or `permissions.defaultMode` is in its settings files. In `default`, any call needing approval is denied unless approved via allow rule, hook, `canUseTool` or a permission prompt tool.
- Subagent inheritance: in a `plan` main session, a subagent whose `AgentDefinition` sets `permissionMode: "acceptEdits"` still runs in plan mode. The subagent inherits `plan`, `acceptEdits`, `auto` or `bypassPermissions` from the main session; under a `default` or `dontAsk` main session it runs in the mode you set. Claude Code never applies a `"bypassPermissions"` value on a subagent (v2.1.267 or later), and applies `"auto"` only when auto mode is available to it. An inherited `bypassPermissions` gives subagents full autonomous access.
- TypeScript: switching a plan-started session to `bypassPermissions` later needs `allowDangerouslySkipPermissions` set from the start.

# Notes

Details per mode: [accept edits](./accept-edits-mode.md), [dont ask](./dont-ask-mode.md), [bypass](./bypass-permissions-mode.md), [plan](./plan-mode.md), [auto](./auto-mode.md).
