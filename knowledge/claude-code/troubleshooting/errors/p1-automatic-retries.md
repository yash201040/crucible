---
type: "Concept"
title: "Automatic retries: what is and is not retried"
description: "Claude Code retries transient API failures up to 10 times with backoff; rules for server errors, dropped connections, stalls, 429s and what is never retried."
resource: "https://code.claude.com/docs/en/errors#automatic-retries"
tags: [retries, backoff, errors, resilience, unattended]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.199"
surfaces: [cli, desktop, cloud]
requires: ""
identifiers:
  - "CLAUDE_CODE_MAX_RETRIES"
  - "CLAUDE_CODE_RETRY_WATCHDOG"
  - "CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK"
  - "Retrying in Ns · attempt x/y"
  - "Waiting for API response · will retry in"
  - "The response stalled before a response was produced"
  - "Connection lost while your computer was asleep"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code retries transient failures up to 10 times with exponential backoff before showing an error. It does not always retry a failure that arrives partway through a response. Any error shown on the page has already had whatever retries apply.

# How to use it

Retried:
- Server errors, overloaded responses and timeouts before any response has streamed. After thinking finished but before any text or tool call, a server error is retried up to two times (before v2.1.284 the turn ended).
- Dropped connections before Claude completed any part of the response; after thinking but before text or tool call, up to two quick re-issues, then the turn ends with `Connection lost before a response was produced`. Computer sleep counts as a drop.
- Stalled streams (headers arrived but no content, or thinking done but nothing started): abort and restream at most once, then `The response stalled before a response was produced`.
- Streaming request with no response headers at the first-byte deadline: abort and re-send; if the re-send also hits the deadline the turn ends with "No response from API". `CLAUDE_CODE_RETRY_WATCHDOG` keeps re-sending within the budget.
- API output content-filter stop before thinking finished or any text or tool call: re-sent once.
- Temporary 429 throttles (not a gateway spend-limit 429). With a claude.ai subscription this includes throttles without plan quota headers (before v2.1.199 only API key and Enterprise sign-ins retried these).
- Input plus `max_tokens` over the context limit: retried with a reduced `max_tokens`, else it compacts instead (before v2.1.218 a still-too-large request could be re-sent until the budget ran out).
- A response announcing a tool call but containing none: up to two retries, then `The model's tool call could not be parsed (retry also failed).` (one retry before v2.1.307).
- Expired or missing Google Cloud credentials or AWS credentials that fail to load: cache discarded, up to two retries (before v2.1.228 the full budget).
- 401 or 403 while an `apiKeyHelper` script supplies the credential: script re-run and retried in the full budget.

Not retried:
- TLS certificate validation failures (before v2.1.199 they were retried).
- A failure after Claude completed a text block or tool call but before the response finished: the completed output is kept, finished tool calls run, and the turn continues (re-running could execute tool calls twice). Before v2.1.199 the partial output was discarded.
- A failure after the response is finished: kept, turn ends normally.
- Amazon Bedrock streaming response with an unexpected content-type (requires v2.1.208 or later).
- A non-streaming retry that gets success status but no API message body.
- A request denied by an organization policy check (Inference hooks, a Claude Enterprise feature); not re-sent to the same or a fallback model (before v2.1.239 it could be re-sent).

While retrying the spinner shows `Retrying in Ns · attempt x/y`; the reason label becomes specific from the third attempt as of v2.1.198 (earlier, only on the final attempt) and the spinner tip is suppressed. A `Waiting for API response · will retry in … · check your network` banner appears after 20 seconds without data (10 before v2.1.185), or 45 seconds (20 before v2.1.309) on `ANTHROPIC_BASE_URL` gateways, Claude apps gateway sessions and Claude Platform on AWS with `ANTHROPIC_AWS_BASE_URL`.

# Notes

Tuning variables are in [Retry tuning variables](./p1-retry-tuning-variables.md).
