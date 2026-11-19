---
type: "Reference"
title: "Custom /model picker entry variables"
description: "Variables that add a non-standard or gateway-specific model as an extra entry in the /model picker."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [models, model-picker, gateway]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "ANTHROPIC_CUSTOM_MODEL_OPTION"
  - "ANTHROPIC_CUSTOM_MODEL_OPTION_DESCRIPTION"
  - "ANTHROPIC_CUSTOM_MODEL_OPTION_NAME"
  - "ANTHROPIC_CUSTOM_MODEL_OPTION_SUPPORTED_CAPABILITIES"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

One extra picker entry that does not replace the built-in aliases.

# How to use it

| Variable | What it does |
| :- | :- |
| `ANTHROPIC_CUSTOM_MODEL_OPTION` | Model ID added as a custom entry. |
| `ANTHROPIC_CUSTOM_MODEL_OPTION_NAME` | Display name; when unset, the recognized model name, else the model ID. |
| `ANTHROPIC_CUSTOM_MODEL_OPTION_DESCRIPTION` | Description; default `Custom model (<model-id>)`. |
| `ANTHROPIC_CUSTOM_MODEL_OPTION_SUPPORTED_CAPABILITIES` | Comma-separated capabilities such as `effort,thinking`. |
