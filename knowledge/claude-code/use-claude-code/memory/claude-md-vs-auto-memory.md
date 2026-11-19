---
type: "Concept"
title: "CLAUDE.md vs auto memory"
description: "The two memory systems that carry knowledge across sessions: instructions you write, and notes Claude writes itself."
resource: "https://code.claude.com/docs/en/memory"
tags: [memory, claude-md, auto-memory, context]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "CLAUDE.md"
  - "AGENTS.md"
  - "MEMORY.md"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "memory"
    resource: "https://code.claude.com/docs/en/memory"
    title: "How Claude remembers your project"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each session starts with a fresh context window. Two mechanisms carry knowledge across sessions: CLAUDE.md files (instructions you write; Claude can also read a repository's AGENTS.md instead) and auto memory (notes Claude writes itself from your corrections and preferences). Both load at the start of every conversation. Claude treats both as context, not enforced configuration.

# How to use it

| | CLAUDE.md files | Auto memory |
| :- | :- | :- |
| Who writes it | You | Claude |
| Contains | Instructions and rules | Learnings and patterns |
| Scope | Project, user, or org | Per repository, shared across worktrees |
| Loaded into | Every session | Every session (first 200 lines or 25KB) |

To block an action regardless of what Claude decides, use a PreToolUse hook, not memory. Subagents can keep their own auto memory (subagent `memory` field).

# Notes

Specific, concise instructions are followed more consistently. See [auto memory](./auto-memory.md) and [where CLAUDE.md files live](./claude-md-locations.md).
