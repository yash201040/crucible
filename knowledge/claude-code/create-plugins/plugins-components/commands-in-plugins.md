---
type: "Feature"
title: "Commands in a plugin"
description: "The older single-file command format: commands/<file>.md, subdirectory naming, and defining commands inline in the manifest."
resource: "https://code.claude.com/docs/en/plugins/components"
tags: [plugins, commands, manifest]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "commands/<file>.md"
  - "commands"
  - "source"
  - "content"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-components"
    resource: "https://code.claude.com/docs/en/plugins/components"
    title: "Add components to a plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A command is one Markdown file the user runs by name. Commands are the older format and skills supersede them for new work; keep `commands/` for files moved over from `.claude/commands/`. Command files take the same frontmatter as skills.

# How to use it

`commands/<file>.md` becomes `/<plugin>:<file>`; a subdirectory adds a segment, so `commands/db/migrate.md` is `/my-plugin:db:migrate`.

The `commands` manifest key replaces the `commands/` scan. It takes a path, an array of paths, or an object mapping each command name to either a `source` file or inline `content` (plus `description`). Example: `"commands": { "about": { "content": "Summarize...", "description": "Summarize the repository" } }` defines `/my-plugin:about` with no Markdown file.
