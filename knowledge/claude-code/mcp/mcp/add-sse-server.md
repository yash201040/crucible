---
type: "Feature"
title: "Add a remote SSE server (deprecated)"
description: "SSE transport is deprecated; HTTP-first fallback to SSE from v2.1.265, or --transport sse directly."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, sse, transport, deprecated]
kind: "cli_flag"
maturity: "deprecated"
since: "2.1.265"
surfaces: [cli]
requires: ""
identifiers:
  - "claude mcp add --transport sse"
  - "sse"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The SSE (Server-Sent Events) transport is deprecated; use HTTP where available. Some services still expose only SSE.

# How to use it

- Add with the same command as HTTP: `claude mcp add --transport http <name> <url>`. Claude Code tries HTTP first and switches to SSE when the server does not accept it. The automatic switch needs Claude Code v2.1.265 or later.
- On earlier versions, or to force SSE: `claude mcp add --transport sse <name> <url>`, optionally with `--header "X-API-Key: your-key-here"`.
