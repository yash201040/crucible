---
type: "Reference"
title: "Context commands in a session"
description: "/clear, /compact and /context control what is in the context window without leaving the session."
resource: "https://code.claude.com/docs/en/sessions"
tags: [context, clear, compact, sessions]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/clear"
  - "/clear <name>"
  - "/compact"
  - "/compact [instructions]"
  - "/context"
  - "--name"
  - "/rename"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sessions"
    resource: "https://code.claude.com/docs/en/sessions"
    title: "Manage sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Command | Effect |
| :- | :- |
| `/clear` | Start with empty context. The previous session is saved: resume with `/resume`, or in the same process from the rewind menu's previous-session entry. With no argument the new session keeps a name set with `--name` or `/rename` but not an AI-generated title |
| `/clear release-prep` | Names the session you are leaving; the new session starts unnamed |
| `/compact [instructions]` | Replaces history with a summary, optionally focused on what you specify |
| `/context` | Shows what consumes context |

# Notes

See the context window guide for how compaction interacts with CLAUDE.md, skills and rules, and Best practices for clear-versus-compact strategy.
