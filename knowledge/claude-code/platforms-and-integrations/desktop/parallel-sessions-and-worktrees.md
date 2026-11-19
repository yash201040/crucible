---
type: "Feature"
title: "Parallel sessions, worktrees and cross-session control"
description: "Run many sessions side by side, isolate them in Git worktrees, use side chats, watch background tasks, and let Claude message other sessions."
resource: "https://code.claude.com/docs/en/desktop"
tags: [desktop, parallel-sessions, worktrees, side-chat, cross-session]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [desktop]
requires: "Git for worktrees"
identifiers:
  - "/btw"
  - ".claude/worktrees/"
  - ".worktreeinclude"
  - "crossSessionInbound"
  - "worktree.location"
  - "Worktree location"
  - "Branch prefix"
  - "Auto-archive after PR merge or close"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "desktop"
    resource: "https://code.claude.com/docs/en/desktop"
    title: "Desktop application"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each session is independent. Desktop supports parallel sessions (sidebar, split view, own window), per-session Git worktrees, side chats, a background tasks pane, and Claude-driven management of other sessions.

# How to use it

- **Parallel**: Cmd/Ctrl+N; Option/Alt-click a session for split view; Cmd/Ctrl-click for a new window.
- **Worktree**: turn on **Worktree** before starting a session in a Git repo (off by default). Stored in `<project-root>/.claude/worktrees/`; change with **Worktree location** (local) or **Worktree folder** (SSH); **Branch prefix** is prepended to branch names. Copy gitignored files with a `.worktreeinclude` file.
- **Add folders**: **+** > **Add folder** in local or SSH sessions (no worktree for them).
- **Archive**: session menu > Archive. Uncommitted worktree changes can be lost; if not prompted, the worktree and session are removed about 30 days after archive or last open (local); **Unarchive** restores.
- **Side chat**: Cmd/Ctrl+; or `/btw`; reads the main thread, writes nothing back; local, SSH and WSL only; not saved to disk.
- **Background tasks pane**: shows subagents, background shell commands and dynamic workflows; click an entry for output or to stop it.
- **Work across sessions**: ask Claude to list, read, message, rename or archive other Desktop sessions (local, SSH, WSL; not cloud, CLI or VS Code sessions). Sees the 20 most recently active; archive asks approval except in Auto and Bypass permissions modes. Messages are quoted with the sender session, held until the receiver's current work finishes, and checked against `crossSessionInbound` (`refuse` drops them; before v2.1.234 all such messages were dropped when the receiver lacked cross-session messaging).
- **Suggested tasks**: cards with **Start**, **Do it here**, **Options**, **Start all** (each task in its own session).
- OS notification when a session finishes and you are not viewing it.

# Limits and defaults

Agent teams are CLI only; Desktop uses dynamic workflows. The `worktree.baseRef`, `worktree.sparsePaths`, `worktree.symlinkDirectories` keys are not used for Code tab worktrees.
