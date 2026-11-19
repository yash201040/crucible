---
type: "Feature"
title: "Interrupt a running response"
description: "interrupt() stops a response partway and keeps the session open; the response ends with an error_during_execution result and unread queued messages still arrive."
resource: "https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode"
tags: [agent-sdk, interrupt, streaming-input, sessions]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "interrupt()"
  - "error_during_execution"
  - "Query"
  - "ClaudeSDKClient"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-streaming-vs-single-mode"
    resource: "https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode"
    title: "Send messages to a running agent"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Calling `interrupt()` on the object that runs the session stops the current response and leaves the session open, so the same session can then take another message.

# How to use it

- TypeScript: pass an async generator as `prompt`, keep the `Query` object that `query()` returns, and call `await conversation.interrupt()`.
- Python: call `await client.interrupt()` on the `ClaudeSDKClient`. If a `receive_response()` loop is reading, that loop ends at the interrupted response's `ResultMessage`. Send the next message after that result arrives.

# Limits and defaults

- The interrupted response ends with an `error_during_execution` result.
- Messages sent before the interrupt that Claude had not yet read still reach Claude once the interrupted response ends.
- In TypeScript, if the last response is the error result the loop yields it and then throws (see [read each response](./read-each-response-result-message.md)).
