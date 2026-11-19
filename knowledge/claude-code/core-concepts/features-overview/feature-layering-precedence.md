---
type: "Reference"
title: "How features layer and which wins"
description: "Precedence and merge rules when CLAUDE.md, skills, subagents, MCP servers and hooks are defined at several levels."
resource: "https://code.claude.com/docs/en/features-overview"
tags: [precedence, scope, skills, subagents, mcp]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers: []
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "features-overview"
    resource: "https://code.claude.com/docs/en/features-overview"
    title: "Extend Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Features can be defined user-wide, per project, via plugins or through managed policies. When one exists at several levels, each feature resolves differently.

# How to use it

| Feature | Rule | Order |
| - | - | - |
| CLAUDE.md files | Additive: all levels contribute at once; conflicts reconciled by Claude's judgment. Working directory and above load at launch; subdirectories load as you work in them | n/a |
| Skills | Override by name | managed > user > project; plugin skills are namespaced |
| Subagents | Override by name | managed > CLI flag > project > user > plugin |
| MCP servers | Override by name | local > project > user |
| Hooks | Merge: all registered hooks fire for matching events regardless of source | n/a |

# Notes

CLAUDE.md can be nested in subdirectories and skills placed in specific packages of a monorepo.
