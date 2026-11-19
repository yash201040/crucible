---
type: "Reference"
title: "API timeouts and streaming watchdog variables"
description: "Variables for the request header timeout, body idle timeout, event-level and byte-level stream watchdogs, first-byte deadline and tool input streaming."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [timeouts, streaming, watchdog, network]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "API_TIMEOUT_MS"
  - "API_FORCE_IDLE_TIMEOUT"
  - "CLAUDE_STREAM_IDLE_TIMEOUT_MS"
  - "CLAUDE_BYTE_STREAM_IDLE_TIMEOUT_MS"
  - "CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS"
  - "CLAUDE_ENABLE_BYTE_WATCHDOG"
  - "CLAUDE_ENABLE_BYTE_WATCHDOG_BEDROCK"
  - "CLAUDE_ENABLE_STREAM_WATCHDOG"
  - "CLAUDE_CODE_CONNECT_TIMEOUT_MS"
  - "CLAUDE_CODE_ENABLE_FINE_GRAINED_TOOL_STREAMING"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Timers that abort or retry slow or silent model streams. See the network-config "Streaming idle watchdogs" section for how they interact.

# How to use it

| Variable | What it does |
| :- | :- |
| `API_TIMEOUT_MS` | Time each API request attempt has to receive response headers (default 600000 = 10 min; max 2147483647). Does not limit a stream after headers. A positive value also requires each non-streaming attempt to finish within it. `0` removes the limit (v2.1.305+); a non-streaming attempt in a local session still times out at 300 s. |
| `API_FORCE_IDLE_TIMEOUT` | Overrides the 5-minute body idle timeout that aborts a stream when no bytes arrive. `0` turns it off, `1` keeps it on for every provider. Unset: active except on the direct Anthropic API, Claude Platform on AWS, and Bedrock with `CLAUDE_ENABLE_BYTE_WATCHDOG_BEDROCK=1`. Stream watchdogs run independently and abort long silent pauses even with `0`. |
| `CLAUDE_STREAM_IDLE_TIMEOUT_MS` | Timeout before the event- and byte-level idle watchdogs close a stalled connection. Explicit minimum `300000` (lower values clamped); byte-level watchdog caps at 30 minutes. `CLAUDE_BYTE_STREAM_IDLE_TIMEOUT_MS` beats it for the byte watchdog. |
| `CLAUDE_BYTE_STREAM_IDLE_TIMEOUT_MS` | Byte-level watchdog timeout, clamped between 10 seconds and 30 minutes; leaves the event-level watchdog unchanged. Requires v2.1.210+. |
| `CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS` | Deadline for the first response byte of a streaming request, where the first-byte deadline runs. Requires v2.1.242+. |
| `CLAUDE_ENABLE_BYTE_WATCHDOG` | `1` forces the byte-level watchdog on, `0` forces it off (also turns off the first-byte deadline where it runs). Unset: on for direct Anthropic API, Claude Platform on AWS, and streaming gateway connections via `ANTHROPIC_BASE_URL` or `ANTHROPIC_AWS_BASE_URL` (before v2.1.222 not on gateways). |
| `CLAUDE_ENABLE_BYTE_WATCHDOG_BEDROCK` | `1` enables the byte watchdog on Bedrock `vnd.amazon.eventstream` responses, and the first-byte deadline on Bedrock streaming. Off by default; timeout via `CLAUDE_STREAM_IDLE_TIMEOUT_MS`. |
| `CLAUDE_ENABLE_STREAM_WATCHDOG` | `0` force-disables, `1` force-enables the event-level watchdog. Unset: on for all providers (before v2.1.196 server-controlled on the direct API and off elsewhere). |
| `CLAUDE_CODE_CONNECT_TIMEOUT_MS` | Removed in v2.1.186, now a no-op; use `API_TIMEOUT_MS` (and `CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS` for streaming response headers). |
| `CLAUDE_CODE_ENABLE_FINE_GRAINED_TOOL_STREAMING` | Whether tool call inputs stream as generated; off, a large input such as a long file write arrives only when finished and can look hung. On by default on the Anthropic API; on Bedrock and Google Cloud's Agent Platform enabled per model where the container supports it; off by default on Foundry and gateways. `0` opts out; `1` forces on through proxies via `ANTHROPIC_BASE_URL`, `ANTHROPIC_VERTEX_BASE_URL` or `ANTHROPIC_BEDROCK_BASE_URL`. |
