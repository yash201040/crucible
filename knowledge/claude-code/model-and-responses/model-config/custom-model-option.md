---
type: "Feature"
title: "Custom model option"
description: "ANTHROPIC_CUSTOM_MODEL_OPTION adds one custom entry to the /model picker without validation."
resource: "https://code.claude.com/docs/en/model-config#add-a-custom-model-option"
tags: [model, picker, custom, gateway]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "ANTHROPIC_CUSTOM_MODEL_OPTION"
  - "ANTHROPIC_CUSTOM_MODEL_OPTION_NAME"
  - "ANTHROPIC_CUSTOM_MODEL_OPTION_DESCRIPTION"
  - "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY"
  - "modelPicker"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`ANTHROPIC_CUSTOM_MODEL_OPTION` adds a single custom entry to the `/model` picker without replacing built-ins; useful for IDs Claude Code does not list. With LLM gateways, `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1` can populate the picker from the gateway's `/v1/models`, so this variable is needed only when discovery is off or misses the model. To list several models in your own order, use `modelPicker`.

# How to use it

```bash
export ANTHROPIC_CUSTOM_MODEL_OPTION="my-gateway/claude-opus-5-5"
export ANTHROPIC_CUSTOM_MODEL_OPTION_NAME="Opus via Gateway"
export ANTHROPIC_CUSTOM_MODEL_OPTION_DESCRIPTION="Custom deployment routed through the internal LLM gateway"
```

Name and description are optional: name defaults to the model's name if recognized, else the ID; description defaults to `Custom model (<model-id>)`. Set before launching (read at startup). The entry is listed after built-ins, then any appended `modelPicker` rows.

# Limits and defaults

- The model ID is not validated; any string the endpoint accepts works.
- With `availableModels` set, include the ID there or the entry is filtered and `--model` rejects it. An ID embedding a family name (e.g. `my-gateway/claude-opus-5-5`) counts as a specific entry and disables that family's wildcard.
