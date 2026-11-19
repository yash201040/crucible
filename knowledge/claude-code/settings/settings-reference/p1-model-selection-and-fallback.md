---
type: "Reference"
title: "Model selection, overrides and fallback"
description: "model, modelOverrides, modelPicker, fallbackModel, switchModelsOnFlag, language, outputStyle: pick and route models and set response style."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [models, fallback, model-picker, settings]
kind: "setting"
maturity: "unlabelled"
since: "2.1.242"
surfaces: []
requires: "modelPicker v2.1.242; behavesAs v2.1.257"
identifiers:
  - "model"
  - "modelOverrides"
  - "modelPicker"
  - "modelPicker.options"
  - "modelPicker.replaceBuiltInOptions"
  - "behavesAs"
  - "fallbackModel"
  - "--fallback-model"
  - "switchModelsOnFlag"
  - "language"
  - "outputStyle"
  - "--model"
  - "ANTHROPIC_MODEL"
  - "ANTHROPIC_DEFAULT_MODEL"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Keys that choose the model for new sessions, map model IDs to provider IDs, shape the `/model` picker, define backup models and set language and output style.

# How to use it

| Key | Scope | Type | Default | What it does |
| :- | :- | :- | :- | :- |
| `model` | Any file | alias or full ID | unset (account default) | Model for every new session. `--model` beats `ANTHROPIC_MODEL`, and both beat the key (even a managed `model`); `availableModels` still applies. The key outranks `ANTHROPIC_DEFAULT_MODEL` |
| `modelOverrides` | Any file | object model ID to provider ID | unset | Maps Anthropic IDs to e.g. Bedrock inference profile ARNs on Bedrock, Agent Platform, Foundry |
| `modelPicker` | User or managed (ignored in project/local) | object `{options, replaceBuiltInOptions}` | unset | Custom `/model` rows. Highest of managed, `--settings`, user supplies the whole lineup; lineups are never combined |
| `fallbackModel` | Any file | array of aliases/IDs; `"default"` expands | unset | Backup models tried in order when the primary is overloaded or unavailable |
| `switchModelsOnFlag` | Any file | Boolean | unset (switches automatically) | What happens when a safety classifier flags a request: `true` switch to fallback and continue; `false` pause in interactive sessions, but in `-p` runs the flagged request ends as an error. Appears in `/config` as **Switch models when a message is flagged** |
| `language` | Any file | any language name | unset | Passed verbatim to Claude as a respond-in-this-language instruction; unvalidated. Also sets voice dictation and session-title language |
| `outputStyle` | Any file | style name | unset | Selects a built-in or custom output style (e.g. `"Explanatory"`). Takes effect next message; before v2.1.251 only after `/clear` or a new session |

`modelPicker.options` rows: required `model`, optional `label`, `description`, `behavesAs` (ID of a model the version knows, applied to a newer model for capabilities and effort defaults; label and request ID unchanged). `replaceBuiltInOptions` (default `false`): `true` shows only these rows, Default and the session's current model, hiding the built-in lineup, `availableModels` rows, gateway-discovered models and `ANTHROPIC_CUSTOM_MODEL_OPTION`. Rows Claude Code cannot serve are dropped, not-yet-selectable rows are grayed out; if none survive the built-in lineup is kept.

# Limits and defaults

- `fallbackModel` does not merge across files: the highest-precedence file supplies the whole chain. At most three distinct allowed models are kept. `--fallback-model` overrides for one session.
- A fallback switch means one turn with a cold prompt cache; the next message tries the primary again. Without a chain Claude Code retries the same model then surfaces the error.
- `modelPicker` label changes what is shown, not which model runs.
