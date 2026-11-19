---
type: "Guide"
title: "Resume across hosts and session helper functions"
description: "Three ways to resume on a different host and the functions for listing, reading and mutating sessions."
resource: "https://code.claude.com/docs/en/agent-sdk/sessions"
tags: [sessions, hosts, ci, session-store]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "sessionStore"
  - "session_store"
  - "listSessions()"
  - "getSessionMessages()"
  - "list_sessions()"
  - "get_session_messages()"
  - "getSessionInfo()"
  - "renameSession()"
  - "tagSession()"
  - "get_session_info()"
  - "rename_session()"
  - "tag_session()"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-sessions"
    resource: "https://code.claude.com/docs/en/agent-sdk/sessions"
    title: "Work with sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Session files are local to the machine that made them. Options for CI workers, ephemeral containers, serverless:
- Pass a `sessionStore` / `session_store` adapter (resume from a `cwd` matching the original run's).
- Move the file: persist `~/.claude/projects/<encoded-cwd>/<session-id>.jsonl` and restore it under any directory in `~/.claude/projects/` on the new host before `resume`.
- Do not rely on resume: capture results as application state and pass them into a fresh session's prompt (often more robust).

# How to use it

| Purpose | TypeScript | Python |
| :- | :- | :- |
| List sessions | `listSessions()` | `list_sessions()` |
| Read messages | `getSessionMessages()` | `get_session_messages()` |
| Look up one | `getSessionInfo()` | `get_session_info()` |
| Rename | `renameSession()` | `rename_session()` |
| Tag | `tagSession()` | `tag_session()` |

Use them for custom session pickers, cleanup logic, transcript viewers, organizing by tag or title.
