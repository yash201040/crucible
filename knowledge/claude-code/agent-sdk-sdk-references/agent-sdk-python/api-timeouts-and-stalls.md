---
type: "Reference"
title: "Timeout, retry and stall variables"
description: "Environment variables the CLI subprocess reads for API timeouts, retries and stall watchdogs, passed via ClaudeAgentOptions.env."
resource: "https://code.claude.com/docs/en/agent-sdk/python"
tags: [timeouts, retries, watchdog, env-vars, subagents]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [sdk, headless]
requires: ""
identifiers:
  - "API_TIMEOUT_MS"
  - "CLAUDE_CODE_MAX_RETRIES"
  - "CLAUDE_CODE_RETRY_WATCHDOG"
  - "CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS"
  - "CLAUDE_ENABLE_STREAM_WATCHDOG"
  - "CLAUDE_STREAM_IDLE_TIMEOUT_MS"
  - "CLAUDE_CODE_EMIT_SESSION_STATE_EVENTS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-python"
    resource: "https://code.claude.com/docs/en/agent-sdk/python"
    title: "Agent SDK reference - Python"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The CLI subprocess started by the SDK reads these variables. Set them with `ClaudeAgentOptions(env={...})`.

# How to use it

| Variable | Default | What it does |
| :- | :- | :- |
| `API_TIMEOUT_MS` | `600000` | how long each attempt waits for response headers; does not limit a streaming response after headers; applies to main loop and all subagents |
| `CLAUDE_CODE_MAX_RETRIES` | `10`, capped at `15` | max API retries; each retry gets its own `API_TIMEOUT_MS` window |
| `CLAUDE_CODE_RETRY_WATCHDOG` | unset | set to `1` for unattended runs: retries transient capacity errors indefinitely; on Claude Code 2.1.199+ also raises the default for other transient errors to `300` and removes the cap on `CLAUDE_CODE_MAX_RETRIES` |
| `CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS` | stream-idle timeout plus 5 minutes (`600000` unless raised) when stream watchdog is on; `600000` when off; before v2.1.257 always `600000` | stall watchdog for subagents; timer resets on each stream event; on stall the subagent is aborted and the parent told; a background subagent is marked failed with any partial result attached |
| `CLAUDE_ENABLE_STREAM_WATCHDOG` | on for all providers | set `0` to disable; aborts when headers arrived but the body stops streaming |
| `CLAUDE_STREAM_IDLE_TIMEOUT_MS` | `300000` (also the minimum) | idle limit for the stream watchdog |
| `CLAUDE_CODE_EMIT_SESSION_STATE_EVENTS` | unset | set `1` to receive `SystemMessage` with `subtype` `session_state_changed` (`message.data["state"]`) between turns |

# Notes

- With a gateway behind `ANTHROPIC_BASE_URL` holding the response open with keep-alives, hosts with `include_partial_messages` keep receiving `ping` `StreamEvent` messages; treat them as liveness. Before v2.1.257 they stopped 5 minutes after the last real event.
- `session_state_changed` can follow the `ResultMessage`, so read it with `receive_messages()` rather than `receive_response()`.
