---
type: "Reference"
title: "Hook timing and persisted environment variables"
description: "Variables that tune SessionEnd and Stop hook limits, persist exports between Bash commands and silence Notification hooks for SDK-hosted permission prompts."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [hooks, session-end, stop-hook, env-file]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS"
  - "CLAUDE_CODE_STOP_HOOK_BLOCK_CAP"
  - "CLAUDE_ENV_FILE"
  - "CLAUDE_CODE_DISABLE_PERMISSION_PROMPT_NOTIFY_HOOKS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Hook-related limits and environment persistence.

# How to use it

| Variable | What it does |
| :- | :- |
| `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` | Time budget for SessionEnd hooks, also the timeout for each hook with no `timeout`. Applies to exit, `/clear` and switching via interactive `/resume`. Default 1.5 s, automatically raised to the highest per-hook `timeout` in settings files, up to 60 s; plugin hook timeouts do not raise it. |
| `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` | Max consecutive times a Stop or SubagentStop hook may block the turn from ending before Claude Code ends it anyway (default 8). `0` disables the cap. |
| `CLAUDE_ENV_FILE` | Path to a shell script run before each Bash command in the same shell process, so exports are visible (for example persist virtualenv or conda activation). PowerShell commands receive its variables from v2.1.296 under stated conditions. Also populated by SessionStart, Setup, CwdChanged and FileChanged hooks. |
| `CLAUDE_CODE_DISABLE_PERMISSION_PROMPT_NOTIFY_HOOKS` | `1` stops running `Notification` hooks for unanswered permission requests in sessions that send them to the Agent SDK `canUseTool` callback (how Claude Desktop and the VS Code extension host Claude Code). No effect in terminal sessions. Requires v2.1.233+. |
