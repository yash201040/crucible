---
type: "Reference"
title: "Resolving skills that share a name"
description: "Precedence table for same-named skills across enterprise, personal, project, bundled, built-in, plugin, added-directory and synced sources."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, precedence, naming, conflicts]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/review"
  - "/cost"
  - "/usage"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Where each skill came from decides which one `/name` runs.

# How to use it

| Same name in | Which runs |
| :- | :- |
| Two of enterprise, personal, project | enterprise over personal over project |
| A location and a bundled skill | your skill replaces the bundled command, not its aliases (project `code-review` replaces `/code-review`; alias `/review` never runs it) |
| A location and a built-in command | in a local terminal session your skill replaces the command, not its aliases (project `usage` replaces `/usage`; `/cost` still runs the built-in) |
| A skill and a `.claude/commands/` file | the skill |
| Project-root skill and nested skill | both load |
| Enterprise/personal/project skill and an added-directory skill | the first; the added one runs under a prefixed name |
| Two added directories | the one added first; the other is prefixed |
| Plugin skill and any other | both load (plugin skills are namespaced) |
| Any of the above and a synced claude.ai skill's short name | the other one; the synced skill runs only by its full name |

# Notes

The frontmatter `name` field has its own rules: see [command names](./skill-name-rules.md).
