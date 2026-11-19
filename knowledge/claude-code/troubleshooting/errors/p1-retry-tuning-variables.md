---
type: "Reference"
title: "Retry and timeout tuning environment variables"
description: "Environment variables that set retry counts, the unattended retry watchdog, 529 backoff, request timeouts and first-byte deadlines."
resource: "https://code.claude.com/docs/en/errors#tune-retry-behavior"
tags: [retries, timeouts, env-vars, ci, watchdog]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.199"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "CLAUDE_CODE_MAX_RETRIES"
  - "CLAUDE_CODE_RETRY_WATCHDOG"
  - "CLAUDE_CODE_RETRY_WATCHDOG_MAX_WAIT_MS"
  - "CLAUDE_CODE_RETRY_WATCHDOG_MAX_USAGE_LIMIT_WAIT_MS"
  - "CLAUDE_CODE_RETRY_WATCHDOG_USAGE_LIMIT_RECHECK_MS"
  - "CLAUDE_CODE_OVERLOADED_RETRY_BASE_DELAY_MS"
  - "CLAUDE_CODE_OVERLOADED_RETRY_MAX_DELAY_MS"
  - "API_TIMEOUT_MS"
  - "CLAUDE_CODE_NONSTREAMING_TIMEOUT_RETRIES"
  - "CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Variables that tune how long and how often Claude Code retries API failures. Set `CLAUDE_CODE_RETRY_WATCHDOG=1` for unattended runs such as CI.

# How to use it

| Variable | Default | Effect |
| :- | :- | :- |
| `CLAUDE_CODE_MAX_RETRIES` | 10 | Number of retries. Capped at 15 as of v2.1.186; the watchdog (v2.1.199+) removes the cap. Lower it so scripts fail faster. |
| `CLAUDE_CODE_RETRY_WATCHDOG` | unset | Set `1` to retry 429 and 529 capacity errors indefinitely. Still fails at once on a standard-speed 429 reporting a spend limit or exhausted usage credits (before v2.1.239 it retried those forever). From v2.1.199 it also raises the default retry count for other transient errors to 300 (about three hours of backoff). Fast mode: see the fast mode docs. |
| `CLAUDE_CODE_RETRY_WATCHDOG_MAX_WAIT_MS` | unset (no limit) | Max ms each request waits out 429 and 529 under the watchdog. Needs v2.1.295+. |
| `CLAUDE_CODE_RETRY_WATCHDOG_MAX_USAGE_LIMIT_WAIT_MS` | no cap | Longest ms one request waits for a plan usage limit to reset; if the reset is further away it fails at once unless usage credits have room or could not be checked. Needs v2.1.301+. |
| `CLAUDE_CODE_RETRY_WATCHDOG_USAGE_LIMIT_RECHECK_MS` | unset | Minimum ms between checks whether a usage limit was lifted while waiting; digits `60000` to `10800000`, otherwise no checks. Needs v2.1.305+. |
| `CLAUDE_CODE_OVERLOADED_RETRY_BASE_DELAY_MS` | 500 | Starting backoff delay for 529 retries; raise up to 32000. No effect with the watchdog set to `1` or for fast mode requests. Needs v2.1.292+. |
| `CLAUDE_CODE_OVERLOADED_RETRY_MAX_DELAY_MS` | 32000 | Ceiling for 529 backoff; raise up to 300000 (values above 64000 need v2.1.323+). Needs v2.1.296+. |
| `API_TIMEOUT_MS` | 600000 | Time each attempt has to receive response headers; does not limit a streaming response afterward. |
| `CLAUDE_CODE_NONSTREAMING_TIMEOUT_RETRIES` | unset | Limit on re-sends of a timed-out non-streaming request; `0` fails sooner. Needs v2.1.285+. |
| `CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS` | unset | Deadline for the first byte of a streaming response. Needs v2.1.242+. |

# Limits and defaults

A non-streaming attempt ends at the earlier of its request timeout (`API_TIMEOUT_MS` if positive, else 300 seconds locally) and the body idle timeout (by default 5 to 6 minutes, however high `API_TIMEOUT_MS` is).
