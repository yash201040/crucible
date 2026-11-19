---
type: "Reference"
title: "Telemetry, error reporting and defaults by API provider"
description: "What metrics and error reports Claude Code sends, opt-out variables, and the default on/off table per provider."
resource: "https://code.claude.com/docs/en/data-usage"
tags: [telemetry, error-reporting, providers, privacy, env-vars]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.198"
surfaces: [cli]
requires: ""
identifiers:
  - "DISABLE_TELEMETRY"
  - "DISABLE_ERROR_REPORTING"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "CLAUDE_CODE_USE_VERTEX"
  - "CLAUDE_CODE_USE_BEDROCK"
  - "CLAUDE_CODE_USE_FOUNDRY"
  - "CLAUDE_CODE_USE_ANTHROPIC_AWS"
  - "CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST"
  - "CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL"
  - "skipWebFetchPreflight"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "data-usage"
    resource: "https://code.claude.com/docs/en/data-usage"
    title: "Data usage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two operational streams: metrics (latency, reliability, usage patterns; never code, prompts or file paths; sent to Anthropic and third-party logging) and error reports (messages and stack traces from Claude Code's internals, to a third-party error tracker, with secrets, paths and emails redacted). Local Claude Code sends prompts and model outputs over TLS 1.2+.

# How to use it

| Service | Claude API | Agent Platform / Bedrock / Foundry / Claude Platform on AWS |
| - | - | - |
| Metrics | On; `DISABLE_TELEMETRY=1` | Off (the matching `CLAUDE_CODE_USE_VERTEX`, `CLAUDE_CODE_USE_BEDROCK`, `CLAUDE_CODE_USE_FOUNDRY` or `CLAUDE_CODE_USE_ANTHROPIC_AWS` must be 1) |
| Error reports | On for Pro, Max, Ultra sign-ins on v2.1.198+; `DISABLE_ERROR_REPORTING=1` | Off |
| `/feedback` reports | On; `DISABLE_FEEDBACK_COMMAND=1` | Off |
| Session quality surveys | On; `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY=1` | On (all providers) |
| WebFetch domain safety check | On; `skipWebFetchPreflight: true` | On (all providers) |

# Limits and defaults

- Error reporting is on only when: Pro, Max or Ultra sign-in, v2.1.198 or later, direct connection to the Claude API, and no ZDR or HIPAA agreement.
- `DISABLE_TELEMETRY` or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` also disables feature-flag evaluation, which can make Remote Control unavailable; `DISABLE_ERROR_REPORTING` does not.
- `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` covers all non-essential traffic including surveys but not the WebFetch check or official plugin marketplace auto-install (use `skipWebFetchPreflight` and `CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL`).
- Signed-in Claude apps gateway sessions: usage analytics, error reporting and survey ratings to Anthropic are disabled by the gateway credential, with no way to re-enable.
- With `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST`, metrics default on for the four cloud providers and follow `DISABLE_TELEMETRY`; error reporting and `/feedback` stay off.
