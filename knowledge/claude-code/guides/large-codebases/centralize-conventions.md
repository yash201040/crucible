---
type: "Guide"
title: "Centralize conventions at scale"
description: "Move conventions from always-loaded CLAUDE.md into skills, plugins and MCP code search, and recommend plugins with a SessionStart hook."
resource: "https://code.claude.com/docs/en/large-codebases"
tags: [plugins, skills, mcp, sessionstart-hook]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "SessionStart"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "large-codebases"
    resource: "https://code.claude.com/docs/en/large-codebases"
    title: "Set up Claude Code in a monorepo or large codebase"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When per-directory CLAUDE.md files drift and lack owners, the team maintaining the repo's Claude Code setup can move content to on-demand mechanisms.

# How to use it

- Skills: reference material loaded only when relevant.
- Plugins: versioned bundles of skills, hooks and commands owned centrally; installable for everyone through managed settings.
- MCP servers: if the organization has a code search or RAG index, expose it as an MCP tool so Claude queries it instead of reading files.
- `SessionStart` hook: plain text the hook prints to stdout is added to Claude's context before the first prompt. A script can read the launch directory from the hook input, look it up in a committed path-to-plugin map, and print a recommendation for Claude to relay in its first reply.

# Notes

Platform teams can enforce this centrally with server-managed or endpoint-managed settings.
