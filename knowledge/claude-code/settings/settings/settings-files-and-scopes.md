---
type: "Reference"
title: "Settings files and scopes"
description: "The four settings scopes (user, shared project, project local, managed) with file paths, who each affects, and the separate ~/.claude.json."
resource: "https://code.claude.com/docs/en/settings"
tags: [settings, scopes, files, managed-settings]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide, desktop]
requires: ""
identifiers:
  - "~/.claude/settings.json"
  - ".claude/settings.json"
  - ".claude/settings.local.json"
  - "managed-settings.json"
  - "~/.claude.json"
  - "CLAUDE_CONFIG_DIR"
  - "/config"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings"
    resource: "https://code.claude.com/docs/en/settings"
    title: "Settings files and precedence"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code reads settings from JSON files; the file decides who a setting applies to. The terminal, VS Code, JetBrains and the desktop app all read the same files. Installing creates none of them.

# How to use it

| Scope | File | Who it affects | Use for |
| :- | :- | :- | :- |
| User | `~/.claude/settings.json` | you, every project on the machine | theme, editor mode, default model, own permission rules |
| Shared project | `.claude/settings.json` | everyone in the folder (commit it) | team permissions, hooks, plugins, project env vars |
| Project local | `.claude/settings.local.json` | you, this project only | personal overrides, testing before sharing |
| Managed | `managed-settings.json` and other managed sources (MDM, server-managed from claude.ai console, embedding host via SDK `managedSettings`) | everyone the org deploys to | security policy, compliance |

- Claude Code creates `~/.claude/settings.json` the first time a `/config` option stored there changes, and `.claude/settings.local.json` the first time you give a standing approval ("Yes, and don't ask again"). A few `/config` options (e.g. Show tips) save to the local file.
- On Windows `~` is `%USERPROFILE%`. `CLAUDE_CONFIG_DIR` relocates settings, session history and plugins.
- `~/.claude.json` is a fifth file Claude Code writes for itself: account details, MCP server configs, per-project state such as trust decisions, and the global config keys `/config` writes. Do not need to edit it.
- Commit `.claude/settings.json` to share settings; teammates override in their own local file. Some committed content waits for folder trust, and a few keys never take effect from a repository file.
- Run `/status`: the `Setting sources` line names the managed source in force. In a Cowork session on desktop, server-managed settings from the console are not fetched, and device policy is read unless the org's Desktop config sets `requireCoworkFullVmSandbox`.

# Notes

See [precedence](./settings-precedence.md), [local file handling](./settings-local-file.md), [cloud sessions](./settings-in-cloud-sessions.md).
