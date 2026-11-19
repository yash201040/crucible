---
type: "Feature"
title: "Authenticate with remote MCP servers (OAuth)"
description: "OAuth 2.0 sign-in via /mcp or claude mcp login, when a server is flagged needs-auth, refresh behavior and headless limits."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, oauth, authentication, headless]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk, cloud]
requires: ""
identifiers:
  - "claude mcp login <name>"
  - "claude mcp logout <name>"
  - "--no-browser"
  - "Re-authenticate"
  - "Clear authentication"
  - "WWW-Authenticate"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code supports OAuth 2.0. A remote server is marked as needing authentication when it answers `401 Unauthorized` or `403 Forbidden`. Tokens are stored securely and refreshed automatically.

# How to use it

- Interactive: run `/mcp`, select the server, choose Authenticate; or `claude mcp login <name>` from the shell. Clear with `claude mcp logout <name>` or "Clear authentication" in `/mcp`. If the browser does not open, copy the URL; if the redirect fails after sign-in, paste the full callback URL into the prompt.
- `claude mcp login` detects no local browser (SSH, Linux without display), prints the URL and asks you to paste the redirect URL; it needs an interactive terminal (`ssh -t`). `--no-browser` forces that URL prompt.
- `claude -p` and Agent SDK runs have no `/mcp` panel and cannot run OAuth: sign in first from an interactive session or `claude mcp login <name>`. With tool search on, Claude is told the server's tools are unavailable until authorized.
- On macOS, a `claude -p` or SDK request sent while the stored token could not be read fails with a stored-credentials error.
- OAuth works with HTTP servers.

# Limits and defaults

- Not flagged as needs-auth: a claude.ai connector whose `401` is claude.ai rejecting your session token (shows `session token rejected` state); a server whose `Authorization` header you configured in `headers` or via `headersHelper` (reported as failed, no OAuth fallback); connectors delivered to a cloud session (re-authorize at claude.ai/customize/connectors).
- A `401` for a stored token: with a refresh token, it refreshes, reconnects and retries once; flagged only if that retry fails. Without a refresh token it connects once without the token; if that works tools work signed-out and the rejected token is deleted.
- A rejected refresh token triggers an immediate notice pointing at `/mcp` (select Re-authenticate).
- A startup notice lists servers needing sign-in, once per server; before v2.1.218 it also counted claude.ai connectors that were not connected in claude.ai.
- A custom server returning `WWW-Authenticate` pointing to its authorization server gets automatic discovery.
