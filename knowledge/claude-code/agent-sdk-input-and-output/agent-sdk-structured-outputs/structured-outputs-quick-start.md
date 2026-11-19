---
type: "Feature"
title: "Structured outputs quick start"
description: "Pass a JSON Schema via outputFormat (TS) or output_format (Python) and read validated JSON from structured_output on the result message."
resource: "https://code.claude.com/docs/en/agent-sdk/structured-outputs"
tags: [agent-sdk, structured-output, json-schema, validation]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "outputFormat"
  - "output_format"
  - "structured_output"
  - "json_schema"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-structured-outputs"
    resource: "https://code.claude.com/docs/en/agent-sdk/structured-outputs"
    title: "Get structured output from agents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Structured outputs return validated JSON matching a schema you define, after the agent has used whatever tools it needs across multiple turns. The SDK validates the output against the schema and re-prompts on mismatch; if validation does not succeed within the retry limit, the result is an error instead of data.

# How to use it

Pass `outputFormat` (TypeScript option) or `output_format` (Python `ClaudeAgentOptions`) with `type: "json_schema"` and a `schema`. When the agent finishes, the result message carries a `structured_output` field.

```
options: { outputFormat: { type: "json_schema", schema } }
```

Check `message.type === "result" && message.subtype === "success" && !message.is_error && message.structured_output` before using the value. Python: `isinstance(message, ResultMessage) and not message.is_error and message.structured_output`. A single-shot `query()` throws (TS) or raises (Python) after yielding an error result, so wrap it in try/catch.

# Notes

Without it, agents return free-form text. The page's examples include a company-info schema and a TODO-tracking agent that uses Grep and Bash across several turns, with optional fields (`author`, `date`) for data that may be missing.
