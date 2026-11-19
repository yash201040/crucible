---
type: "Guide"
title: "Plan cross-package changes"
description: "Give Claude a whole cross-package change in one session and plan first in plan mode; the plan file is re-injected after compaction."
resource: "https://code.claude.com/docs/en/large-codebases"
tags: [plan-mode, compaction, monorepo, context]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers: []
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "large-codebases"
    resource: "https://code.claude.com/docs/en/large-codebases"
    title: "Set up Claude Code in a monorepo or large codebase"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two techniques for changes spanning packages (for example a shared type plus every call site).

# How to use it

- Hand Claude the whole change in one session so decisions stay consistent rather than being re-derived per package.
- Plan first in plan mode. Claude writes the plan to a file; a long session compacts its context, and Claude Code re-injects the plan file after each compaction, so the plan survives where conversation history may not.

# Notes

Suggested next steps on the page: hooks for per-directory linters or type-checkers after edits; the Manage costs page for token usage and spend limits; running exploration in a subagent keeps file reads out of the main conversation.
