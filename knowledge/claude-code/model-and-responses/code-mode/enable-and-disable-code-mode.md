---
type: "Guide"
title: "Turn Code Mode on, off, or block it"
description: "Enable with CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1, resume only with it on, and block it organization-wide with managed settings."
resource: "https://code.claude.com/docs/en/code-mode"
tags: [code-mode, env-var, managed-settings, resume]
kind: "env_var"
maturity: "experimental"
since: "2.1.323"
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_EXPERIMENTAL_CODE_MODE"
  - "claude --continue"
  - "claude --resume"
  - "--permission-mode auto"
  - "/status"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-mode"
    resource: "https://code.claude.com/docs/en/code-mode"
    title: "Run tool calls from code with Code Mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Code Mode is controlled by the environment variable `CLAUDE_CODE_EXPERIMENTAL_CODE_MODE`.

# How to use it

- Try it: `CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1 claude` (PowerShell: `$env:CLAUDE_CODE_EXPERIMENTAL_CODE_MODE = "1"` then `claude`). For every session, put `{ "env": { "CLAUDE_CODE_EXPERIMENTAL_CODE_MODE": "1" } }` in `~/.claude/settings.json`. Claude Code ignores this variable in a project's settings files, so a cloned repo cannot turn it on.
- First time, a confirmation asks "Yes, turn on Code Mode"; Claude Code restarts and shows `Code Mode (experimental) is on · this session can be resumed only with Code Mode on`. If the line reads `Code Mode (experimental) isn't available`, the reason is on the same line and in `/status`.
- Resume: keep the variable `1` for `claude --continue` or `claude --resume`; with it off Claude Code refuses to resume a Code Mode session. Sessions started without Code Mode resume without it even if the variable is set.
- Turn off: remove the variable from shell and `~/.claude/settings.json`, or set `0`. A `0` in one place wins over `1` in the other.
- Block for an organization: put `"CLAUDE_CODE_EXPERIMENTAL_CODE_MODE": "0"` in the `env` block of managed settings. Users already in a session stay until exit or restart, then start without Code Mode and cannot resume Code Mode sessions while the `0` is in place. Managed settings cannot turn Code Mode on for users.
