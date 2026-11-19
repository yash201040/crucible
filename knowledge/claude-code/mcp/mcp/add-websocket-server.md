---
type: "Feature"
title: "Add a remote WebSocket server"
description: "WebSocket MCP servers keep a persistent connection; configured only via JSON, header-only auth, no OAuth."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, websocket, transport, headers]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "ws"
  - "claude mcp add-json"
  - "headersHelper"
  - "timeout"
  - "alwaysLoad"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

WebSocket servers hold a persistent bidirectional connection, suiting remote servers that push events unprompted. Use HTTP if the server only answers requests, since HTTP supports OAuth and `claude mcp add --transport`; WebSocket supports neither.

# How to use it

```
claude mcp add-json events-server '{"type":"ws","url":"wss://mcp.example.com/socket","headers":{"Authorization":"Bearer YOUR_TOKEN"}}'
```

`type: "ws"` accepts the same `url`, `headers`, `headersHelper`, `timeout` and `alwaysLoad` fields as `http`. Authentication is header-only (static token or `headersHelper`). `claude mcp add --transport` does not accept `ws`.

# Limits and defaults

A WebSocket message over 16 MiB closes the connection. A WebSocket server's first connection is not retried automatically; select Reconnect in `/mcp`.
