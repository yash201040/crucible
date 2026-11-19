---
type: "Feature"
title: "Bypass permissions mode"
description: "bypassPermissions auto-approves tool calls except a short list that still reach hooks, rules or the callback."
resource: "https://code.claude.com/docs/en/agent-sdk/permissions"
tags: [permission-modes, bypasspermissions, root, safety]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "bypassPermissions"
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

Auto-approves tool uses without prompting, except the actions no mode auto-approves. Hooks still run and can block. Docs warn: use with extreme caution, in controlled environments only.

# How to use it

Still enforced in this mode:
- Deny rules, explicit `ask` rules and hooks (evaluated before the mode check).
- Falling through to `canUseTool`: org-`ask` connector tools, tools requiring user interaction, recognized critical-path removals, Bash commands flagged `Dangerous rm operation not ruled out`; outside a cloud session also custom tools marked `always_ask`. The critical-path removal prompt can be turned off (see permission-modes docs).
- Cross-session messaging safeguards still apply.

# Limits and defaults

- `allowed_tools` does not constrain this mode; unlisted tools are approved too.
- On Linux and macOS, Claude Code refuses to start in this mode as root or under `sudo` outside a recognized sandbox; the query fails before the first turn.
- The recognizing check for critical paths can miss some commands.
