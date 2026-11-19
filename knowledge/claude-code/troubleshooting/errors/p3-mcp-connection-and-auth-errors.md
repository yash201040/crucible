---
type: "Reference"
title: "MCP connection, OAuth and permission-prompt errors"
description: "MCP runtime errors: Anthropic-hosted connectors, headersHelper 401/403, Java SDK elicitation, --permission-prompt-tool, OAuth port, plugin MCP skip cache."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, mcp, oauth, permission-prompt-tool, elicitation]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "headersHelper"
  - "bareElicitationCapability"
  - "--permission-prompt-tool"
  - "MCP_TIMEOUT"
  - "MCP_OAUTH_CALLBACK_PORT"
  - "--callback-port"
  - "claude mcp login"
  - "/mcp"
  - "Elicitation"
  - "onElicitation"
  - "timeout"
  - "reconnectMcpServer()"
  - "ClaudeSDKClient.reconnect_mcp_server()"
  - "toggleMcpServer()"
  - "toggle_mcp_server()"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors when connecting to, authenticating with or calling MCP servers, including unattended (`-p`) and SDK runs.

# How to use it

| Error | Cause | Fix |
|---|---|---|
| `"gmail" is Anthropic-hosted and doesn't support local OAuth` | Local OAuth refused for hosts such as `microsoft365.mcp.claude.com`, `gmail.mcp.claude.com`, `gcal.mcp.claude.com` (from `/mcp` and `claude mcp login`) | `claude mcp remove <name>`, then connect at claude.ai/customize/connectors with a claude.ai subscription login |
| `Server rejected the Authorization header minted by the configured headersHelper (HTTP 401)` | `headersHelper` supplies `Authorization`, so no OAuth fallback. Helper re-runs on each connection attempt. Before v2.1.248, OAuth discovery ran and failed with `Incompatible auth server: does not support dynamic client registration` | Run the helper yourself with its directory and env; then `/mcp` > Reconnect |
| `This server (Java MCP SDK 0.17.0 or older) rejected Claude Code's elicitation capability` | Java MCP SDK 0.11.0 to 0.17.0 cannot parse `form`/`url` elicitation modes | Upgrade to Java MCP SDK 0.17.1+ (Spring AI 1.0.7+ or 1.1.6+), or set `"bareElicitationCapability": true` on the server entry (stdio, `sse`, `http`, `ws`; needs v2.1.281+); restart |
| `Error: MCP tool mcp__<server>__<tool> (passed via --permission-prompt-tool) not found. Available MCP tools: ...` | Tool not connected at first permission decision; non-interactive run exits 1 on first tool call. Startup now waits up to the 30 s `MCP_TIMEOUT` for the server (before v2.1.206 it did not wait) | `claude mcp list`; check the `mcp__<server>__<tool>` name; raise `MCP_TIMEOUT` |
| `Permission prompt tool returned an invalid result` | Must return one text block: `{"behavior": "allow"}` or `{"behavior": "deny", "message": "<reason>"}`; `updatedInput` optional (v2.1.86 to v2.1.206 required `"updatedInput": {}` on allow). No `structuredContent` (FastMCP `structured_output=False` / `output_schema=None`; TS SDK without `outputSchema`). Inputs of about 40 KB or more: do not copy into `updatedInput` | See `/en/mcp#raise-the-limit-for-a-specific-tool` |
| `OAuth callback port <port> is already in use` | Fixed port from `MCP_OAUTH_CALLBACK_PORT` or `--callback-port` held by another process | `lsof -ti:<port> -sTCP:LISTEN` (Windows `netstat -ano \| findstr :<port>`) |
| `No available ports for OAuth redirect` | Cannot bind a `127.0.0.1` port (security software, sandbox, Windows Hyper-V reserved ranges). Before v2.1.268 no OS-assigned fallback | Allow local listeners |
| `Skipping connection (recent failure cached; retries automatically in 15 min ...)` | Stdio MCP server from a plugin failed less than 15 minutes ago; not retried in that session | `/mcp` Reconnect; SDK `reconnectMcpServer()` (TS) / `ClaudeSDKClient.reconnect_mcp_server()` (Python); for `claude -p` reconnect in an interactive session with the same user, machine and `CLAUDE_CONFIG_DIR`; or edit the plugin server's `command`, `args` or `env` |
| `MCP server <name> is blocked by enterprise managed policy` | `deniedMcpServers`, `allowedMcpServers`, `strictPluginOnlyCustomization` with `mcp`, or `disableClaudeAiConnectors` | Check own settings; else ask admin. Before v2.1.257 Reconnect could connect a server blocked mid-session |
| `"workspace" is a reserved MCP server name and was not loaded` | Reserved built-in server name | Rename the server |

# Limits and defaults

- `MCP_TIMEOUT` per-server connection wait: 30 seconds default.
- Plugin MCP failure cache: 15 minutes.

# Notes

Tool-call results for MCP problems (closed connection, disabled server, elicitation timeout) are in [tool errors](./p3-tool-errors-mcp-and-agents.md).
