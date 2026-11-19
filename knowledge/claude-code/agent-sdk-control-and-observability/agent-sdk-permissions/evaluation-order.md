---
type: "Concept"
title: "Six-step permission evaluation order"
description: "How the SDK decides a tool call: hooks, deny rules, ask rules, permission mode, allow rules, then the canUseTool callback."
resource: "https://code.claude.com/docs/en/agent-sdk/permissions"
tags: [permissions, evaluation, hooks, canusetool]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "canUseTool"
  - "disallowed_tools"
  - "allowed_tools"
  - "PreToolUse"
  - "PermissionRequest"
  - "permissionPrompts"
  - "_meta[\"anthropic/requiresUserInteraction\"]"
  - "permission_policy"
  - "always_ask"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-permissions"
    resource: "https://code.claude.com/docs/en/agent-sdk/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Every tool request passes through six steps in a fixed order. Each step can decide the call, send it to the `canUseTool` callback, or pass it on.

# How to use it

| Step | What happens |
| :- | :- |
| 1. Hooks | Hooks run. A hook can deny outright or pass on. A hook `allow` does not skip deny-rule and ask-rule steps. A `PreToolUse` `allow` cannot approve an `rm`/`rmdir` on a recognized critical path (such as `rm -rf ~`). |
| 2. Deny rules | A match in `disallowed_tools` or a loaded settings file denies the call; `canUseTool` is not called. Applies even in `bypassPermissions` and after a hook `allow`. |
| 3. Ask rules | `ask` rules from settings.json send the call to `canUseTool`, even in `bypassPermissions`. |
| 4. Permission mode | Active mode applies (bypass approves, acceptEdits approves file ops, plan routes some calls to callback or classifier, default/dontAsk pass on, auto uses the classifier). |
| 5. Allow rules | Rules from `allowed_tools` and settings.json approve. Calls a tool approves on its own (file reads in working directories, read-only Bash) resolve here. |
| 6. `canUseTool` | Called when nothing earlier resolved the call. In `dontAsk` mode this step is skipped and the call is denied. |

Calls that fall through to the callback even when an allow rule matches (denied instead in `dontAsk`):
- `AskUserQuestion`
- MCP tools whose server sets `_meta["anthropic/requiresUserInteraction"]` (needs Claude Code v2.1.199 or later)
- claude.ai connector tools the organization set to `ask`; the callback gets the reason `Your organization requires approval for this tool`, even in `bypassPermissions`
- TypeScript SDK custom tools with `permission_policy` `always_ask`: no allow rule (not even `allowedTools`) approves them; in `auto`, `plan` or `bypassPermissions` mode Claude Code can approve them before the callback

# Limits and defaults

- Allow rules do not approve reads from network paths, nor recognized critical-path removals; commands flagged `Dangerous rm operation not ruled out` are not approved by a `Bash` or `Bash(*)` rule. In an SDK session in `auto` mode, these are denied by default without calling the callback.
- TypeScript SDK `permissionPrompts: 'none'`: the callback is not called at step 6; a `PermissionRequest` hook can still decide, otherwise the call is denied. Needs Claude Code v2.1.259 or later.

# Notes

To check calls that rules or modes auto-approve, put the check in a `PreToolUse` hook. A plugin's mod decisions are covered on the main permissions page.
