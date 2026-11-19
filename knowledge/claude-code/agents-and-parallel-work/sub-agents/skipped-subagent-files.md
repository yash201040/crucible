---
type: "Reference"
title: "Subagent files Claude Code skips"
description: "Frontmatter problems that make Claude Code skip an agent file, and how to validate an agents directory."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, validation, debugging, frontmatter]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin validate"
  - "--debug"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A file in a project, user or managed `agents` directory (or under an `--add-dir` directory) is skipped for these frontmatter problems:

| Problem | Result |
| :- | :- |
| No `name` | Treated as documentation kept beside agents |
| Opening `---` not on the first line | Read as no frontmatter, treated as documentation |
| `name` starts with `-`, contains `:`, or exceeds 256 characters | Skipped, error in debug log |
| `name` but no `description` | Skipped, reason in debug log |
| YAML does not parse | No fields read, skipped, parse error in debug log |

# How to use it

- See the debug log by running Claude Code with `--debug`.
- Pre-check a directory: `claude plugin validate .claude/agents` (or `~/.claude/agents`). It checks only the directory you name and does not flag a file that parses but has no `name`.

# Notes

A plugin subagent with no `name` or unparsable frontmatter still loads, under its filename.
