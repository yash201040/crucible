---
type: "Feature"
title: "Workflow agent stalls and automatic restarts"
description: "A silent agent restarts up to five times; stallMs and CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS lengthen the stall window."
resource: "https://code.claude.com/docs/en/workflows"
tags: [workflows, stall, retry, timeouts]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "stallMs"
  - "CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS"
  - "CLAUDE_STREAM_IDLE_TIMEOUT_MS"
  - "agent stalled on all 6 attempts"
  - "agent lost its reply on all 6 attempts"
  - "agent abandoned after 6 attempts"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "workflows"
    resource: "https://code.claude.com/docs/en/workflows"
    title: "Orchestrate subagents at scale with dynamic workflows"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An agent whose output stops long enough restarts from the same prompt, shown as `(retry 1)` in `/workflows` with `attempt 2 (stalled)`. The new attempt has no transcript of the stalled one; files already changed stay changed and spent tokens stay in the run total. Time waiting on the agent's own tool calls or a usage-limit reset does not count toward the stall window.

# How to use it

- One agent: `agent(prompt, { stallMs: 1800000 })` (30 minutes).
- Every agent (also subagents outside workflows): `CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS`.

# Limits and defaults

At most five restarts (counting ones you request with `r`); the sixth stall fails the `agent()` call with one of:
- `agent stalled on all 6 attempts`: every attempt silent the whole window; lengthen the window.
- `agent lost its reply on all 6 attempts`: response streams went silent and the streaming idle watchdog ended them; `CLAUDE_STREAM_IDLE_TIMEOUT_MS` sets that timeout, lengthening the stall window does not help.
- `agent abandoned after 6 attempts`: attempts ended differently, listed in order.

Afterwards: inside `parallel()` or `pipeline()` the run continues with `null` for that agent; awaited directly, the run ends with the error. Relaunch to retry.
