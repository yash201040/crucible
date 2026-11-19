---
type: "Reference"
title: "Response headers and system prompt attribution block"
description: "Response headers a gateway must return for retries and limits, and how the attribution block interacts with prompt caching and CLAUDE_CODE_ATTRIBUTION_HEADER."
resource: "https://code.claude.com/docs/en/llm-gateway-protocol"
tags: [gateway, retries, prompt-caching, headers, rate-limits]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.181"
surfaces: [cli]
requires: ""
identifiers:
  - "content-type"
  - "retry-after"
  - "x-should-retry"
  - "anthropic-ratelimit-unified-*"
  - "CLAUDE_CODE_RETRY_WATCHDOG"
  - "CLAUDE_CODE_ATTRIBUTION_HEADER"
  - "capability_rejected:"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "llm-gateway-protocol"
    resource: "https://code.claude.com/docs/en/llm-gateway-protocol"
    title: "Claude Code gateway compatibility guide"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code reads response headers to detect stalled streams, decide retries and show usage limits. Error bodies should be forwarded unmodified so capability-rejection recovery can match the upstream wording.

# How to use it

| Header | Return |
| - | - |
| `content-type` | `text/event-stream` for Anthropic-format streams; `application/vnd.amazon.eventstream` unmodified for Bedrock-format |
| `retry-after` | Integer seconds, not an HTTP date. Claude Code waits at least that long; outside `CLAUDE_CODE_RETRY_WATCHDOG` sessions a value above 60 stops retries and shows the error |
| `x-should-retry` | Pass upstream value unchanged; `true` retryable, `false` not |
| `anthropic-ratelimit-unified-*` | Forward unchanged on every response; used to show plan usage for claude.ai sign-ins and to tell a plan limit or spend cap from a throttle on `429` |

# Limits and defaults

Attribution block: Claude Code prepends a short block (client version plus fingerprint) as the first system block. `api.anthropic.com` strips it only if the `system` array arrives unchanged with the block first and in its own entry; prepending, reordering, converting to a string or merging defeats this (a merged block drops everything merged into it). If the gateway must reshape system content set `CLAUDE_CODE_ATTRIBUTION_HEADER=0` (a gateway and caching compatibility switch, not a privacy control). On auto mode classifier requests to `api.anthropic.com` (no third-party provider, credential not an Anthropic profile or federation credential) the block is kept even with `0` (exception since v2.1.229). From v2.1.181 the block is stable for a conversation on a custom base URL; earlier versions carry a per-request token, so set `CLAUDE_CODE_ATTRIBUTION_HEADER=0` for a body-keyed gateway cache or a third-party provider upstream.

# Notes

A gateway wrapping errors in its own envelope breaks recovery unless the message carries a `capability_rejected:` token (Claude apps gateway substitutes these, for example `capability_rejected: prompt_too_long`).
