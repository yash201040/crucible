---
type: "Reference"
title: "Model fallback, remap and fast mode variables"
description: "Variables that control automatic model switches, legacy Opus remapping, fast mode availability checks and two removed fast-mode variables."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [fallback, fast-mode, models, bedrock]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_DISABLE_LEGACY_MODEL_REMAP"
  - "CLAUDE_CODE_DISABLE_MODEL_ACCESS_FALLBACK"
  - "CLAUDE_CODE_SKIP_MODEL_ACCESS_MEMORY"
  - "CLAUDE_CODE_DISABLE_REFUSAL_FALLBACK"
  - "CLAUDE_CODE_DISABLE_FAST_MODE"
  - "CLAUDE_CODE_SKIP_FAST_MODE_NETWORK_ERRORS"
  - "CLAUDE_CODE_SKIP_FAST_MODE_ORG_CHECK"
  - "CLAUDE_CODE_ENABLE_OPUS_4_7_FAST_MODE"
  - "CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Switches around which model a request lands on when access or classification changes, and fast mode.

# How to use it

| Variable | What it does |
| :- | :- |
| `CLAUDE_CODE_DISABLE_LEGACY_MODEL_REMAP` | `1` stops auto-remapping Opus 4 and Opus 4.1 to the current Opus on the Anthropic API (the remap does not run on Bedrock, Google Cloud's Agent Platform or Foundry). |
| `CLAUDE_CODE_DISABLE_MODEL_ACCESS_FALLBACK` | `1` stops Bedrock and Google Cloud's Agent Platform sessions switching to an older model when access to the session's model is lost mid-session; the request fails at once. A configured fallback model chain still switches; startup model checks still fall back at launch. Requires v2.1.285+. |
| `CLAUDE_CODE_SKIP_MODEL_ACCESS_MEMORY` | `1` turns off the per-machine memory (up to a day) of models the startup checks found uninvokable on Bedrock and Google Cloud's Agent Platform. Requires v2.1.285+. |
| `CLAUDE_CODE_DISABLE_REFUSAL_FALLBACK` | `1` turns off the automatic model switch when a safety classifier flags a request (what the `switchModelsOnFlag` setting controls). |
| `CLAUDE_CODE_DISABLE_FAST_MODE` | `1` disables fast mode. |
| `CLAUDE_CODE_SKIP_FAST_MODE_NETWORK_ERRORS` | `1` treats a failed fast-mode availability check as available (networks blocking `api.anthropic.com`); a "disabled by your organization" response is still honored. |
| `CLAUDE_CODE_SKIP_FAST_MODE_ORG_CHECK` | `1` skips the client-side availability check (proxies that intercept it); the API still rejects fast mode if the org disabled it. |
| `CLAUDE_CODE_ENABLE_OPUS_4_7_FAST_MODE` | Removed in v2.1.142, when the fast mode default moved from Opus 4.6 to Opus 4.7. |
| `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE` | Removed in v2.1.160, now a no-op; Opus 4.6 no longer supports fast mode. |
