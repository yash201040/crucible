---
type: "Guide"
title: "Pin models for third-party deployments"
description: "Why and how to pin version-specific model IDs on Bedrock, Agent Platform, Foundry and Claude Platform on AWS, including 1M suffix rules."
resource: "https://code.claude.com/docs/en/model-config#pin-models-for-third-party-deployments"
tags: [model, pinning, bedrock, foundry, providers]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.323"
surfaces: [cli]
requires: "Third-party provider; ID matching to 1M by default needs v2.1.323+"
identifiers:
  - "ANTHROPIC_DEFAULT_OPUS_MODEL"
  - "ANTHROPIC_DEFAULT_SONNET_MODEL"
  - "ANTHROPIC_DEFAULT_HAIKU_MODEL"
  - "ANTHROPIC_DEFAULT_FABLE_MODEL"
  - "[1m]"
  - "availableModels"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

On Bedrock, Agent Platform, Foundry and Claude Platform on AWS, aliases resolve to a built-in default ID per provider that can lag the newest release and may not be enabled in the account. Without pinning, on Bedrock and Agent Platform a startup check shows a notice and falls back to an earlier version (an Opus default with no Opus available falls back to the default Sonnet); on Foundry Claude Code switches to an older model or the request fails. Docs warn to set version IDs during initial setup so you control when users move.

# How to use it

| Provider | Example |
| :- | :- |
| Amazon Bedrock | `export ANTHROPIC_DEFAULT_OPUS_MODEL='us.anthropic.claude-opus-4-8'` |
| Google Cloud's Agent Platform | `export ANTHROPIC_DEFAULT_OPUS_MODEL='claude-opus-4-8'` |
| Microsoft Foundry | `export ANTHROPIC_DEFAULT_OPUS_MODEL='claude-opus-4-8'` |

Same pattern for `ANTHROPIC_DEFAULT_FABLE_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, `ANTHROPIC_DEFAULT_HAIKU_MODEL`. To upgrade, update the variables and redeploy.

# Limits and defaults

- On Bedrock and Agent Platform, starting on a specific Sonnet or Opus version (`--model`, `ANTHROPIC_MODEL`, `model`) pins it for the matching alias and skips the fallback notice (before v2.1.211 the check could still show a notice).
- A pinned ID is treated as 1M with no suffix when it matches a natively-1M model (contains its Anthropic API ID such as `claude-opus-4-8`, or is mapped via `modelOverrides`), or when it cannot be matched (set the real window if it accepts less; before v2.1.323 200K was assumed, so append `[1m]`).
- For Opus 4.6 / Sonnet 4.6: append `[1m]`, e.g. `export ANTHROPIC_DEFAULT_OPUS_MODEL='claude-opus-4-6[1m]'`. The suffix is stripped before sending, only valid if the model supports 1M, and read per variable (on Bedrock/Agent Platform/Foundry an ID without it uses 200K even if another variable has it).
- With an `ANTHROPIC_DEFAULT_*_MODEL` set the picker shows one row for it in place of the family's rows; users reach 1M with `/model opus[1m]` or `/model sonnet[1m]`.
- `availableModels` matches an alias, version prefix, or full provider-form ID; provider prefixes such as `us.anthropic.` are not stripped; map via `modelOverrides` or list the full ID. Agent Platform `@` dated IDs (`claude-sonnet-4-5@20250929`) need the date in the entry. For pinned models list the variable's value. Any `[1m]` suffix is stripped before matching.
