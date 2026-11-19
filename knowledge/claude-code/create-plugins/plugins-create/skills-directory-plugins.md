---
type: "Feature"
title: "Skills-directory plugins and plugin init"
description: "A folder with .claude-plugin/plugin.json under ~/.claude/skills/ auto-loads every session; claude plugin init scaffolds one."
resource: "https://code.claude.com/docs/en/plugins/create"
tags: [plugins, skills-dir, init, scaffolding]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin init"
  - "--with skills"
  - "claude plugin disable"
  - "~/.claude/skills/"
  - "<project>/.claude/skills/<name>/"
  - "my-tool@skills-dir"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-create"
    resource: "https://code.claude.com/docs/en/plugins/create"
    title: "Create a Claude Code plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A folder under `~/.claude/skills/` containing `.claude-plugin/plugin.json` is a skills-directory plugin; Claude Code loads each at session start with no flag or install (unless an administrator blocked skills-directory plugins). `claude plugin init my-tool` creates `~/.claude/skills/my-tool/` with a manifest and root `SKILL.md`, prints `It will auto-load next session as my-tool@skills-dir. Run /reload-plugins to load it now.`

# How to use it

- `--with skills` scaffolds a skill under `skills/` too; other `--with` values are on the CLI reference.
- The root skill is also a personal skill, invoked `/my-tool` not `/my-tool:my-tool`; skills under `skills/` get the prefix (`/my-tool:example`).
- Stop loading: delete the directory or run `claude plugin disable my-tool@skills-dir` (`skills-dir` stands where a marketplace name would).
- Per-repository: create the same layout at `<project>/.claude/skills/<name>/` including `.claude-plugin/plugin.json`.
