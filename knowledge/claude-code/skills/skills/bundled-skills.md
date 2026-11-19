---
type: "Feature"
title: "Bundled skills"
description: "Prompt-based skills shipped with Claude Code (/doctor, /code-review, /batch, /debug, /loop, /claude-api) and how to turn them off."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, bundled, commands, disable]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/doctor"
  - "/code-review"
  - "/batch"
  - "/debug"
  - "/loop"
  - "/claude-api"
  - "/workflow-authoring"
  - "disableBundledSkills"
  - "DISABLE_DOCTOR_COMMAND"
  - "skillOverrides"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Bundled skills are prompt-based: they hand Claude detailed instructions and let it orchestrate the work with its tools, unlike most built-in commands, which run fixed logic. You invoke one by typing `/` plus its name; Claude may also invoke some automatically. They are listed in the commands reference with **Skill** in the Purpose column.

# How to use it

- Most bundled skills exist in every session. Some need a feature: `/workflow-authoring` exists only when [dynamic workflows](https://code.claude.com/docs/en/workflows) are enabled.
- Turn all bundled skills off with the `disableBundledSkills` setting.
- `/doctor` stays typable even with `disableBundledSkills` on. Hide it with the `DISABLE_DOCTOR_COMMAND` environment variable or a `skillOverrides` entry `"doctor": "off"`.
- Your own skill with the same name replaces the bundled command but not its aliases (see [name resolution](./skill-name-resolution.md)).

# Notes

Examples named on the page: `/doctor`, `/code-review`, `/batch`, `/debug`, `/loop`, `/claude-api`. See also [run and verify](./run-and-verify-skills.md) and [/claude-api](./claude-api-skill.md).
