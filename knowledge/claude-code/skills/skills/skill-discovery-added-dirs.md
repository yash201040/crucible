---
type: "Feature"
title: "Skill discovery in subdirectories and added dirs"
description: "How project skills load from parent, nested, worktree and --add-dir directories, and how same-named skills get prefixed."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, monorepo, worktrees, add-dir]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.246"
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "/add-dir"
  - "--add-dir"
  - "/cd"
  - "additionalDirectories"
  - "add_dirs"
  - "permissions.additionalDirectories"
  - "strictPluginOnlyCustomization"
  - "--safe-mode"
  - "/apps/web:deploy"
  - "/<prefix>:<skill-name>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Rules for which project skills a session finds beyond the starting directory.

# How to use it

- Project skills load from `.claude/skills/` in the start directory and every parent up to the repository root. `/cd` (v2.1.246 or later) adds the new directory's project skills.
- In a linked git worktree (`--worktree` or `git worktree add`), parents are searched only up to the worktree root. From v2.1.277, if the worktree has no `.claude/skills` at its root, the main checkout's project skills load.
- Skills in a `.claude/skills/` below the start directory load the first time Claude reads or edits a file there; until then they are not in the `/` menu. `/add-dir <path>` loads them sooner (v2.1.257 or later).
- Same-named nested skill: with `deploy` at the root and in `apps/web/.claude/skills/`, `/deploy` runs the root one (Claude is also told about directory-qualified variants) and `/apps/web:deploy` runs the nested one.
- `--add-dir` / `/add-dir` loads that directory's `.claude/skills/`, `.claude/commands/` and `.claude/agents/`. The Agent SDK's `additionalDirectories` (TypeScript) and `add_dirs` (Python) behave the same since they pass `--add-dir`. The `permissions.additionalDirectories` setting grants file access only and loads none of these.
- Only `.claude/skills/` of an added directory is watched for changes; restart after changing its commands or agents.
- Prefixed names (v2.1.309 or later): a clashing skill from an added directory runs as `/<prefix>:<skill-name>`, e.g. `--add-dir ../cli` gives `/cli:verify`.

# Limits and defaults

Added-directory loading depends on the `project` setting source (on by default); a `strictPluginOnlyCustomization` policy, bare mode and `--safe-mode` restrict it further.
