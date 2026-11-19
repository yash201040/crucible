---
type: "Guide"
title: "Package a channel as a plugin"
description: "Distribute a channel as a plugin enabled per session with --channels; allowlist rules for the official marketplace and org lists."
resource: "https://code.claude.com/docs/en/channels-reference"
tags: [channels, plugins, allowlist, marketplace]
kind: "cli_flag"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: "Team or Enterprise plan for allowedChannelPlugins"
identifiers:
  - "--channels plugin:<name>@<marketplace>"
  - "--dangerously-load-development-channels"
  - "allowedChannelPlugins"
  - "/plugin install"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "channels-reference"
    resource: "https://code.claude.com/docs/en/channels-reference"
    title: "Channels reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Wrap the channel in a plugin and publish it to a marketplace. Users install with `/plugin install`, then enable it per session with `--channels plugin:<name>@<marketplace>`.

# Limits and defaults

- A channel in your own marketplace still needs `--dangerously-load-development-channels` because it is not on the approved allowlist.
- The default allowlist is the channel plugins in `claude-plugins-official`; the community marketplace is not on it.
- For an official listing, coordinate with an Anthropic partner contact. On Team and Enterprise plans an admin can put the plugin in the organization's `allowedChannelPlugins` list, which replaces the default Anthropic allowlist.
