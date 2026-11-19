---
type: "Concept"
title: "The response above may be incomplete"
description: "Notice when a stream fails after completed output: variants, what Claude Code keeps, and the automatic continue in non-interactive runs and subagents."
resource: "https://code.claude.com/docs/en/errors#the-response-above-may-be-incomplete"
tags: [streaming, partial-output, headless, subagents, continue]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.199"
surfaces: [cli, headless, sdk, cloud]
requires: ""
identifiers:
  - "API Error: Server error mid-response. The response above may be incomplete."
  - "API Error: Connection lost mid-response. The response above may be incomplete."
  - "API Error: The response stopped arriving. The response above may be incomplete."
  - "API Error: Part of the response never arrived. The response above may be incomplete."
  - "API Error: The response stream was malformed. The response above may be incomplete."
  - "API Error: Content block not found"
  - "API Error: Content block already closed"
  - "API Error: Stream event unreadable"
  - "CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK"
  - "--output-format json"
  - "stream-json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A streaming request fails while the response is in progress, after Claude completed a text block or tool call (or started one after thinking). Re-sending could run tool calls twice, so Claude Code keeps the completed output, runs finished tool calls, and appends this notice naming the cause: server error, connection lost, computer asleep, response stopped arriving (idle watchdog), part never arrived (dropped event), or stream malformed (duplicate or damaged event).

# How to use it

- Interactive: read what remains; an interrupted final block is discarded, so reply `continue`.
- Non-interactive `-p`: default text output prints the last completed text block then the message (message alone if no text is held, for example after mid-turn compaction; before v2.1.219 only the message). With `--output-format json` or `stream-json` the message is in the `result` field. To continue, resume the session and send `continue`.
- In non-interactive sessions (`-p`, Agent SDK, cloud sessions), when the cut-off is in the main conversation and has text but no tool calls, Claude Code prompts Claude to continue, up to three times in a row; the notice appears only when those are used up (before v2.1.246 it ended on the first cut-off).
- In a subagent (any session type), a cut-off with text but no tool calls prompts the subagent to continue; the notice becomes its last message only after the continuations are used (before v2.1.257 it showed on the first).
- If a stream event is dropped, duplicated or damaged before any text or tool call: thinking-only responses are re-issued, ending with `Part of the response never arrived and no response was produced. Try again.` or `The response stream was malformed and no response was produced. Try again.`; with nothing completed the request is re-sent non-streaming, unless `CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK` is set, which yields `Content block not found`, `Content block already closed` or `Stream event unreadable`.

# Limits and defaults

Variant names changed in v2.1.227 (previously `Connection closed mid-response`, `Response stalled mid-stream`). `Server error mid-response` needs v2.1.199+; the idle-watchdog variant could wrongly fire on gateway connections before v2.1.222. A failure after the response is finished is not reported.
