---
type: "Concept"
title: "Where the session picker looks"
description: "Which sessions the picker and --continue list, and which they hide: /loop, -p, SDK and running background sessions."
resource: "https://code.claude.com/docs/en/sessions"
tags: [sessions, picker, worktrees, headless, sdk]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.257"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "claude -p --continue"
  - "claude --continue"
  - "/loop"
  - "/cd"
  - "/add-dir"
  - "claude agents"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sessions"
    resource: "https://code.claude.com/docs/en/sessions"
    title: "Manage sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Sessions are stored per project directory. By default the picker shows sessions from the current worktree (background sessions are marked `bg`) and sessions started elsewhere that added the current directory with `/add-dir`. `Ctrl+W` widens to all worktrees; `Ctrl+A` to every project.

# How to use it

- Hidden from the picker and from `claude --continue`: sessions whose first prompt was a `/loop` command (running `/loop` later does not hide), and sessions created by `claude -p` or the Agent SDK. They can be resumed with `claude --resume <session-id>`. `claude -p --continue` includes `-p`, SDK and `/loop` sessions.
- `claude --continue` opens a finished background session (v2.1.257 or later) but not a running one: if the most recent conversation is still running in the background it exits with `Your most recent conversation is running in the background` and the ID. Attach from `claude agents`, or run `claude --resume`.
- Selecting a session from another worktree of the same repo resumes it in place; if its worktree no longer exists it resumes in the current directory. A session from an unrelated project copies a `cd` and resume command to the clipboard (or resumes in the current directory if that project's directory is gone).
- `/cd` relocates a session to the new directory's project storage.
