---
type: "Feature"
title: "Working directories and additional directories"
description: "The launch directory is the primary working directory; extend access with --add-dir, /add-dir or additionalDirectories."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, working-directories, add-dir, trust]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.326"
surfaces: [cli, ide]
requires: ""
identifiers:
  - "--add-dir"
  - "/add-dir"
  - "additionalDirectories"
  - "permissions.additionalDirectories"
  - "permissions.blockReadsOutsideWorkingDirectories"
  - "permissions.blockWritesOutsideWorkingDirectories"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude can access files in the directory where it was launched (the primary working directory until moved with `/cd`). Extend access at startup with `--add-dir <path>`, in-session with `/add-dir`, or persistently with `additionalDirectories` in settings files. Files in additional directories follow the same rules: readable without prompts (apart from the network-path check), edits follow the permission mode.

# How to use it

| Key | Effect |
| :- | :- |
| `permissions.blockReadsOutsideWorkingDirectories` = `true` | File tools refuse reads outside working directories in every mode including `bypassPermissions`, apart from files Claude Code needs. In auto mode Claude Code can offer to enable it on first outside read |
| `permissions.blockWritesOutsideWorkingDirectories` = `true` | `Write`, `Edit`, `NotebookEdit` refuse writes outside, apart from some of Claude Code's own files such as plan files. Does not limit shell commands, MCP tools or hook programs (use sandboxing). Needs v2.1.314+ |

To keep one outside directory reachable while a key is true, add it as a working directory.

# Notes

- In an interactive terminal session, `claude --add-dir` or `/add-dir` for a folder your workspace trust does not cover asks you to trust it first. Needs v2.1.326+.
- Network paths (e.g. UNC share) cannot be added as working directories; on Windows map to a drive letter.
- Background sessions on macOS: the session host requests access to `~/Desktop`, `~/Documents`, `~/Downloads` separately; reads that fail with `Operation not permitted` need folder access granted (see Agent view docs).
