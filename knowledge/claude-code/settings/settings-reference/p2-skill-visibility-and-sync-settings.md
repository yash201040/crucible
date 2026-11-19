---
type: "Reference"
title: "Skill and synced-plugin settings"
description: "Settings that disable bundled skills, inline shell in skills, override skill visibility and stop claude.ai skill and plugin sync."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, skills, plugins, sync]
kind: "setting"
maturity: "unlabelled"
since: "2.1.273"
surfaces: [cli, cloud]
requires: ""
identifiers:
  - "disableBundledSkills"
  - "disableSkillShellExecution"
  - "skillOverrides"
  - "syncClaudeAiSkills"
  - "syncClaudeAiPlugins"
  - "CLAUDE_CODE_DISABLE_BUNDLED_SKILLS"
  - "DISABLE_DOCTOR_COMMAND"
  - "~/.claude/skills/synced/"
  - "~/.claude/plugins/synced/"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Five settings that decide which skills and plugins load.

# How to use it

| Name | Type / scope | Default | What it does |
| :- | :- | :- | :- |
| `disableBundledSkills` | Boolean, any file | unset | `true` removes bundled skills and workflows and hides built-in commands such as `/init` from the model (still typable). Skills from plugins, `.claude/skills/`, `.claude/commands/` unaffected. `CLAUDE_CODE_DISABLE_BUNDLED_SKILLS=1` does it per session; neither can undo the other. `/doctor` stays typable; hide with `DISABLE_DOCTOR_COMMAND` |
| `disableSkillShellExecution` | Boolean, any file | unset | `true` replaces inline `` !`...` `` and ` ```! ` blocks in skills and custom commands (user, project, plugin, add-dir sources) with `[shell command execution disabled by policy]`. A managed `true` cannot be overridden. Bundled skills and managed-deployed skills unaffected |
| `skillOverrides` | object skill name to `"on"`, `"name-only"`, `"user-invocable-only"`, `"off"`; any file | all `"on"` | `name-only`: Claude sees name without description; `user-invocable-only`: hidden from Claude but `/name` works; `off`: hidden from Claude and autocomplete. `/skills` menu writes `.claude/settings.local.json`. Not applied to plugin skills. In managed and `--settings` files an alias key (for example `checkup` for `/doctor`) also applies |
| `syncClaudeAiSkills` | Boolean; user, local, managed, `--settings` | unset (sync on) | Only `false` is honored: stops downloading claude.ai account skills into `~/.claude/skills/synced/` (terminal sessions signed in with claude.ai, interactive or not, plus Cowork and cloud) and stops loading them; in user or managed settings also moves them to `~/.claude/skills/.trash/` |
| `syncClaudeAiPlugins` | Boolean; user, local, managed, `--settings` | unset (sync on) | Same for plugins in `~/.claude/plugins/synced/`, loaded as `<name>@synced`; trash is `~/.claude/plugins/.trash/`. Needs v2.1.273+. One plugin off: `"<name>@synced": false` in `enabledPlugins` |
