---
type: "Reference"
title: "CLAUDE.md and rules load locations"
description: "Where CLAUDE.md, rules and local files load from and which setting source gates each; all levels are additive."
resource: "https://code.claude.com/docs/en/agent-sdk/claude-code-features"
tags: [claude-md, rules, memory, setting-sources]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "CLAUDE.md"
  - ".claude/CLAUDE.md"
  - ".claude/rules/*.md"
  - "CLAUDE.local.md"
  - "~/.claude/CLAUDE.md"
  - "~/.claude/rules/*.md"
  - "systemPrompt"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-claude-code-features"
    resource: "https://code.claude.com/docs/en/agent-sdk/claude-code-features"
    title: "Use Claude Code features in the SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Level | Location | Requires source |
| :- | :- | :- |
| Project root | `<cwd>/CLAUDE.md` or `<cwd>/.claude/CLAUDE.md` | `project` |
| Project rules | `<cwd>/.claude/rules/*.md` and in every parent directory | `project` |
| Parent dirs | `CLAUDE.md` above `cwd`, loaded at session start | `project` |
| Child dirs | `CLAUDE.md` in subdirectories, loaded on demand | `project` |
| Local | `<cwd>/CLAUDE.local.md` and parents | `local` |
| User | `~/.claude/CLAUDE.md` | `user` |
| User rules | `~/.claude/rules/*.md` | `user` |

# Limits and defaults

All levels are additive; there is no hard precedence. Conflicting instructions are resolved by Claude's interpretation, so write non-conflicting rules or state precedence explicitly.

# Notes

You can inject context via `systemPrompt` instead of CLAUDE.md; use CLAUDE.md to share context with interactive sessions.
