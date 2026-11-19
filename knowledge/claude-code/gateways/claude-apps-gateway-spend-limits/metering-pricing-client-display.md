---
type: "Concept"
title: "Gateway spend metering, pricing and client display"
description: "How the gateway prices requests for caps, bills aborted streams, long-prompt rates, and which Claude Code versions show usage warnings."
resource: "https://code.claude.com/docs/en/claude-apps-gateway-spend-limits"
tags: [gateway, spend-limits, metering, pricing, usage]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "pricing.overrides"
  - "pricing.multiplier"
  - "/usage"
  - "rate_limits.spend_limit"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "principal_emails"
  - "spend"
  - "spend_limits"
  - "admin_audit"
  - "admin.spend_retention_months"
  - "admin.audit_retention_days"
  - "admin.identity_retention_days"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-apps-gateway-spend-limits"
    resource: "https://code.claude.com/docs/en/claude-apps-gateway-spend-limits"
    title: "Claude apps gateway spend limits"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

After each response a usage meter reads token counts and adds cost to daily, weekly and monthly counters without touching the bytes sent to the client. Amounts are USD estimates (a circuit breaker, not an invoice); reconcile billing with the provider.

# How to use it

Rate selection order: (1) matching `pricing.overrides` row for the serving upstream (v2.1.227 or later); (2) list price for the upstream model ID if Claude Code's cost table recognizes it (Anthropic, Bedrock, Google Cloud Agent Platform, Foundry forms); (3) list price of the `models[].id` mapped to that upstream ID, for ARNs or deployment names (v2.1.218 or later); (4) unknown-model tier of 5 USD input and 25 USD output per million tokens, with a boot warning and a once-per-ID runtime warning. The result is multiplied by `pricing.multiplier` (default 1).

Client aborts are billed: when a stream ends without the final usage frame, the meter bills a floor of about four characters per output token for text already sent.

Long prompts: Claude Haiku 5.5 has a higher rate above a token threshold; a gateway on v2.1.293 or later prices the whole request at that rate (input, cache read and cache write tokens count); an override row applies at any length.

Client display requirements:

| Display | Developer machine | Gateway |
| - | - | - |
| Usage warnings at 75% and 95% | v2.1.225 | v2.1.225 |
| Spend limit bar in `/usage`, `rate_limits.spend_limit` in status line | v2.1.251 | v2.1.225 |
| Dollar amounts in the bar and status line | v2.1.284 | v2.1.284 |
| Spend (UTC) in `/usage` when no cap applies (needs `admin:`) | v2.1.319 | v2.1.319 |

# Limits and defaults

Warnings and percentages come from `anthropic-ratelimit-unified-*` headers added to successful `/v1/messages` responses for developers with a cap; the gateway strips the provider's own rate-limit headers. The dollar-amount request is sent even with `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` from v2.1.295 (earlier it was skipped).

Data lifecycle tables: `spend` (13 months), `spend_limits` (until deleted), `admin_audit` (365 days), `principal_emails` (PII, 90 days since last activity); hourly sweep. To offboard, delete per-user caps via the API; to erase immediately run `DELETE FROM principal_emails WHERE principal = '<sub>'`.
