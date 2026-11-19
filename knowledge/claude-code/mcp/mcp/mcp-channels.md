---
type: "Feature"
title: "Push messages with channels"
description: "An MCP server declaring claude/channel can push messages into a session when opted in with --channels."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, channels, events, push]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude/channel"
  - "--channels"
  - "MCP_PROTOCOL_NEGOTIATION"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A server can push CI results, alerts or chat messages into the session. The server declares the `claude/channel` capability and you opt it in with `--channels` at startup (see the Channels and Channels reference pages).

# Limits and defaults

On the v2 runtime, a channel server that negotiates protocol revision 2026-07-28 cannot deliver channel messages, so it is not registered as a channel; one that does not support that revision connects on the earlier handshake and registers normally. Stdio servers are asked for the newer revision by default; set `MCP_PROTOCOL_NEGOTIATION=legacy` to keep a stdio channel server (and every server) on the earlier handshake.
