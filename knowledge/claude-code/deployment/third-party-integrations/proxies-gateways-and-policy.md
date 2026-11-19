---
type: "Guide"
title: "Proxies, gateways, pinning and provider allowlist"
description: "Corporate proxy versus LLM gateway variables, CMEK telemetry caveat, model pinning advice, and the allowedProviders managed setting."
resource: "https://code.claude.com/docs/en/third-party-integrations"
tags: [proxy, llm-gateway, managed-settings, providers]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [cli]
requires: "allowedProviders needs Claude Code v2.1.285 or later"
identifiers:
  - "HTTPS_PROXY"
  - "HTTP_PROXY"
  - "ANTHROPIC_BASE_URL"
  - "ANTHROPIC_BEDROCK_BASE_URL"
  - "ANTHROPIC_AWS_BASE_URL"
  - "ANTHROPIC_VERTEX_BASE_URL"
  - "ANTHROPIC_FOUNDRY_BASE_URL"
  - "ANTHROPIC_DEFAULT_FABLE_MODEL"
  - "ANTHROPIC_DEFAULT_OPUS_MODEL"
  - "ANTHROPIC_DEFAULT_SONNET_MODEL"
  - "ANTHROPIC_DEFAULT_HAIKU_MODEL"
  - "DISABLE_TELEMETRY"
  - "allowedProviders"
  - "/status"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "third-party-integrations"
    resource: "https://code.claude.com/docs/en/third-party-integrations"
    title: "Enterprise deployment overview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two separate, combinable configurations: a corporate proxy (HTTP/HTTPS egress via `HTTPS_PROXY` or `HTTP_PROXY`) and an LLM gateway (a service between Claude Code and the provider for centralized usage tracking, rate limits or budgets, and auth), configured with `ANTHROPIC_BASE_URL`, `ANTHROPIC_BEDROCK_BASE_URL`, `ANTHROPIC_AWS_BASE_URL`, `ANTHROPIC_VERTEX_BASE_URL` or `ANTHROPIC_FOUNDRY_BASE_URL`.

# How to use it

- Run `/status` to see which provider, base URL and proxy a session uses.
- Pin versions on cloud providers with `ANTHROPIC_DEFAULT_FABLE_MODEL`, `ANTHROPIC_DEFAULT_OPUS_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, `ANTHROPIC_DEFAULT_HAIKU_MODEL` so aliases do not move to newer or not-yet-enabled defaults.
- Limit which providers a managed machine may use with the `allowedProviders` managed setting, e.g. `["bedrock"]` for Bedrock only; add `"mantle"` for a Bedrock fleet that also enables Mantle; the setting's entry says which endpoint variables also need a managed `env` pin. With Desktop signed in to claude.ai, a Cowork session counts as `"anthropic"`; leaving it out of an MDM or managed list refuses that session.
- Managed permissions that local config cannot override; shared `.mcp.json` checked in for MCP integrations; CLAUDE.md at multiple levels, including an organization-wide one.

# Limits and defaults

With customer-managed encryption keys (CMEK) and an LLM gateway or custom `ANTHROPIC_BASE_URL`, CMEK does not cover Claude Code's operational telemetry on those sessions; deliver `DISABLE_TELEMETRY` through managed settings to turn it off for everyone.
