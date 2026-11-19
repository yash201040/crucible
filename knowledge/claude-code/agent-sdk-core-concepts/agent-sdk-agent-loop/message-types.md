---
type: "Reference"
title: "SDK message types"
description: "The five core message types yielded by the loop and the SystemMessage subtypes."
resource: "https://code.claude.com/docs/en/agent-sdk/agent-loop"
tags: [messages, system-message, stream, result]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "SystemMessage"
  - "AssistantMessage"
  - "UserMessage"
  - "StreamEvent"
  - "ResultMessage"
  - "init"
  - "compact_boundary"
  - "informational"
  - "worker_shutting_down"
  - "prompt_suggestion"
  - "include_partial_messages"
  - "includePartialMessages"
  - "SDKMessage"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-agent-loop"
    resource: "https://code.claude.com/docs/en/agent-sdk/agent-loop"
    title: "How the agent loop works"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Type | Meaning |
| :- | :- |
| `SystemMessage` | Lifecycle events by `subtype`: `"init"` (session metadata; `SessionStart`/`Setup` hook lifecycle messages arrive before it), `"compact_boundary"` (after compaction), `"informational"` (plain-text status banners), `"worker_shutting_down"` (host exiting or Remote Control disconnected) |
| `AssistantMessage` | One per content block of Claude's responses; messages from one response share a message ID |
| `UserMessage` | After each tool execution with results; also for user inputs streamed mid-loop |
| `StreamEvent` | Only with partial messages enabled (`include_partial_messages` / `includePartialMessages`): raw API streaming events |
| `ResultMessage` | End of loop: result text, usage, cost, session ID; check `subtype` |

# How to use it

- Final results only: handle `ResultMessage`. Progress: `AssistantMessage`. Live: partial messages.
- Python: `isinstance()` against `claude_agent_sdk` classes. TypeScript: check the `type` string; `AssistantMessage`/`UserMessage` wrap the raw message in `.message`, so content is `message.message.content`.
- In TypeScript each `SystemMessage` subtype other than `"init"` is its own type in the `SDKMessage` union.
- A few trailing system events such as `prompt_suggestion` can arrive after `ResultMessage`, so iterate the stream to completion rather than breaking on the result.

# Notes

Both SDKs also yield observability events such as rate-limit status and task notifications that are not needed to drive the loop.
