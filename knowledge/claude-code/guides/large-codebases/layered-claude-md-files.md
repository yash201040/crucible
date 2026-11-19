---
type: "Guide"
title: "Layer CLAUDE.md files by directory"
description: "Split instructions into a root CLAUDE.md plus per-directory files so only relevant conventions load; compare with path-scoped rules."
resource: "https://code.claude.com/docs/en/large-codebases"
tags: [claude-md, memory, rules, monorepo]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE.md"
  - ".claude/rules/"
  - "paths:"
  - "/doctor"
  - "/context all"
  - "Stop"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "large-codebases"
    resource: "https://code.claude.com/docs/en/large-codebases"
    title: "Set up Claude Code in a monorepo or large codebase"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code loads every CLAUDE.md from the working directory and each parent at launch, then loads each subdirectory's file on demand. A two-level split works: root `CLAUDE.md` for repository-wide rules (coding standards, commit conventions) and one per package or subsystem (for example `src/db/`, `src/api/`) for stack-specific conventions. Commit them so teammates inherit them.

# How to use it

- Starting from `packages/api/` loads `packages/api/CLAUDE.md` and the root file, and nothing from `packages/web/`.
- Confirm what loaded with `/context all` and the **Memory files** list.
- Trim an oversized file with the `/doctor` checkup.
- Keep files current: review CLAUDE.md edits in pull requests; revisit after major model releases (workarounds for old model limits may become overhead); add a `Stop` hook, which receives the session transcript path when Claude finishes responding, so a script can propose CLAUDE.md updates.

| Approach | Location | Loads when | Use when |
| :- | :- | :- | :- |
| Per-directory `CLAUDE.md` | Inside the directory | At launch from that directory, or on demand | Directory owners keep conventions versioned with code |
| Path-scoped rule in `.claude/rules/` | Central `.claude/` at repo root | When Claude works with a file matching the rule's `paths:` glob | All conventions in one place, or one rule over scattered paths |
