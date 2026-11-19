---
type: "Guide"
title: "Example: build a webhook receiver channel"
description: "Walkthrough of a one-file Bun channel that forwards HTTP POSTs on port 8788 into a session, with registration and troubleshooting."
resource: "https://code.claude.com/docs/en/channels-reference"
tags: [channels, webhook, example, mcp-json]
kind: "behavior"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - ".mcp.json"
  - "--dangerously-load-development-channels"
  - "server:webhook"
  - "~/.claude/debug/<session-id>.txt"
  - "/mcp"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "channels-reference"
    resource: "https://code.claude.com/docs/en/channels-reference"
    title: "Channels reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A single-file `webhook.ts` (Bun, `bun add @modelcontextprotocol/sdk zod`) creates an MCP `Server` with `capabilities: { experimental: { 'claude/channel': {} } }` and `instructions`, connects via `StdioServerTransport`, and runs `Bun.serve` on `127.0.0.1:8788` (localhost only). Each POST body is sent with `mcp.notification({ method: 'notifications/claude/channel', params: { content, meta } })`.

# How to use it

1. Register in `.mcp.json` (relative path) or `~/.claude.json` (absolute path): `{ "mcpServers": { "webhook": { "command": "bun", "args": ["./webhook.ts"] } } }`. Claude Code reads MCP config at startup and spawns each server.
2. Start: `claude --dangerously-load-development-channels server:webhook`. A full-screen warning appears (**I am using this for local development** or **Exit**); on first start in the project a consent dialog "New MCP server found in this project: webhook" appears (**Use this MCP server**). A dim notice confirms: `Channels (experimental) messages from server:webhook inject directly in this session · restart without --dangerously-load-development-channels to stop`.
3. Test: `curl -X POST localhost:8788 -d "build failed on main: https://ci.example.com/run/1234"`. Claude sees `<channel source="webhook" path="/" method="POST">...</channel>`; the terminal shows a one-line summary `← webhook: ...`.

# Notes

Troubleshooting: if curl succeeds but nothing arrives, run `/mcp` (status `failed` usually means a dependency or import error) or restart with `claude --debug --dangerously-load-development-channels server:webhook` and read `~/.claude/debug/<session-id>.txt`. If curl reports connection refused, a stale process may hold the port: `lsof -i :<port>` and `kill` it. The fakechat server extends this with a web UI, attachments and a reply tool.
