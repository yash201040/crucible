---
type: "Reference"
title: "Effort level settings"
description: "effortLevel, maxEffortLevel and modelSettings set, cap and save per-model reasoning effort (low to max), with precedence rules."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [effort, models, settings, cost]
kind: "setting"
maturity: "unlabelled"
since: "2.1.251"
surfaces: [cli, headless, sdk, ide]
requires: "modelSettings v2.1.251; maxEffortLevel v2.1.267; modelSettings.autoCompactWindow v2.1.288"
identifiers:
  - "effortLevel"
  - "maxEffortLevel"
  - "modelSettings"
  - "modelSettings.<model>.effortLevel"
  - "modelSettings.<model>.maxEffortLevel"
  - "modelSettings.<model>.autoCompactWindow"
  - "--effort"
  - "CLAUDE_CODE_EFFORT_LEVEL"
  - "/effort"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Keys that set a default reasoning effort, cap it, or save a level per model. Lower effort is faster and cheaper; higher reasons more deeply.

# How to use it

| Key | Type | Default | What it does |
| :- | :- | :- | :- |
| `effortLevel` | `"low"`, `"medium"`, `"high"`, `"xhigh"` | unset | Default for models with no saved level. Before v2.1.251 `/effort` wrote this key; now `/effort low\|medium\|high\|xhigh` in an interactive local session writes `modelSettings` |
| `maxEffortLevel` | `"low"`, `"medium"`, `"high"`, `"xhigh"`, `"max"` (`"max"` = no cap) | unset | Caps effort for every model on every provider (Bedrock, Agent Platform, Foundry included). Higher levels from `/effort`, `/model`, `--effort`, `CLAUDE_CODE_EFFORT_LEVEL`, skill or subagent `effort` frontmatter or the model default run at the cap |
| `modelSettings` | object: model name to `{effortLevel, maxEffortLevel, autoCompactWindow}` | unset | Saved per-model values; written under the canonical name (e.g. `claude-opus-5-5`) and matched for alias, dated, `[1m]` and provider IDs. `autoCompactWindow` is a token count of `100000` or more, or `"auto"`; `/autocompact` saves here |

```json
{ "maxEffortLevel": "medium", "modelSettings": { "claude-sonnet-4-6": { "maxEffortLevel": "max" } } }
```

# Limits and defaults

- Precedence for one session: `CLAUDE_CODE_EFFORT_LEVEL` over `--effort` over the setting.
- Within one file a model's saved level beats the top-level `effortLevel`. Across files each model is resolved separately; the highest-precedence file that sets either decides, so managed `effortLevel` outranks a saved user level.
- `maxEffortLevel`: with several scopes the lowest cap applies. A model's `maxEffortLevel` replaces the top-level one only within the source that sets both; `"max"` there exempts the model from that source only. Organization effort limits also apply; the lower wins.
- In a session attached to a remote worker, in a `-p` run and in the Agent SDK, `/effort` applies to that session only.
- In user `~/.claude/settings.json`, `effortLevel` keeps applying to Opus 5, Fable 5.1 and earlier; Opus 5.5 and later ignore it until a level is saved. In project, local, managed settings and `--settings` it applies to every model.
- `/effort auto` clears the saved level for the current model.
