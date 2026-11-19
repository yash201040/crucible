---
type: "Feature"
title: "Enforce allowlist for Default and merge rules"
description: "enforceAvailableModels extends availableModels to the Default option; controls combination and how lists merge across scopes."
resource: "https://code.claude.com/docs/en/model-config#enforce-the-allowlist-for-the-default-model"
tags: [model, allowlist, managed-settings, default]
kind: "setting"
maturity: "unlabelled"
since: "2.1.175"
surfaces: [cli]
requires: "Claude Code v2.1.175+; managed settings"
identifiers:
  - "enforceAvailableModels"
  - "availableModels"
  - "modelOverrides"
  - "deniedModels"
  - "availableModelsMatch"
  - "model"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

With prefix matching, `availableModels` alone leaves the Default option on the account's runtime default. Setting `enforceAvailableModels: true` with a non-empty `availableModels` in managed settings makes Default obey the allowlist: if the account-type default (or organization default) is not allowed, Default resolves to the first `availableModels` entry that names an allowed, available model. This applies at startup, selecting Default in `/model`, the `"default"` keyword in fallback chains, and the fallback when an excluded selection is dropped. A model recorded on the account is also checked.

# How to use it

```json
{
  "model": "claude-sonnet-4-5",
  "availableModels": ["claude-sonnet-4-5", "haiku"],
  "enforceAvailableModels": true,
  "env": { "ANTHROPIC_DEFAULT_SONNET_MODEL": "claude-sonnet-4-5" }
}
```

The `model` setting is an initial selection, not enforcement. Combine: `availableModels` (which named models), `enforceAvailableModels` (Default), `deniedModels` + `availableModelsMatch` (block versions), `model` (initial), and the `ANTHROPIC_DEFAULT_*_MODEL` variables (alias targets and account-type default version). `enforceAvailableModels` pins Default to the allowlist; the `env` block pins which version an alias resolves to.

# Limits and defaults

- Remaps Default only when `availableModels` is non-empty; if no entry resolves to an allowed and available model enforcement is skipped (warning only under `--debug`). `availableModels: []` makes `enforceAvailableModels` ineffective.
- Deploy both keys in the highest-ranked managed source; by default only that source is read. Under the opt-in merge, a `modelOverrides` map from a source ranked below the one setting `availableModels` is ignored.
- Merge: if managed settings define `availableModels`, that list alone applies; user, project, local entries cannot extend it and it is never merged across managed sources. Otherwise lists from user, project, local are concatenated and deduplicated. Before v2.1.175 lower-scope entries merged into the managed list.
- A specific entry in a family (version prefix or full ID) disables that family's wildcard: with `["sonnet","claude-sonnet-4-5"]` only IDs matching `claude-sonnet-4-5` are pickable.
- Mantle model IDs: entries starting with `anthropic.` are added to the picker as custom options; with the Bedrock Mantle endpoint enabled, matching entries route there. A Mantle ID embeds a family name so it disables that family's wildcard; also list version prefixes or full IDs to keep.
