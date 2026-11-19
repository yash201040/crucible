---
type: "Feature"
title: "Plugin channels"
description: "channels declares message channels (e.g. a chat bridge) each bound to one of the plugin's MCP servers, with optional userConfig prompts."
resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
tags: [plugins, channels, mcp, userconfig]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "channels"
  - "server"
  - "displayName"
  - "userConfig"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-manifest-reference"
    resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
    title: "Plugin manifest reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`channels` declares the message channels a plugin provides, such as a bridge to a chat app; Claude Code can prompt for the channel's configuration when the plugin is enabled. Each entry is a strict object bound to one of the plugin's MCP servers. How the server injects messages is in the channels reference.

# How to use it

| Field | Required | Description |
| :- | :- | :- |
| `server` | Yes | Key of the MCP server in this plugin's `mcpServers` that the channel binds to |
| `displayName` | No | Name in the configuration dialog title; defaults to the server name |
| `userConfig` | No | Options to prompt for, same shape as top-level `userConfig`; saved values substitute into `${user_config.KEY}` references in the server's `env` |

Example: an `mcpServers.telegram` with `"env": { "BOT_TOKEN": "${user_config.bot_token}" }` and `"channels": [ { "server": "telegram", "displayName": "Telegram", "userConfig": { "bot_token": { "type": "string", "title": "Bot token", "description": "Telegram bot token", "sensitive": true } } } ]`.
