---
type: "Reference"
title: "Session picker shortcuts"
description: "Keyboard shortcuts for navigating, searching and widening the interactive session picker."
resource: "https://code.claude.com/docs/en/sessions"
tags: [sessions, picker, shortcuts, ui]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Ctrl+R"
  - "Ctrl+A"
  - "Ctrl+W"
  - "Ctrl+B"
  - "Ctrl+V"
  - "Failed to resume the conversation"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sessions"
    resource: "https://code.claude.com/docs/en/sessions"
    title: "Manage sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Opened by `/resume` or `claude --resume` with no arguments.

# How to use it

| Shortcut | Action |
| :- | :- |
| `↑`/`↓` or `k`/`j` | Navigate |
| `→`/`←` | Expand or collapse grouped sessions |
| `Enter` | Resume highlighted session |
| `1` to `9` | Resume the session at that position |
| `Space` | Preview (`Ctrl+V` also works where terminal does not capture it as paste) |
| `Ctrl+R` | Rename |
| `/` or printable character other than `Space`, `j`, `k`, digit | Search; paste a GitHub, GitHub Enterprise, GitLab or Bitbucket PR/MR URL to find the session that created it |
| `Ctrl+A` | All projects on this machine (toggle) |
| `Ctrl+W` | All worktrees of the repository (toggle; multi-worktree repos only) |
| `Ctrl+B` | Filter to current git branch (toggle) |
| `Esc` | Exit picker or search |

# Notes

Rows show name (else AI title, summary or first prompt), time since activity, git branch, file size. Sessions from `/branch` or `--fork-session` are separate rows, grouped under one row if duplicates exist. If a session picked from `claude --resume` cannot load, it prints `Failed to resume the conversation` with a retry command and exits 1; from `/resume` the current conversation keeps running.
