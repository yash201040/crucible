---
type: "Guide"
title: "Create and dispatch a skill"
description: "Author a SKILL.md in a project or personal skills directory and dispatch it from the SDK with /<name>."
resource: "https://code.claude.com/docs/en/agent-sdk/skills"
tags: [skills, authoring, skill-md, discovery]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - ".claude/skills/<name>/SKILL.md"
  - "~/.claude/skills/"
  - ".claude/commands/"
  - "name"
  - "description"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-skills"
    resource: "https://code.claude.com/docs/en/agent-sdk/skills"
    title: "Extend agents with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A skill is a directory with a `SKILL.md` holding YAML frontmatter and Markdown content. The `description` field decides when Claude invokes it.

# How to use it

1. Save at a discovery level: project `.claude/skills/` (current project only) or personal `~/.claude/skills/` (all projects).
2. Write frontmatter with `name` and `description`, then instructions (example: `name: security-check`, `description: Run a security vulnerability scan`).
3. Dispatch with `prompt: "/security-check"` or let Claude match the description. The name also appears in `slash_commands`.

# Notes

- Existing `.claude/commands/deploy.md` creates `/deploy` and behaves like `.claude/skills/deploy/SKILL.md`. Name clashes are resolved per the Claude Code skills guide ("Resolve skills that share a name").
- Authoring depth (frontmatter fields, `$ARGUMENTS`, `$0`, `$1`, named arguments, `${CLAUDE_*}` variables, `` !`command` `` dynamic context) is in the Claude Code skills guide and applies to SDK sessions.
