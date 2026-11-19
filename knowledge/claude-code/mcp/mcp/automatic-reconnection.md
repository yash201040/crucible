---
type: "Feature"
title: "Automatic reconnection and retries"
description: "Reconnect behavior for remote and stdio MCP servers in interactive, claude -p and Agent SDK runs, with retry counts and windows."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, reconnect, retry, headless]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.284"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "/mcp reconnect all"
  - "needs-auth"
  - "failed"
  - "claude mcp login <name>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code reconnects a remote server that drops mid-session and retries an HTTP or SSE server's first connection after a transient error.

# How to use it

Mid-session drop of a remote server: up to five reconnect attempts with exponential backoff (1 s start, doubling).
- Interactive: `/mcp` shows pending; after five failures the server is failed or needs auth. Notice `disconnected · still retrying` means retries continue up to about a day (shown as `retrying`); `disconnected · open /mcp to reconnect` means no background retry. Disable the server in `/mcp` to stop retries.
- `claude -p` and Agent SDK: same five attempts; if all fail the run continues without the server's tools. After a transient error (5xx, timeout) HTTP/SSE servers keep retrying in background (up to about half an hour, or about a day for some servers) and tools return when one connects; an SDK session reports status `failed` meanwhile and your code can reconnect it (in `claude -p`, start the run again). If sign-in is needed, retrying stops; SDK status is `needs-auth`; run `claude mcp login <name>` then restart the run or reconnect.

First connection of HTTP/SSE: up to three retries on transient errors (5xx, connection refused, timeout). Not applied to: stdio first connection; WebSocket first connection (use Reconnect in `/mcp`); auth or not-found errors (except when a `headersHelper` is the only source of `Authorization`, which is re-run each attempt).

Stdio servers that exit or fail to start:

| Run type | Process exits mid-session | First connection fails |
|---|---|---|
| Interactive | marked failed; Reconnect in `/mcp` | marked failed; Reconnect in `/mcp` |
| `claude -p` | restarted next time Claude calls one of its tools | run continues without its tools; start run again. Plugin-provided servers are skipped for 15 minutes after a failure |
| Agent SDK | restarted on next tool call | session continues without tools; your code can reconnect |

Discovery requests (`tools/list`, `prompts/list`, `resources/list`): retried up to three times with short backoff on transient errors; not on auth errors, 4xx or timeouts.

`/mcp reconnect all` retries every failed or needs-auth server, interactive only, v2.1.284 or later.

# Notes

How Claude learns of failure: with tool search, Claude is told which server failed and its error (also in `ToolSearch` results with no match); without tool search, failed connections are not reported to Claude.
