---
type: "Feature"
title: "OAuth callback port and pre-configured credentials"
description: "Fix the OAuth callback port and supply a client ID and secret for servers without dynamic client registration."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, oauth, credentials, ci]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.231"
surfaces: [cli]
requires: ""
identifiers:
  - "--callback-port"
  - "--client-id"
  - "--client-secret"
  - "MCP_CLIENT_SECRET"
  - "oauth.clientId"
  - "oauth.callbackPort"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

By default Claude Code uses a random free port for the OAuth callback. Servers that need a pre-registered redirect URI `http://localhost:PORT/callback` need `--callback-port`. Servers without Dynamic Client Registration (error `Incompatible auth server: does not support dynamic client registration`) need a registered OAuth app; Client ID Metadata Document (CIMD) servers are discovered automatically.

# How to use it

```
claude mcp add --transport http --callback-port 8080 my-server https://mcp.example.com/mcp
claude mcp add --transport http --client-id your-client-id --client-secret --callback-port 8080 my-server https://mcp.example.com/mcp
claude mcp add-json my-server '{"type":"http","url":"https://mcp.example.com/mcp","oauth":{"clientId":"your-client-id","callbackPort":8080}}' --client-secret
MCP_CLIENT_SECRET=your-secret claude mcp add --transport http --client-id your-client-id --client-secret --callback-port 8080 my-server https://mcp.example.com/mcp
```

`--client-secret` prompts with masked input; `MCP_CLIENT_SECRET` skips the prompt (CI). `oauth.callbackPort` alone fixes the port with automatic registration. Then run `/mcp` to authenticate.

# Limits and defaults

- The secret is stored in the macOS keychain or a credentials file, not config; it can be set only at add time (later `login` or `/mcp` uses the stored one and ignores `MCP_CLIENT_SECRET`). To change it, remove the server and re-add with the same `--scope`.
- Public clients: use only `--client-id`.
- Applies only to HTTP and SSE, not stdio. `claude mcp get <name>` confirms credentials.
- v2.1.229 sent `http://127.0.0.1:PORT/callback`, causing redirect URI mismatch on exact-match servers; v2.1.231 restored `localhost`.
