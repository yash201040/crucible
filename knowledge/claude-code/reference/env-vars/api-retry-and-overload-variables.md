---
type: "Reference"
title: "API retry, retry watchdog and overload backoff variables"
description: "Variables that set API retry counts, the unattended retry watchdog for 429 and 529 errors, overload backoff delays and non-streaming retries."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [retries, rate-limits, unattended, resilience]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.186"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_MAX_RETRIES"
  - "CLAUDE_CODE_RETRY_WATCHDOG"
  - "CLAUDE_CODE_RETRY_WATCHDOG_MAX_WAIT_MS"
  - "CLAUDE_CODE_RETRY_WATCHDOG_USAGE_LIMIT_RECHECK_MS"
  - "CLAUDE_CODE_OVERLOADED_RETRY_BASE_DELAY_MS"
  - "CLAUDE_CODE_OVERLOADED_RETRY_MAX_DELAY_MS"
  - "CLAUDE_CODE_NONSTREAMING_TIMEOUT_RETRIES"
  - "CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Resilience controls for failed API requests, central for eval harnesses, CI jobs and remote workers that must survive capacity errors.

# How to use it

| Variable | What it does |
| :- | :- |
| `CLAUDE_CODE_MAX_RETRIES` | Retries for failed API requests (default 10). May stop earlier on `529` (for example with an API key on an Opus model it stops at the third `529` with the "Repeated 529 Overloaded errors" error; with a `fallbackModel` it switches instead). Capped at 15 as of v2.1.186; as of v2.1.199 `CLAUDE_CODE_RETRY_WATCHDOG` raises the default and removes the cap. |
| `CLAUDE_CODE_RETRY_WATCHDOG` | `1` for unattended sessions: retries `429` and `529` capacity errors indefinitely instead of failing after `CLAUDE_CODE_MAX_RETRIES`. Fails at once on a standard-speed `429` reporting a spend limit or exhausted usage credits (before v2.1.239 it retried these indefinitely). Backs off up to 5 minutes, or until a reported reset time, so a usage-limit hit waits out the window. On v2.1.199+ also raises the retry default for other transient errors to 300 (about three hours of backoff) and removes the cap of 15. Requires v2.1.186+. |
| `CLAUDE_CODE_RETRY_WATCHDOG_MAX_WAIT_MS` | Max time each request spends waiting out `429`/`529` with the watchdog on (positive whole number, plain digits, for example `1800000`); unset means no limit. Requires v2.1.295+. |
| `CLAUDE_CODE_RETRY_WATCHDOG_USAGE_LIMIT_RECHECK_MS` | Minimum interval between checks whether a usage limit was already lifted while waiting under the watchdog; whole number from `60000` to `10800000`. Checks occur only for a claude.ai subscription's session or weekly limit while usage credits are not in use, and not with `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` set; outside the range, no checks. Requires v2.1.305+. |
| `CLAUDE_CODE_OVERLOADED_RETRY_BASE_DELAY_MS` | Starting backoff delay for `529` retries (default 500); whole ms from 500 to 32000, plain digits; other values read as unset. Requires v2.1.292+. |
| `CLAUDE_CODE_OVERLOADED_RETRY_MAX_DELAY_MS` | Backoff ceiling for `529` retries (default 32000); whole ms from 32000 to 300000 in plain digits; values above 64000 need v2.1.323+. Requires v2.1.296+. |
| `CLAUDE_CODE_NONSTREAMING_TIMEOUT_RETRIES` | Times a timed-out non-streaming request is re-sent; `0` fails on the first timeout. Requires v2.1.285+. |
| `CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK` | `1` disables the non-streaming fallback when a streaming request fails mid-stream (use when a proxy makes the fallback cause duplicate tool execution). |
