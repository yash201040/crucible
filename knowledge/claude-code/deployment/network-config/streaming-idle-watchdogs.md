---
type: "Reference"
title: "Streaming idle watchdogs and timeouts"
description: "Four timers that abort quiet streaming responses, their defaults, which providers each runs on, and the variables that tune them."
resource: "https://code.claude.com/docs/en/network-config"
tags: [timeouts, watchdog, streaming, retries]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.328"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS"
  - "CLAUDE_STREAM_IDLE_TIMEOUT_MS"
  - "CLAUDE_BYTE_STREAM_IDLE_TIMEOUT_MS"
  - "CLAUDE_ENABLE_STREAM_WATCHDOG"
  - "CLAUDE_ENABLE_BYTE_WATCHDOG"
  - "CLAUDE_ENABLE_BYTE_WATCHDOG_BEDROCK"
  - "API_TIMEOUT_MS"
  - "API_FORCE_IDLE_TIMEOUT"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "network-config"
    resource: "https://code.claude.com/docs/en/network-config"
    title: "Enterprise network configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Four independent timers abort a model response stream that goes quiet so a dead connection fails and retries instead of hanging.

# How to use it

| Timer | Aborts when | Default |
|---|---|---|
| First-byte deadline | no response headers after sending the request | 180 s direct Anthropic API; 300 s on Claude Platform on AWS or Bedrock; plus 1 s per 32KB of request body |
| Event-level watchdog | no response events parse (bytes and keep-alive pings extend it for a limited time where the byte watchdog runs) | 300 s; every provider |
| Byte-level watchdog | no bytes on the wire including SSE pings | 180 s direct API; 300 s on Claude Platform on AWS, Bedrock, Claude apps gateway sessions and custom `ANTHROPIC_BASE_URL` |
| Body idle timeout | no bytes, counting wait for headers | 5 minutes; providers other than direct API, Claude Platform on AWS, and Bedrock with `CLAUDE_ENABLE_BYTE_WATCHDOG_BEDROCK=1` |

Where they run: the first-byte deadline runs on the direct API and Claude Platform on AWS (not when `ANTHROPIC_BASE_URL` or `ANTHROPIC_AWS_BASE_URL` routes through a gateway), is opt-in for Claude apps gateway sessions and on Bedrock (`CLAUDE_ENABLE_BYTE_WATCHDOG_BEDROCK=1`), and does not run on Google Cloud's Agent Platform or Foundry. The byte watchdog does not run on Agent Platform or Foundry either.

Variables:
- `CLAUDE_ENABLE_STREAM_WATCHDOG`, `CLAUDE_ENABLE_BYTE_WATCHDOG`: `1` forces on, `0` off, within the connections each covers; byte `0` also disables the first-byte deadline.
- `CLAUDE_STREAM_IDLE_TIMEOUT_MS`: sets both watchdogs; values under 5 minutes raised to 5 minutes; capped at 30 minutes for the byte watchdog; above 5 minutes also lengthens the body idle timeout up to 30 minutes on v2.1.328+.
- `CLAUDE_BYTE_STREAM_IDLE_TIMEOUT_MS`: byte watchdog only, clamped 10 seconds to 30 minutes, takes precedence.
- `CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS`: first-byte deadline (turns it on in Claude apps gateway sessions); if unset where it runs, uses the byte watchdog timeout.
- `API_TIMEOUT_MS`: limits wait for headers; where the first-byte deadline does not run, a positive value under `300000` retries sooner. Keep above the longest expected header wait and non-streaming request.
- `API_FORCE_IDLE_TIMEOUT`: `0` turns the body idle timeout off, `1` on for every provider.

# Limits and defaults

On abort the request is retried, or the turn ends with an error, or an incomplete-response notice is shown. In non-interactive sessions and for subagent responses Claude Code may first prompt Claude to continue the cut-off response. A first-byte abort has no partial output to keep. Bedrock streams with the byte watchdog on log `wire-heartbeat: _chunkTimes absent` in debug.
