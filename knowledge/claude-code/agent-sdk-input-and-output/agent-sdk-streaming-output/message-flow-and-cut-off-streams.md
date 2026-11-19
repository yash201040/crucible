---
type: "Concept"
title: "Message flow and cut-off streams"
description: "Order of StreamEvent and AssistantMessage messages, and what to expect when a stream is interrupted, dropped or falls back to non-streaming."
resource: "https://code.claude.com/docs/en/agent-sdk/streaming-output"
tags: [streaming, message-order, interruption, reliability]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.290"
surfaces: [sdk]
requires: ""
identifiers:
  - "AssistantMessage"
  - "ResultMessage"
  - "SystemMessage"
  - "SDKCompactBoundaryMessage"
  - "message_stop"
  - "content_block_stop"
  - "message_delta"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-streaming-output"
    resource: "https://code.claude.com/docs/en/agent-sdk/streaming-output"
    title: "Stream responses in real-time"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An `AssistantMessage` is emitted as each non-empty content block completes, so a text block plus a tool call yields two, each carrying only its own block and sharing the same message ID (`message.message.id` in TypeScript, `message.message_id` in Python). With partial messages on, each `AssistantMessage` arrives before that block's `content_block_stop`. Sequence: `message_start`, block start, deltas, `AssistantMessage`, block stop (per block), then `message_delta`, `message_stop`, tool executes, more events for the next turn, final `ResultMessage`.

Without partial messages you get all types except `StreamEvent`: `SystemMessage` (initialization), `AssistantMessage`, `ResultMessage`, and a compact boundary message (`SDKCompactBoundaryMessage` in TypeScript; `SystemMessage` with subtype `"compact_boundary"` in Python).

# How to use it

If a stream is cut off mid-message (interrupted turn, dropped connection, fallback to a non-streaming request) you still get that message's `message_stop` before the turn ends:
- `content_block_stop` arrives for the open block unless it is a tool call; if `message_stop` arrives while a tool call block is open, treat its input as incomplete.
- `message_delta` arrives on interrupt but can be missing after a dropped connection or non-streaming fallback; do not wait for it.

# Notes

Before Claude Code v2.1.290 a cut stream could end the turn without `message_stop`, leaving a reply shown as in progress. TypeScript Agent SDK bundles Claude Code v2.1.290 or later from v0.3.290, Python from v0.2.164; update the SDK if a reply stays in progress.
