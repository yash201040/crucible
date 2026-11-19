---
type: "Feature"
title: "Effort levels"
description: "Per-model effort levels, resolution order, how to set them, persistence, defaults and subagent/skill effort."
resource: "https://code.claude.com/docs/en/model-config#adjust-effort-level"
tags: [effort, reasoning, model, cost, subagents]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk, ide, desktop]
requires: "s key (session only) needs v2.1.257+; Remote Control device effort needs v2.1.234+"
identifiers:
  - "/effort"
  - "/effort auto"
  - "/effort status"
  - "--effort"
  - "CLAUDE_CODE_EFFORT_LEVEL"
  - "effortLevel"
  - "modelSettings"
  - "maxEffortLevel"
  - "applyFlagSettings()"
  - "effort"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Effort levels control adaptive reasoning: lower is faster and cheaper, higher reasons deeper. Models not listed do not support effort. If a level is unsupported, Claude Code uses the highest supported level at or below it (`xhigh` runs as `high` on Opus 4.6). The scale is calibrated per model, so a level name is not the same underlying value across models.

# How to use it

| Model | Levels |
| :- | :- |
| Fable models; Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8, Opus 4.7 | `low`, `medium`, `high`, `xhigh`, `max` |
| Opus 4.6, Sonnet 4.6 | `low`, `medium`, `high`, `max` |

Resolution order, first that applies:
1. `CLAUDE_CODE_EFFORT_LEVEL`
2. A level picked in session (`/effort`, `/model` picker, `applyFlagSettings()`)
3. `--effort`
4. Settings: per-model level in `modelSettings` or the `effortLevel` key
5. Model default: Fable 5.2, Opus 5.5, Sonnet 5.5, Haiku 5.5 default `medium`; Opus 4.7 `xhigh`; others `high`; an org default effort for the organization default model applies to it.

Ways to set it: `/effort` (slider), `/effort <level>`, `/effort auto` (clear saved level for active model); `/model` slider; `--effort <level>`; `CLAUDE_CODE_EFFORT_LEVEL` (or `auto`/`unset`, see [send no effort](./send-no-effort-level.md)); settings `modelSettings` or `effortLevel` (`low`, `medium`, `high`, `xhigh`; `max` not accepted; `ultracode` has its own key); Remote Control device (session only); `effort` frontmatter in a skill or subagent file.

# Limits and defaults

- `Enter` or typing a level saves it as default; `s` applies this session only. Saved per model under `modelSettings` in user settings. `max` applies to the current session only unless set through `CLAUDE_CODE_EFFORT_LEVEL`. In `-p` runs `/effort` applies to that session only.
- Opus 5.5 starts at `medium`; a top-level `effortLevel` in user settings does not count for Opus 5.5 (it still applies on Opus 5, Fable 5.1 and earlier); in project, local or managed settings or via `--settings` it applies to every model.
- A skill `effort` applies to the end of its turn (or the forked subagent run with `context: fork`); a subagent `effort` applies while it runs unless its invocation overrides. `CLAUDE_CODE_EFFORT_LEVEL` beats both; `maxEffortLevel` and org caps still limit. Managed `effortLevel` applies at the settings step; users can change it.
- Subagent or teammate with no `effort`: on the main conversation's model it runs at the session or `--effort` level; on another model that level does not apply.
- New level starts with the next message; queue a message to apply it mid-turn. Before v2.1.242 `/effort` could itself queue until the turn ended.
- Guidance: `low` for quick reviewed exchanges; `medium` default on newest models for scoped work; `high` for verification-heavy work; `xhigh` deeper at more spend; `max` for hard problems, may overthink, test first. Moving from Opus 5 to Opus 5.5, start at `medium`.
- Phone/browser effort control via Remote Control applies to that session only.
