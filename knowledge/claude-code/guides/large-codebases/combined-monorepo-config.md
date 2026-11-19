---
type: "Guide"
title: "Combined monorepo configuration"
description: "Worked example for packages/api combining sparse worktrees, additionalDirectories and deny rules, with a second deny copy at the root for worktrees."
resource: "https://code.claude.com/docs/en/large-codebases"
tags: [monorepo, worktrees, permissions, settings]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "packages/api/.claude/settings.json"
  - "worktree.sparsePaths"
  - "worktree.symlinkDirectories"
  - "permissions.additionalDirectories"
  - "permissions.deny"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "large-codebases"
    resource: "https://code.claude.com/docs/en/large-codebases"
    title: "Set up Claude Code in a monorepo or large codebase"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The committed `packages/api/.claude/settings.json` sets `worktree.sparsePaths` (`.claude`, `packages/api`, `packages/shared`), `worktree.symlinkDirectories` (`node_modules`), `permissions.additionalDirectories` (`../shared`) and Read deny rules for `dist/` and `build/`.

# How to use it

Because a worktree created from that session has the worktree root as working directory, the per-package file does not load there. Siblings are reachable inside the worktree anyway, but the deny rules need a second copy in the repo root `.claude/settings.json`. Add `claudeMdExcludes` to the root `.claude/settings.local.json` only if you also start from the root.

Result when starting from `packages/api/`: loads root and api CLAUDE.md but not web; can read and edit `packages/api/` and `packages/shared/`; skips `dist/` and `build/` reads; `api-testing` skill available on demand; worktrees contain `.claude/`, `packages/api/`, `packages/shared/` and root-level files with deny rules applied.
