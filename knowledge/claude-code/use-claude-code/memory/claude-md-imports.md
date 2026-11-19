---
type: "Feature"
title: "CLAUDE.md @path imports"
description: "Pull other files into CLAUDE.md with @path syntax, with a four-hop depth limit and an approval dialog for external files."
resource: "https://code.claude.com/docs/en/memory"
tags: [claude-md, imports, approval, worktrees]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [desktop]
requires: ""
identifiers:
  - "@path/to/import"
  - "@~/.claude/my-project-instructions.md"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "memory"
    resource: "https://code.claude.com/docs/en/memory"
    title: "How Claude remembers your project"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

CLAUDE.md files can import files with `@path/to/import`. Imported files are expanded into context alongside the importer.

# How to use it

- Relative and absolute paths work; relative paths resolve against the importing file, not the working directory.
- Imports recurse to a maximum depth of four hops.
- Spaces in a path need a backslash before each space (`@Design\ Docs/api-conventions.md`). A quoted path is not imported at all.
- Code spans and fenced code blocks are skipped by import parsing; wrap `@README` in backticks to keep it literal.
- A gitignored `CLAUDE.local.md` exists only in the worktree where created; to share personal instructions across worktrees import a home-directory file such as `@~/.claude/my-project-instructions.md`.

# Limits and defaults

An import in a project-level memory file is external when its path resolves outside the working directory. The first time Claude Code meets external imports in a project it shows an approval dialog; if declined, imports stay disabled and the dialog does not reappear. User-scope files (`~/.claude/CLAUDE.md`, `~/.claude/rules/`) load imports without the dialog, except in Cowork sessions on the desktop, where Claude Code skips any user-scope import resolving outside the working directory, skips a `~/.claude/CLAUDE.md` that is a symlink or hard link, and skips a symlinked `~/.claude/rules/` directory or rule file pointing outside the working directory.
