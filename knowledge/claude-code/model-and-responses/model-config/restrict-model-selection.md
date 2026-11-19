---
type: "Feature"
title: "Restrict model selection (availableModels)"
description: "Managed allowlist of models users can select, where it applies, and how blocked selections are handled per entry point."
resource: "https://code.claude.com/docs/en/model-config#restrict-model-selection"
tags: [model, allowlist, managed-settings, governance]
kind: "setting"
maturity: "unlabelled"
since: "2.1.205"
surfaces: [cli, sdk, desktop, web]
requires: "Managed or policy settings"
identifiers:
  - "availableModels"
  - "replaceBuiltInOptions"
  - "modelPicker"
  - "CLAUDE_CODE_SUBAGENT_MODEL"
  - "advisorModel"
  - "--advisor"
  - "CLAUDE_CODE_AUTO_MODE_MODEL"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Administrators use `availableModels` in managed or policy settings to restrict which models can be selected. An entry is a model family (`sonnet`), a version prefix (`claude-sonnet-4-5`, which also matches later IDs extending it, so `claude-fable-5` permits Fable 5, 5.1 and 5.2 while `claude-fable-5-1` permits 5.1 only), or a full model ID (`claude-sonnet-4-5-20250929`).

# How to use it

`{ "availableModels": ["sonnet", "haiku"] }`

The allowlist applies to: main session model (`/model`, `--model`, `ANTHROPIC_MODEL`, `model`, `ANTHROPIC_DEFAULT_MODEL`, resumed model); alias resolution (`ANTHROPIC_DEFAULT_OPUS/SONNET/HAIKU/FABLE_MODEL` cannot redirect an allowed alias outside the list); fast mode (`/fast` refuses with "is not in your organization's allowed models"); subagent and teammate models (frontmatter `model`, Agent tool `model` parameter, agent team teammates, `CLAUDE_CODE_SUBAGENT_MODEL`); skill and command `model` frontmatter; `advisorModel` and `--advisor`; the background agent dispatch picker.

Blocked selection handling by source:

| Source | Result |
| - | - |
| Family alias on Anthropic API / Claude Platform on AWS | Newest permitted version of the family substituted, with notice (e.g. `["sonnet","claude-opus-4-6"]` makes `opus` select Opus 4.6); before v2.1.205 rejected or replaced |
| `/model` | Rejected with an error |
| `--model`, `ANTHROPIC_MODEL`, `model` setting | Replaced at startup with a warning; session starts on default model |
| `ANTHROPIC_DEFAULT_MODEL` | Variable ignored |
| Subagent or teammate override | Runs on a fallback model instead of failing; interactive sessions warn for a top-level subagent, no teammate report (substitution of newest permitted version applies from v2.1.222) |
| Skill or command override | Ignored; runs on session model (in-subagent skills follow subagent behavior) |
| `advisorModel` | Advisor disabled for the session |
| `--advisor` | Exits with error at launch; background session starts without advisor |
| `CLAUDE_CODE_AUTO_MODE_MODEL` | Ignored; classifier model chosen as if unset |

# Limits and defaults

- Model changes Claude Code makes itself are checked too: [fallback chains](./fallback-model-chains.md) drop outside entries; plan-mode upgrades (e.g. `opusplan`) use the newest permitted version on Anthropic API and Claude Platform on AWS, otherwise are skipped; automatic model fallback targets that are excluded do not run (request ends in refusal); auto mode classifier requests that would use an excluded default classifier model run on the session model, or an Opus model in Fable sessions (on other providers `ANTHROPIC_DEFAULT_OPUS_MODEL` or Opus 5, allowlist not consulted; v2.1.210+); fast mode enabling refused when the resulting model is outside the list; availability fallback on Bedrock and Agent Platform skips excluded models (startup checks skip them only with `enforceAvailableModels`).
- The picker hides excluded models. On Anthropic API, Claude Platform on AWS, Claude apps gateway or an LLM gateway, a listed Opus/Sonnet/Haiku ID without a built-in row appears as its own row (before v2.1.199 only by typing `/model <id>`); `replaceBuiltInOptions` in `modelPicker` suppresses it. On Bedrock, Agent Platform, Foundry a row is added only for IDs starting with `anthropic.`; otherwise add the ID to a `modelPicker` lineup.
- `availableModels: []` blocks named selections.
- Related: [surface coverage](./allowlist-surface-coverage.md), [enforce and merge](./enforce-allowlist-and-merge.md), [deny models](./block-specific-models.md).
