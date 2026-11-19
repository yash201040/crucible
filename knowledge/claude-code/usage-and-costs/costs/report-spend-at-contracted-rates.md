---
type: "Guide"
title: "Report spend at contracted rates"
description: "Set the modelPricing managed setting so cost figures in /usage, the status line and OpenTelemetry match contracted rates."
resource: "https://code.claude.com/docs/en/costs"
tags: [modelpricing, managed-settings, cost, contracted-rates, multiplier]
kind: "setting"
maturity: "unlabelled"
since: "2.1.242"
surfaces: [cli]
requires: "Claude Code v2.1.242 or later; markup (multiplier above 1) needs v2.1.271 or later; managed settings"
identifiers:
  - "modelPricing"
  - "multiplier"
  - "overrides"
  - "managed-settings.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "costs"
    resource: "https://code.claude.com/docs/en/costs"
    title: "Manage costs effectively"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

By default every cost figure is computed at list price, so /usage, the status line and OpenTelemetry may differ from a contracted-rate bill. The `modelPricing` managed setting changes what Claude Code reports, not what Anthropic charges.

# How to use it

1. Take per-million-token rates from your contract. Claude Code does not fetch them from the Console; update when the contract changes.
2. Write the setting: `multiplier` below 1 is a flat discount, above 1 a markup; `overrides` lists each model's four per-token rates; or use both.
3. Deliver as managed settings: server-managed settings, an MDM policy, `managed-settings.json`, or a policy helper program.

Verify by running `/usage` in a session that has received the managed settings: `Total cost` carries `at your organization's configured rates`.

# Limits and defaults

- Ignored in user, project and local settings and in `--settings`.
- Figures remain estimates, not an invoice. The `/model` picker prices stay at list price.
