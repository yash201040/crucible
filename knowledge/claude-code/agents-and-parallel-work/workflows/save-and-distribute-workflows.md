---
type: "Feature"
title: "Saving, sharing and parameterizing workflows"
description: "Save a run's script as /<name> in .claude/workflows/ or ~/.claude/workflows/, ship it in a plugin, and pass input via args."
resource: "https://code.claude.com/docs/en/workflows"
tags: [workflows, save, plugins, args, reuse]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop]
requires: ""
identifiers:
  - ".claude/workflows/"
  - "~/.claude/workflows/"
  - "CLAUDE_CONFIG_DIR"
  - "workflows/"
  - "meta.name"
  - "args"
  - "workflows"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "workflows"
    resource: "https://code.claude.com/docs/en/workflows"
    title: "Orchestrate subagents at scale with dynamic workflows"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Saved workflows run as `/<name>` in future sessions and appear in `/` autocomplete.

# How to use it

Save: `/workflows`, select the run, press `s`; Tab toggles location, Enter saves.
- `.claude/workflows/` in the project (shared via the repo).
- `~/.claude/workflows/` (all projects, only you); under `$CLAUDE_CONFIG_DIR/workflows/` when `CLAUDE_CONFIG_DIR` is set.

Plugin: put the script in `workflows/` at the plugin root or point elsewhere with the `workflows` manifest field. Plugin workflows are namespaced: `meta.name` `release-audit` in plugin `acme-tools` runs as `/acme-tools:release-audit`.

Input: a saved workflow reads the global `args` (structured data; `undefined` if omitted). Example: `Run /triage-issues on issues 1024, 1025, and 1030`.

# Limits and defaults

- Symlink checks: project location is refused if `.claude`, `.claude/workflows` or the target file is a symlink; personal location only if the target file is a symlink.
- Monorepo: saving writes to the closest existing `.claude/workflows/` between the working directory and repo root (or the repo root); project workflows load from every `.claude/workflows/` along that path, closest wins on name clash. A project workflow beats a personal one of the same name.
