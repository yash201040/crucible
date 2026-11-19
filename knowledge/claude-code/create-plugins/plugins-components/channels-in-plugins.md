---
type: "Feature"
title: "Channels in a plugin"
description: "A plugin channel is an MCP server plus a channels manifest entry that binds to it and can prompt for its own userConfig."
resource: "https://code.claude.com/docs/en/plugins/components"
tags: [plugins, channels, mcp, userconfig]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "channels"
  - "channels[].server"
  - "channels[].userConfig"
  - "${user_config.<key>}"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-components"
    resource: "https://code.claude.com/docs/en/plugins/components"
    title: "Add components to a plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A channel lets an outside system such as a chat app send messages into a session. In a plugin, a channel is one of the plugin's MCP servers plus a `channels` entry that binds to it.

# How to use it

In `plugin.json`, add the server under `mcpServers` (for example `telegram`, with `env: { "BOT_TOKEN": "${user_config.bot_token}" }`) and a `channels` array entry `{ "server": "telegram", "userConfig": { "bot_token": { "type": "string", "title": "Bot token", "description": "...", "sensitive": true } } }`. `server` must match a key in `mcpServers`. The per-channel `userConfig` has the same shape as the top-level `userConfig`.

# Notes

What the server must implement and how users enable a channel plugin is in the channels reference (Package as a plugin).
