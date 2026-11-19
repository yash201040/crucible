---
type: "Concept"
title: "Gateway credential variables versus claude.ai login"
description: "An active gateway credential variable or apiKeyHelper replaces the subscription login; ANTHROPIC_BASE_URL alone keeps it and needs Authorization and OAuth beta forwarded."
resource: "https://code.claude.com/docs/en/llm-gateway"
tags: [gateway, billing, oauth, subscription]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "ANTHROPIC_BASE_URL"
  - "apiKeyHelper"
  - "anthropic-beta"
  - "Authorization"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "llm-gateway"
    resource: "https://code.claude.com/docs/en/llm-gateway"
    title: "Other LLM gateways"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

While a gateway credential variable or `apiKeyHelper` is active, requests carry that credential instead of the claude.ai login; the subscription limits do not apply. Claude Code keeps the saved login but does not send it. Traffic is billed per token to the owner of the credential the gateway forwards (Console account, or the Bedrock, Agent Platform or Foundry account).

# Limits and defaults

- Setting only `ANTHROPIC_BASE_URL` does not replace the subscription: requests route through the gateway but the saved claude.ai login remains active, with its limits and billing.
- Gateways passing that traffic to Anthropic must forward `Authorization` and the OAuth capability in `anthropic-beta`.
