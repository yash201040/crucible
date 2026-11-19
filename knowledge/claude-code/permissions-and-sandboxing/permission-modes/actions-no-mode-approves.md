---
type: "Limit"
title: "Actions no mode auto-approves"
description: "Calls that still prompt or are denied in every permission mode, including bypassPermissions."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [permissions, bypass, ask-rules, safeguards]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.257"
surfaces: [cli]
requires: ""
identifiers:
  - "permissions.blockReadsOutsideWorkingDirectories"
  - "permissions.blockWritesOutsideWorkingDirectories"
  - "AskUserQuestion"
  - "requiresUserInteraction"
  - "EndConversation"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A fixed set of actions that Claude Code never auto-approves in any mode, `bypassPermissions` included (the dangerous-`rm` prompt can be switched off in `bypassPermissions`, see [critical-path prompt off](./critical-path-prompt-off.md)).

# How to use it

Never auto-approved:

- Tools matched by an explicit ask rule.
- Connector tools the organization set to `ask`, where that setting reaches Claude Code.
- Tools needing user interaction: built-in `AskUserQuestion` and MCP tools marked `requiresUserInteraction`.
- Recognized `rm` / `rmdir` critical-path removals (no allow rule or `PreToolUse` hook `"allow"` approves them) and Bash flagged `Dangerous rm operation not ruled out`.
- The cross-session messaging safeguards.
- Reads outside working directories while `permissions.blockReadsOutsideWorkingDirectories` is on: recognized file-reading Bash commands prompt even in auto and `bypassPermissions`, as does an unsandboxed retry needing approval. Needs v2.1.257 or later. Commands the shell parser cannot trace (multiple `cd`, subshell) prompt too; no prompt if the sandbox enforces the block.
- Writes outside working directories while `permissions.blockWritesOutsideWorkingDirectories` is on: `Write`, `Edit`, `NotebookEdit` are refused apart from some of Claude's own files. It does not limit shell commands, MCP tools or hook programs; use sandboxing for those. Needs v2.1.314 or later.
- PowerShell commands flagged `could not fully check your permission rules`: approve if trusted; if denied, ask Claude to reword.
