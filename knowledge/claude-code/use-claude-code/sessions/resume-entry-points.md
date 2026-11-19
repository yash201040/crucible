---
type: "Reference"
title: "Resume entry points"
description: "The commands and flags that reopen a saved session: --continue, --resume, --from-pr and /resume."
resource: "https://code.claude.com/docs/en/sessions"
tags: [sessions, resume, continue, cli]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude --continue"
  - "claude --resume"
  - "claude --resume <name>"
  - "claude --resume <session-id>"
  - "claude --resume <transcript-path>"
  - "claude --from-pr <number>"
  - "/resume"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sessions"
    resource: "https://code.claude.com/docs/en/sessions"
    title: "Manage sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A session is a saved conversation tied to a project directory, stored locally and saved continuously. The page covers the CLI; the desktop app, claude.ai/code and the VS Code extension keep their own session lists (the desktop app can also resume a CLI session).

# How to use it

| Command | What it does |
| :- | :- |
| `claude --continue` | Reopens the most recent session in the current directory |
| `claude --resume` | Opens the session picker |
| `claude --resume <name>` | Resumes the named session directly |
| `claude --resume <session-id>` | Resumes the session with that ID |
| `claude --resume <transcript-path>` | Resumes the session in the `.jsonl` transcript at that absolute path |
| `claude --from-pr <number>` | Session picker filtered to sessions linked to that pull request |
| `/resume` | Switch to a different session inside an active session |

# Notes

See [resume by ID or name](./resume-by-id-or-name.md), [what a resume restores](./what-a-resume-restores.md) and [the picker](./session-picker-scope.md).
