---
type: "Reference"
title: "Where skills live"
description: "Skill locations (enterprise, personal, project, nested, added directory, plugin, claude.ai) with paths and what each loads in, plus folder rules."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, locations, scope, plugins]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli, cloud]
requires: ""
identifiers:
  - ".claude/skills/<skill-name>/SKILL.md"
  - "~/.claude/skills/<skill-name>/SKILL.md"
  - "<subdir>/.claude/skills/<skill-name>/SKILL.md"
  - "<plugin>/skills/<skill-name>/SKILL.md"
  - ".claude/commands/"
  - "~/.claude/skills/synced/"
  - ".claude-plugin/plugin.json"
  - "<name>@skills-dir"
  - "--add-dir"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Where a skill is saved decides which sessions load it.

# How to use it

| Location | Path | Loads in |
| :- | :- | :- |
| Enterprise | `.claude/skills/<skill-name>/SKILL.md` in the managed settings directory | all users where the org deploys it |
| Personal | `~/.claude/skills/<skill-name>/SKILL.md` | all your projects on this machine; not Cowork or cloud sessions |
| Project | `.claude/skills/<skill-name>/SKILL.md` | sessions in the repo; not cloud threads in a project |
| Nested | `<subdir>/.claude/skills/<skill-name>/SKILL.md` | sessions in or below `<subdir>`; a session above loads it once Claude works on files there |
| Additional directory | `.claude/skills/<skill-name>/SKILL.md` in a `--add-dir` directory | that session |
| Plugin | `<plugin>/skills/<skill-name>/SKILL.md` | where the plugin is enabled, as `/plugin-name:skill-name` |
| claude.ai account | skills enabled for your account | Cowork, cloud sessions, and terminal sessions signed in with that account |

# Limits and defaults

- Symlinks: a `<skill-name>` entry in enterprise, personal or project location may symlink elsewhere; loaded once even if several point at one target. Plugin skills handle symlinks differently.
- Reserved folder name `synced` (any capitalization): skipped in enterprise, personal and project locations; `~/.claude/skills/synced/` is for claude.ai downloads.
- Outside a plugin, a folder or command named `anthropic-skills` or starting `anthropic-skills:` does not load.
- Outside a plugin, a folder name with a zero-width space, `<` etc. does not load (see [invalid names](./skill-name-rules.md)).
- `.claude/commands/` Markdown files still work, with the same frontmatter except `name` and `paths`.
- A personal or project skill folder can be a plugin by adding `.claude-plugin/plugin.json`, loaded as `<name>@skills-dir` with its own agents, hooks and MCP servers. In a project's `.claude/skills/` it requires accepting the workspace trust dialog, and in either place that admins have not blocked skills-directory plugins.
