---
type: "Reference"
title: "Permission rule warnings"
description: "Startup warnings for malformed, mistyped or over-broad permission rules, and for denying Bash switching off the PowerShell tool."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, permissions, warnings, rules, headless]
kind: "setting"
maturity: "unlabelled"
since: "2.1.210"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "--allowedTools"
  - "--allowed-tools"
  - "--disallowedTools"
  - "--disallowed-tools"
  - "--settings"
  - "--debug"
  - "Edit(path)"
  - "Read(path)"
  - "Write"
  - "NotebookEdit"
  - "MultiEdit"
  - "Glob"
  - "Bash(*)"
  - "CLAUDE_CODE_USE_POWERSHELL_TOOL"
  - "/permissions"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Warnings about permission rules in settings files, managed settings, or `--allowedTools`/`--disallowedTools`/`--settings` values. Delivery depends on mode: interactive shows a row below the startup banner (since v2.1.305; earlier stderr) with the full text in the debug log; `-p` with text output prints to stderr; background sessions and `--output-format json` or `stream-json` write to the debug log (`--debug`, file `~/.claude/debug/<session-id>.txt`) so machine-read output stays clean.

# How to use it

| Warning | Meaning | Fix |
|---|---|---|
| `Invalid permission rule "Bash(ls) x" was skipped: Malformed Tool(content) rule` | Not of the form `Tool` or `Tool(content)`; skipped and listed in the invalid-settings dialog and `claude doctor`. Parentheses inside content are literal, e.g. `Edit(./Finance (2024)/**)`. Before v2.1.260: `Mismatched parentheses` | End the rule at its closing `)` |
| `Deny rule Bsh matches no tool` (stderr: `Permission deny rule "Bsh" matches no known tool - check for typos.`) | Unknown tool name in a deny or ask rule, including a transcript label instead of the canonical name | Use the canonical name from the tools reference; `/permissions` shows the rule source (`From CLI argument` for `--disallowedTools`) |
| `Write(docs/**) never matches` / `is not matched by file permission checks` (since v2.1.210) | Path rules for `Write`, `NotebookEdit`, `MultiEdit` or `Glob` are never consulted; only `Edit` and `Read` path rules are. Allow rules get no row. Bare `Write` or `Glob` are fine (`Glob` in `--allowedTools` is accepted) | Use `Edit(path)` (covers all file-editing tools) and `Read(path)` |
| `Allow rule Bash(git -C * status *) allows any option at its *` (since v2.1.246) | A `*` before the word that identifies the command also matches inserted options; `Bash(git * main)` approves `git -c core.fsmonitor=<script> diff main`. Rule is kept unchanged | Use exact values before the subcommand and `*` only after it: `Bash(git status *)` |
| `Denying Bash also turns off the PowerShell tool` (since v2.1.287) | On Windows with Git Bash, `--disallowedTools Bash`, bare `Bash` or `Bash(*)` removes the PowerShell tool too, leaving no shell tool | Set `CLAUDE_CODE_USE_POWERSHELL_TOOL=1`, or use scoped rules such as `Bash(git push *)` |

# Notes

Managed-settings rule warnings read `managed policy settings` and cannot be cleared by the user. The permission-rule typo warning is the way a misspelled tool in a deny list is discovered, since the rule silently does not apply.
