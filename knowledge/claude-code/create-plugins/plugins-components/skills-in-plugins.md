---
type: "Feature"
title: "Skills in a plugin"
description: "Put a SKILL.md in its own directory under skills/ to ship a skill, with command naming, extra directories, and root-skill rules."
resource: "https://code.claude.com/docs/en/plugins/components"
tags: [plugins, skills, naming]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "skills/<name>/SKILL.md"
  - "skills"
  - "description"
  - "name"
  - "CLAUDE.md"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-components"
    resource: "https://code.claude.com/docs/en/plugins/components"
    title: "Add components to a plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A skill is a `SKILL.md` file Claude loads when its `description` matches the task; the user can also run it as a command. Each skill goes in its own directory under `skills/`.

# How to use it

- Command name is `/<plugin>:<directory>`, so `skills/review/SKILL.md` in `my-plugin` is `/my-plugin:review`. A frontmatter `name` replaces only the last segment; the plugin prefix stays.
- Who can invoke it (Claude, the user or both) is set by frontmatter.
- Extra directories: list them in the `skills` manifest key. They add to the default `skills/` scan, unlike `commands` and `agents` which replace.
- A single skill at the plugin root: with no `skills/` directory and no `skills` key, a root `SKILL.md` loads as one skill. Set `name` in its frontmatter, otherwise a marketplace install names it after the cache directory.

# Limits and defaults

- Claude Code does not load a `CLAUDE.md` at the plugin root; `claude plugin validate` warns `CLAUDE.md at the plugin root is not loaded as project context`. To ship instructions, write them as a skill.
- A rule that must hold every time (for example blocking edits to protected files) belongs in a hook, not a skill.
