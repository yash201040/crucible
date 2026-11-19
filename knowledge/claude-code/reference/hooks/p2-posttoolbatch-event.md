---
type: "Feature"
title: "PostToolBatch hook event"
description: "Fires once after every tool call in a parallel batch resolves, before the next model request."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, posttoolbatch, parallel-tools, context]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "PostToolBatch"
  - "tool_calls"
  - "additionalContext"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs exactly once after all tool calls in a batch resolve, before the next request to the model. `PostToolUse` fires per tool (concurrently for parallel calls); PostToolBatch suits context that depends on the whole set. No matcher.

# How to use it

Input adds `tool_calls`: array of `{tool_name, tool_input, tool_use_id, tool_response}`. Here `tool_response` is the serialized `tool_result` content the model sees (string or content-block array; for `Read`, line-number-prefixed text), unlike PostToolUse's structured Output object. Responses can be large; parse only needed fields.

Output: `hookSpecificOutput.additionalContext` injected once before the next model call.

# Limits and defaults

`decision: "block"` or `continue: false` stops the agentic loop before the next model call; the message comes from `reason`/`stopReason` or stderr on exit 2, shows as a transcript warning and stays in the conversation.
