---
type: "Reference"
title: "MCP server status and reconnection"
description: "Init-message status values for MCP servers, how pending differs from failure, and reconnect calls."
resource: "https://code.claude.com/docs/en/agent-sdk/mcp"
tags: [mcp, status, reconnect, init-message]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "pending"
  - "connected"
  - "failed"
  - "needs-auth"
  - "disabled"
  - "mcp_servers"
  - "reconnectMcpServer()"
  - "reconnect_mcp_server()"
  - "get_mcp_status()"
  - "error_during_execution"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-mcp"
    resource: "https://code.claude.com/docs/en/agent-sdk/mcp"
    title: "Connect to external tools with MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The `system` init message (subtype `init`) carries each MCP server's `status` in `mcp_servers`: `"pending"`, `"connected"`, `"failed"`, `"needs-auth"` or `"disabled"`. MCP connection failures do not throw.

# How to use it

- Do not treat `pending` as failure: it can mean not yet connected, tool list served from cache (connects on first use), or an expired deadline (reports `pending` or `failed` by timing).
- Detect unusable servers by filtering for `failed` or `needs-auth`.
- Later status: `mcpServerStatus()` (TypeScript) or `ClaudeSDKClient.get_mcp_status()` (Python). A connected remote server that drops goes back to `pending` while reconnecting.
- After five reconnection attempts fail the server reports `failed` (or `needs-auth` if it must be re-authorized). A failed HTTP/SSE server can still return to `connected` through background retries.
- Manual retry: `reconnectMcpServer()` (TypeScript) or `ClaudeSDKClient.reconnect_mcp_server()` (Python).

# Notes

Claude can fall back to built-in tools when an MCP server is unavailable, so check status before trusting a result. Causes of `failed`: missing env vars, server not installed (npx package or Node.js not in PATH), invalid connection string, network issues. If tools are visible but not called, add `allowedTools`.
