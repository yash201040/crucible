---
type: "Feature"
title: "acceptEdits mode"
description: "Auto-approves file edits and common filesystem commands inside the working directory; lists what still prompts."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [acceptedits, permissions, filesystem, powershell]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide]
requires: ""
identifiers:
  - "acceptEdits"
  - "--permission-mode acceptEdits"
  - "additionalDirectories"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`acceptEdits` lets Claude create and edit files in the working directory without prompting. Status bar: `⏵⏵ accept edits on`. It also auto-approves `mkdir`, `touch`, `rm`, `rmdir`, `mv`, `cp`, `sed`. Except `touch`, these are also approved with safe env-var prefixes (`LANG=C`, `NO_COLOR=1`) or wrappers (`timeout`, `nice`, `nohup`). Scope is the working directory or `additionalDirectories`, and each path goes through the symlink check.

# How to use it

`claude --permission-mode acceptEdits`, or press `Shift+Tab` once from Manual.

# Limits and defaults

Still prompts: paths outside scope; writes to protected paths; recognized `rm`/`rmdir` critical-path removals; `touch` with options, globs or a prefix such as `timeout 5` or `LANG=C`; all other Bash except the built-in read-only set.

With the PowerShell tool enabled it also approves `Set-Content`, `Add-Content`, `Clear-Content`, `Remove-Item` (and aliases) on in-scope paths, with their own `Remove-Item` check. A positional argument containing a quote character (for example `Set-Content .\notes.txt "It's done"`) still prompts; use a named parameter such as `-Value`.
