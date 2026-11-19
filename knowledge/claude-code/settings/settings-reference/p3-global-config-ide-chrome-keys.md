---
type: "Reference"
title: "Global config keys: IDE and Chrome"
description: "Keys in ~/.claude.json that control IDE auto-connect, IDE extension install, the diff viewer and Chrome integration by default."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [global-config, ide, chrome, claude-json]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide]
requires: ""
identifiers:
  - "~/.claude.json"
  - "autoConnectIde"
  - "autoInstallIdeExtension"
  - "claudeInChromeDefaultEnabled"
  - "diffTool"
  - "CLAUDE_CODE_AUTO_CONNECT_IDE"
  - "CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL"
  - "--chrome"
  - "--no-chrome"
  - "--ide"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Global config settings live in `~/.claude.json`, not in a settings file. Claude Code ignores these keys anywhere else, including `settings.json`. Claude Code and `/config` write most of them; you can also edit by hand. Scope for all of them is `Global config`.

# How to use it

| Name | Type | Default | What it does |
| - | - | - | - |
| `autoConnectIde` | boolean | `false` | When `true`, connects to a running IDE automatically when started from an external terminal. When `false`, inside a VS Code or JetBrains terminal or with `--ide` it still connects. `/config` label: Auto-connect to IDE (external terminal). Overridden per session, either direction, by `CLAUDE_CODE_AUTO_CONNECT_IDE`. |
| `autoInstallIdeExtension` | boolean | `true` | When `true`, `/ide` installs the extension in a running VS Code, Cursor or Devin Desktop when run from an external terminal. Claude Code no longer installs or updates it at `claude` startup; before v2.1.318 it did, unless this key was `false`. `CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL=1` skips install for one session. `/config` label: Auto-install IDE extension (inside a VS Code or JetBrains terminal). |
| `claudeInChromeDefaultEnabled` | boolean | unset (Chrome off, setup still offered) | `true` starts every interactive CLI session with Chrome integration on, as `--chrome` does; `false` starts with it off and stops offering setup. `--chrome` and `--no-chrome` override it for one interactive session. Also followed by sessions started by `claude remote-control` for project threads (except `bypassPermissions` mode) and, on v2.1.287 or later, by VS Code extension sessions (when `false`, a session connects on `@browser`). Set by `/chrome` or the "Claude in Chrome extension detected" dialog. `/config` label: Claude in Chrome enabled by default. |
| `diffTool` | string: `"auto"` or `"terminal"` | `"auto"` | Where the diff of a proposed `Edit` or `Write` appears when a VS Code or JetBrains IDE is connected: `"auto"` uses the IDE diff viewer, `"terminal"` keeps it in the terminal. `/config` label: Diff tool (only while connected to an IDE). |

Example: `{ "autoConnectIde": true }` in `~/.claude.json`.
