---
type: "Reference"
title: "Permission modes and mode-lock settings"
description: "The six permission modes, their aliases, and the settings that disable bypass or auto mode or deny instead of prompting."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permission-modes, auto-mode, bypass, dontask]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide, desktop]
requires: ""
identifiers:
  - "defaultMode"
  - "default"
  - "manual"
  - "acceptEdits"
  - "plan"
  - "auto"
  - "dontAsk"
  - "bypassPermissions"
  - "permissions.disableBypassPermissionsMode"
  - "permissions.disableAutoMode"
  - "permissions.denyInsteadOfPrompting"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Permission modes control how Claude Code approves tool calls. Set the default for new sessions with `defaultMode` in settings files.

# How to use it

| Mode | What it does |
| :- | :- |
| `default` | Prompts on first use of each tool. Labeled Manual in the CLI, VS Code and JetBrains extensions and desktop app; `manual` is accepted as an alias |
| `acceptEdits` | Auto-accepts file edits and common filesystem commands (`mkdir`, `touch`, `mv`, `cp`) for paths in the working directory or `additionalDirectories` |
| `plan` | Reads files and runs read-only shell commands to explore, no source edits; with auto mode available, classifier-approved commands also run |
| `auto` | No routine prompts; a background classifier checks actions such as shell commands and network requests against the request |
| `dontAsk` | Auto-denies every call that would prompt. Reads in working directories, no-approval actions and tools pre-approved via `/permissions` or `permissions.allow` still run. `AskUserQuestion` and some other calls are denied even if allowed. In some setups an installed mod can still approve some calls |
| `bypassPermissions` | Skips prompts except the actions no mode auto-approves |

| Setting | Effect |
| :- | :- |
| `permissions.disableBypassPermissionsMode` = `"disable"` | Prevents bypassPermissions; works from any scope, best in managed settings |
| `permissions.disableAutoMode` = `"disable"` | Prevents auto mode |
| `permissions.denyInsteadOfPrompting` = `true` | Denies calls that would wait on a prompt so an unattended session keeps working; set in user or managed settings; combines with whichever mode is active, unlike `dontAsk` which is a mode |

# Limits and defaults

`bypassPermissions` also skips prompts for writes to protected paths such as `.git` and `.claude`. Cross-session messaging safeguards still apply. Use it only in containers or VMs.
