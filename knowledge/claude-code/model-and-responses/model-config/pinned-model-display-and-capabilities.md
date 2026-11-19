---
type: "Reference"
title: "Pinned model display and capabilities"
description: "_NAME, _DESCRIPTION and _SUPPORTED_CAPABILITIES companion variables for pinned models and the capability values."
resource: "https://code.claude.com/docs/en/model-config#customize-pinned-model-display-and-capabilities"
tags: [model, pinning, capabilities, env-var]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Third-party provider; _NAME and _DESCRIPTION also with an LLM gateway; no effect on api.anthropic.com"
identifiers:
  - "ANTHROPIC_DEFAULT_OPUS_MODEL_NAME"
  - "ANTHROPIC_DEFAULT_OPUS_MODEL_DESCRIPTION"
  - "ANTHROPIC_DEFAULT_OPUS_MODEL_SUPPORTED_CAPABILITIES"
  - "ANTHROPIC_DEFAULT_SONNET_MODEL_NAME"
  - "ANTHROPIC_DEFAULT_SONNET_MODEL_DESCRIPTION"
  - "ANTHROPIC_DEFAULT_SONNET_MODEL_SUPPORTED_CAPABILITIES"
  - "ANTHROPIC_DEFAULT_HAIKU_MODEL_NAME"
  - "ANTHROPIC_DEFAULT_HAIKU_MODEL_DESCRIPTION"
  - "ANTHROPIC_DEFAULT_HAIKU_MODEL_SUPPORTED_CAPABILITIES"
  - "ANTHROPIC_DEFAULT_FABLE_MODEL_NAME"
  - "ANTHROPIC_DEFAULT_FABLE_MODEL_DESCRIPTION"
  - "ANTHROPIC_DEFAULT_FABLE_MODEL_SUPPORTED_CAPABILITIES"
  - "ANTHROPIC_CUSTOM_MODEL_OPTION_NAME"
  - "ANTHROPIC_CUSTOM_MODEL_OPTION_DESCRIPTION"
  - "ANTHROPIC_CUSTOM_MODEL_OPTION_SUPPORTED_CAPABILITIES"
  - "effort"
  - "xhigh_effort"
  - "max_effort"
  - "thinking"
  - "adaptive_thinking"
  - "interleaved_thinking"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A pinned model's `/model` row shows the model's name if Claude Code recognizes the pinned ID (exact ID of a known model, Anthropic or provider/gateway form, with or without `[1m]`; e.g. `us.anthropic.claude-sonnet-4-5-20250929-v1:0` reads `Sonnet 4.5`), otherwise the raw ID (e.g. application inference profile ARNs, unknown versions) unless a `modelOverrides` entry maps a model to it. On Foundry deployment names are user-defined so they are never recognized and the row shows the deployment name. A recognized row's description includes the pinned ID.

Claude Code enables features such as effort and thinking by matching IDs against known patterns; provider IDs often do not match. `_SUPPORTED_CAPABILITIES` declares the real capabilities: when set, listed capabilities are enabled and unlisted disabled for that pinned model; when unset, built-in ID detection applies.

# How to use it

| Variable (OPUS shown) | Description |
| - | - |
| `ANTHROPIC_DEFAULT_OPUS_MODEL_NAME` | Display name; default model name if recognized else the ID |
| `ANTHROPIC_DEFAULT_OPUS_MODEL_DESCRIPTION` | Display description; default begins `Custom Opus model` |
| `ANTHROPIC_DEFAULT_OPUS_MODEL_SUPPORTED_CAPABILITIES` | Comma-separated capabilities |

The same `_NAME`, `_DESCRIPTION`, `_SUPPORTED_CAPABILITIES` suffixes exist for `ANTHROPIC_DEFAULT_SONNET_MODEL`, `ANTHROPIC_DEFAULT_HAIKU_MODEL`, `ANTHROPIC_DEFAULT_FABLE_MODEL` and `ANTHROPIC_CUSTOM_MODEL_OPTION`.

| Capability value | Enables |
| - | - |
| `effort` | Effort levels and `/effort` |
| `xhigh_effort` | `xhigh` level |
| `max_effort` | `max` level |
| `thinking` | Extended thinking |
| `adaptive_thinking` | Adaptive reasoning |
| `interleaved_thinking` | Thinking between tool calls |

Example: `ANTHROPIC_DEFAULT_OPUS_MODEL='arn:aws:bedrock:us-east-1:123456789012:custom-model/abc'` with `..._NAME='Opus via Bedrock'` and `..._SUPPORTED_CAPABILITIES='effort,xhigh_effort,max_effort,thinking,adaptive_thinking,interleaved_thinking'`.

# Limits and defaults

The variables take effect on third-party providers (Bedrock, Agent Platform, Foundry); `_NAME` and `_DESCRIPTION` also with an LLM gateway `ANTHROPIC_BASE_URL`; no effect against `api.anthropic.com`.
