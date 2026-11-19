---
type: "Feature"
title: "claude plugin prune"
description: "Removes auto-installed dependencies that no installed plugin needs; --dry-run previews and -y is required without a TTY."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, prune, dependencies, cleanup]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin prune"
  - "claude plugin autoremove"
  - "--dry-run"
  - "-y, --yes"
  - "-s, --scope <scope>"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude plugin prune [options]` (alias `autoremove`) removes auto-installed dependencies no installed plugin needs. It never removes a plugin you installed yourself.

# How to use it

| Flag | Description |
| :- | :- |
| `-s, --scope <scope>` | `user`, `project` or `local`; default `user` |
| `--dry-run` | List what would be removed; ends with `(dry run — nothing removed)`; with none, `Nothing to prune` |
| `-y, --yes` | Skip confirmation; required when stdin/stdout is not a TTY |

| Terminal and flags | What happens |
| :- | :- |
| Interactive, no `-y` | Lists and asks `Remove? [y/N]` |
| Any terminal, `-y` | Removes and prints `Removed N auto-installed plugins: <names>` |
| Non-TTY, no `-y` | Prints the list and ``Not a TTY — run `claude plugin prune -y` to remove.``, removes nothing |

# Limits and defaults

Exit code is `0` whatever you answer at the prompt.
