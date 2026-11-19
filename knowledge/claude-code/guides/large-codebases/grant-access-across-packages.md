---
type: "Feature"
title: "Access across packages and repos"
description: "additionalDirectories, --add-dir and /add-dir grant file access to sibling directories; they differ in whether CLAUDE.md and skills load."
resource: "https://code.claude.com/docs/en/large-codebases"
tags: [add-dir, permissions, directories, claude-md]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "permissions.additionalDirectories"
  - "additionalDirectories"
  - "--add-dir"
  - "/add-dir"
  - "CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "large-codebases"
    resource: "https://code.claude.com/docs/en/large-codebases"
    title: "Set up Claude Code in a monorepo or large codebase"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Started from `packages/api/`, Claude can read and write only that directory. For cross-package tasks, or a separately checked-out repo, grant access to more directories. Not needed when starting from the root of a single tree.

# How to use it

```json
{ "permissions": { "additionalDirectories": ["../shared", "../web"] } }
```

Relative paths resolve against the launch directory. At runtime: `claude --add-dir ../shared`.

| Added with | Loads CLAUDE.md and rules | Loads skills |
| :- | :- | :- |
| `additionalDirectories` setting | Never | Never |
| `--add-dir` flag or `/add-dir` | Only with the env var below | Yes |

```bash
CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1 claude --add-dir ../shared
```

# Limits and defaults

The env var has no effect on directories from the `additionalDirectories` setting. Commit `additionalDirectories` to `.claude/settings.json` for shared access; use `.claude/settings.local.json` or `--add-dir` for personal or one-off access.
