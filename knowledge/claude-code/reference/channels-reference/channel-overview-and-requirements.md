---
type: "Concept"
title: "Channel contract overview and requirements"
description: "A channel is a local MCP server that pushes events into a session over stdio; what it must declare and emit."
resource: "https://code.claude.com/docs/en/channels-reference"
tags: [channels, mcp, stdio, research-preview]
kind: "mixed"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: "Node.js-compatible runtime (Bun, Node or Deno) and @modelcontextprotocol/sdk; Team and Enterprise orgs must enable channels"
identifiers:
  - "claude/channel"
  - "notifications/claude/channel"
  - "@modelcontextprotocol/sdk"
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

A channel is an MCP server that runs on the same machine as Claude Code, is spawned as a subprocess and talks over stdio. It pushes events (webhooks, alerts, chat messages) into a running session so Claude can react to things outside the terminal. One-way channels forward alerts; two-way channels (chat bridges) also expose a reply tool; a channel with a trusted sender path can also relay permission prompts. Included in the research preview: Telegram, Discord, iMessage and fakechat.

Typical shapes: chat platforms (the plugin polls the platform API, no URL exposed) and webhooks (the server listens on a local HTTP port).

# How to use it

The server must: (1) declare the `claude/channel` capability so Claude Code registers a listener, (2) emit `notifications/claude/channel` events, (3) connect over stdio transport. The only dependency is `@modelcontextprotocol/sdk`; the pre-built plugins use Bun but any of Bun, Node, Deno works.

# Limits and defaults

- Research preview; Team and Enterprise organizations must explicitly enable channels (the `channelsEnabled` policy). If you see "blocked by org policy", an admin must enable them.
- Custom channels are not on the approved allowlist; see [testing with the development flag](./test-with-development-flag.md).

# Notes

Next: [server options](./server-options.md), [notification format](./notification-format.md).
