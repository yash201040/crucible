---
type: "Reference"
title: "Telemetry, nonessential traffic, feedback and feature-flag opt-outs"
description: "Variables that opt out of telemetry, error reporting, surveys, feedback commands and feature-flag fetching, including the presence-only semantics."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [telemetry, privacy, feedback, feature-flags]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "DISABLE_TELEMETRY"
  - "DO_NOT_TRACK"
  - "DISABLE_ERROR_REPORTING"
  - "CLAUDE_CODE_DISABLE_FEATURE_FLAGS"
  - "DISABLE_GROWTHBOOK"
  - "CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY"
  - "CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL"
  - "CLAUDE_CODE_SEND_FEEDBACK"
  - "CLAUDE_CODE_ENABLE_SHARE_BUNDLE"
  - "DISABLE_FEEDBACK_COMMAND"
  - "DISABLE_BUG_COMMAND"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Switches that cut outbound traffic. Several of them also turn off feature-flag fetching, which disables features listed in [features that need feature-flag fetching](./features-that-need-feature-flags.md).

# How to use it

| Variable | What it does |
| :- | :- |
| `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` | Any non-empty value (even `0` or `false`) disables auto-updates, telemetry, error reporting, `/feedback`, Claude-drafted feedback, release notes, PR and MR status badge checks and availability checks such as the fast mode check. Unset to allow again. Also stops background runs of plugin `command` sources (local commands that can trigger dependency installs), disables feature-flag fetching, and turns artifacts off. Does not cover official marketplace auto-install (use `CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL`) or gateway model discovery (own opt-in). |
| `DISABLE_TELEMETRY` | Any non-empty value (even `0` or `false`) opts out of telemetry; telemetry events carry no code, file paths or Bash commands. Also disables feature-flag fetching. |
| `DO_NOT_TRACK` | `1` opts out of telemetry like `DISABLE_TELEMETRY`, including feature-flag fetching. Read as a standard boolean, so `0` leaves telemetry on. |
| `DISABLE_ERROR_REPORTING` | Any non-empty value (even `0` or `false`) opts out of error reporting; unset to turn back on. |
| `CLAUDE_CODE_DISABLE_FEATURE_FLAGS` | `1` turns off feature-flag fetching; Remote Control and other flag features become unavailable. Telemetry event logging stays on unless `DISABLE_TELEMETRY` is also set. Requires v2.1.319+. |
| `DISABLE_GROWTHBOOK` | `1`, older name of the same switch (requires v2.1.124+; the only name v2.1.124 through v2.1.318 read). Use the new name unless a machine on v2.1.318 or earlier reads the config. |
| `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY` | `1` disables the "How is Claude doing?" surveys. Surveys are also off with `DISABLE_TELEMETRY`, `DO_NOT_TRACK` or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, unless the OTEL variable opts back in. Use the `feedbackSurveyRate` setting for a sample rate. |
| `CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL` | `1` routes survey ratings only to your own OpenTelemetry collector as events (nothing to Anthropic) when Anthropic-bound traffic is blocked by the three variables above; no effect otherwise. `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY` and the organization feedback policy take precedence. |
| `CLAUDE_CODE_SEND_FEEDBACK` | `0` turns off Claude-drafted feedback for a session; `1` turns it on where the account already has access (cannot grant access; `DISABLE_FEEDBACK_COMMAND` and the `feedbackDrafts` setting `off` value still apply). |
| `CLAUDE_CODE_ENABLE_SHARE_BUNDLE` | `1` makes `/share` save the report and full session transcript to a local archive under `~/.claude/feedback-bundles/` instead of sending the report. Cannot re-enable `/share` if organization policy disabled it. Requires v2.1.299+. |
| `DISABLE_FEEDBACK_COMMAND` | `1` disables `/feedback` and Claude-drafted feedback, and also `/bug` and `/share` (before v2.1.212 they were aliases, so every name was disabled). |
| `DISABLE_BUG_COMMAND` | Older accepted name of `DISABLE_FEEDBACK_COMMAND`. |
