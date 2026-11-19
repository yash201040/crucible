---
type: "Reference"
title: "worktree settings"
description: "The worktree object: base ref, symlinked dirs, sparse checkout, background-session isolation and the desktop SSH location."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, worktrees, isolation, background-sessions]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop]
requires: ""
identifiers:
  - "worktree"
  - "worktree.baseRef"
  - "worktree.symlinkDirectories"
  - "worktree.sparsePaths"
  - "worktree.bgIsolation"
  - "worktree.location"
  - "--worktree"
  - "EnterWorktree"
  - ".worktreeinclude"
  - "WorktreeCreate"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`worktree` (any file, default unset) configures git worktrees for `--worktree`, the `EnterWorktree` tool, isolated subagents and background sessions. Fields: `baseRef`, `symlinkDirectories`, `sparsePaths`, `bgIsolation` (and desktop-only `location`). To copy gitignored files such as `.env` into new worktrees use a `.worktreeinclude` file in the project root, not a setting.

# How to use it

| Key | Values | Default | What it does |
| :- | :- | :- | :- |
| `worktree.baseRef` | `"fresh"` (branch from `origin/<default-branch>`) or `"head"` (current local `HEAD`, incl. unpushed commits) | `"fresh"` | Inside a linked worktree `"head"` resolves to that worktree's `HEAD` |
| `worktree.symlinkDirectories` | array of repo-relative paths | unset | Symlink dirs (for example `node_modules`, `.cache`) from the main repo into each worktree |
| `worktree.sparsePaths` | array of repo-relative dirs | unset (full tree) | Git sparse-checkout: only those dirs plus root-level files. Include `.claude` to get `.claude/settings.json` and `.claude/rules/`. Git enables `extensions.worktreeConfig` in the shared `.git/config` while a sparse worktree exists |
| `worktree.bgIsolation` | `"worktree"` or `"none"` | `"worktree"` | `"worktree"` blocks `Edit` and `Write` in the main checkout until the session calls `EnterWorktree`; `"none"` lets background jobs edit the working copy. A session moved to background with `←` or `/background` edits in place regardless. Outside a git repo a failing `WorktreeCreate` hook releases the block |
| `worktree.location` | absolute path or `~/` path; user scope on the remote machine | unset | Folder for Desktop SSH session worktrees instead of `<project-root>/.claude/worktrees/`. Only the desktop app reads it (needs Claude Desktop v1.44121.0+); the CLI paths ignore it. A Worktree folder set on the SSH connection wins; org folder restrictions keep worktrees inside the project |
