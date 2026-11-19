---
type: "Feature"
title: "Skill command names and invalid characters"
description: "How the invoked command name derives from file layout and frontmatter name, and which characters make Claude Code refuse a name."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, naming, plugins, validation]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.246"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "/skill-name"
  - "/plugin-name:skill-name"
  - "/frontend:component"
  - "claude --debug"
  - "[names]"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The command you type comes from file location and, for skill directories and plugin skills, the frontmatter `name`.

# How to use it

| Layout | Command name |
| :- | :- |
| Skill dir under `~/.claude/skills/` or `.claude/skills/` | frontmatter `name` or directory name (both invoke it): `deploy-staging/SKILL.md` gives `/deploy-staging`, or `/deploy` with `name: deploy` |
| Nested `.claude/skills/` on a clash | subdirectory path then skill name: `/apps/web:deploy` |
| Added directory on a clash (v2.1.309+) | `/<folder>:<skill>`; two added dirs with the same folder name use the parent folder too, e.g. `/b/cli:verify` |
| `.claude/commands/deploy.md` | `/deploy` |
| `.claude/commands/frontend/component.md` | `/frontend:component` |
| Plugin `skills/` subdirectory | `/my-plugin:review`, or `/my-plugin:fancy` with `name: fancy` (bare `/fancy` also works unless taken) |
| Plugin root `SKILL.md` | frontmatter `name` supplies the final segment; falls back to plugin directory name |
| Synced claude.ai skill | `anthropic-skills:<name>`, or short `/<name>` if unused |

- If a plugin skill's `name` already starts with the plugin prefix, it is not doubled from v2.1.246; v2.1.216-v2.1.245 doubled it.
- In non-interactive sessions `help` and `feedback` are not reserved, so a plugin skill with those names keeps its bare command; other terminal-only built-in names such as `/login` stay reserved.

# Limits and defaults

Refused characters in a command name or frontmatter `name`: zero-width space or control character; private-use or unassigned character; direction-changing character; any blank other than one plain space between words (no-break space, double space, leading or trailing space); `<` or `>`. A command or skill whose directory or file name is refused does not load. In a plugin, only the folder-name characters become hyphens (type the hyphens); a bad frontmatter `name` means the `/` menu does not show it and typing it does not invoke it.

# Notes

Find the refused name with `claude --debug` and search the debug log for `[names]`; interactive sessions also show a startup notice. Restart after a rename unless the directory is watched.
