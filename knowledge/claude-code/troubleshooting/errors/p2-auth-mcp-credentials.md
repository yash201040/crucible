---
type: "Reference"
title: "MCP server authentication errors"
description: "Errors when an MCP server or claude.ai connector rejects credentials, keychain reads fail, or OAuth checks (issuer, redirects, HTTPS) refuse."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, mcp, oauth, headershelper, keychain]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk, desktop]
requires: ""
identifiers:
  - "headersHelper"
  - "oauth.scopes"
  - "authServerMetadataUrl"
  - "MCP_SDK_GENERATION"
  - "claude mcp login"
  - "claude mcp list"
  - "claude mcp get"
  - "/mcp"
  - "/mcp reconnect"
  - "reconnectMcpServer()"
  - "ClaudeSDKClient.reconnect_mcp_server()"
  - "claude doctor"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors tied to MCP servers: expired or rejected sign-ins, unreadable credential stores, and OAuth safety checks.

# How to use it

| Message | Meaning and fix |
|---|---|
| `claude.ai rejected the session token. Run /login, then reconnect.` | claude.ai connector fails because your Claude Code login was rejected (`/mcp` shows `session token rejected`). `/login` first, then `/mcp reconnect <server>`. |
| `MCP server "<name>" needs you to sign in again (run /mcp to re-authenticate)` | Server rejected credential mid-session; `/mcp` marks it as needing authentication. |
| `... rejected the credential from its headersHelper` | Helper re-run and call retried once already. Fix the helper output, reconnect. |
| `... rejected the Authorization header in its config` | Static header wrong; update then reconnect. In Cowork (no `/mcp`), start a new task or chat instead. |
| `... needs additional permissions (scope: "<scope>")` | Server sent 403 `insufficient_scope`. Requests the named scope unless `oauth.scopes` or `authServerMetadataUrl` is set; with a pinned `oauth.scopes`, add the scope yourself. |
| `Couldn't read the stored credentials for MCP server "<name>"` | Credential store unreadable (e.g. locked macOS keychain). In `claude -p` or SDK runs on macOS a request may go out without credentials: `A request to MCP server "<name>" was sent without your stored credentials...`. Retry; SDK apps call `reconnectMcpServer()` (TypeScript) or `ClaudeSDKClient.reconnect_mcp_server()` (Python). Check `claude doctor` for `macOS Keychain is not writable`. Before v2.1.307 this showed as needing authentication. |
| `This server's URL is missing or not a valid URL` | `claude mcp login <name>` refuses a bad `url`; fix it or the `${VAR}` it references. |
| `Issuer mismatch in authorization response (RFC 9207)` | `iss` differs from metadata issuer (mix-up attack protection). Server-side fix; `MCP_SDK_GENERATION=v1` bypasses the check but removes protection. v2 runtime default only in gradual rollout before v2.1.232. |
| `Stopped an OAuth request` | An OAuth endpoint redirected it elsewhere or more than 5 times. |
| `Refusing to send credentials to non-https token endpoint` | v2 runtime sends token requests only over HTTPS or localhost/127.0.0.1/::1. Serve over TLS, or use `MCP_SDK_GENERATION=v1` (applies to every server until exit). |
| `MCP server "<name>" connection timed out. Your computer went to sleep or its clock changed while connecting.` | Clock jumped forward during connect. Reconnect; shell runs of `claude -p`, `claude mcp list`, `claude mcp get` may show `Skipping connection (recent failure cached`; wait 15 minutes. |

# Notes

Before v2.1.273 several of these showed `MCP server "<name>" requires re-authorization (token expired)`.
