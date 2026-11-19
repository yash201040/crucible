---
type: "Feature"
title: "Remove-Item and cmd removal checks"
description: "PowerShell Remove-Item and cmd rd/del checks: system paths and wildcards denied in every mode, and the opt-out variable."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [powershell, remove-item, windows, deletion, safety]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.283"
surfaces: [cli]
requires: "PowerShell tool enabled; Windows"
identifiers:
  - "Remove-Item"
  - "CLAUDE_CODE_DISABLE_POWERSHELL_CMD_RM_DENY"
  - "cmd /c rd /s /q"
  - "rd"
  - "rmdir"
  - "del"
  - "erase"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

With the PowerShell tool enabled, `Remove-Item` and the `cmd` built-ins `rd`, `rmdir`, `del`, `erase` get their own checks, separate from the `rm` critical-path list. First matching case for `Remove-Item`:

- System paths (filesystem root and top-level dirs, drive roots and their top-level dirs, home directory): denied in every mode, without asking.
- Wildcards (bare `*`, or any target ending `/*` or `\*`, including `$dir/*`): denied in every mode before the classifier sees it.
- Working directory or a parent with `-Recurse`: treated like any command needing approval in the mode (asks; classifier in `auto`; denied in `dontAsk`); `bypassPermissions` skips this check.

# How to use it

The system-paths case also covers `rd`, `rmdir`, `del`, `erase` run through `cmd`, as in `cmd /c rd /s /q C:\Users` (needs v2.1.283+). For `cmd` targets, a PowerShell variable after literal text is treated as empty, so `cmd /c rd /s /q "C:\$name"` is denied; a trailing wildcard counts as the folder it empties, so `cmd /c del /q C:\*` is denied and `cmd /c del /q dist\*` in your project is not.

# Limits and defaults

Set `CLAUDE_CODE_DISABLE_POWERSHELL_CMD_RM_DENY=1` in the launching environment (ignored in a settings `env` block) to turn the `cmd` check off. `Remove-Item` on a system path stays denied either way.
