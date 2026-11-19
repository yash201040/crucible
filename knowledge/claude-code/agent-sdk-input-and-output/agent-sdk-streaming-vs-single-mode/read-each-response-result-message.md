---
type: "Feature"
title: "Read each response and its result message"
description: "Each response ends with a result message whose subtype reports how it ended; loop behavior on error results differs between TypeScript and Python."
resource: "https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode"
tags: [agent-sdk, result-message, errors, streaming-input]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "subtype"
  - "success"
  - "error_during_execution"
  - "uuid"
  - "user_message_uuids"
  - "receive_response()"
  - "ResultMessage"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-streaming-vs-single-mode"
    resource: "https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode"
    title: "Send messages to a running agent"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude ends every response with a result message. Its `subtype` field reports how the response ended, for example `success` or `error_during_execution`.

# How to use it

- TypeScript: the `for await` loop over `query()` yields all responses' messages in order and ends after the last response's result message, once your generator has returned. To match a result to the messages it answers, set a `uuid` on each message you send and read the result's `user_message_uuids`.
- Python: start a `receive_response()` loop per response; each loop stops after the next `ResultMessage`. The client keeps conversation context from one message to the next.

# Limits and defaults

- TypeScript, last response is an error result: the loop yields that result and then throws, so wrap it in `try`/`catch`. To continue, start a new `query()` that resumes the session. While the generator still has messages to send, an error result for an earlier response does not throw.
- Python: `receive_response()` on `ClaudeSDKClient` yields the error result without raising.

# Notes

What each result subtype means is documented under agent-loop "Handle the result".
