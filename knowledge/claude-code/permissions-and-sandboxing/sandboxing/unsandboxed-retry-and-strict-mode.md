---
type: "Feature"
title: "Unsandboxed retry and strict sandbox mode"
description: "How Claude can retry a failed command outside the sandbox with dangerouslyDisableSandbox, who approves it per permission mode, and how to turn it off."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, escape-hatch, strict-mode, permissions]
kind: "setting"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [cli]
requires: ""
identifiers:
  - "dangerouslyDisableSandbox"
  - "sandbox.allowUnsandboxedCommands"
  - "sandbox.failIfUnavailable"
  - "Bash(dangerouslyDisableSandbox:true)"
  - "permissions.blockReadsOutsideWorkingDirectories"
  - "CLAUDE_CODE_SUBPROCESS_ENV_SCRUB"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When a command fails in the sandbox, Claude may retry it with the `dangerouslyDisableSandbox` parameter, which runs it unsandboxed. When the sandbox blocks a network connection, Claude Code names the denied host in the result.

# How to use it

Who approves the retry in an interactive session:

| Permission mode | Result |
| - | - |
| `bypassPermissions` | Runs without a prompt |
| Manual, `acceptEdits` | Prompt titled "Bash command (unsandboxed)" |
| Auto mode | A separate classifier evaluates the underlying command |
| `dontAsk` | Denied |
| Plan mode | See permission-modes docs |

Modifiers: a matching allow rule such as `Bash(curl *)` also approves the retry; an ask rule `Bash(dangerouslyDisableSandbox:true)` prompts on retries (also in auto and `bypassPermissions`, and beats an allow rule); `permissions.blockReadsOutsideWorkingDirectories` adds prompts.

Strict sandbox mode: set `"allowUnsandboxedCommands": false` in sandbox settings. Claude Code then ignores `dangerouslyDisableSandbox` and commands are sandboxed unless they match `excludedCommands`. Add `failIfUnavailable` so commands do not run unsandboxed when the sandbox cannot start. The Overrides tab calls this Strict sandbox mode.

# Limits and defaults

- A `false` in user settings, `--settings` or managed settings holds even when project settings say `true` (before v2.1.285 a project `true` overrode a user `false`).
- Disabling the retry in managed settings or with `--settings` makes the sandbox admin-required (see [admin-required sandbox](./admin-required-sandbox-and-locks.md)).
- Strict mode covers commands Claude runs. Commands typed at the `!` prompt run outside the sandbox unless the session is a background session, or a Linux session with `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` set. Before v2.1.260 strict mode sandboxed shell-mode commands in every session.
- While commands are refused with `Sandbox is required`, the parameter is ignored and the retry refused.
