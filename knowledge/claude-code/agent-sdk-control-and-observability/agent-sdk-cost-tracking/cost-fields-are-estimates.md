---
type: "Limit"
title: "Cost fields are client-side estimates"
description: "total_cost_usd and costUSD are computed locally from a bundled price table and must not drive billing or financial decisions."
resource: "https://code.claude.com/docs/en/agent-sdk/cost-tracking"
tags: [cost, estimates, billing, data-residency]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: "Data residency multiplier: TypeScript Agent SDK v0.3.239+ or Python Agent SDK v0.2.144+"
identifiers:
  - "total_cost_usd"
  - "costUSD"
  - "modelPricing"
  - "inference_geo"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-cost-tracking"
    resource: "https://code.claude.com/docs/en/agent-sdk/cost-tracking"
    title: "Track cost and usage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`total_cost_usd` and `costUSD` are client-side estimates, not authoritative billing. The SDK computes them locally from a price table bundled at build time, unless a `modelPricing` table is in effect.

# Limits and defaults

They can drift from the real bill when pricing changes, when the installed SDK version does not recognize a model, or when billing rules apply that the client cannot model. One rule it does model is data residency pricing: when a response's `usage` reports `inference_geo: "us"`, the list price of that response's tokens is multiplied by 1.1 (per-request fees such as web search are not multiplied). That needs TypeScript Agent SDK v0.3.239+ or Python Agent SDK v0.2.144+.

Use them for development insight and approximate budgeting; for authoritative billing see Manage costs for your organization. Do not bill end users or trigger financial decisions from these fields.
