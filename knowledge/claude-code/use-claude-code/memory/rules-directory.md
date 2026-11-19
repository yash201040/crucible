---
type: "Feature"
title: "Rules in .claude/rules/ and path-scoped rules"
description: "Modular instruction files, optionally scoped by a paths glob frontmatter field, with symlink sharing and user-level rules."
resource: "https://code.claude.com/docs/en/memory"
tags: [rules, paths, glob, symlinks, frontmatter]
kind: "frontmatter"
maturity: "unlabelled"
since: "2.1.211"
surfaces: []
requires: ""
identifiers:
  - ".claude/rules/"
  - "~/.claude/rules/"
  - "paths"
  - "--setting-sources"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "memory"
    resource: "https://code.claude.com/docs/en/memory"
    title: "How Claude remembers your project"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Markdown files in `.claude/rules/` (discovered recursively, one topic per file) organize instructions. Rules without `paths` load at launch with the priority of `.claude/CLAUDE.md`. Rules with `paths` frontmatter load only when Claude uses Read, Write or Edit (or a single-file Bash read such as `cat`) on a matching file; matching also works through a symlinked project path. Task-specific instructions that need not always be in context belong in skills.

# How to use it

Frontmatter: `paths` is the only field read (YAML list or comma-separated string); other fields are ignored. Frontmatter is removed before loading. If the YAML does not parse, the rule loads as if it had no `paths` (`claude --debug` shows the error).

| Pattern | Matches |
| `**/*.ts` | `.ts` anywhere under base dir |
| `src/**/*` | all files under `src/` |
| `*.md` | `.md` anywhere |
| `/*.md` | `.md` directly in base dir |
| `src/components/*.tsx` | `.tsx` directly in that folder |

- Base directory: project rules use the directory containing `.claude`; user-level rules use the session primary working directory. To match a sibling worktree start in it or use `/cd`.
- Brace expansion works (`src/**/*.{ts,tsx}`); a rule's `paths` list shares one budget of 1,000 expanded patterns and 4 MiB; over budget, the pattern is used unexpanded and matches nothing.
- A pattern with an unreadable `[` (e.g. `photos [2024/**`) is invalid and matches nothing; escape inside single quotes: `'photos \[2024/**'`.
- Symlinks are supported (`ln -s ~/shared-claude-rules .claude/rules/shared`); circular ones are handled. A symlink whose target is outside the working directory counts as an external import: load needs project approval, then only rules without `paths` load. Links to network paths (UNC `\\server\share`, `/net`, `/Network`) are not followed; `\\wsl$` is not a network path.
- `~/.claude/rules/` applies to every project and loads before project rules; neither overrides the other.

# Limits and defaults

Project rules are skipped if `project` is excluded from `--setting-sources`. Before v2.1.211, on-demand rules loaded even when `project` was excluded.
