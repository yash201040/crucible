---
type: "Feature"
title: ".worktreeinclude and reusing worktree names"
description: "Copy gitignored files into new worktrees with .worktreeinclude; reopen vs reset rules when a name is reused; WorktreeCreate hook replaces it."
resource: "https://code.claude.com/docs/en/worktrees"
tags: [worktrees, worktreeinclude, env-files, reuse]
kind: "file"
maturity: "unlabelled"
since: "2.1.239"
surfaces: [cli, desktop]
requires: ""
identifiers:
  - ".worktreeinclude"
  - "WorktreeCreate"
  - "WorktreeRemove"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "worktrees"
    resource: "https://code.claude.com/docs/en/worktrees"
    title: "Run parallel sessions with worktrees"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A `.worktreeinclude` file at the project root uses `.gitignore` syntax; only files that match a pattern and are also gitignored are copied into each new worktree (tracked files are never duplicated). It applies to every git-created worktree: `--worktree`, subagent worktrees and desktop-app parallel sessions. With a `WorktreeCreate` hook it is not processed; copy files inside the hook script.

# How to use it

```text
.env
.env.local
config/secrets.json
```

`**/` patterns inside a wholly ignored directory copy only when that directory matches, or when the first name after `**/` is a name in the directory's path (`**/.claude/skills/*.md` copies from an ignored `.claude/`). Otherwise name the directory: `vendor/**/config.json` not `**/config.json`. Before v2.1.239 only the directory-matches case copied.

Reusing a name: if the `--worktree` name exists, Claude Code opens it. With the `"fresh"` base it resets to the default branch instead of its old tip only when ALL hold: the sandbox is not restricting file writes and neither `.claude` settings file enables it; no uncommitted or untracked files; still on its Claude-created branch; no commits of its own, or its PR/MR was merged and remote branch deleted (detected from git state: remote branch gone and every commit already on the default branch).

# Limits and defaults

Otherwise it reopens at the old tip: a failed condition, unverifiable state, `worktree.baseRef` `"head"`, or a PR/MR reference name. With the sandbox and `"fresh"`, run `git fetch origin` and pass a new name to start from the latest default. Errors `belongs to a different repository` / `is a leftover worktree`: see troubleshooting.
