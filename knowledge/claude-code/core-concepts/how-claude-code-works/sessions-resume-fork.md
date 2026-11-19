---
type: "Feature"
title: "Sessions, resume and fork"
description: "Conversations are stored as local JSONL; resume reuses the session ID, fork copies history into a new ID; worktrees give parallel sessions."
resource: "https://code.claude.com/docs/en/how-claude-code-works"
tags: [sessions, resume, fork, worktrees, jsonl]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude --continue"
  - "claude --resume"
  - "--fork-session"
  - "/branch"
  - "/resume"
  - "~/.claude/projects/"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "how-claude-code-works"
    resource: "https://code.claude.com/docs/en/how-claude-code-works"
    title: "How Claude Code works"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each message, tool use and result is written to a plaintext JSONL file under `~/.claude/projects/`, enabling rewind, resume and fork. Before code changes Claude snapshots the affected files. Sessions are independent: a new session starts with a fresh context window; cross-session learning comes from auto memory and CLAUDE.md.

# How to use it

| Action | Command | Effect |
| - | - | - |
| Resume | `claude --continue` or `claude --resume` | Reopens under the same session ID, appends to the conversation |
| Fork | `--fork-session` or `/branch` | Copies history into a new session ID; original unchanged |
| Picker | `/resume` | Shows sessions from the current worktree by default, with shortcuts to widen to other worktrees or projects |

Each conversation is tied to the current directory. Switching branches shows the new branch's files but conversation history stays. Parallel sessions use git worktrees (separate directories per branch).

# Notes

Paths, retention and clearing are covered in the application data page; picker shortcuts and the two-terminals case in "Manage sessions".
