---
type: "Feature"
title: "/compact and /clear in SDK sessions"
description: "Compact or reset conversation history from the SDK by sending /compact or /clear, with a compact_boundary message reporting compaction."
resource: "https://code.claude.com/docs/en/agent-sdk/skills"
tags: [compact, clear, context, sessions]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "/compact"
  - "/clear"
  - "compact_boundary"
  - "compact_metadata.pre_tokens"
  - "compact_metadata.trigger"
  - "continue"
  - "continue_conversation"
  - "resume"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-skills"
    resource: "https://code.claude.com/docs/en/agent-sdk/skills"
    title: "Extend agents with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/compact` summarizes older messages to shrink history while keeping important context. `/clear` resets the conversation to empty context; the previous conversation stays on disk and can be resumed by passing its session ID to the `resume` option.

# How to use it

- `/compact`: send as the prompt in a session with prior turns, for example `query({ prompt: "/compact", options: { continue: true, maxTurns: 1 } })` (Python: `continue_conversation=True`). When compaction runs, a system message with subtype `compact_boundary` arrives; `compact_metadata.pre_tokens` gives the token count before and `compact_metadata.trigger` is e.g. `manual`.
- `/clear`: useful in streaming input mode with many prompts on one connection.

# Limits and defaults

- A fresh one-shot `query()` has empty context, so `/compact` has nothing to do and `/clear` has no practical effect (start a new `query()` instead).
- If nothing can be summarized, the run still ends with a `success` result, no `compact_boundary` message arrives, and the result text carries the reason (e.g. `Not enough messages to compact.`).
