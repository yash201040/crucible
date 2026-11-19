---
type: "Concept"
title: "Cloud provider cost attribution"
description: "On Bedrock, Google Cloud's Agent Platform and Foundry billing is on the cloud account; per-user attribution via OpenTelemetry or gateways."
resource: "https://code.claude.com/docs/en/costs"
tags: [bedrock, foundry, opentelemetry, gateway, cost-attribution]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, cloud]
requires: "Amazon Bedrock, Google Cloud's Agent Platform or Microsoft Foundry"
identifiers: []
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "costs"
    resource: "https://code.claude.com/docs/en/costs"
    title: "Manage costs effectively"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

On these providers usage is billed per token to your cloud account and spend controls live in the cloud billing console. Claude Code does not send cloud metrics back to Anthropic, so the analytics dashboards and the Claude Code Analytics API do not cover this usage.

# How to use it

Three options for per-user attribution:
- OpenTelemetry: export metrics from each developer machine to your observability stack (per-user tokens, costs, tool activity, any provider).
- A Claude apps gateway: self-hosted; gives per-user usage attribution, OTLP metrics with token counts and per-user spend limits.
- An LLM gateway: proxy that tracks spend per key; LiteLLM was reported by several large enterprises (unaffiliated with Anthropic, not security-audited).
