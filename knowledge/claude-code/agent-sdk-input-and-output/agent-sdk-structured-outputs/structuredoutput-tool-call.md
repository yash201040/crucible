---
type: "Concept"
title: "The StructuredOutput tool call"
description: "Claude Code adds a StructuredOutput tool to sessions with an output format; the agent calls it to return its answer, possibly several times."
resource: "https://code.claude.com/docs/en/agent-sdk/structured-outputs"
tags: [agent-sdk, structured-output, tool, stream]
kind: "tool"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "StructuredOutput"
  - "tool_use"
  - "tool_result"
  - "tool_use_id"
  - "is_error"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-structured-outputs"
    resource: "https://code.claude.com/docs/en/agent-sdk/structured-outputs"
    title: "Get structured output from agents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When `outputFormat` or `output_format` is set, the message stream carries a tool call named `StructuredOutput` that you never defined. Claude Code adds it, the system init message lists it in the `tools` array, and the agent calls it to return the answer.

# How to use it

Each call arrives as two blocks: a `tool_use` block named `StructuredOutput` whose input is the produced object, and a `tool_result` reading `Structured output provided successfully`. When the object does not match the schema the `tool_result` has `is_error: true` and the agent calls `StructuredOutput` again, so one query can hold several calls.

Read the validated data from `structured_output` on the result message, not from a `tool_use` block. If your application shows or logs tool calls, skip `StructuredOutput` calls; a `tool_result` has no tool name, only `tool_use_id`, so match it against the `id` of each skipped call.
