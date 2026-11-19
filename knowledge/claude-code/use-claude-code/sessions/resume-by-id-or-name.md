---
type: "Feature"
title: "Resume by session ID or name"
description: "Lookup order for session IDs across projects and how exact and ambiguous names resolve."
resource: "https://code.claude.com/docs/en/sessions"
tags: [sessions, resume, ids, names]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude --resume <session-id>"
  - "claude --resume <name>"
  - "/resume <name>"
  - "No conversation found with session ID: <session-id>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sessions"
    resource: "https://code.claude.com/docs/en/sessions"
    title: "Manage sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude --resume <session-id>` works from any directory. Lookup order: (1) the current project directory and its worktrees, (2) every other project on the machine. The cross-project search resolves the ID only when exactly one other project holds a transcript with messages for it, so a hand-copied duplicate yields not-found. No match prints `No conversation found with session ID: <session-id>`.

# How to use it

Names resolve across the current repository and its worktrees; an exact match resumes directly even in another worktree.

| Command | Exact match | Ambiguous name |
| :- | :- | :- |
| `claude --resume <name>` | Resumes directly | Opens the picker with the name pre-filled as search |
| `/resume <name>` | Resumes directly | Error; run `/resume` with no argument for the picker |
