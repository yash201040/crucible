---
type: "Reference"
title: "Model selection and pinned alias variables"
description: "Variables that choose the session model, pin what the fable, haiku, opus and sonnet aliases resolve to, and customize their /model picker rows."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [models, aliases, pinning, model-picker]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "ANTHROPIC_MODEL"
  - "ANTHROPIC_DEFAULT_MODEL"
  - "ANTHROPIC_DEFAULT_FABLE_MODEL"
  - "ANTHROPIC_DEFAULT_FABLE_MODEL_DESCRIPTION"
  - "ANTHROPIC_DEFAULT_FABLE_MODEL_NAME"
  - "ANTHROPIC_DEFAULT_FABLE_MODEL_SUPPORTED_CAPABILITIES"
  - "ANTHROPIC_DEFAULT_HAIKU_MODEL"
  - "ANTHROPIC_DEFAULT_HAIKU_MODEL_DESCRIPTION"
  - "ANTHROPIC_DEFAULT_HAIKU_MODEL_NAME"
  - "ANTHROPIC_DEFAULT_HAIKU_MODEL_SUPPORTED_CAPABILITIES"
  - "ANTHROPIC_DEFAULT_OPUS_MODEL"
  - "ANTHROPIC_DEFAULT_OPUS_MODEL_DESCRIPTION"
  - "ANTHROPIC_DEFAULT_OPUS_MODEL_NAME"
  - "ANTHROPIC_DEFAULT_OPUS_MODEL_SUPPORTED_CAPABILITIES"
  - "ANTHROPIC_DEFAULT_SONNET_MODEL"
  - "ANTHROPIC_DEFAULT_SONNET_MODEL_DESCRIPTION"
  - "ANTHROPIC_DEFAULT_SONNET_MODEL_NAME"
  - "ANTHROPIC_DEFAULT_SONNET_MODEL_SUPPORTED_CAPABILITIES"
  - "ANTHROPIC_SMALL_FAST_MODEL"
  - "ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Model choice by environment. Each family (Fable, Haiku, Opus, Sonnet) has four variables: the model ID the alias resolves to, plus `_NAME`, `_DESCRIPTION` and `_SUPPORTED_CAPABILITIES` for the `/model` picker row.

# How to use it

| Variable | What it does |
| :- | :- |
| `ANTHROPIC_MODEL` | Model setting to use. `--model` and `/model` override it; it beats the `model` setting. |
| `ANTHROPIC_DEFAULT_MODEL` | Model new sessions start on. Requires v2.1.236+. |
| `ANTHROPIC_DEFAULT_FABLE_MODEL` | ID the `fable` alias resolves to; also the ID recognized as Fable for automatic model fallback on third-party providers. |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | ID the `haiku` alias resolves to; also used for background functionality. |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` | ID the `opus` alias resolves to; `opusplan` uses it while Plan Mode is active. |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | ID the `sonnet` alias resolves to; `opusplan` uses it when Plan Mode is not active. |
| `ANTHROPIC_DEFAULT_<FAMILY>_MODEL_NAME` | Picker display name; falls back to the recognized model name, else the pinned ID. |
| `ANTHROPIC_DEFAULT_<FAMILY>_MODEL_DESCRIPTION` | Picker description; default begins `Custom <Family> model`. |
| `ANTHROPIC_DEFAULT_<FAMILY>_MODEL_SUPPORTED_CAPABILITIES` | Comma-separated capabilities such as `effort,thinking`. |
| `ANTHROPIC_SMALL_FAST_MODEL` | [DEPRECATED] Haiku-class model for background tasks. |
| `ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION` | AWS region for the Haiku-class model on Bedrock or Mantle. On Bedrock it only works when `ANTHROPIC_DEFAULT_HAIKU_MODEL` or the deprecated variable is also set; otherwise Bedrock runs background tasks on the default Sonnet or primary model in the session region. |

# Notes

`<FAMILY>` stands for `FABLE`, `HAIKU`, `OPUS`, `SONNET`; each of the 16 resulting names is listed in this concept's identifiers. Subagent model variables are in [subagent controls](./subagent-limits-and-models.md).
