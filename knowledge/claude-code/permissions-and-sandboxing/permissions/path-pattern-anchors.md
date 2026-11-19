---
type: "Reference"
title: "Path pattern anchors and depth"
description: "Read and Edit rules use gitignore syntax with //, ~/, / and relative anchors, and depth differs between allow and deny/ask."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, paths, gitignore, patterns]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "//path"
  - "~/path"
  - "/path"
  - "./path"
  - "Read(//Users/alice/secrets/**)"
  - "Read(~/Documents/*.pdf)"
  - "Edit(/src/**/*.ts)"
  - "Read(*.env)"
  - "Edit(**/src/**)"
  - "--settings"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Read and Edit rules use gitignore pattern syntax (`*` within one segment, `**` across directories) with four pattern types.

# How to use it

| Pattern | Meaning | Example |
| - | - | - |
| `//path` | Absolute from filesystem root | `Read(//Users/alice/secrets/**)` |
| `~/path` | From home directory | `Read(~/Documents/*.pdf)` |
| `/path` | Relative to the settings source | `Edit(/src/**/*.ts)` |
| `path` or `./path` | Relative to current directory | `Read(*.env)` |

`/Users/alice/file` is not absolute; use `//Users/alice/file`.

Where `/path` anchors:

| Rule defined in | Resolves to |
| :- | :- |
| `.claude/settings.json` | `<primary working directory>/path` |
| `.claude/settings.local.json` | `<primary working directory>/path` (in a worktree session, that worktree) |
| `~/.claude/settings.json` | `~/.claude/path` |
| `--settings <file>` | `<directory of file>/path` |
| CLI flags or session rules | `<primary working directory>/path` |

A rule added via `/permissions` follows the file it is saved to. A user-settings `Read(/secrets/**)` blocks `~/.claude/secrets/**`, not the project; use `//` or `~/` there.

# Limits and defaults

- Windows: paths normalize to POSIX (`C:\Users\alice` -> `/c/Users/alice`); use `//c/**/.env` for a drive, `//**/.env` for all drives.
- Bare filenames match at any depth (`Read(.env)` equals `Read(**/.env)`). `Read(//**/.env)` blocks any `.env` on the filesystem.
- Single-directory-segment patterns such as `src/**`: as allow, only `<cwd>/src`; as deny or ask, a `src` directory at any depth. Other shapes match at the same depth in every rule type (`Edit(/src/**)`, `Edit(src/components/**)` only at anchor; `Edit(**/src/**)` any depth). To allow a name at any depth write `Edit(**/src/**)`.
