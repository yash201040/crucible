---
type: "Reference"
title: "MCP allowlists and denylists"
description: "allowedMcpServers and deniedMcpServers entry types, URL/command/name matching, evaluation order and the managed-only lock."
resource: "https://code.claude.com/docs/en/managed-mcp#policy-based-control-with-allowlists-and-denylists"
tags: [mcp, allowlist, denylist, policy]
kind: "setting"
maturity: "unlabelled"
since: "2.1.273"
surfaces: [cli]
requires: "v2.1.273+ for reading the lock and allowlist across sources; v2.1.219+ for pinned environment expansion"
identifiers:
  - "allowedMcpServers"
  - "deniedMcpServers"
  - "allowManagedMcpServersOnly"
  - "allowManagedPermissionRulesOnly"
  - "serverUrl"
  - "serverCommand"
  - "serverName"
  - "disableClaudeAiConnectors"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "managed-mcp"
    resource: "https://code.claude.com/docs/en/managed-mcp"
    title: "Control MCP server access for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Lists filter which configured servers may load; they are not a registry. Each entry is an object with one key.

# How to use it

| Key | Matches |
| :- | :- |
| `serverUrl` | remote URL, exact or `*` wildcards (HTTP/SSE) |
| `serverCommand` | exact command+args array for stdio, e.g. `["npx","-y","server"]`; `env` not compared |
| `serverName` | exact user label, no wildcards; not a security control |

- `allowedMcpServers`: unset = all allowed; `[]` = none (except servers that skip the check); populated = only matches.
- `deniedMcpServers`: unset or `[]` blocks nothing. In the denylist `serverName` accepts any non-empty string (e.g. `{ "serverName": "claude.ai Slack" }`); in the allowlist it is limited to letters, numbers, hyphens, underscores.
- URL matching: host case-insensitive, trailing dot ignored, paths case-sensitive. No port: written-out host = default port only (443/80); host containing `*` = every port. `https://mcp.example.com:*/*` = any port; `https://*.example.com/*` = any subdomain, any port; `*://host/*` = any scheme on default port.
- To make the allowlist authoritative set `allowedMcpServers` plus `allowManagedMcpServersOnly: true` in a managed source (separate from `allowManagedPermissionRulesOnly`). Allowlists otherwise merge from every scope; denylists always merge.

# Limits and defaults

Evaluation order: (1) merge lists, (2) denylist match blocks, nothing overrides, (3) allowlist. Remote servers need a `serverUrl` match (a `serverName` counts only if no `serverUrl` entries exist); stdio need `serverCommand` (name counts only if no command entries). Skipped from the allowlist check: `managedMcpServers`, `managed-mcp.json` entries without `${VAR}` outside `env`, built-in servers (Claude in Chrome, `ide`), Claude Tag Slack tools; in-process `type: "sdk"` skip all checks. `${VAR}` and `${VAR:-default}` expand in `serverUrl`/`serverCommand` on both sides; policy entries expand from a pinned environment (allowlist entries whose expansion changes scheme/host/path are ignored). Both lists also filter `--mcp-config` servers.
