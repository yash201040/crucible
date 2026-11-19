---
type: "Reference"
title: "Raw API request and response body events"
description: "api_request_body and api_response_body events, inline or file mode with index.jsonl, enabled by OTEL_LOG_RAW_API_BODIES."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [events, api-bodies, debugging, privacy]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.274"
surfaces: [cli, headless, sdk]
requires: "Claude Code v2.1.274 or later for request_body_id, message.id and index.jsonl"
identifiers:
  - "OTEL_LOG_RAW_API_BODIES"
  - "claude_code.api_request_body"
  - "claude_code.api_response_body"
  - "body"
  - "body_ref"
  - "body_length"
  - "body_truncated"
  - "request_body_id"
  - "message.id"
  - "index.jsonl"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

With `OTEL_LOG_RAW_API_BODIES` set, one `claude_code.api_request_body` event is emitted per request attempt (retries with adjusted parameters each produce one) and one `claude_code.api_response_body` per successful response. Bodies hold the whole conversation; extended-thinking content is always redacted.

# How to use it

- `=1`: inline `body` (JSON-serialized, truncated at the content limit, 60 KB by default); `body_truncated` is `"true"` when cut.
- `=file:<dir>`: untruncated `<dir>/<uuid>.request.json` and `<dir>/<request_id>.response.json`; events carry `body_ref` (absolute path). Ship the directory with a log collector or sidecar. For each successful response one line is appended to `<dir>/index.jsonl` with `timestamp`, `session_id`, `query_source`, `model`, `request_id`, `message_id`, `message_uuid`, `request_file`, `response_file`.
- `body_length`: UTF-8 bytes in file mode, UTF-16 code units for `=1`.
- Request event also has `model`, `query_source`, `request_body_id`; response event has `model`, `query_source`, `request_id`, `request_body_id` (pairs it to the request), `message.id`, `message.uuid` (links transcript message to bodies).
