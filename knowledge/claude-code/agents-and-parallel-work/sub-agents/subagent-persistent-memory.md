---
type: "Feature"
title: "Subagent persistent memory"
description: "The memory field gives a subagent a directory that persists across conversations, at user, project or local scope."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, memory, persistence]
kind: "frontmatter"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "auto memory enabled"
identifiers:
  - "memory"
  - "~/.claude/agent-memory/<name-of-agent>/"
  - ".claude/agent-memory/<name-of-agent>/"
  - ".claude/agent-memory-local/<name-of-agent>/"
  - "autoMemoryEnabled"
  - "CLAUDE_CODE_DISABLE_AUTO_MEMORY"
  - "MEMORY.md"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`memory: user | project | local` gives the subagent a persistent directory to accumulate knowledge (preferences, corrections, decisions).

# How to use it

| Scope | Location | Use when |
| :- | :- | :- |
| `user` | `~/.claude/agent-memory/<name-of-agent>/` | learnings across all projects |
| `project` | `.claude/agent-memory/<name-of-agent>/` | project-specific, shareable via version control (recommended default) |
| `local` | `.claude/agent-memory-local/<name-of-agent>/` | project-specific, not checked in |

When enabled: the system prompt gets instructions for reading/writing the directory plus the first 200 lines or 25KB of `MEMORY.md` (whichever first) with instructions to curate it; Read, Write and Edit tools are automatically enabled.

# Limits and defaults

Part of auto memory: turning it off with `autoMemoryEnabled` or `CLAUDE_CODE_DISABLE_AUTO_MEMORY` makes the field a no-op (no memory instructions or tool access).

# Notes

Tips: ask the subagent to consult memory before work and update it afterward; put memory-maintenance instructions in the agent's markdown.
