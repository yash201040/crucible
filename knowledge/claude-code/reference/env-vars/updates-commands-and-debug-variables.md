---
type: "Reference"
title: "Updates, installation, hidden commands and debug logging variables"
description: "Variables that block auto-updates, hide slash commands such as /login and /doctor, silence installation checks and enable debug logging."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [updates, commands, debug, administration]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "DISABLE_AUTOUPDATER"
  - "DISABLE_UPDATES"
  - "DISABLE_INSTALLATION_CHECKS"
  - "CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE"
  - "DISABLE_DOCTOR_COMMAND"
  - "DISABLE_EXTRA_USAGE_COMMAND"
  - "DISABLE_INSTALL_GITHUB_APP_COMMAND"
  - "DISABLE_LOGIN_COMMAND"
  - "DISABLE_LOGOUT_COMMAND"
  - "DISABLE_UPGRADE_COMMAND"
  - "DEBUG"
  - "CLAUDE_CODE_DEBUG_LOGS_DIR"
  - "CLAUDE_CODE_DEBUG_LOG_LEVEL"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Administration variables for managed deployments and troubleshooting.

# How to use it

| Variable | What it does |
| :- | :- |
| `DISABLE_AUTOUPDATER` | `1` disables automatic background updates; manual `claude update` still works. |
| `DISABLE_UPDATES` | `1` blocks all updates including `claude update` and `claude install`; stricter than `DISABLE_AUTOUPDATER`. |
| `DISABLE_INSTALLATION_CHECKS` | `1` disables installation warnings (use only when managing the install location yourself). |
| `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE` | `1` lets Claude Code run the package manager upgrade command in the background (Homebrew and WinGet only; other managers show the command). |
| `DISABLE_DOCTOR_COMMAND` | `1` hides the `/doctor` checkup skill and its `/checkup` alias; does not affect `claude doctor`. Before v2.1.205 it hid the `/doctor` diagnostics screen command. |
| `DISABLE_EXTRA_USAGE_COMMAND` | `1` hides `/usage-credits` (purchase extra usage beyond rate limits). |
| `DISABLE_INSTALL_GITHUB_APP_COMMAND` | `1` hides `/install-github-app` (already hidden on Bedrock, Google Cloud's Agent Platform, Foundry). |
| `DISABLE_LOGIN_COMMAND` | `1` hides `/login` (auth handled externally via API keys or `apiKeyHelper`). |
| `DISABLE_LOGOUT_COMMAND` | `1` hides `/logout`. |
| `DISABLE_UPGRADE_COMMAND` | `1` hides `/upgrade`. |
| `DEBUG` | `1` enables debug mode like `--debug`; logs to `~/.claude/debug/<session-id>.txt` or `CLAUDE_CODE_DEBUG_LOGS_DIR`. Only `1`, `true`, `yes`, `on` count, so namespaces like `DEBUG=express:*` do not trigger it. |
| `CLAUDE_CODE_DEBUG_LOGS_DIR` | Overrides the debug log file path (a file path despite the name; default `~/.claude/debug/<session-id>.txt`). Debug mode must be enabled separately via `--debug`, `/debug` or `DEBUG`; `--debug-file` does both. |
| `CLAUDE_CODE_DEBUG_LOG_LEVEL` | Minimum level written: `verbose`, `debug` (default), `info`, `warn`, `error`. `verbose` adds high-volume diagnostics such as full status line command output. |
