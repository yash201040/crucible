---
type: "Reference"
title: "Critical-path removals per mode and timeouts"
description: "Outcome of a critical-path removal in each mode and surface, the two-minute countdown, and CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [critical-paths, timeout, headless, permissions, unattended]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.281"
surfaces: [cli, headless, sdk, ide, desktop]
requires: ""
identifiers:
  - "CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT"
  - "PermissionRequest"
  - "--permission-prompts none"
  - "claudeCode.environmentVariables"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

What happens to a recognized critical-path removal per mode:

| Mode | Outcome |
| :- | :- |
| `default`, `acceptEdits` | Asks you |
| `plan` | Asks you; when the classifier reviews planning commands and no bypass is available, handled as in `auto` |
| `auto` | Asks in the terminal, with a time limit; elsewhere denies |
| `dontAsk` | Denies |
| `bypassPermissions` | In the terminal asks, before a time limit; elsewhere see below |

An explicit ask rule match asks you even in `auto`, with no time limit. In modes that ask, a `PermissionRequest` hook can answer the prompt.

# How to use it

In `auto` and `bypassPermissions` the terminal prompt shows a two-minute countdown. If it runs out, the command is denied and Claude is told what to do instead, so an unattended session keeps working. Any key stops the countdown. After three unanswered prompts in a session, further critical-path removals are denied immediately; a new message resets the count. The time limit and the `auto` denial outside the terminal apply from v2.1.281.

Away from the terminal:

| Where | `auto` | `bypassPermissions` |
| :- | :- | :- |
| VS Code chat panel | Denies | Denies unless a `PermissionRequest` hook allows |
| Desktop app | Denies | Denies unless a `PermissionRequest` hook allows |
| `-p` or Agent SDK | Denies | `--permission-prompt-tool` or `canUseTool` decides; with neither, or under `--permission-prompts none`, denies unless a `PermissionRequest` hook allows |

Set `CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT=1` in the launching environment (shell or SDK `env` option, not a Claude Code settings file): `bypassPermissions` then has no time limit and VS Code asks; `auto` lets the classifier decide in the terminal, VS Code chat panel, `-p` and SDK. For the chat panel add `{ "name": "CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT", "value": "1" }` to `claudeCode.environmentVariables` in VS Code user settings and start a new conversation.
