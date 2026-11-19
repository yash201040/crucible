---
type: "Feature"
title: "managedMcpServers setting"
description: "Provides remote HTTP/SSE MCP servers to every user through managed settings without exclusive control."
resource: "https://code.claude.com/docs/en/managed-mcp#provide-servers-through-managed-settings"
tags: [mcp, managed-settings, remote-servers, oauth]
kind: "setting"
maturity: "unlabelled"
since: "2.1.259"
surfaces: [cli]
requires: "Claude Code v2.1.259 or later; earlier clients ignore the key"
identifiers:
  - "managedMcpServers"
  - "managedSourcesBehavior"
  - "/mcp"
  - "claude mcp remove"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "managed-mcp"
    resource: "https://code.claude.com/docs/en/managed-mcp"
    title: "Control MCP server access for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`managedMcpServers` is an object keyed by server name; each entry has the shape of an HTTP or SSE server in `.mcp.json` (optional `headers`, `oauth`). Users keep their own servers and receive yours too.

# How to use it

```json
{ "managedMcpServers": { "search": {"type":"http","url":"https://search.example.com/mcp"} } }
```

Delivered via server-managed settings, a Claude apps gateway policy, MDM/registry, or `managed-settings.json`. An entry loads only if: `type` is `http` or `sse` (`streamable-http` alias for `http`); `url` is `https://` (plain http and localhost refused); no `command`, `args`, `env`, `headersHelper`; no `${VAR}` references; name uses only letters, numbers, hyphens, underscores, no control characters. A failing entry is dropped with a notice in `/status`; others load. Header values are readable by anyone with access to the settings.

# Limits and defaults

- Precedence: beats same-name local/project/user servers and plugin/connector servers with the same URL; with `managed-mcp.json`, the file's entry wins on a name clash. Survives `strictPluginOnlyCustomization` locking `mcp`. `deniedMcpServers` applies (a user can block one for themselves); no allowlist entry needed.
- Users cannot edit or remove (`claude mcp remove` says provided by the organization); can disable in `/mcp` (listed under **Managed MCPs**). `claude mcp get` and `/mcp` show URL host only and header names without values.
- Without `managed-mcp.json`: `--mcp-config` same-name server replaces the provided one for that run (checked against `allowedMcpServers`); `--strict-mcp-config` omits provided servers.
- Read from the selected managed source, or every admin source when `managedSourcesBehavior` is `"merge"` (higher-ranked wins per name). Never read from HKCU, parent settings, or user/project/local files. Not read in Claude Desktop's Code tab on a third-party deployment or Cowork sessions.
- Timing (server-managed): cached copy withheld until the server confirms; waits for it before loading MCP; on failure the session runs without them. First launch: interactive sessions connect on arrival; a `claude -p` run already started can finish without them. Gateway sign-in loads the policy before the session. Running interactive sessions apply adds and changes live; removal disconnects interactive sessions, while `-p` runs keep it until they end.
