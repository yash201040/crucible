---
type: "Feature"
title: "WorktreeRemove hook event"
description: "Cleans up worktrees that a WorktreeCreate hook made; exit code decides success, with git fallback rules."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, worktree, cleanup, isolation]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "WorktreeRemove"
  - "worktree_path"
  - "ExitWorktree"
  - "discard_changes"
  - "claude rm"
  - "worktree removal failed, kept: <path>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs when Claude Code cleans up a worktree your WorktreeCreate hook created. Input adds `worktree_path` (the path WorktreeCreate returned).

Fires when: you exit an interactive worktree session and choose removal; you exit an un-named session with no changed or untracked files (removed without prompting); you delete a background session in that worktree; Claude removes it with `ExitWorktree`; a `claude remote-control` worktree-mode session ends without crashing, or remote-control is stopped, and no changed or untracked files and no new commits are found (runs without prompting).

# How to use it

Pair it with WorktreeCreate. Example: `bash -c 'p=$(jq -er .worktree_path) && rm -rf -- "$p"'`.

Outcomes:
- Hook exits 0: counts as removed; Claude Code reads nothing else, so make sure the hook deleted the directory.
- Hook exits non-zero: removal fails if the directory at `worktree_path` still exists afterward, with no git fallback; if the directory was deleted first it counts as removed. A background-session delete then keeps the session too (agent view reports how the hook ended, e.g. `exited 1`, quotes the start of stderr); `claude remote-control` shows `worktree removal failed, kept: <path>`.
- No WorktreeRemove hook: exit or `ExitWorktree` falls back to git (as `git worktree remove --force`; a worktree git does not recognize, such as non-git VCS, stays); `claude remote-control` keeps the worktree.

# Limits and defaults

- When a subagent or workflow agent finishes, Claude Code keeps the worktree your hook made for it and does not run WorktreeRemove; remove those yourself.
- `ExitWorktree` refuses to remove a hook-created worktree unless called with `discard_changes: true`.
- Claude Code uses git to look for changed or untracked files, so it finds none in a non-git worktree even with uncommitted work; check inside your hook before deleting.
- Claude Code never deletes the branch of a hook-created worktree; delete it in your hook. JSON output (`systemMessage`, `continue`) is discarded.
- Background-session delete: the stored path is verified first (symlink or path through one below the repo root is refused); the hook runs for a worktree that still has files only when you confirm in agent view; `claude rm` keeps the session and worktree instead.
