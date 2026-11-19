---
type: "Concept"
title: "Which mode a session starts in"
description: "Order of precedence and built-in default for a new session's permission mode, with version gates."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [permissions, defaults, startup, settings, versions]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.283"
surfaces: [cli, ide, headless, sdk]
requires: ""
identifiers:
  - "permissions.defaultMode"
  - "disableAutoMode"
  - "--permission-mode"
  - "--dangerously-skip-permissions"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

How a new terminal session picks its permission mode.

# How to use it

Order, first that applies wins: 1) `--permission-mode` or `--dangerously-skip-permissions`; 2) `permissions.defaultMode` in a settings file; 3) the built-in default.

Settings-file caveats: `"auto"` in `.claude/settings.json` or `.claude/settings.local.json` does not take effect, and Claude Code then uses the built-in default rather than a `defaultMode` from `~/.claude/settings.json`. `"bypassPermissions"` in those two files does not take effect either; the session starts Manual. Other values apply from any settings file. Move `auto` to `~/.claude/settings.json`.

Built-in default, first matching row:

| Run | Mode |
| :- | :- |
| Any settings file has `disableAutoMode` = `"disable"` | `default` |
| `claude -p` or Agent SDK | `default` |
| HIPAA configuration applied and session eligible | `default` on v2.1.285 through v2.1.325; other versions follow next row |
| Terminal or VS Code | `auto` with v2.1.283+; earlier: `auto` on Pro, Max, Ultra, Team in sessions that fetch feature flags, else `default` |

# Limits and defaults

- Built-in `auto` default needs v2.1.228+ on macOS/Linux/WSL, v2.1.233+ on native Windows; earlier the default is Manual.
- If the flag, a settings file or the default selects `auto` but auto mode is unavailable (settings turned it off, unsupported model, or server-side off), the session starts Manual.
- A notice linking to the page shows the first time the default starts a session in auto (once at top of terminal session; a dismissible card in VS Code).
- If `~/.claude/settings.json` sets a `defaultMode` other than `auto` and no other file sets one, sessions keep that mode. On Pro, Max, Ultra, Team and in sessions that do not fetch feature flags, Claude Code asks once whether to switch the setting to auto.
- Resumed sessions: see the sessions docs "permission mode on resume".
