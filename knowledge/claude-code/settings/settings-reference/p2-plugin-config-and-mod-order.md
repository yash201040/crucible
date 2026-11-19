---
type: "Reference"
title: "pluginConfigs and mod ordering keys"
description: "Stored plugin option answers plus the managed lists that run organization mods before or after users' mods."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, plugins, mods, ordering]
kind: "setting"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [cli]
requires: ""
identifiers:
  - "pluginConfigs"
  - "prependPlugins"
  - "appendPlugins"
  - "sec-default@builtin"
  - "cc-plugin-agents-md@builtin"
  - "~/.claude/.credentials.json"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Three plugin keys.

# How to use it

| Name | Scope | Type | What it does |
| :- | :- | :- | :- |
| `pluginConfigs` | user or managed | object plugin ID to `{ options, mcpServers? }` | Stores non-sensitive answers to a plugin's `userConfig` dialog, written for you. Sensitive options go to macOS Keychain (fallback `~/.claude/.credentials.json`) or that file where no keychain exists. Project and local entries ignored, because values are substituted into plugin hook, MCP and LSP config. Built-in plugins use an `@builtin` ID suffix; Project instructions (`AGENTS.md` reading) is `pluginConfigs["cc-plugin-agents-md@builtin"].options.instructionFiles` (before v2.1.285 the ID was `agents-md@builtin`; both read) |
| `prependPlugins` | user or managed | array of `plugin@marketplace` | Managed plugins whose mods run before every user-installed mod, in order. Name `sec-default@builtin` to keep the built-in guard. Read from managed settings; from user settings only on a machine with no managed settings or `managed-mcp.json` and a non-Team/Enterprise `/login`; ignored in project, local, `--settings` |
| `appendPlugins` | same | same | Mods run after user mods; an id in both lists is prepended |

# Notes

In managed settings an id is skipped if its plugin does not count as the organization's.
