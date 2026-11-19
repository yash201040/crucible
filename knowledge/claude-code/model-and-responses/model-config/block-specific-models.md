---
type: "Feature"
title: "Block specific models or versions"
description: "deniedModels and availableModelsMatch managed settings hold back newer model releases that a prefix allowlist would permit."
resource: "https://code.claude.com/docs/en/model-config#block-specific-models-or-versions"
tags: [model, deny, managed-settings, governance]
kind: "setting"
maturity: "unlabelled"
since: "2.1.283"
surfaces: [cli]
requires: "Claude Code v2.1.283+; managed settings only"
identifiers:
  - "deniedModels"
  - "availableModelsMatch"
  - "requiredMinimumVersion"
  - "exact"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An `availableModels` entry such as `claude-opus-5` also permits later releases (e.g. Opus 5.5). Two managed settings hold a release back:

- `deniedModels`: list of models to block, even when `availableModels` permits them; works with no allowlist too. Unblocked releases stay permitted.
- `availableModelsMatch`: set to `"exact"` so each model ID in `availableModels` permits only the version it names.

# How to use it

```json
{ "availableModels": ["opus", "sonnet"], "deniedModels": ["claude-opus-5-5"] }
```

This blocks Opus 5.5 in every spelling including dated and provider-specific IDs. Earlier Claude Code versions ignore both keys, so also set `requiredMinimumVersion`.

# Limits and defaults

- A blocked model is hidden from `/model`, `/model <name>` rejects it, and naming it with `--model`, `ANTHROPIC_MODEL` or `model` drops it at startup and resolves Default. A hook or background request naming a denied model (e.g. an agent hook `model` field) runs on the session's model.
- Default follows both keys whether or not `enforceAvailableModels` is set. Without it, a Default that would resolve to a blocked model steps down: newest permitted version of the family; newest permitted of each lower-cost family (Sonnet, then Haiku); first `availableModels` entry naming a permitted model. If none, the session refuses to start with an error naming the key to fix. An `"exact"` list affects Default only when managed `availableModels` names at least one model or family.
- Read from managed settings only; set in user, project, local settings or `--settings`, it is ignored with a warning.
