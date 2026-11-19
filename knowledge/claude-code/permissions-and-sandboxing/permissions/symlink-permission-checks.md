---
type: "Concept"
title: "Symlink handling in permission checks"
description: "Permission checks cover both the requested path and its resolved target; allow needs both to match, deny needs either."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, symlinks, security, deny-rules]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.268"
surfaces: [cli]
requires: ""
identifiers: []
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When a requested path passes through a symlink (macOS, Linux, Windows; directory junctions on Windows), both the requested path and the file it resolves to are checked.

# How to use it

- Allow rules apply only when both paths match. Deny rules apply when either matches. With `Read(./project/**)` allowed and `Read(~/.ssh/**)` denied, `./project/key` pointing at `~/.ssh/id_rsa` is blocked.
- On macOS and Linux a deny/ask rule written through a symlinked directory with `//`, `~/` or `/` also applies at the real location (`Read(//etc/**)` blocks `/private/etc/hosts` on macOS). Before v2.1.268 it did not.
- Grep and Glob apply `Read` deny to the directory their `path` resolves to.
- A `Read` deny covers attachments by either path: `@`-mentions, pasted images, changed files Claude Code re-reads, IDE context. With `permissions.blockReadsOutsideWorkingDirectories` or a `--restricted` session, attachments from refused paths are also left out. A file whose path cannot be examined shows `Referenced <path> (not read: could not be examined)`; Claude is told to read it with file tools.
- Edit and Write refuse to write when the target path is itself a symlink, directing Claude to the link target. Writes through a symlinked directory or via Bash/PowerShell can still pass: if the resolved file is outside working directories the write is not auto-approved in `acceptEdits`, and in auto mode it prompts the user (unless an allow rule approves) with the resolved path named. If it resolves to a protected path the requested path does not name, the protected-paths outcome applies, except classifier routing becomes a prompt.
- Unresolvable paths (for example looping symlinks) make Read, Edit and Write refuse, and a tool re-confirms the path still resolves to the approved location when opening the file.
