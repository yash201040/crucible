---
type: "Limit"
title: "Testing channels with --dangerously-load-development-channels"
description: "During the research preview custom channels bypass the allowlist only through a per-entry development flag that needs an interactive session."
resource: "https://code.claude.com/docs/en/channels-reference"
tags: [channels, allowlist, development-flag, non-interactive]
kind: "cli_flag"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: "Interactive session"
identifiers:
  - "--dangerously-load-development-channels"
  - "--channels"
  - "plugin:yourplugin@yourmarketplace"
  - "server:webhook"
  - "channelsEnabled"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "channels-reference"
    resource: "https://code.claude.com/docs/en/channels-reference"
    title: "Channels reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Every channel must be on the approved allowlist to register. The development flag bypasses the allowlist for specific entries after a confirmation prompt.

# How to use it

```bash
# a plugin you're developing
claude --dangerously-load-development-channels plugin:yourplugin@yourmarketplace
# a bare .mcp.json server
claude --dangerously-load-development-channels server:webhook
```

# Limits and defaults

- Run it in an interactive session. With `-p` (non-interactive) or through the Agent SDK, Claude Code ignores the flag and the channel does not register.
- The bypass is per entry: combining it with `--channels` does not extend the bypass to the `--channels` entries.
- It skips the allowlist only; the `channelsEnabled` organization policy still applies. Do not use it for untrusted channels.

# Notes

See [packaging as a plugin](./package-as-plugin.md) for the allowlist that applies once published.
