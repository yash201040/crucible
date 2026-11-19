---
type: "Reference"
title: "Output formats, JSON schema and streaming"
description: "--output-format text/json/stream-json, --json-schema structured_output, and partial-message streaming."
resource: "https://code.claude.com/docs/en/headless"
tags: [headless, output-format, json-schema, streaming]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [headless, sdk]
requires: ""
identifiers:
  - "--output-format"
  - "text"
  - "json"
  - "stream-json"
  - "--json-schema"
  - "structured_output"
  - "--verbose"
  - "--include-partial-messages"
  - "result"
  - "session_id"
  - "total_cost_usd"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "headless"
    resource: "https://code.claude.com/docs/en/headless"
    title: "Run Claude Code programmatically"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`--output-format` controls the response form.

# How to use it

| Value | Output |
| --- | --- |
| `text` (default) | Plain text |
| `json` | Structured JSON with `result`, session ID and metadata |
| `stream-json` | Newline-delimited JSON for real-time streaming |

- `--output-format json --json-schema '<schema>'` returns the schema-conforming value in `structured_output`, alongside metadata (session ID, usage).
- An invalid schema exits with `Error: --json-schema is not a valid JSON Schema` and the validator diagnostic. The `format` keyword (e.g. `"format": "email"`) is accepted but treated as an annotation, not enforced.
- If a run ends without valid structured output (e.g. Claude declined), there is no `structured_output` field: check it exists before use.
- Streaming tokens: `claude -p "..." --output-format stream-json --verbose --include-partial-messages`. Each line is a JSON event; the last line is a `result` message with the final text, cost and session metadata. Filter text deltas with jq (`select(.type == "stream_event" and .event.delta.type? == "text_delta")`).

# Limits and defaults

If the consumer reads slowly, Claude Code waits for queued output to drain before exiting, scaled by queue size and capped at 30 seconds.
