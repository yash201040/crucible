---
type: "Guide"
title: "Write effective instructions and audit them"
description: "Size, structure and consistency guidance for CLAUDE.md, plus the /doctor prompt-audit check."
resource: "https://code.claude.com/docs/en/memory"
tags: [claude-md, instructions, audit, doctor]
kind: "slash_command"
maturity: "unlabelled"
since: "2.1.283"
surfaces: []
requires: "Claude Code v2.1.283 or later for /doctor prompt-audit"
identifiers:
  - "/doctor prompt-audit"
  - "/doctor"
  - "skillOverrides"
  - "disableBundledSkills"
  - "/claude-api"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "memory"
    resource: "https://code.claude.com/docs/en/memory"
    title: "How Claude remembers your project"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

CLAUDE.md is context, not enforced configuration, so wording affects adherence.

# How to use it

- Write checkable instructions ("Use 2-space indentation", "Run `npm test` before committing").
- Size: target under 200 lines per CLAUDE.md. Imports do not reduce context cost because imported files load with the importer.
- Structure with markdown headers and bullets.
- Consistency: contradicting instructions may be resolved arbitrarily; periodically review CLAUDE.md, nested files and `.claude/rules/`.
- `/doctor prompt-audit` reports outdated, broken-reference or contradictory instructions with proposed edits; nothing changes until you ask. Default scope: CLAUDE.md, CLAUDE.local.md, AGENTS.md, and rules, skills, commands, subagents and output styles under `.claude/` and `~/.claude/`. Pass a path to narrow, e.g. `/doctor prompt-audit .claude/skills/deploy`.
- The `/doctor` checkup also proposes trims for a checked-in CLAUDE.md: it removes derivable content (directory layouts, dependency lists, architecture overviews) and keeps pitfalls, rationale and non-default conventions.

# Limits and defaults

The audit runs through the bundled `/claude-api` skill, so it is unavailable if that skill is turned off in `skillOverrides` or with `disableBundledSkills`. Requires v2.1.283+.
