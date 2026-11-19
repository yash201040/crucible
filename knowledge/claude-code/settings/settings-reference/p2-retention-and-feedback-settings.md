---
type: "Reference"
title: "Retention, feedback and telemetry-adjacent settings"
description: "Settings for transcript retention, desktop transcript age limit, Claude-drafted feedback, survey rate and WebFetch preflight."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, privacy, retention, feedback]
kind: "setting"
maturity: "unlabelled"
since: "2.1.248"
surfaces: [cli, desktop]
requires: ""
identifiers:
  - "cleanupPeriodDays"
  - "desktopSessionCleanupPeriodDays"
  - "feedbackDrafts"
  - "feedbackSurveyRate"
  - "skipWebFetchPreflight"
  - "DISABLE_TELEMETRY"
  - "DISABLE_ERROR_REPORTING"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "CLAUDE_CODE_SEND_FEEDBACK"
  - "CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY"
  - "SendFeedback"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Privacy-section keys. The switches that turn off usage metrics and error reports are environment variables (`DISABLE_TELEMETRY`, `DISABLE_ERROR_REPORTING`, `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`), set in the `env` key or the shell, not settings keys.

# How to use it

| Name | Scope | Type / default | What it does |
| :- | :- | :- | :- |
| `cleanupPeriodDays` | any file | whole number of days, min `1`; default `30` | Days to keep session transcripts and other app data; background sweep after a session starts deletes silently, so older sessions vanish from the `/resume` picker. Desktop and Cowork session transcripts are kept past it by default (before v2.1.248 they were deleted), though it still applies in some cases such as the HIPAA configuration. `0` fails validation; use for example `3650` for long retention. To stop writing transcripts see Plaintext storage in the claude-directory docs |
| `desktopSessionCleanupPeriodDays` | user or managed, or `--settings`; ignored in project and local. Needs v2.1.248+ | whole number, min `0`; default `0` (no age limit) | Age limit for Desktop and Cowork transcripts; deleted only when older than both this and `cleanupPeriodDays` (a `7` still keeps 30 days at default) |
| `feedbackDrafts` | user or managed; ignored in project and local | `"notify"` (default), `"quiet"`, `"off"` | Claude-drafted feedback. `notify`: card above prompt, by default up to three per session; `quiet`: no card, count in footer, review in `/feedback`; `off`: removes the SendFeedback tool. `CLAUDE_CODE_SEND_FEEDBACK=0` turns it off per session. Managed value beats user setting. `/config`: Claude-drafted feedback |
| `feedbackSurveyRate` | any file | number `0` to `1`; unset uses the remote rate, or built-in `0.005` on Bedrock, Google Cloud's Agent Platform and Foundry | Probability the session quality survey appears; `0` never. Same rate for VS Code. `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY=1` turns it off per session whatever the rate |
| `skipWebFetchPreflight` | any file | Boolean; unset runs the check | `true` skips the WebFetch domain safety check that sends each hostname to `api.anthropic.com` (once per hostname per session, again after a blocked or failed check). Skipping means WebFetch tries any URL without the blocklist, so pair with `WebFetch` permission rules |
