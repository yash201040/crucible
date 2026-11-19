---
type: "Concept"
title: "CLAUDE.md vs rules vs skills vs output styles"
description: "How the standing-instruction features differ in loading, scope and purpose, and the 200-line CLAUDE.md rule of thumb."
resource: "https://code.claude.com/docs/en/features-overview"
tags: [claude-md, rules, skills, output-styles, comparison]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - ".claude/rules/"
  - "paths"
  - "@path"
  - "/<name>"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "features-overview"
    resource: "https://code.claude.com/docs/en/features-overview"
    title: "Extend Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Four features store instructions but load differently.

# How to use it

| Aspect | CLAUDE.md | `.claude/rules/` | Skill | Output style |
| - | - | - | - | - |
| Loads | Every session, automatically | Every session, or when matching files are opened | On demand (invoked or relevant) | Always; one active at a time |
| Scope | Whole project | Can be scoped to file paths | Task-specific | Whole session |
| Holds | Facts and rules | Language- or directory-specific guidelines | Reference material, `/<name>` workflows | Role, tone, response format |
| `@path` imports | Yes | not stated | Yes | not stated |
| Can trigger workflows | No | not stated | Yes, with `/<name>` | not stated |

Rules with `paths` frontmatter load only when Claude works with matching files, saving context.

# Limits and defaults

- Keep CLAUDE.md under 200 lines; move reference content to skills or split into `.claude/rules/` files.
- CLAUDE.md and an output style combine: both are followed as instructions, neither is enforced. For anything that must happen every time, use a hook.

# Notes

Put in CLAUDE.md what is true of the project whatever the style; use an output style for how Claude responds (length, format, a non-engineering role). Claude Code includes built-in output styles.
