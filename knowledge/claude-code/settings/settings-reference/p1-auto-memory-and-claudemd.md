---
type: "Reference"
title: "Auto memory and CLAUDE.md settings"
description: "autoMemoryEnabled, autoMemoryDirectory, claudeMd and claudeMdExcludes control memory storage and which CLAUDE.md files load."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [memory, claude-md, settings, managed-settings]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "autoMemoryEnabled"
  - "autoMemoryDirectory"
  - "claudeMd"
  - "claudeMdExcludes"
  - "CLAUDE_CODE_DISABLE_AUTO_MEMORY"
  - "--bare"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Keys for the auto memory directory and for which CLAUDE.md memory loads.

# How to use it

| Key | Scope | Type | Default | What it does |
| :- | :- | :- | :- | :- |
| `autoMemoryEnabled` | Any file | Boolean | `true` | `false`: no reads or writes of the auto memory directory. `/memory` toggles it and writes user settings. `true` stays on unless `--bare`, safe mode or `CLAUDE_CODE_DISABLE_AUTO_MEMORY` turns it off; that variable overrides in either direction |
| `autoMemoryDirectory` | Any file | absolute or `~/` path | `~/.claude/projects/<project>/memory/` | Where auto memory is stored. From project or local settings it is honored under the same workspace trust rule as hooks |
| `claudeMd` | Managed | string (Markdown, line breaks as `\n`) | unset | Injects organization-wide CLAUDE.md text as a managed memory entry loaded ahead of user and project files |
| `claudeMdExcludes` | Any file | array of globs or absolute paths | unset | Skip matching CLAUDE.md files (patterns match absolute paths); applies only to user, project and local memory, never to managed policy CLAUDE.md |

```json
{ "claudeMdExcludes": ["**/vendor/**/CLAUDE.md"] }
```
