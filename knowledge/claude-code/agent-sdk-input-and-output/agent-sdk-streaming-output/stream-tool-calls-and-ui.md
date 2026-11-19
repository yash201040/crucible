---
type: "Guide"
title: "Stream tool calls and build a streaming UI"
description: "Track tool_use blocks and accumulate input_json_delta chunks, using an in_tool flag to show progress in a chat UI."
resource: "https://code.claude.com/docs/en/agent-sdk/streaming-output"
tags: [streaming, tool-calls, ui, input-json-delta]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "content_block_start"
  - "input_json_delta"
  - "partial_json"
  - "content_block_stop"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-streaming-output"
    resource: "https://code.claude.com/docs/en/agent-sdk/streaming-output"
    title: "Stream responses in real-time"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Tool calls also stream incrementally.

# How to use it

1. `content_block_start` with `content_block.type == "tool_use"`: a tool begins; record `content_block.name` and reset an input buffer.
2. `content_block_delta` with `delta.type == "input_json_delta"`: append `delta.partial_json` to the buffer.
3. `content_block_stop`: the call is complete; the buffer holds the final JSON input.

For a UI, keep an `in_tool` flag: show a status such as `[Using Read...]` at block start, stream `text_delta` text only while not in a tool, and print "done" at block stop. A `ResultMessage` signals the agent finished.
