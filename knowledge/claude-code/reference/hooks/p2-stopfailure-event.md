---
type: "Reference"
title: "StopFailure hook event and error types"
description: "Runs instead of Stop when a turn ends on an API error; input error values for matching and logging."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, stopfailure, errors, rate-limits]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "StopFailure"
  - "rate_limit"
  - "authentication_failed"
  - "oauth_org_not_allowed"
  - "account_on_hold"
  - "billing_error"
  - "invalid_request"
  - "model_not_found"
  - "server_error"
  - "max_output_tokens"
  - "cloud_credential_error"
  - "unknown"
  - "error_details"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs instead of Stop when the turn ends due to an API error. Output and exit code are ignored (except `terminalSequence`); no decision control. Use to log failures, send alerts or take recovery actions on rate limits, authentication problems and other API errors.

# How to use it

Input adds `error` (also used for matcher filtering), optional `error_details` (e.g. `"429 Too Many Requests"`), optional `last_assistant_message` (here the rendered API error string, such as `"API Error: Rate limit reached"`, not conversational output).

| `error` value | Note |
| :- | :- |
| `rate_limit` | |
| `authentication_failed` | |
| `oauth_org_not_allowed` | |
| `account_on_hold` | |
| `billing_error` | |
| `invalid_request` | |
| `model_not_found` | |
| `server_error` | Also the value for an HTTP 529 overloaded response |
| `max_output_tokens` | |
| `cloud_credential_error` | |
| `unknown` | |
