---
type: "Reference"
title: "Event correlation attributes"
description: "prompt.id, event.sequence, message.uuid, request_id and client_request_id link events to prompts, transcripts and API calls."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [events, correlation, transcripts, ordering]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "prompt.id"
  - "event.sequence"
  - "event.timestamp"
  - "message.uuid"
  - "request_id"
  - "client_request_id"
  - "tool_use_id"
  - "x-client-request-id"
  - "x-amzn-requestid"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Keys for tying events together. Filter by one `prompt.id` to get the `user_prompt`, every `api_request` and every `tool_result` for that prompt.

# How to use it

| Attribute | Meaning |
| - | - |
| `prompt.id` | UUID v4 linking all events from processing one user prompt |
| `event.sequence` | 0-based counter per Claude Code process (not per session); keeps counting across `/clear`; when a session is resumed without forking it keeps `session.id` but takes sequence values from the resuming process, so a later event may carry a lower or repeated value. Order by `event.timestamp`, using sequence only to break ties |
| `message.uuid` | UUID of the message in the transcript `~/.claude/projects/*/*.jsonl`; on `assistant_response`, `api_response_body` (v2.1.274+) and `user_prompt` (absent on command dispatches). On responses it is the final transcript entry that the next turn's `parentUuid` chains from |
| `request_id` | Server request ID from the `request-id` header (e.g. `req_011...`); falls back to `x-amzn-requestid` on Amazon Bedrock (v2.1.282+). On `api_request`, `api_error`, `api_refusal`, `assistant_response`, `api_response_body`, `tool_result`, `tool_decision`. Matches the `llm_request` span |
| `client_request_id` | Client UUID sent as `x-client-request-id`; on `api_request`/`api_error` for first-party connections; absent for third-party providers and the non-streaming fallback retry. Survives timeouts that never got a server ID |

# Notes

The transcript entry format is internal and changes between versions; joins on these fields (`message.uuid`, `request_id` stored as `requestId` on assistant entries, `tool_use_id` on `tool_result`, `tool_decision` and `safety_event`) are version-specific, not a stable contract.
