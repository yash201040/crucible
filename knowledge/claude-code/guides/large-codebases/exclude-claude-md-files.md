---
type: "Feature"
title: "claudeMdExcludes setting"
description: "claudeMdExcludes skips CLAUDE.md and rules files by absolute-path glob so they never load."
resource: "https://code.claude.com/docs/en/large-codebases"
tags: [claude-md, settings, exclude, monorepo]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claudeMdExcludes"
  - ".claude/settings.local.json"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "large-codebases"
    resource: "https://code.claude.com/docs/en/large-codebases"
    title: "Set up Claude Code in a monorepo or large codebase"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When starting from the repository root, subdirectory CLAUDE.md files can load on demand. `claudeMdExcludes` skips chosen files by path or glob so they never load, for directories you never work in (other teams' packages, legacy code, vendored trees). It is a static list, not a per-task switch; to focus on another package, start Claude from that directory instead.

# How to use it

```json
{ "claudeMdExcludes": ["**/packages/web/**"] }
```

Patterns are globs matched against absolute file paths, so start relative-style patterns with `**/`.

| Pattern | Effect |
| :- | :- |
| `**/packages/web/**` | Every CLAUDE.md and rules file under that package |
| `**/packages/*/CLAUDE.md` | Every package's CLAUDE.md, root kept |
| `**/packages/legacy-*/**` | Packages matching the name glob, including rules |
| `/home/user/monorepo/legacy/CLAUDE.md` | One file by absolute path |

# Limits and defaults

Settable at any scope: user, project, local or managed; arrays merge across scopes. A pattern never skips an organization's managed CLAUDE.md, whichever scope sets it. For personal-only use put it in `.claude/settings.local.json`; Claude Code adds that file to your global gitignore only when it saves a setting there, so add it yourself when creating it by hand.
