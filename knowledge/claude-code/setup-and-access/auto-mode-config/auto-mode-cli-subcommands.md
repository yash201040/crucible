---
type: "Reference"
title: "claude auto-mode subcommands"
description: "claude auto-mode defaults, config, critique and reset for inspecting and resetting classifier rules."
resource: "https://code.claude.com/docs/en/auto-mode-config#inspect-the-defaults-and-your-effective-config"
tags: [auto-mode, cli, inspect, classifier]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude auto-mode defaults"
  - "claude auto-mode config"
  - "claude auto-mode critique"
  - "claude auto-mode reset"
  - "--label"
  - "--yes"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "auto-mode-config"
    resource: "https://code.claude.com/docs/en/auto-mode-config"
    title: "Configure auto mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Subcommands to inspect, validate and reset auto mode rules. `defaults` and `config` print the four lists (`environment`, `allow`, `soft_deny`, `hard_deny`) as one JSON object of prose strings.

# How to use it

| Command | What it does |
| :- | :- |
| `claude auto-mode defaults` | built-in rules; `--label 'Git Destructive'` filters by case-insensitive label prefix |
| `claude auto-mode config` | effective rules with your settings applied |
| `claude auto-mode critique` | AI feedback flagging ambiguous, redundant or false-positive-prone custom entries |
| `claude auto-mode reset` | removes `autoMode` from the user settings file; asks `Reset auto mode configuration to defaults?`; `--yes` skips |

# Limits and defaults

- Reset changes only `~/.claude/settings.json`; managed and `--settings` rules still apply.
- While `/status` shows `Auto mode server` as `Enabled`, server-side built-in rules can differ from this output and no subcommand prints them.
- `/permissions` has an **Auto mode** tab (v2.1.246+) to edit rules and environment entries; managed and `--settings` entries are read-only; not in the desktop app.
