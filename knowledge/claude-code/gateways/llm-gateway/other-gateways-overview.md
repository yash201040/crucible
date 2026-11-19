---
type: "Concept"
title: "Other LLM gateways: what a gateway provides and rollout sequence"
description: "Value of a gateway (credentials, usage, budgets, audit, provider switching) and the four-step rollout for a gateway product the organization already runs."
resource: "https://code.claude.com/docs/en/llm-gateway"
tags: [gateway, rollout, audit, managed-settings]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "ANTHROPIC_BASE_URL"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "llm-gateway"
    resource: "https://code.claude.com/docs/en/llm-gateway"
    title: "Other LLM gateways"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Any gateway exposing a supported API format works. A gateway centralizes: credentials (provider key stays server-side), usage tracking by developer or team, cost controls (budgets, rate limits), audit logging of every model request, and provider switching without touching developer machines.

# How to use it

Rollout sequence, the same for any product:

1. Deploy the gateway with the provider credential.
2. Issue each developer a gateway credential (attribution; offboarding revokes one credential).
3. Distribute configuration through a managed settings file and secrets tooling so each machine gets the base URL and a credential.
4. Have each developer check the configuration in Claude Code.

# Limits and defaults

- Provider switching without reconfiguring clients needs a single Anthropic-format endpoint; a provider-native format ties client config to that provider and changes what Claude Code sends.
- The gateway becomes infrastructure to operate and must be kept updated as Claude Code adds capabilities, or those features break.
- Anthropic does not endorse, maintain or audit third-party gateways and does not support routing to non-Claude models.
