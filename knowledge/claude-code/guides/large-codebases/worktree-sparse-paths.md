---
type: "Feature"
title: "Sparse worktrees"
description: "worktree.sparsePaths uses git sparse-checkout so created worktrees hold only listed directories; symlinkDirectories avoids duplicating node_modules."
resource: "https://code.claude.com/docs/en/large-codebases"
tags: [worktrees, sparse-checkout, subagents, isolation]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "git with extensions.worktreeConfig enabled while a sparse worktree exists"
identifiers:
  - "--worktree"
  - "worktree.sparsePaths"
  - "worktree.symlinkDirectories"
  - "extensions.worktreeConfig"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "large-codebases"
    resource: "https://code.claude.com/docs/en/large-codebases"
    title: "Set up Claude Code in a monorepo or large codebase"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`--worktree` starts a session in a new git worktree, checking out the whole repo by default. `worktree.sparsePaths` writes only the listed directories plus root-level files to disk, so worktrees start faster and use less space. This is especially useful for subagent worktree isolation: each subagent in a worktree gets a lightweight checkout.

# How to use it

```json
{ "worktree": {
  "sparsePaths": [".claude", "packages/api", "packages/shared"],
  "symlinkDirectories": ["node_modules"] } }
```

`symlinkDirectories` symlinks each worktree's `node_modules/` to the main repo's copy instead of duplicating it.

# Limits and defaults

- Paths are relative to the repo root regardless of launch subdirectory; list directories, not files.
- Root-level files (`package.json`, `tsconfig.base.json`, lock files) are always checked out; root-level directories are not, so include `.claude` to have the root `.claude/settings.json` or `.claude/rules/` in the worktree.
- All worktrees in a session share the same `sparsePaths`; list every directory any subagent needs.
- Commit to `.claude/settings.json` for everyone; `.claude/settings.local.json` lists merge across scopes, so local can add paths but not remove committed ones.
- Claude Code removes the `extensions.worktreeConfig` entry after the last worktree is removed, only if it added it.

# Notes

Both settings are read from the starting directory before the worktree is created. Afterward the working directory is the worktree root, so project settings load from the worktree root's `.claude/settings.json` (the checked-out copy of the repo root file). Put permission rules or hooks needed in worktrees in the root `.claude/settings.json`.
