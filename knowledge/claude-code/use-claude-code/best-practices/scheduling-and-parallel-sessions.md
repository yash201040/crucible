---
type: "Feature"
title: "Scheduling runs and parallel worktree sessions"
description: "/loop, /schedule cloud tasks, claude -w worktrees, .worktreeinclude, cleanup, /batch and claude agents (research preview)."
resource: "https://code.claude.com/docs/en/best-practices"
tags: [scheduling, worktrees, parallel, loop, batch]
kind: "mixed"
maturity: "research-preview"
since: ""
surfaces: [cli, desktop, cloud]
requires: "/schedule needs a claude.ai login, not an API key"
identifiers:
  - "/loop"
  - "/schedule"
  - "claude -w"
  - "claude -p --worktree"
  - ".worktreeinclude"
  - "worktree.symlinkDirectories"
  - "cleanupPeriodDays"
  - "/batch"
  - "claude agents"
  - "git worktree remove"
  - "git worktree unlock"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "best-practices"
    resource: "https://code.claude.com/docs/en/best-practices"
    title: "Best practices for Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Something must decide to start a run: you, a timer or an event such as a failed CI check or new PR. Parallel work gets its own checkout so edits cannot collide.

# How to use it

- `/loop 15m check CI on this branch, and if it's red pull the failing job's log, fix it and push` repeats a prompt in an open session; each run is another turn in the same session, so do not leave one in a long conversation.
- `/schedule` sets up a cloud scheduled task (runs while the laptop is closed); add a GitHub-event trigger by asking Claude, or an API trigger at claude.ai/code/routines. Protect `main` with a GitHub branch rule the task cannot bypass, and watch the first runs.
- `claude -w feature-auth` starts a session in a new worktree; the desktop app runs several side by side; cloud sessions run them in the cloud.
- A worktree is a fresh checkout without gitignored files or installed dependencies. List needed gitignored files (e.g. `.env`, `config/dev-credentials.json`) in `.worktreeinclude` at the repo root (`.gitignore` syntax); it copies, not links, so keep it to small files. For large directories use `worktree.symlinkDirectories` or put the install command in CLAUDE.md.
- `/batch migrate every handler to the v2 response helpers` splits work into 5 to 30 units, shows the plan, then each unit gets its own worktree and opens a PR or reports.
- `claude agents` (still a research preview) gives one screen for everything running in the background on your machine.
- A second session reviewing `@src/middleware/rateLimiter.ts` is an independent reviewer; you carry messages between them.

# Limits and defaults

Cleanup: exiting an unnamed worktree session removes a git-created worktree if empty; named or changed sessions ask. Subagent worktrees disappear when the subagent finishes without changes. Leftover subagent and background-session worktrees are swept once older than `cleanupPeriodDays` and holding no work. A `claude -p --worktree` run is cleaned by you with `git worktree remove <path>` (or `git worktree unlock <path>` first if locked).
