---
type: "Feature"
title: "EnterWorktree tool behavior"
description: "Creates or enters a git worktree; prompt rules for paths outside .claude/worktrees and when the tool is removed."
resource: "https://code.claude.com/docs/en/tools-reference#enterworktree-tool-behavior"
tags: [worktree, isolation, tools, permissions]
kind: "tool"
maturity: "unlabelled"
since: "2.1.206"
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "EnterWorktree"
  - "ExitWorktree"
  - "path"
  - "permissions.blockWritesOutsideWorkingDirectories"
  - ".claude/worktrees/"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`EnterWorktree` creates an isolated git worktree and switches into it. Given a `path` it switches into an existing worktree instead.

# How to use it

- First entry may target a worktree of the current repository, or of a repository nested inside it.
- A `path` outside `.claude/worktrees/` prompts for approval (before v2.1.206 it did not); creating a new worktree or using paths under `.claude/worktrees/` does not prompt.
- From inside a worktree only the `path` form is available, and the target must be under `.claude/worktrees/` of the session's repository. Same for a subagent with a pinned working directory such as `isolation: worktree`.

# Limits and defaults

When `permissions.blockWritesOutsideWorkingDirectories` is on, `EnterWorktree` and `ExitWorktree` are removed or calls refused (see the worktrees page, "Claude has no EnterWorktree tool").
