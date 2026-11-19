---
type: "Feature"
title: "/batch parallel codebase changes"
description: "A bundled skill that decomposes a large change into 5 to 30 independent units and runs one background subagent per unit in its own worktree."
resource: "https://code.claude.com/docs/en/commands"
tags: [batch, subagents, worktrees, parallel]
kind: "slash_command"
maturity: "unlabelled"
since: "2.1.281"
surfaces: [cli]
requires: "A git repository, or a WorktreeCreate hook that creates worktrees"
identifiers:
  - "/batch"
  - "WorktreeCreate"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "commands"
    resource: "https://code.claude.com/docs/en/commands"
    title: "Commands"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/batch <instruction>` is a bundled skill for large-scale changes across a codebase in parallel.

# How to use it

`/batch migrate src/ from JavaScript to TypeScript`. It researches the codebase, decomposes the work into 5 to 30 independent units and presents a plan. After approval it spawns one background subagent per unit, each in an isolated worktree; each implements its unit, runs tests, and opens a PR or reports what happened.

# Limits and defaults

Requires a git repository or a `WorktreeCreate` hook that creates the worktrees. Outside a git repository it requires v2.1.281 or later.
