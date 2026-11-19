---
type: "Reference"
title: "Streaming input errors and image blocks"
description: "Abort errors, the silent Python prompt-stream failure, and the note Claude gets for an image block with no source."
resource: "https://code.claude.com/docs/en/agent-sdk/troubleshooting"
tags: [streaming-input, abort, errors, images]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "Operation aborted"
  - "Claude Code process aborted by user"
  - "AbortError"
  - "abortController"
  - "Prompt stream failed; closing stdin"
  - "[Image could not be processed: image block has no source object]"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-troubleshooting"
    resource: "https://code.claude.com/docs/en/agent-sdk/troubleshooting"
    title: "Troubleshoot the Agent SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Failures tied to the async generator you pass as streaming input.

# How to use it

- TypeScript: the `for await` loop throws an `AbortError` with `Operation aborted` or `Claude Code process aborted by user`. Causes: your code called `abort()` on the `abortController` you passed, or your async generator threw (its own message is not included; wrap the generator body in try/catch, log, rethrow).
- Python: if the async generator passed to `query()` raises, the `async for` loop ends with no exception. The SDK logs `Prompt stream failed; closing stdin: <message>` at ERROR level (stderr if logging is unconfigured). Wrap the generator body in try/except to see the traceback.
- An image block without a `source` object raises no error: Claude receives the note `[Image could not be processed: image block has no source object]` and answers without the image.
