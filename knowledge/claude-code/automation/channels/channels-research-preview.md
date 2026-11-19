---
type: "Limit"
title: "Channels research-preview limits"
description: "Preview status: flag syntax may change, flags hidden from --help, allowlist-only plugins, and the development flag."
resource: "https://code.claude.com/docs/en/channels"
tags: [channels, research-preview, flags]
kind: "cli_flag"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "--channels"
  - "--dangerously-load-development-channels"
  - "plugin:<name>@<marketplace>"
  - "server:<name>"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "channels"
    resource: "https://code.claude.com/docs/en/channels"
    title: "Push events into a running session with channels"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Channels are a research preview: availability rolls out gradually, and the `--channels` flag syntax and protocol contract may change. Neither `--channels` nor `--dangerously-load-development-channels` appears in `claude --help` during preview; they work anyway.

# How to use it

- `--channels` accepts only plugins on an Anthropic-maintained allowlist (the plugins in claude-plugins-official are the default set) or the organization's `allowedChannelPlugins`. Anything else: Claude Code starts, the channel does not register, and the startup notice says why.
- To test a channel you are building, pass `--dangerously-load-development-channels` in `plugin:<name>@<marketplace>` or `server:<name>` form.
- Build your own with the Channels reference; a webhook receiver is its worked example.
