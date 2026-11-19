---
type: "Concept"
title: "How CLAUDE.md files load"
description: "Hierarchy walk, ordering, on-demand subdirectory loading, comment stripping and loading from --add-dir directories."
resource: "https://code.claude.com/docs/en/memory"
tags: [claude-md, loading, add-dir, monorepo]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD"
  - "--add-dir"
  - "--setting-sources"
  - "CLAUDE.local.md"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "memory"
    resource: "https://code.claude.com/docs/en/memory"
    title: "How Claude remembers your project"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code loads CLAUDE.md and CLAUDE.local.md from the working directory and every directory above it. Files are concatenated, not overriding, ordered from filesystem root down to the working directory, so the closest instructions are read last. Within a directory CLAUDE.local.md is appended after CLAUDE.md.

# How to use it

- Subdirectory CLAUDE.md and CLAUDE.local.md files load once Claude reads, writes or edits another file in that subdirectory (including a single-file Bash read like `cat` or `head`).
- Block-level HTML comments are stripped before injection (comments in code blocks are kept; the Read tool still shows them).
- Large monorepos: skip other teams' files with [`claudeMdExcludes`](./managed-claude-md-and-excludes.md).
- `--add-dir` gives access to extra directories but does not load their CLAUDE.md by default. Set `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` (inline: `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1 claude --add-dir ../shared-config`, or in the `env` block of `~/.claude/settings.json`) to also load that directory's `CLAUDE.md`, `.claude/CLAUDE.md`, `CLAUDE.local.md` and `.claude/rules/*.md`, except rules with a `paths` field.

# Limits and defaults

`CLAUDE.local.md` is skipped if `local` is excluded from `--setting-sources`. For worktrees under `.claude/worktrees/` see the worktrees page.
