---
type: "Guide"
title: "Running hooks in PowerShell on Windows"
description: "shell: powershell on a command hook; placeholder rewriting for CLAUDE_PROJECT_DIR and friends."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, windows, powershell, paths]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Windows"
identifiers:
  - "shell"
  - "powershell"
  - "pwsh.exe"
  - "powershell.exe"
  - "CLAUDE_PROJECT_DIR"
  - "CLAUDE_PLUGIN_ROOT"
  - "CLAUDE_PLUGIN_DATA"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

On Windows, set `"shell": "powershell"` on a command hook to run it in PowerShell. Claude Code auto-detects `pwsh.exe` (PowerShell 7+) and falls back to `powershell.exe` (Windows PowerShell 5.1).

# How to use it

In a PowerShell shell-form command write `${CLAUDE_PROJECT_DIR}` or `$env:CLAUDE_PROJECT_DIR`. Claude Code rewrites the `${CLAUDE_PROJECT_DIR}`, `${CLAUDE_PLUGIN_ROOT}` and `${CLAUDE_PLUGIN_DATA}` placeholders to PowerShell's `${env:NAME}` form, whether the hook is in `settings.json`, a plugin or a skill. They work inside double-quoted strings, not single-quoted ones (PowerShell never expands variables there).

Example: `"command": "& \"$env:CLAUDE_PROJECT_DIR\\.claude\\hooks\\check.ps1\""`.

# Limits and defaults

- Do not write bare `$CLAUDE_PROJECT_DIR` in PowerShell: it parses as an undefined local variable and resolves to `$null`, dropping the project-root prefix. Claude Code does not rewrite that form and logs a warning in the debug log.
- Hooks running in PowerShell do not have `CLAUDE_ENV_FILE`.
