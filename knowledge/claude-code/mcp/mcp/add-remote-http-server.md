---
type: "Feature"
title: "Add a remote HTTP server"
description: "HTTP is the recommended transport for remote MCP servers; syntax, headers, the streamable-http alias and rejected entries."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, http, transport, headers]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "claude mcp add --transport http"
  - "--header"
  - "-H"
  - "-t"
  - "streamable-http"
  - "type"
  - "url"
  - "headers"
  - "type: sdk"
  - "mcp_server_errors"
  - "--mcp-config"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

HTTP servers are the recommended option for remote MCP servers and the most widely supported transport for cloud services.

# How to use it

```
claude mcp add --transport http <name> <url>
claude mcp add --transport http secure-api https://api.example.com/mcp --header "Authorization: Bearer your-token"
```

`--transport` and `--header` also accept `-t` and `-H`. In JSON config (`.mcp.json`, `~/.claude.json`, `claude mcp add-json`) the `type` field accepts `streamable-http` as an alias for `http`.

# Limits and defaults

- A JSON entry with `url` but no `type` is read as stdio and skipped, reporting `MCP server "<name>" has a "url" but no "type"; add "type": "http" (or "sse" / "ws") to this entry`.
- `"type": "sdk"` (in-process) can only be registered by an SDK host application (Agent SDK app or desktop app). In `.mcp.json`, `~/.claude.json` or settings it is skipped with a `Skipped` message.
- In `--output-format stream-json` runs, a skipped `--mcp-config` entry is reported in the `system/init` event's `mcp_server_errors` field, so scripts can detect that a server never loaded.
