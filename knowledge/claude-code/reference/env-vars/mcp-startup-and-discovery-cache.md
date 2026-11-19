---
type: "Reference"
title: "MCP startup, connection and discovery cache variables"
description: "Variables for MCP server connection timing, batch sizes, first-turn waits, the discovery cache and the MCP client runtime and protocol negotiation."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [mcp, startup, discovery-cache, connections]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "MCP_CONNECTION_NONBLOCKING"
  - "MCP_CONNECT_TIMEOUT_MS"
  - "MCP_TIMEOUT"
  - "MCP_REMOTE_SERVER_CONNECTION_BATCH_SIZE"
  - "MCP_SERVER_CONNECTION_BATCH_SIZE"
  - "CLAUDE_CODE_MCP_STARTUP_WAIT_MS"
  - "MCP_DISCOVERY_CACHE"
  - "MCP_DISCOVERY_CACHE_MAX_STALE_S"
  - "MCP_DISCOVERY_CACHE_STRIKES"
  - "MCP_DISCOVERY_CACHE_TTL_S"
  - "MCP_PROTOCOL_NEGOTIATION"
  - "MCP_SDK_GENERATION"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

How fast and in what order MCP servers connect, which determines whether their tools exist on the first turn of an unattended run.

# How to use it

| Variable | What it does |
| :- | :- |
| `MCP_CONNECTION_NONBLOCKING` | MCP startup is non-blocking by default (tools appear as servers finish). `0` makes Claude Code wait before the first query. Servers with `alwaysLoad: true` still make startup wait (except when served from the discovery cache). In `-p` mode without `--input-format stream-json` it waits for pending servers before the first turn regardless; with `--mcp-config` the wait has a longer deadline. |
| `MCP_CONNECT_TIMEOUT_MS` | Wait for the connection batch before snapshotting tools (default 5000); applies with `MCP_CONNECTION_NONBLOCKING=0` or `alwaysLoad: true` servers; stragglers keep connecting. Distinct from `MCP_TIMEOUT`. |
| `MCP_TIMEOUT` | Timeout for MCP server startup, per connect attempt (default 30000 ms). |
| `MCP_REMOTE_SERVER_CONNECTION_BATCH_SIZE` | Remote (HTTP/SSE) servers connected in parallel at startup (default 20). |
| `MCP_SERVER_CONNECTION_BATCH_SIZE` | Local (stdio) servers connected in parallel at startup (default 3). |
| `CLAUDE_CODE_MCP_STARTUP_WAIT_MS` | How long the first turn of a non-interactive session waits for still-connecting servers, replacing the default first-turn wait; `0` skips the wait for every other server (some servers keep their own wait). Requires v2.1.274+. |
| `MCP_DISCOVERY_CACHE` | `1` turns the discovery cache on (a used remote HTTP/SSE server can show status `cached` and connects on its first tool call instead of at startup); `0` keeps it off even when a gradual rollout enabled it. Off by default unless rolled out; before v2.1.238 on by default. `cached` status requires v2.1.221+. |
| `MCP_DISCOVERY_CACHE_MAX_STALE_S` | Max age of an entry (default 14400 = 4 h; capped at 7 days); older entries are discarded and the server connects at startup. Before v2.1.238: default 86400, no cap. |
| `MCP_DISCOVERY_CACHE_STRIKES` | Consecutive failed background refreshes before an entry is discarded (default 1). Requires v2.1.238+. |
| `MCP_DISCOVERY_CACHE_TTL_S` | Seconds an entry is used without refresh (default 900); older entries are used but refreshed in the background until `MCP_DISCOVERY_CACHE_MAX_STALE_S`. Capped at that value (before v2.1.238 uncapped). |
| `MCP_PROTOCOL_NEGOTIATION` | v2 MCP client runtime only: `legacy` keeps every server on the earlier handshake, `auto` probes supporting server kinds for MCP protocol revision 2026-07-28; unset probes but may skip some. Other values ignored with a debug-log warning. Requires v2.1.221+. |
| `MCP_SDK_GENERATION` | Pins the MCP client runtime: `v1` (MCP TypeScript SDK 1.x) or `v2` (SDK 2.0; the default). From v2.1.221 the v2 runtime fails sign-in with `Issuer mismatch in authorization response` if the OAuth issuer does not match; v1 does not check. Unrecognized values ignored with a warning; read once per process. Requires v2.1.218+. |
