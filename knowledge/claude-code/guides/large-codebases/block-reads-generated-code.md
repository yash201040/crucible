---
type: "Feature"
title: "Read deny rules for generated code"
description: "Use Read deny rules in permissions.deny to keep checked-in build output and vendored code out of context, with coverage limits."
resource: "https://code.claude.com/docs/en/large-codebases"
tags: [permissions, deny-rules, context, gitignore]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "permissions.deny"
  - "Read(./**/dist/**/*)"
  - "Read(./**/build/**/*)"
  - "Read(./**/*.generated.*)"
  - "Read(./**/vendor/**/*)"
  - "Read(//absolute/path/to/repo/**/vendor/**/*)"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "large-codebases"
    resource: "https://code.claude.com/docs/en/large-codebases"
    title: "Set up Claude Code in a monorepo or large codebase"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Content searches respect `.gitignore` by default, so `node_modules/`, `dist/`, `build/` in it stay out of results. For checked-in paths (vendored SDK, committed generated code), add `Read` deny rules in `permissions.deny`.

# How to use it

```json
{ "permissions": { "deny": [
  "Read(./**/dist/**/*)", "Read(./**/build/**/*)",
  "Read(./**/*.generated.*)", "Read(./**/vendor/**/*)" ] } }
```

Patterns end in `/**/*` (not `/**`) so contents are blocked but Claude can still list or `cd` into the directory.

| Scope | Where |
| :- | :- |
| Everyone in the repo | Commit to `.claude/settings.json` at the root if starting there, or in each package's `.claude/` if starting from subdirectories |
| Yourself only | `.claude/settings.local.json` at the repo root (loads in every CLI session in the repo, except where Claude Code does not use the repo root, such as Windows) |
| Everyone, enforced | Managed settings, which user and project settings cannot override |

# Limits and defaults

- Relative patterns still anchor at the session's current working directory, not the repo root; for sessions from subdirectories write `//`-absolute paths.
- Coverage: built-in file tools; in Bash, recognized file commands (`cat`, `head`, `grep`, `find`) when a denied path is an argument, and redirection targets such as `< file`. Built-in Grep and Glob make a best-effort attempt to omit denied paths. A Bash `grep -r` or `find` over a directory containing denied files still includes them. Subprocesses that open files themselves are not covered.
