---
type: "Feature"
title: "skillOverrides setting"
description: "Set a skill to on, name-only, user-invocable-only or off from settings without editing SKILL.md."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, settings, visibility, overrides]
kind: "setting"
maturity: "unlabelled"
since: "2.1.260"
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "skillOverrides"
  - "on"
  - "name-only"
  - "user-invocable-only"
  - "off"
  - ".claude/settings.local.json"
  - "--settings"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`skillOverrides` controls skill visibility from settings, for skills whose SKILL.md you do not want to edit. The `/skills` menu writes it: highlight, press `Space` to cycle states, `Esc` to save to `.claude/settings.local.json`.

# How to use it

```json
{ "skillOverrides": { "legacy-context": "name-only", "deploy": "off" } }
```

| Value | Listed to Claude | In `/` menu |
| :- | :- | :- |
| `"on"` | name and description | yes |
| `"name-only"` | name only | yes |
| `"user-invocable-only"` | hidden | yes (menu label `user-only`) |
| `"off"` | hidden | hidden |

A skill not listed is `"on"`.

# Limits and defaults

- `"off"` also hides the skill from command lists given to Remote Control clients and Agent SDK callers; invoking a hidden skill by full name returns the `skillOverrides` error.
- Aliases (e.g. `checkup` for `/doctor`): an entry under an alias in managed settings or a `--settings` file applies to the skill behind it, can only restrict, and an entry under the skill's own name in managed settings wins. Before v2.1.260 alias entries were not applied. In user, project and local settings, entries match skill names only (`review` does not hit `/code-review`).
- Plugin skills are not affected; manage them via `/plugin`.
