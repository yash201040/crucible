---
type: "Reference"
title: "Turn mods on or off and see which are loaded"
description: "Mods are on by default; ways to stop one, all installed mods for a session, or all in every session, plus the loaded-mods line in /plugin."
resource: "https://code.claude.com/docs/en/plugins/mods/overview"
tags: [mods, safe-mode, settings, disable]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.287"
surfaces: [cli, desktop]
requires: "Claude Code v2.1.287 or later (Desktop v2.1.286)"
identifiers:
  - "--safe-mode"
  - "disableAllHooks"
  - "allowManagedModsOnly"
  - "CLAUDE_CODE_ENABLE_FUNCTION_HOOKS"
  - "--bare"
  - "claude --version"
  - "/plugin"
  - "/status"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-overview"
    resource: "https://code.claude.com/docs/en/plugins/mods/overview"
    title: "Mods overview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Mods are on by default. Check version: terminal `claude --version` (v2.1.287+); Desktop Code tab `/status`, **Claude Code** row (mods work from 2.1.286).

# How to use it

| Scope | How |
| :- | :- |
| One mod | disable or uninstall its plugin on the **Installed** tab of `/plugin` |
| All installed mods, one session | start with `--safe-mode` (also disables other customizations) |
| All installed mods, every session | `"disableAllHooks": true` in `~/.claude/settings.json` (settings hooks and custom status line stop too; what the organization manages keeps running) |
| Organization | administrators limit which mods load via managed settings |

`disableAllHooks` and the organization's `allowManagedModsOnly` stop a mod but leave the rest of its plugin (skills, commands, agents, MCP servers) loaded and installed.

Run `/plugin` to see a dim line such as `1 mod active · first-mod`; built-in mods are omitted from it.

# Notes

`CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` from early access should be removed: v2.1.287 and later ignore it, so setting it to `0` does not keep mods off. `--safe-mode`, `--bare` and `disableAllHooks` do not stop built-in mods.
