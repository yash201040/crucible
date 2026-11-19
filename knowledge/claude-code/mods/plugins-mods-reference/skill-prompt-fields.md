---
type: "Reference"
title: "skill.prompt source and frontmatter fields"
description: "Fields a skill.prompt hook can read about where a skill came from and its frontmatter; only text and frontmatter may be changed."
resource: "https://code.claude.com/docs/en/plugins/mods/reference"
tags: [mods, skills, frontmatter, events]
kind: "hook"
maturity: "unlabelled"
since: "2.1.299"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "e.skill"
  - "e.text"
  - "e.source"
  - "e.pluginName"
  - "e.path"
  - "e.frontmatter"
  - "e.frontmatterProblem"
  - "policySettings"
  - "userSettings"
  - "projectSettings"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-reference"
    resource: "https://code.claude.com/docs/en/plugins/mods/reference"
    title: "Mods reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Field | Type | Holds |
| :- | :- | :- |
| `e.skill` | string | the skill's name |
| `e.text` | string | the text Claude reads |
| `e.source` | string | provider: `policySettings`, `userSettings`, `projectSettings` for enterprise, personal, project locations; otherwise a word such as `plugin`, `mcp`, `syncedSkills`, `built-in` |
| `e.pluginName` | string | plugin name when `e.source` is `plugin` |
| `e.path` | string | absolute path of `SKILL.md` (or the `.md` of a command-file skill); absent when no file on this machine, e.g. built-in |
| `e.frontmatter` | object | the file's frontmatter as plain data |
| `e.frontmatterProblem` | string | why `e.frontmatter` lacks the file's frontmatter or a key, e.g. `is a list or a single value, not a table`; absent otherwise |

# Limits and defaults

A hook may pass a changed `text` or `frontmatter` to `next` (later hooks read both; Claude reads the final `text`). Changing any other field makes the hook fail. `e.source`, `e.pluginName`, `e.path`, `e.frontmatter`, `e.frontmatterProblem` need v2.1.299+.
