---
type: "Feature"
title: "Non-git version control via WorktreeCreate hooks"
description: "WorktreeCreate and WorktreeRemove hooks replace git worktree logic for SVN, Perforce, Mercurial and enable /batch outside git."
resource: "https://code.claude.com/docs/en/worktrees"
tags: [worktrees, hooks, svn, batch, non-git]
kind: "hook"
maturity: "unlabelled"
since: "2.1.281"
surfaces: [cli]
requires: ""
identifiers:
  - "WorktreeCreate"
  - "WorktreeRemove"
  - "/batch"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "worktrees"
    resource: "https://code.claude.com/docs/en/worktrees"
    title: "Run parallel sessions with worktrees"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A `WorktreeCreate` hook replaces the default git logic entirely, including placing worktrees somewhere other than `.claude/worktrees/`. Pair it with `WorktreeRemove` for cleanup. Because it replaces git behavior, `.worktreeinclude` is not processed; copy local config in the hook script.

# How to use it

The hook reads the worktree name as JSON on stdin (`jq -r .name`), creates the working copy, and prints the directory path on stdout so Claude Code uses it as the working directory. Example in `settings.json`: a `command` hook that runs `svn checkout https://svn.example.com/repo/trunk "$HOME/.claude/worktrees/$NAME"` (output of svn sent to stderr) and echoes the directory.

A `WorktreeCreate` hook also lets `/batch` run outside a git repository: each `/batch` subagent publishes its change with the project's VCS commands and, if it cannot open a pull request, reports what it published. Requires v2.1.281 or later.

# Limits and defaults

- Hook-created worktrees have no git metadata marker, so the cleanup sweep keeps them. A directory with no git metadata passes the isolation check only when no git repository contains it; create hook directories outside any repository.
- If the hook prints something other than the created directory, or the directory was deleted, Claude Code prints an error naming the path and exits with code 1 at startup.
