---
type: "Feature"
title: "Resuming a worktree session"
description: "Resumed sessions return to their worktree (interactive, -p --continue/--resume, SDK) after verification; launch-directory and fork rules."
resource: "https://code.claude.com/docs/en/worktrees"
tags: [worktrees, resume, sessions, headless]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.212"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "--resume"
  - "--continue"
  - "--fork-session"
  - "/cd"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "worktrees"
    resource: "https://code.claude.com/docs/en/worktrees"
    title: "Run parallel sessions with worktrees"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Resuming a session that ended inside a worktree without exiting it returns the session to that worktree: interactive resume, `--continue` and `--resume` with `-p`, and the Agent SDK. `--continue` picks the most recent session recorded under the launch directory. Before returning, Claude Code verifies the worktree is still a separate checkout and declines otherwise. A worktree with no git metadata (e.g. from a `WorktreeCreate` hook) can pass.

# How to use it

- Launch directory: resume with `--resume` from the main checkout or another directory of the repository. A git-created worktree under `.claude/worktrees/` is re-entered even when launching from inside it. Launching from inside any other worktree re-enters only if Claude Code can vouch for it; a worktree that is its own repository, one without git metadata, or a launch from a subdirectory of a `git worktree add` worktree declines, so launch those from the main checkout.
- `--fork-session`: the fork starts in the launch directory; the original worktree is untouched.
- Deleted worktree: resumes in the launch directory, says the worktree is gone and clears the binding.
- Entering/exiting a git-created worktree moves the transcript to the new working directory (as `/cd` does) so `/desktop` and `--resume` find it. A `WorktreeCreate`-hook worktree keeps its transcript at the launch directory.

# Limits and defaults

Before v2.1.212, a non-interactive resume stayed in the starting directory and `ExitWorktree` reported no active worktree session.
