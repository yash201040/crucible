---
type: "Guide"
title: "Create your first subagent"
description: "Quickstart: ask Claude to write a user-level subagent file in ~/.claude/agents/ and delegate to it."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, quickstart, agents-directory]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "~/.claude/agents/"
  - ".claude/agents/"
  - "/agents"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Subagents are Markdown files with YAML frontmatter. You can ask Claude to write one, write it by hand, define it with `--agents`, or ship it in a plugin.

# How to use it

1. Ask Claude to create it, naming a location, for example a personal subagent in `~/.claude/agents/`.
2. Review the file: frontmatter with `name`, `description`, `tools`, `model`, then the system prompt as body.
3. Delegate: "Use the code-improver agent ...". The transcript shows a row like `code-improver(Suggest code improvements)`.

A file in `~/.claude/agents/` is available in every project; `.claude/agents/` scopes it to one project.

# Notes

- If `~/.claude/agents/` did not exist when the session started, restart Claude Code to see a newly created directory.
- `/agents` now prints a reminder to ask Claude or edit the directories directly. On v2.1.197 and earlier it opens an interactive wizard with a Running tab (live subagents) and a Library tab (create, edit, delete).
