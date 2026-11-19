---
type: "Feature"
title: "PermissionRequest hook event"
description: "Fires when Claude Code is about to ask for permission; hook can allow or deny on the user's behalf."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, permissionrequest, permissions, unattended]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "PermissionRequest"
  - "permission_suggestions"
  - "behavior"
  - "updatedInput"
  - "updatedPermissions"
  - "message"
  - "interrupt"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs when Claude Code is about to ask you for permission to use a tool, or when it would otherwise auto-deny a call that cannot prompt. In sessions that cannot show a prompt (background subagents in non-interactive mode) the hooks still run, and if none returns a decision the call is denied. For a call reaching `--permission-prompt-tool` or the SDK `canUseTool` callback, hooks run alongside the host and whichever decides first applies. Matches on tool name like PreToolUse. Does not fire for `EndConversation` or for a sandboxed command's network request (use the `permission_prompt` notification instead). PreToolUse runs before every call; this runs only when a prompt would appear. A Notification `permission_prompt` hook fires only after the prompt waited about six seconds, so use this event for an immediate signal.

# How to use it

Input: `tool_name`, `tool_input` (no `tool_use_id`), `mcp_server` for MCP tools, optional `permission_suggestions` (array of [permission update entries](./p2-permission-update-entries.md)). The array is not an exact list of dialog options: some dialogs (file edits) ignore it, some withhold options (e.g. `allowManagedPermissionRulesOnly` hides rule-saving), and some options (like "Yes, and switch to auto mode") have no entry.

Return `hookSpecificOutput.decision`:

| Field | Description |
| :- | :- |
| `behavior` | `"allow"` or `"deny"`; cannot approve what a deny rule refuses, unless a mod overrides the rule |
| `updatedInput` | allow only; replaces whole input; re-evaluated against deny and ask rules; required (with allow) for `AskUserQuestion`/`ExitPlanMode` |
| `updatedPermissions` | allow only; array of permission update entries |
| `message` | deny only; tells Claude why |
| `interrupt` | deny only; `true` stops Claude |

# Limits and defaults

- Exit 2 without a `decision` object leaves the permission flow unchanged and stderr is discarded.
- Supports `command`, `http`, `mcp_tool` and `prompt` hooks, not `agent` hooks (an agent hook here is skipped). A prompt hook's `ok: false` has no effect here.
