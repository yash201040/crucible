---
type: "Reference"
title: "Model allow and deny lists"
description: "availableModels, availableModelsMatch, deniedModels and enforceAvailableModels restrict which models can be selected, with prefix or exact matching."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [models, allowlist, managed-settings, governance]
kind: "setting"
maturity: "unlabelled"
since: "2.1.283"
surfaces: []
requires: "availableModelsMatch and deniedModels need v2.1.283; enforceAvailableModels needs v2.1.175"
identifiers:
  - "availableModels"
  - "availableModelsMatch"
  - "deniedModels"
  - "enforceAvailableModels"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Settings that limit which models the main session, subagents, skills and the advisor can use.

# How to use it

| Key | Scope | Type | Default | What it does |
| :- | :- | :- | :- | :- |
| `availableModels` | Any file (deploy as managed to enforce) | array of aliases or IDs | unset = all models | Allowlist; constrains `/model`, `--model` and the `model` key. A model ID entry such as `"claude-opus-5"` also permits later versions (Opus 5.5) under prefix matching |
| `availableModelsMatch` | Managed only | `"prefix"` or `"exact"` | `"prefix"` | With `"exact"` an ID entry permits only the version it names (`claude-opus-5` permits Opus 5, not `claude-opus-5-5`; `claude-opus-4-5` also permits its dated ID). A family alias such as `"opus"` still permits the family; `best`, `opusplan`, `default` entries are ignored. With `"exact"` the Default option is also limited to listed models |
| `deniedModels` | Managed only | array of aliases or IDs | unset = none blocked | Blocks models even if `availableModels` permits them; hidden from `/model`. `"opus"` blocks the family; `"claude-opus-5-5"` blocks that version in every spelling; `"claude-opus-5"` also blocks later minors, so write `"claude-opus-5-0"` to block Opus 5 alone |
| `enforceAvailableModels` | Any file (managed source alone is read when managed settings exist) | Boolean | `false` | `true` makes **Default** resolve to the first available model in `availableModels` when it would otherwise be outside the list. No effect when `availableModels` is unset or empty |

```json
{ "availableModels": ["opus", "sonnet"], "deniedModels": ["claude-opus-5-5"] }
```

# Notes

- Managed-only keys are ignored with a warning in user, project and local settings and in `--settings`.
- Plain prefix matching does not remap the account default; pair with `enforceAvailableModels`.
