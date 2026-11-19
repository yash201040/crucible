---
type: "Feature"
title: "First read outside working directories"
description: "Auto mode asks once before the first Read/Grep/Glob outside working directories; the four answers and the setting they write."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [auto-mode, reads, working-directory, settings]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "permissions.blockReadsOutsideWorkingDirectories"
  - "/add-dir"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

While `permissions.blockReadsOutsideWorkingDirectories` is off, file reads (other than network-path reads) run without a prompt in auto mode, even outside working directories. The first time Read, Grep or Glob touches such a path, Claude Code asks whether to allow it.

# How to use it

Answers:
- **Yes, and keep allowing any reads outside the working directories**: later reads run; the answer is recorded.
- **No, and block reads outside the working directories from now on**: read refused; sets `permissions.blockReadsOutsideWorkingDirectories` to `true` in user settings, so file tools refuse such reads in every later session and mode. To lift, remove it from every settings file and restart running sessions; for one directory use `/add-dir`.
- **No, and ask again next time**: refused, prompts again.
- **Yes, but ask again next time**: runs, nothing saved.

# Limits and defaults

The prompt does not appear in `-p` runs, Agent SDK sessions, background sessions, the VS Code chat panel or the desktop app; the read just runs there.
