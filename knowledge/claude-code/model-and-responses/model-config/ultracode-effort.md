---
type: "Feature"
title: "Ultracode"
description: "A Claude Code setting (not an effort level) that makes Claude plan dynamic workflows for substantive tasks; ways to turn it on and limits."
resource: "https://code.claude.com/docs/en/model-config#adjust-effort-level"
tags: [ultracode, workflows, effort, orchestration]
kind: "setting"
maturity: "unlabelled"
since: "2.1.203"
surfaces: [cli, sdk]
requires: "--effort ultracode needs v2.1.203+; off form and non-xhigh levels need v2.1.284+"
identifiers:
  - "ultracode"
  - "/effort ultracode"
  - "/effort ultracode off"
  - "--effort ultracode"
  - "effortLevel"
  - "applyFlagSettings()"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The `/effort` slider has an **Ultracode** toggle. Ultracode is a Claude Code setting, not a model effort level: when on, Claude orchestrates [dynamic workflows](/docs/en/workflows) for substantive tasks at whichever effort level the session runs.

# How to use it

- `/effort ultracode` turns on for the session; `/effort ultracode off` turns off; in the slider press `Tab` to flip, `Enter` to apply.
- `claude --effort ultracode` starts at `xhigh` with ultracode on.
- `"ultracode": true` in a settings file, via `--settings`, or in an Agent SDK control request. An `applyFlagSettings()` request also accepts `effortLevel: "ultracode"` (turns on and sets `xhigh`).

Turning it on or off with `/effort` or the `ultracode` setting leaves the effort level unchanged; the `--effort ultracode` flag and SDK `effortLevel: "ultracode"` also set `xhigh`. Picking a level in the slider or `/model` leaves ultracode as it was.

# Limits and defaults

- The off form, slider toggle, and staying on at levels other than `xhigh` need v2.1.284+. Before that, turning it on set `xhigh`, picking another level turned it off, and an effort cap below `xhigh` made it unavailable.
- Before v2.1.203 `--effort ultracode` printed `Unknown --effort value 'ultracode'`.
- The persisted `effortLevel` setting and `CLAUDE_CODE_EFFORT_LEVEL` do not accept `ultracode`. If `CLAUDE_CODE_EFFORT_LEVEL` or an effort cap sets the level, ultracode stays on at that level.
- Unavailable when workflows are turned off or the model lacks `xhigh`; `--effort ultracode` then starts with it off at the highest level allowed, up to `xhigh`.
