---
type: "Feature"
title: "Enable partial message streaming"
description: "Set includePartialMessages / include_partial_messages to receive StreamEvent messages with raw API deltas as text and tool calls are generated."
resource: "https://code.claude.com/docs/en/agent-sdk/streaming-output"
tags: [streaming, partial-messages, streamevent, sdk]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "includePartialMessages"
  - "include_partial_messages"
  - "StreamEvent"
  - "stream_event"
  - "SDKPartialAssistantMessage"
  - "content_block_delta"
  - "text_delta"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-streaming-output"
    resource: "https://code.claude.com/docs/en/agent-sdk/streaming-output"
    title: "Stream responses in real-time"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

By default the SDK yields a complete `AssistantMessage` per non-empty content block after Claude finishes it. Enabling partial streaming adds `StreamEvent` messages carrying raw API events as they arrive, in addition to the usual `AssistantMessage` and `ResultMessage`.

# How to use it

Set `include_partial_messages=True` (Python) or `includePartialMessages: true` (TypeScript). Then: distinguish `StreamEvent` from other types; read its `event` field and `type`; for `content_block_delta` with `delta.type` of `text_delta`, take the text chunk. Events are raw, so you accumulate text yourself.

# Notes

Related pages: sending messages to a running session (streaming vs single mode) and CLI streaming via the headless docs.
