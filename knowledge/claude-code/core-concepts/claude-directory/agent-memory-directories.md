---
type: "Feature"
title: "Subagent memory directories"
description: "Where subagents with a memory frontmatter field keep persistent MEMORY.md notes, and how much loads into their system prompt."
resource: "https://code.claude.com/docs/en/claude-directory"
tags: [subagents, memory, persistence, agent-memory]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "auto memory on"
identifiers:
  - ".claude/agent-memory/"
  - ".claude/agent-memory/<agent-name>/MEMORY.md"
  - "~/.claude/agent-memory/"
  - "memory: project"
  - "memory: user"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-directory"
    resource: "https://code.claude.com/docs/en/claude-directory"
    title: "Explore the .claude directory"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Subagents get their own persistent memory, separate from the main session's auto memory in `~/.claude/projects/`. Each subagent reads and writes its own `MEMORY.md`, an index of notes it saved (same format as main auto memory).

# How to use it

- `memory: project` in the subagent frontmatter: directory at `.claude/agent-memory/<agent-name>/` in the project (committable; project-scoped).
- `memory: user`: directory under `~/.claude/agent-memory/`; knowledge persists across all projects.

# Limits and defaults

- First 200 lines of the subagent's `MEMORY.md`, capped at 25KB, load into its system prompt when it runs.
- Only while auto memory is on.
- `agent-memory/` is a state file to keep (not safe to delete).
