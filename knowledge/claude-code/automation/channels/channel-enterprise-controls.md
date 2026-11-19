---
type: "Reference"
title: "Channel enterprise controls"
description: "Managed settings channelsEnabled and allowedChannelPlugins, defaults by authentication type, and what happens when blocked."
resource: "https://code.claude.com/docs/en/channels"
tags: [channels, managed-settings, enterprise, allowlist]
kind: "setting"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: "Owner role for the admin UI; Team/Enterprise or Console managed settings"
identifiers:
  - "channelsEnabled"
  - "allowedChannelPlugins"
  - "--dangerously-load-development-channels"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "channels"
    resource: "https://code.claude.com/docs/en/channels"
    title: "Push events into a running session with channels"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two managed settings users cannot override. Defaults: claude.ai Team and Enterprise block channels until an Owner enables them; Console with API key auth permits them by default (setting needed only if you deploy managed settings). Pro, Max and Ultra users without an organization skip these checks. In all cases no channel runs until a user opts it in with `--channels`.

# How to use it

| Setting | Purpose | When not configured |
| --- | --- | --- |
| `channelsEnabled` | Master switch; must be `true` for any channel to deliver. Blocks all channels including the development flag when off | Team/Enterprise: blocked. Console: allowed unless managed settings are deployed, then blocked until set |
| `allowedChannelPlugins` | Plugins that can register once enabled; replaces the Anthropic list when set | Anthropic default list |

Enable via Organization settings > Claude Code > Channels (Owner) or `channelsEnabled: true` in managed settings. Restrict plugins:

```json
{
  "channelsEnabled": true,
  "allowedChannelPlugins": [
    { "marketplace": "claude-plugins-official", "plugin": "telegram" },
    { "marketplace": "acme-corp-plugins", "plugin": "internal-alerts" }
  ]
}
```

# Limits and defaults

- If disabled or unset, the MCP server still connects and tools work but channel messages do not arrive; a startup warning tells the user to ask an admin.
- An empty `allowedChannelPlugins` array blocks all allowlisted channel plugins, but `--dangerously-load-development-channels` can still bypass it. To block everything including the dev flag, leave `channelsEnabled` unset.
- A plugin not on your list: Claude Code starts, the channel does not register, and the startup notice explains why. On the v2 MCP client runtime a channel can also fail to register if the server negotiates protocol revision 2026-07-28.
