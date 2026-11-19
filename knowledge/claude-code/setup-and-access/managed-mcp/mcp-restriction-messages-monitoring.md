---
type: "Reference"
title: "MCP restriction messages and monitoring"
description: "What users see when MCP policy blocks something, the configuration summary table, and OTEL logging of MCP usage."
resource: "https://code.claude.com/docs/en/managed-mcp#how-restrictions-appear-to-users"
tags: [mcp, errors, monitoring, otel]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "OTEL_LOG_TOOL_DETAILS"
  - "not allowed by enterprise policy"
  - "server is explicitly blocked by enterprise policy"
  - "MCP server <name> is blocked by enterprise managed policy"
  - "Your organization now manages MCP servers on this computer"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "managed-mcp"
    resource: "https://code.claude.com/docs/en/managed-mcp"
    title: "Control MCP server access for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

User-visible outcomes of MCP policy, plus a summary of delivery for each surface.

# How to use it

| Situation | User sees |
| :- | :- |
| `claude mcp add` on a denylisted server | `Cannot add MCP server "<name>": server is explicitly blocked by enterprise policy` |
| `claude mcp add` on a non-allowlisted server | `Cannot add MCP server "<name>": not allowed by enterprise policy` |
| `strictPluginOnlyCustomization` true or includes `mcp` | `Cannot add MCP server: your organization's managed settings allow only MCP servers that plugins provide` |
| `claude mcp remove` on a `managedMcpServers` server | `MCP server "<name>" is provided by your organization (managed settings) and cannot be removed locally.` |
| `managed-mcp.json` appears mid-session | notice beginning `Your organization now manages MCP servers on this computer` |
| Server newly blocked | disappears from `/mcp` and `claude mcp list` silently |
| Reconnect of a blocked server | `MCP server <name> is blocked by enterprise managed policy` |
| `claude --chrome` under managed-mcp.json | exits naming `allowClaudeInChromeWithManagedMcp` |

Monitoring: with OpenTelemetry export, set `OTEL_LOG_TOOL_DETAILS=1` to include MCP server and tool names in tool events and cost/token counters.

# Limits and defaults

- Delivery summary: `managed-mcp.json` only via system path (MDM/GPO/fleet), never server-managed; `managedMcpServers`, `allowedMcpServers`, `deniedMcpServers`, `allowManagedMcpServersOnly`, `allowAllClaudeAiMcps` via managed sources; `allowClaudeInChromeWithManagedMcp` device sources only.
- Desktop-delivered connectors in local/SSH sessions are governed by claude.ai organization settings, not these controls.
