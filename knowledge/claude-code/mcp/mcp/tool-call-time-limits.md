---
type: "Limit"
title: "Time limits on MCP tool calls"
description: "Per-server timeout, MCP_TOOL_TIMEOUT, MCP_TIMEOUT, the per-request timer and the idle timeout CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, timeout, limits, idle]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "timeout"
  - "MCP_TOOL_TIMEOUT"
  - "MCP_TIMEOUT"
  - "CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT"
  - "MCP_CONNECTION_NONBLOCKING"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Limits on how long a server takes to start and how long a tool call may run.

# How to use it

| Name | Kind | Default | What it does |
|---|---|---|---|
| `MCP_TIMEOUT` | env var (ms) | 30 seconds startup (the quickstart notes 30 s; the tips there show `MCP_TIMEOUT=10000 claude` as a 10 s example) | server startup timeout |
| `timeout` | per-server field in `.mcp.json` entry (ms) | none | hard wall-clock limit per tool call; progress notifications do not extend it; overrides `MCP_TOOL_TIMEOUT` for that server; values below 1000 are ignored |
| `MCP_TOOL_TIMEOUT` | env var (ms) | about 28 hours when unset | tool-call limit across servers |
| `CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT` | env var (ms) | 5 min for HTTP, SSE, WebSocket and claude.ai connector servers; 30 min for stdio | abort a call with no response or progress for this window; `0` disables the check |
| `MCP_CONNECTION_NONBLOCKING` | env var | background connect | `0` makes startup wait for servers too |

# Limits and defaults

- A per-server `timeout` of at least 1000 is also a floor on the idle timeout.
- The idle timeout applies to every server type except IDE servers and SDK in-process servers.
- HTTP, SSE and claude.ai connector servers also have a per-request timer to the first response byte: the greatest of 60 seconds, the applicable tool timeout and `MCP_TIMEOUT` (the 28-hour unset default is excluded). Stdio and WebSocket have none.
- Timeouts bound how long a call runs, not necessarily how long it blocks: see [automatic backgrounding](./automatic-backgrounding.md).
