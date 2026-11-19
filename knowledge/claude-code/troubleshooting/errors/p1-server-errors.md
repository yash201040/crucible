---
type: "Reference"
title: "Server errors: 500, 529, timeouts, no response"
description: "Meaning and recovery for API 5xx, repeated 529 overload, request timeout and no-response-from-API errors, including first-byte deadline rules."
resource: "https://code.claude.com/docs/en/errors#server-errors"
tags: [errors, 529, timeout, overloaded, first-byte]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.242"
surfaces: [cli, desktop, cloud]
requires: ""
identifiers:
  - "API Error: 500 Internal server error"
  - "API Error: Repeated 529 Overloaded errors"
  - "Request timed out"
  - "API Error: No response from API"
  - "API_TIMEOUT_MS"
  - "CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS"
  - "ENABLE_TOOL_SEARCH"
  - "ANTHROPIC_BASE_URL"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors from the inference provider (Anthropic, or Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry or a custom gateway). The trailing sentence names the matching status page, or the gateway host for a custom `ANTHROPIC_BASE_URL`.

# How to use it

- **500 / any 5xx**: unexpected API failure, not caused by prompt, settings or account. HTML error pages from proxies show status code plus page title (before v2.1.281 the code was dropped or raw markup printed). Wait, then resend (type `try again`); run `/feedback` if it persists. If requests go through a gateway and all fail, check it accepts tool search fields: by default Claude Code sends `defer_loading` tool fields and `tool_reference` blocks with the `anthropic-beta` header; before v2.1.304 tool search was off behind a gateway unless `ENABLE_TOOL_SEARCH` was set.
- **Repeated 529 Overloaded**: API at capacity for all users; does not count against quota. Switch model with `/model` (capacity is tracked per model); Claude Code prompts for this, for example `Opus is experiencing high load, please use /model to switch to Sonnet` (Fable models name Fable; the Desktop app says `Switch to Sonnet.` and uses the model picker).
- **Request timed out**: default request timeout is 10 minutes. `API_TIMEOUT_MS=0` turns that off, but the first-byte deadline and body idle timeout stay, and a non-streaming attempt keeps 300 seconds locally. On a version before v2.1.305 with `API_TIMEOUT_MS=0` every request may fail; update or set a positive value.
- **No response from API**: streaming request got no headers by the first-byte deadline; Claude Code aborts and re-sends, and ends the turn if the re-send also hits the deadline (unless `CLAUDE_CODE_RETRY_WATCHDOG`). First attempt wait: `CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS` (1 or more, clamped to 10 seconds to 30 minutes) else the byte-level watchdog timeout, plus one second per 32KB of request body. Retry wait: one second less than `API_TIMEOUT_MS` (just under 10 minutes by default); on Bedrock the retry uses the first attempt's deadline. If `API_TIMEOUT_MS` is `0` (non-Bedrock) the retry waits 10 minutes plus one second per 32KB. No wait exceeds one second less than a positive `API_TIMEOUT_MS`; a positive `API_TIMEOUT_MS` under 11 seconds turns the deadline off.

# Limits and defaults

Version notes: before v2.1.242 an unanswered streaming request waited the full `API_TIMEOUT_MS`; before v2.1.261 the retry used the same deadline and the message showed no durations; before v2.1.307 `CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS` was ignored in a Claude apps gateway session, where the deadline runs only if that variable is 1 or more.
