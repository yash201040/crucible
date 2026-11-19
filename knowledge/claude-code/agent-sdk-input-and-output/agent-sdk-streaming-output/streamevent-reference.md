---
type: "Reference"
title: "StreamEvent reference"
description: "Type names per SDK, the raw event types, and caveats such as no subagent deltas and parent_tool_use_id always empty."
resource: "https://code.claude.com/docs/en/agent-sdk/streaming-output"
tags: [streaming, events, subagents, reference]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "message_start"
  - "content_block_start"
  - "content_block_delta"
  - "content_block_stop"
  - "message_delta"
  - "message_stop"
  - "input_json_delta"
  - "parent_tool_use_id"
  - "user_message_uuid"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-streaming-output"
    resource: "https://code.claude.com/docs/en/agent-sdk/streaming-output"
    title: "Stream responses in real-time"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The wrapper types are Python `StreamEvent` (import from `claude_agent_sdk.types`) and TypeScript `SDKPartialAssistantMessage` with `type: 'stream_event'`. Both hold raw Claude API streaming events, not accumulated text.

# How to use it

| Event | Meaning |
| --- | --- |
| `message_start` | Start of a new message |
| `content_block_start` | Start of a text or tool use block |
| `content_block_delta` | Incremental update (`text_delta`, or `input_json_delta` with `partial_json` for tool input) |
| `content_block_stop` | End of a content block |
| `message_delta` | Message-level updates (stop reason, usage) |
| `message_stop` | End of the message |

# Limits and defaults

- `parent_tool_use_id` is always `None` (Python) / `null` (TypeScript) on stream events. Stream events are emitted for the main session only; subagent token-level deltas are not forwarded. To attribute output to a subagent use complete messages, which carry `parent_tool_use_id`.
- Claude Code sets `user_message_uuid` on a turn's first non-ping stream event and again when the answered message changes; the Python `StreamEvent` does not expose it.
- Structured output: with partial messages, JSON streams as unvalidated `input_json_delta` chunks of a tool call; only the validated result reaches `ResultMessage.structured_output`.
