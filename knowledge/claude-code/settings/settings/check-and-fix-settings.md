---
type: "Guide"
title: "Confirming loaded settings and fixing errors"
description: "/status shows loaded setting sources; Settings Error, Settings Warning, managed and ~/.claude.json failures and how -p runs treat them."
resource: "https://code.claude.com/docs/en/settings"
tags: [settings, status, errors, headless, doctor]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "/status"
  - "claude doctor"
  - "claude -p"
  - "~/.claude/backups/.claude.json.corrupted.<timestamp>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings"
    resource: "https://code.claude.com/docs/en/settings"
    title: "Settings files and precedence"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/status` (Status tab) has a `Setting sources` line listing each settings file loaded (e.g. `User settings`, `Project local settings`); for managed settings it shows in parentheses how they arrived. It does not show which file supplied each key. `claude doctor` lists rejected entries. `/status` and `/config` open the same dialog on different tabs.

# How to use it

Problems shown at the start of an interactive session:

| Message | Cause | Result |
| :- | :- | :- |
| Settings Error | user, project or local file has invalid JSON or a schema-rejected value | dialog: fix with Claude's help, exit, or continue without the broken settings |
| Settings Warning | single entries fail (malformed permission rule, unknown hook event name) | those values skipped, rest of file kept |
| Managed settings | invalid entries | rest still enforced; some keys fall back to a stricter value |
| Configuration error | `~/.claude.json` unparseable | `claude -p` exits; file copied to `~/.claude/backups/.claude.json.corrupted.<timestamp>`; interactive asks to exit or reset; blank file with no backup starts with defaults |

# Limits and defaults

A `-p` run shows no dialog: unless a managed settings document cannot be parsed, Claude Code skips a broken user, project or local file or its broken values and continues. After a `-p` run that ignored a setting, run `claude doctor` to see what was dropped.
