---
type: "Guide"
title: "Agent SDK session patterns: ephemeral, long-running, hybrid, multi-agent"
description: "Four container lifecycle patterns with the SDK calls each uses, including streamInput, startup, prewarm, ClaudeSDKClient and resume with a SessionStore."
resource: "https://code.claude.com/docs/en/agent-sdk/hosting"
tags: [agent-sdk, containers, session-patterns, resume, prewarm]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "TASK_PROMPT"
  - "maxTurns"
  - "max_turns"
  - "error_max_turns"
  - "streamInput()"
  - "startup()"
  - "prewarm()"
  - "ClaudeSDKClient"
  - "resume"
  - "sessionStore"
  - "session_store"
  - "mirror_error"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-hosting"
    resource: "https://code.claude.com/docs/en/agent-sdk/hosting"
    title: "Hosting the Agent SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Pattern | Lifecycle | Notes |
| - | - | - |
| Ephemeral | Container per task, destroyed after | One-shot entrypoint reads `TASK_PROMPT`, calls the SDK, exits; e.g. `query({ prompt, options: { maxTurns: 20 } })`. Hitting the limit yields a result message with `subtype` `error_max_turns` and then `query()` raises, so wrap the loop to exit cleanly. `success` subtype on completion. |
| Long-running | Persistent containers, often many SDK processes each | HTTP or WebSocket endpoint maps each session to a long-lived query. TypeScript: `streamInput()` adds turns, `startup()` pre-warms subprocesses, `prewarm()` when the working directory is unknown until the first request. Python: `ClaudeSDKClient` holds a session open. Size memory for peak concurrent sessions. |
| Hybrid | Ephemeral containers hydrate from a `SessionStore`, persist back | `options: { resume: sessionId, sessionStore }` (Python `resume=`, `session_store=`). The store is required, not optional: shutdown without one loses the transcript. Tune provider idle timeout to user return rate. |
| Multi-agent container | Several SDK subprocesses in one container | Give each its own working directory and isolate settings loading so per-agent `CLAUDE.md` does not leak. |

# Limits and defaults

- `SessionStore` mirrors transcripts only (not `CLAUDE.md` or artifacts). The subprocess writes to local disk first and the SDK forwards a copy of each batch; a fresh session's local transcript outlives the run, while a run resumed from the store deletes its local copy at the end, leaving the store as the only durable copy.
- When a batch cannot be delivered the SDK drops it, emits `{ type: "system", subtype: "mirror_error" }` and continues the query; alert on these if durability matters.
