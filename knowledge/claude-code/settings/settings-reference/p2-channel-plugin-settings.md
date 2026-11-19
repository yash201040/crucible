---
type: "Reference"
title: "Channel plugin settings"
description: "Managed settings that allow channels and restrict which plugins may push messages into sessions."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, channels, plugins, managed]
kind: "setting"
maturity: "unlabelled"
since: "2.1.267"
surfaces: [cli]
requires: "Managed settings; Team or Enterprise plan needs channelsEnabled true"
identifiers:
  - "allowedChannelPlugins"
  - "channelsEnabled"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two managed-scope keys governing channels (plugins that push messages into sessions).

# How to use it

| Name | Type | Default | What it does |
| :- | :- | :- | :- |
| `channelsEnabled` | Boolean | unset | Allows channels for the org. Unset: blocked on Team and Enterprise plans and on Console accounts with managed settings; allowed on Pro, Max, Ultra and on Console accounts without managed settings. `false` is same as unset |
| `allowedChannelPlugins` | array of `{marketplace, plugin}` objects or `"plugin@marketplace"` strings | unset (Anthropic default allowlist) | Replaces the default allowlist. String form needs v2.1.267+ (earlier versions reject the whole value). Empty array blocks every channel plugin. Takes effect once `channelsEnabled` passes the gate |

Example: `{ "channelsEnabled": true, "allowedChannelPlugins": [ { "marketplace": "claude-plugins-official", "plugin": "telegram" } ] }`.
