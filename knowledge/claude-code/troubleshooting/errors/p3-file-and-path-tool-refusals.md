---
type: "Reference"
title: "File tool and path permission refusals"
description: "Tool-result refusals for Read/Edit/Write/Grep: deny rules, blockWritesOutsideWorkingDirectories, symlink changes, null bytes, UTF-8, 128 MB images."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, permissions, file-tools, symlinks]
kind: "tool"
maturity: "unlabelled"
since: "2.1.228"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "permissions.blockWritesOutsideWorkingDirectories"
  - "permissions.additionalDirectories"
  - "permissions.blockReadsOutsideWorkingDirectories"
  - "/add-dir"
  - "--add-dir"
  - "Read"
  - "Edit"
  - "Write"
  - "NotebookEdit"
  - "Glob"
  - "Grep"
  - "--agents"
  - "--mcp-config"
  - "managed-settings.d/"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors returned by Claude's file tools when permission rules or safety checks refuse the operation. Claude usually adapts; the person changes settings only where noted.

# How to use it

| Message | Cause / fix |
|---|---|
| `File is covered by a Read deny rule in your permission settings and cannot be edited` (or `written`) | Edit or Write on a path matched by a `Read` deny rule, including new files. NotebookEdit is not covered by `Read` deny rules, so add an `Edit` deny too. Before v2.1.228 only Edit was blocked; before v2.1.208 only an `Edit` deny blocked edits |
| `<path> is outside <dirs>; the permissions.blockWritesOutsideWorkingDirectories setting blocks writes outside the working directories` | Refused in every permission mode. Fix: `/add-dir <dir>`, `--add-dir`, list in `permissions.additionalDirectories` (user or managed), or remove the setting from every file (may also come from `--settings`, a host application, or fail-closed managed settings) |
| `Writes to Claude Code settings files are blocked while permissions.blockWritesOutsideWorkingDirectories is on` | Settings files can lift the block, so the person edits them. Also counts files passed to `--agents`/`--mcp-config`, stored server-managed settings, and any `.json` while the `managed-settings.d/` folder cannot be resolved |
| `Read file_path cannot contain null bytes` | Read/Write/Edit/NotebookEdit/Glob/Grep check path or pattern; error goes to Claude (before v2.1.281 it ended the turn with `Path contains null bytes`) |
| `Refusing to read/write/search <path>: its symlink resolution changed after permission was checked` | Permission check is repeated when the file opens (reads/searches since v2.1.251; before only writes). Variants: parent-directory symlink changed; destination could not be determined (v2.1.280+); write at a symlink location (`Write to the link's target path instead`); `Refusing to write through symlink`; `Refusing to write into symlinked directory`; Read deny rule path changed; `EACCES` on search root; permission check expired under too many concurrent file operations; ripgrep found only by name on PATH so searches outside the working directory are refused. Fixes: stop what rewrites links; upgrade to v2.1.265 on Windows AppContainer/restricted-token sandboxes or v2.1.273 on macOS for false refusals; install ripgrep |
| `File is not valid UTF-8` | Edit/NotebookEdit refused (before v2.1.296 they wrote `U+FFFD` replacements); use a shell command that preserves the encoding or convert |
| `File is too large to read as an image (the limit is 128MB)` | Read image limit 128 MB; a pipe or device sending over 128 MB gives `Cannot read this as an image` |
| `The search failed, so this is not a "no matches" result` | Grep/Glob ripgrep failure; Claude retries once; capture `rg error (signal=` line with `--debug-file claude-debug.log` |

# Limits and defaults

- Image read limit: 128 MB.

# Notes

Network paths and `/add-dir` refusals for UNC/automount paths are in [configuration warnings](./p4-configuration-warnings-startup.md).
