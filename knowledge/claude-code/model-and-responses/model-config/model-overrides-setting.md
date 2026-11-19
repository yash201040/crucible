---
type: "Feature"
title: "modelOverrides setting"
description: "Map Anthropic model IDs to provider-specific IDs such as Bedrock ARNs, with precedence and managed-source rules."
resource: "https://code.claude.com/docs/en/model-config#override-model-ids-per-version"
tags: [model, overrides, bedrock, governance, managed-settings]
kind: "setting"
maturity: "unlabelled"
since: "2.1.200"
surfaces: [cli]
requires: "Managed-source restriction needs v2.1.200+"
identifiers:
  - "modelOverrides"
  - "CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST"
  - "availableModels"
  - "enforceAvailableModels"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`modelOverrides` maps individual Anthropic model IDs to the provider strings Claude Code sends (Bedrock inference profile ARNs, Agent Platform version names, Foundry deployment names), for governance, cost allocation or regional routing. Use it instead of the family-level env vars when several versions of one family need distinct provider IDs.

# How to use it

```json
{
  "modelOverrides": {
    "claude-opus-4-7": "arn:aws:bedrock:us-east-2:123456789012:application-inference-profile/opus-prod",
    "claude-opus-4-6": "arn:aws:bedrock:us-east-2:123456789012:application-inference-profile/opus-46-prod",
    "claude-sonnet-4-6": "arn:aws:bedrock:us-east-2:123456789012:application-inference-profile/sonnet-prod"
  }
}
```

Keys must be Anthropic model IDs from the Models overview (dated IDs with the date suffix); unknown keys are ignored. Values already provider-native pass through as-is. Adding an entry whose value is a gateway alias stops the `[claude-code:unrecognized_model]` diagnostic.

# Limits and defaults

- Overrides replace built-in IDs backing picker entries; on Bedrock they beat auto-discovered inference profiles.
- They also apply to an Anthropic ID passed via `--model`, `ANTHROPIC_MODEL` or `ANTHROPIC_DEFAULT_*_MODEL` (before v2.1.200 these went as-is). On Bedrock, Agent Platform and Mantle an Anthropic ID with no entry resolves like the picker row, when the provider supports it; Mantle supports a subset, otherwise the raw ID is sent.
- The allowlist evaluates against the Anthropic ID, not the override value. With `enforceAvailableModels`, the enforced Default resolves through `modelOverrides` from managed settings only.
- When managed settings set `availableModels`, only managed `modelOverrides` apply to directly passed IDs (v2.1.200+); user/project overrides are ignored and an ID the managed list excludes is never resolved via overrides.
- With `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST`, host model config takes precedence over managed model settings.
