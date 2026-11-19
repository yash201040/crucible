---
type: "Guide"
title: "Status line examples and troubleshooting"
description: "Ready-made status line patterns (context bar, git, cost, rate limits, links, caching, Windows) and fixes for a blank or garbled status line."
resource: "https://code.claude.com/docs/en/statusline"
tags: [statusline, examples, troubleshooting, windows]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "FORCE_HYPERLINK"
  - "COLUMNS"
  - "LINES"
  - "claude --debug"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "statusline"
    resource: "https://code.claude.com/docs/en/statusline"
    title: "Customize your status line"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The page gives Bash, Python and Node.js examples for: a context window progress bar (colors green under 70%, yellow 70-89%, red 90%+), git status with colors, cost and duration tracking, multi-line output, clickable OSC 8 repo links, rate limit and gateway spend display, and a cached-git-info script. Windows examples use PowerShell or Git Bash. Community projects named: ccstatusline, starship-claude.

# How to use it

Save a script, `chmod +x`, point `statusLine.command` at it. Keep output short because the bar has limited width and long output truncates or wraps. Cache `git status`/`git diff` in a temp file named with `session_id`.

# Limits and defaults

Troubleshooting checklist for a blank status line: script executable, prints to stdout not stderr, runs manually, forward slashes on Windows Git Bash, no `disableAllHooks`/`allowManagedHooksOnly` override, workspace trust accepted, `claude --debug`.

# Notes

- `--` or empty values: fields may be null before the first API response; use fallbacks.
- Terminal escape sequences (ANSI, OSC 8) can garble output when overlapping other UI updates; multi-line scripts with escapes are more prone. Simplify to plain text.
- Literal `\e]8;;` text: use `printf '%b'` rather than `echo -e`. SSH and tmux may strip OSC sequences.
- Slow scripts block updates until they finish; an in-flight script is cancelled by a new update.
