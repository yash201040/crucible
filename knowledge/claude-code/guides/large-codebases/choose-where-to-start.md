---
type: "Concept"
title: "Choose where to start Claude"
description: "The launch directory decides file access, which CLAUDE.md files load at startup, and which project settings apply."
resource: "https://code.claude.com/docs/en/large-codebases"
tags: [monorepo, working-directory, claude-md, settings]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - ".claude/settings.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "large-codebases"
    resource: "https://code.claude.com/docs/en/large-codebases"
    title: "Set up Claude Code in a monorepo or large codebase"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Where `claude` is launched determines what it can read and edit without a permission grant, which CLAUDE.md files load into context at startup, and which project settings apply. In a large codebase, default settings tuned for small projects can fill context with unrelated instructions and file reads.

# How to use it

| Start from | File access | CLAUDE.md at launch | Use when |
| :- | :- | :- | :- |
| Repository root | Every file | Root only; subdirectory files load on demand | Tasks span packages |
| A subdirectory | That subtree only, until more is granted | That directory's plus every ancestor's | Work is scoped to one package |

# Limits and defaults

Project settings in `.claude/settings.json` are not inherited from parent directories the way CLAUDE.md files are. Each subdirectory's settings file must be self-contained. Settings are independent and layer rather than replace each other.

# Notes

Each setting on the page is marked personal (local) or committed (repository). The page's example monorepo has `packages/api`, `packages/web`, `packages/shared`, each with its own CLAUDE.md.
