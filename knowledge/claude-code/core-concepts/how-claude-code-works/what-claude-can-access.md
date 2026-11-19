---
type: "Concept"
title: "What Claude can access"
description: "The project files, terminal, git state, CLAUDE.md, auto memory and extensions available when claude runs in a directory."
resource: "https://code.claude.com/docs/en/how-claude-code-works"
tags: [access, claude-md, auto-memory, git]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "MEMORY.md"
  - "CLAUDE.md"
  - "AGENTS.md"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "how-claude-code-works"
    resource: "https://code.claude.com/docs/en/how-claude-code-works"
    title: "How Claude Code works"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Running `claude` in a directory gives access to: project files (and files elsewhere with permission), the terminal (any command you could run), git state (branch, uncommitted changes, recent commits), CLAUDE.md, auto memory, and configured extensions (MCP servers, skills, subagents, Claude in Chrome).

# Limits and defaults

- Auto memory: the first 200 lines or 25KB of `MEMORY.md`, whichever comes first, load at the start of each session.
- If a repository has an AGENTS.md for other coding agents, Claude can read that in place of a CLAUDE.md.

# Notes

Because Claude sees the whole project it makes coordinated edits across files, unlike inline assistants that see only the current file.
