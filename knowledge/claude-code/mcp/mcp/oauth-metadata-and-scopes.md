---
type: "Feature"
title: "OAuth metadata override and scope pinning"
description: "authServerMetadataUrl bypasses OAuth discovery; oauth.scopes pins requested scopes and handles insufficient_scope."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, oauth, scopes, discovery]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "oauth.authServerMetadataUrl"
  - "oauth.scopes"
  - "offline_access"
  - "insufficient_scope"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Fields in a server's `oauth` object in `.mcp.json`.

# How to use it

- `authServerMetadataUrl`: bypass default discovery (RFC 9728 `/.well-known/oauth-protected-resource`, then RFC 8414 `/.well-known/oauth-authorization-server`). Must be `https://`; its `scopes_supported` overrides what the upstream advertises.
- `scopes`: a single space-separated string (RFC 6749 section 3.3), for example `"channels:read chat:write search:read"`. It is the supported way to restrict a server to an approved subset, and takes precedence over `authServerMetadataUrl` and `.well-known` scopes.

# Limits and defaults

- Without `oauth.scopes`, Claude Code does not request the full `scopes_supported` of auto-discovered metadata; metadata from a configured `authServerMetadataUrl` still supplies its list.
- If the server advertises `offline_access`, it is appended to pinned scopes so tokens refresh without a new sign-in.
- A later 403 `insufficient_scope` fails the call with a `needs additional permissions` message naming the scope and shows needs-auth; add the scope to `oauth.scopes`, then re-authenticate in `/mcp` (the pinned scopes, not the named one, are requested).
