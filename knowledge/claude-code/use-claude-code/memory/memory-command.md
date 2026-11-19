---
type: "Feature"
title: "The /memory command"
description: "Lists and opens CLAUDE.md, CLAUDE.local.md and auto memory files, and toggles auto memory."
resource: "https://code.claude.com/docs/en/memory"
tags: [memory, slash-command, auto-memory, editor]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/memory"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "memory"
    resource: "https://code.claude.com/docs/en/memory"
    title: "How Claude remembers your project"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/memory` lists CLAUDE.md, CLAUDE.local.md and other memory file locations across user and project scopes (including user and project entries that do not exist yet), toggles auto memory, and opens the auto memory folder. Selecting a file opens it in your editor; selecting a missing one creates it. GUI editors open separately; terminal editors such as Vim take over the terminal.

# How to use it

Asking Claude to "remember" something (e.g. "always use pnpm, not npm") saves it to auto memory. To write to CLAUDE.md say "add this to CLAUDE.md" or edit it via `/memory`. An AGENTS.md read directly also appears in the list.
