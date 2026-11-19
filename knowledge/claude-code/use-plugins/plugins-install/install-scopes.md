---
type: "Reference"
title: "Plugin install scopes"
description: "User, project and local scopes, which settings file each writes, precedence, defaultEnabled, and shared settings across surfaces."
resource: "https://code.claude.com/docs/en/plugins/install"
tags: [plugins, scope, settings, enabledplugins]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "enabledPlugins"
  - "~/.claude/settings.json"
  - ".claude/settings.json"
  - ".claude/settings.local.json"
  - "--scope project"
  - "--scope local"
  - "defaultEnabled"
  - "claude plugin enable"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-install"
    resource: "https://code.claude.com/docs/en/plugins/install"
    title: "Install and manage plugins"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A plugin's install scope decides who gets it and which settings file records it in `enabledPlugins`.

# How to use it

| Scope | Prompt label | Settings file | Effect |
| :- | :- | :- | :- |
| User | Install for you | `~/.claude/settings.json` | Every project on this machine |
| Project | Install for all collaborators on this repository | `.claude/settings.json` (committed) | Enabled for everyone in the repo |
| Local | Install for you, in this repo only | `.claude/settings.local.json` | This repository only, just you |

Committing a project entry enables the plugin for collaborators but does not download it: each runs `claude plugin install <name>@<marketplace> --scope project` once per clone.

# Limits and defaults

- Precedence when set at several scopes: local overrides project overrides user.
- A plugin whose author sets `defaultEnabled` to off is installed but stays off until `claude plugin enable <name>` or the **Installed** tab.
- The terminal, the desktop app's local sessions and the VS Code extension on one computer read the same settings files, so a user-scope install in one is available in the others.
