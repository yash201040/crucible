---
type: "Feature"
title: "modelPricing: contracted spend rates"
description: "Managed key that makes cost figures use organization rates, via a multiplier and per-model overrides, affecting /usage, total_cost_usd and --max-budget-usd."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [cost, pricing, managed-settings, budget]
kind: "setting"
maturity: "unlabelled"
since: "2.1.242"
surfaces: [cli, sdk]
requires: "v2.1.242; markup (multiplier above 1) v2.1.271"
identifiers:
  - "modelPricing"
  - "modelPricing.multiplier"
  - "modelPricing.overrides"
  - "--max-budget-usd"
  - "total_cost_usd"
  - "CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Reports spend at the rates your organization pays instead of list price. Claude Code applies it in `/usage`, the status line, the Agent SDK `total_cost_usd`, the `--max-budget-usd` limit, and the OpenTelemetry cost metric and events. You supply the rates; they are not read from a contract or the Console.

# How to use it

Scope `Managed` only: ignored in user, project, local, `--settings`, and in the Windows user-writable HKCU registry. Deploy via server-managed settings, MDM, `managed-settings.json` or a policy helper. Default unset (list price).

| Field | Type | What it does |
| :- | :- | :- |
| `multiplier` | number > 0 and at most 10 | Scales every computed cost, including rows with overrides. Below 1 discount, above 1 markup |
| `overrides` | map model ID to `{input, output, cacheRead, cacheWrite}` | USD per million tokens, each 0 to 10000, all four required; `cacheWrite` covers 5-minute and 1-hour writes |

```json
{ "modelPricing": { "multiplier": 0.85, "overrides": { "claude-sonnet-4-6": { "input": 2.4, "output": 12, "cacheRead": 0.24, "cacheWrite": 3 } } } }
```

# Limits and defaults

- Rows are used exactly as written: no fast-mode surcharge and no US-only-inference rate; `multiplier` applies on top.
- A key that is a built-in model's ID (own, Bedrock, Agent Platform or Foundry ID) applies to every dated and provider ID of that model; any other key (such as a gateway alias) applies to that ID only; an exact match wins. A Bedrock application inference profile gets the row of the model it resolves to via `modelOverrides` or `bedrock:GetInferenceProfile`.
- Unparseable rows or multipliers are dropped, the rest kept. Earlier versions than v2.1.271 ignore a `multiplier` above 1 with a warning.
- With server-managed settings, costs show at list price until the session's settings fetch confirms the key.
- A host app that sets `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` can supply its own table through the SDK `managedSettings` option (used only if no managed source sets the key, v2.1.246+).
