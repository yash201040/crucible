---
type: "Feature"
title: "CLAUDE_ENV_FILE persisted environment"
description: "Hooks write export lines to CLAUDE_ENV_FILE so later Bash and PowerShell commands in the session see them."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, environment, env-file, powershell]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_ENV_FILE"
  - "Session environment is not all plain assignments"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`CLAUDE_ENV_FILE` is a file path given to hooks; variables written there persist for shell commands Claude runs later. Available only to SessionStart, Setup, CwdChanged and FileChanged hooks. Not available to other events, nor to a hook that runs in PowerShell (via `"shell": "powershell"` or by default on Windows without Git Bash).

# How to use it

Append `export NAME=value` lines with `>>` so other hooks' variables survive. To capture all changes from setup commands, diff `export -p | sort` before and after and append the difference. Each Bash command runs the file's contents as shell code first, so lines may use anything Bash evaluates (for example `$PATH`).

For CwdChanged and FileChanged hooks, variables persist until the next CwdChanged event, when Claude Code clears them.

PowerShell commands (v2.1.296 or later) get the variables only by Claude Code parsing the file; PowerShell never runs it. Accepted only if every line (across all hooks in the session and any script `CLAUDE_ENV_FILE` is set to before launch) is a blank line, a `#` comment, or one assignment `export NAME=value`, `declare -x NAME=value` or `NAME=value`, with value made of unquoted text using only letters, digits and `_ @ % + = : , . / -`, single-quoted text, or double-quoted text with `$`, backtick, `"` backslash-escaped.

# Limits and defaults

- Any other line kind (unescaped `$PATH`, `source`, `$'...'` from `direnv export bash`) means PowerShell gets none of the variables, and `claude --debug` logs `Session environment is not all plain assignments`. Bash still gets all.
- On Windows, PowerShell commands also skip any variable whose value contains `/` or `\`.
- A sandboxed PowerShell command receives none of the variables.
