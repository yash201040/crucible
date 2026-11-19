---
type: "Guide"
title: "Prompt recipes for everyday tasks"
description: "Prompt patterns for exploring code, fixing bugs, refactoring, tests, pull requests, docs, notes folders and capability questions."
resource: "https://code.claude.com/docs/en/common-workflows"
tags: [recipes, prompts, pull-requests, tests, refactoring]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, web, ide]
requires: ""
identifiers:
  - "claude --from-pr"
  - "/resume"
  - "/powerup"
  - "gh pr create"
  - "glab mr create"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "common-workflows"
    resource: "https://code.claude.com/docs/en/common-workflows"
    title: "Common workflows"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Short recipes that work in any Claude Code surface. Pattern: start broad then narrow (codebase overview, architecture, data models, authentication; find the files, how they interact, trace the execution flow). For monorepos see the "Monorepos and large repos" page.

# How to use it

- Bugs: share the error and the reproduce command or stack trace, say whether it is intermittent, ask for fix options, then apply.
- Refactor: find deprecated API usage, ask for recommendations, apply while preserving behavior, run tests; do it in small testable increments.
- Tests: find uncovered functions, generate scaffolding matching existing patterns, add edge cases, run and fix.
- Pull requests: ask "create a pr" or go step by step. `claude --from-pr 1234` opens the session picker filtered to sessions linked to that PR; pasting the PR URL into `/resume` search also works. Claude Code links the session when Claude creates the PR with `gh pr create` or `glab mr create`, and when it works on an existing PR.
- Documentation: find undocumented code, generate JSDoc or docstrings, enhance, verify against standards.
- Notes and non-code folders: Claude Code works in any directory; `.claude/` and `CLAUDE.md` coexist with other tools' config; files are read fresh on each tool call, so edits from another app are seen at the next read.
- Capability questions: Claude answers from the current documentation, not limited to your version. `/powerup` gives interactive lessons with animated demos.
