---
type: "Feature"
title: "Worktree cleanup on exit"
description: "What happens to a worktree when an interactive session exits, and why -p runs leave worktrees behind."
resource: "https://code.claude.com/docs/en/worktrees"
tags: [worktrees, cleanup, exit, headless, locks]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "git worktree remove"
  - "git worktree unlock"
  - "claude --worktree <name> --resume"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "worktrees"
    resource: "https://code.claude.com/docs/en/worktrees"
    title: "Run parallel sessions with worktrees"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

On exiting an interactive worktree session Claude checks for work removal would delete: changed or untracked files, uncommitted work in checked-out submodules, and new commits. Applies to worktrees Claude created with git; a worktree made by a `WorktreeCreate` hook is handled by `WorktreeRemove`.

# How to use it

| State | Result |
| :- | :- |
| Clean | Unnamed session: removed automatically with its branch. Named session: prompts first |
| Has work | Prompts keep or remove. Keep preserves directory and branch (return with the `claude --worktree <name> --resume` command printed on exit). Remove deletes the directory, its branch and all work |
| Another branch checked out, with commits past the starting commit | Prompts; either answer keeps that other branch and commits; remove deletes the directory and the worktree's own branch |
| State cannot be verified | Prompts, naming what could not be checked |

# Limits and defaults

- Non-interactive `-p` runs have no exit prompt: Claude does not clean up their worktrees, and the lock taken at creation stays until a later session's stale-lock sweep. Remove with `git worktree remove` (run `git worktree unlock` first if git refuses because it is locked).
- On Windows, removal deletes only a link (NTFS junction or directory symlink) inside the worktree, not its target.
