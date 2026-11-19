---
type: "Feature"
title: "MCP authentication in the SDK"
description: "Pass credentials through env or headers; the SDK runs no interactive OAuth flow and reports needs-auth or failed instead."
resource: "https://code.claude.com/docs/en/agent-sdk/mcp"
tags: [mcp, authentication, oauth, headers]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.307"
surfaces: [sdk]
requires: ""
identifiers:
  - "env"
  - "headers"
  - "${API_KEY}"
  - "needs-auth"
  - "failed"
  - "mcpServerStatus()"
  - "get_mcp_status()"
  - "McpServerStatus"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-mcp"
    resource: "https://code.claude.com/docs/en/agent-sdk/mcp"
    title: "Connect to external tools with MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Credentials go into server config: the `env` field for stdio servers, `headers` (e.g. `Authorization: Bearer ...`) for HTTP/SSE. In `.mcp.json`, `${API_KEY}` syntax expands environment variables at runtime.

# How to use it

- OAuth 2.1: the SDK does not open a browser or run an interactive flow. Without a usable token the server reports:
  - `needs-auth`: no sign-in Claude Code can use. Pass a token in `headers`, or sign in from an interactive Claude Code session on the same machine before the run.
  - `failed` with an `error` starting `Couldn't read the stored credentials` or `A request to MCP server`: credential store unreadable. Before v2.1.307 a locked Mac login keychain gave `needs-auth` instead.
- Either way the run continues without that server's tools. The init `mcp_servers` may still show `pending`. Poll `mcpServerStatus()` (TypeScript) or `get_mcp_status()` (Python) to confirm.
- To supply credentials, complete OAuth in your own app and pass the access token in `headers`.

# Notes

Example: the remote GitHub MCP server at `https://api.githubcopilot.com/mcp/` with `Authorization: Bearer ${GITHUB_TOKEN}`. Example: DBHub for Postgres; `readonly = true` in `dbhub.toml` makes `execute_sql` reject writes (otherwise it runs whatever SQL the agent emits).
