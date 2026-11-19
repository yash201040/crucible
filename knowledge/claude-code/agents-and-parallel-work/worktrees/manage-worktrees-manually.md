---
type: "Guide"
title: "Managing worktrees manually with git"
description: "Create, list and remove worktrees with git worktree commands when you need a specific branch or an outside location."
resource: "https://code.claude.com/docs/en/worktrees"
tags: [worktrees, git, manual]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "git worktree add"
  - "git worktree list"
  - "git worktree remove"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "worktrees"
    resource: "https://code.claude.com/docs/en/worktrees"
    title: "Run parallel sessions with worktrees"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Use git directly to check out a specific existing branch or place a worktree outside the repository.

# How to use it

```bash
git worktree add ../project-feature-a -b feature-a   # new branch
git worktree add ../project-bugfix fix-issue-456      # existing branch
cd ../project-feature-a && claude
git worktree list
git worktree remove ../project-feature-a
```
