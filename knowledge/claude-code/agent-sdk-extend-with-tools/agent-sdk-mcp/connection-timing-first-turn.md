---
type: "Feature"
title: "MCP connection timing and first-turn wait"
description: "How long the first turn waits for MCP servers to connect, by server type and config source, and how to change it."
resource: "https://code.claude.com/docs/en/agent-sdk/mcp"
tags: [mcp, startup, timeouts, first-turn]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.274"
surfaces: [sdk]
requires: "CLAUDE_CODE_MCP_STARTUP_WAIT_MS needs Claude Code v2.1.274 or later"
identifiers:
  - "MCP_TIMEOUT"
  - "CLAUDE_CODE_MCP_STARTUP_WAIT_MS"
  - "MCP_CONNECTION_NONBLOCKING"
  - "MCP_CONNECT_TIMEOUT_MS"
  - "alwaysLoad"
  - "permissionPromptToolName"
  - "ANTHROPIC_BASE_URL"
  - "ENABLE_TOOL_SEARCH"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-mcp"
    resource: "https://code.claude.com/docs/en/agent-sdk/mcp"
    title: "Connect to external tools with MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code starts connecting MCP servers when the session starts and sends the init message once the first-turn wait (if any) ends. The wait depends on where the server is configured.

# How to use it

Servers in `options.mcpServers`:

| Server type | Delays first turn? | Wait |
| --- | --- | --- |
| stdio, or HTTP/SSE without cached tool list | Yes | `MCP_TIMEOUT`, 30 s default; connection fails at deadline |
| Remote with cached tool list (saved from a previous connection) | No | None; connects on first tool call (own timeout) |
| In-process SDK server | Yes | `MCP_TIMEOUT` (30 s default) per connect attempt |

A cached tool list exists only when the MCP discovery cache is on. If `permissionPromptToolName` is set, the first turn always waits for that tool's server, up to `MCP_TIMEOUT`.

Servers from settings files (`.mcp.json`) or plugins often show `pending` at init:
- `options.mcpServers` has a stdio/HTTP/SSE server: first turn waits for them too, up to `MCP_TIMEOUT`.
- Else `ANTHROPIC_BASE_URL` points to a gateway and `ENABLE_TOOL_SEARCH` unset: waits up to 2 s for every pending one.
- Else tool search on (default): waits up to 2 s, only for servers with `alwaysLoad: true` or [named servers](#); others connect in the background.
- Else tool search off: waits up to 2 s for every pending one.

Named servers: a server is named by listing any of its tools (`mcp__github__list_issues`, `mcp__github__*`) in `allowedTools` or a `permissions.allow` rule in the `settings` option, or by an `mcp_tool` hook on a prompt-submission, tool-use, permission, subagent, task, elicitation or worktree event. Before v2.1.284 naming had no effect on the wait.

Set the wait yourself with `CLAUDE_CODE_MCP_STARTUP_WAIT_MS` in the `env` option (e.g. `"5000"`): applies to settings-file and plugin servers and replaces the `MCP_TIMEOUT` wait for stdio/HTTP/SSE servers in `options.mcpServers`. `0` skips the wait for every other server.

# Limits and defaults

Waits that apply whatever value, including `0`: a `permissionPromptToolName` server (up to `MCP_TIMEOUT`); an in-process SDK server (up to `MCP_TIMEOUT` per attempt); a still-connecting named server (at least 2 s).

Making startup itself wait before init: `MCP_CONNECTION_NONBLOCKING=0` waits for the whole batch, up to 5 s by default (change with `MCP_CONNECT_TIMEOUT_MS`, ms); `alwaysLoad: true` on a server config waits up to the same cap and gives full schemas, exempt from tool-search deferral. Servers pending at the cap keep connecting in the background.

# Notes

The init message reports each server status as of the moment it is sent. An SDK MCP server registered by an `initialize` control request begins connecting as soon as it is processed.
