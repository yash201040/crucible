---
type: "Feature"
title: "claude purge: delete local project state"
description: "The claude purge command deletes one project's transcripts, memory and history entries, with dry-run, yes, all and interactive options."
resource: "https://code.claude.com/docs/en/claude-directory"
tags: [purge, cleanup, privacy, cli]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.288"
surfaces: [cli]
requires: ""
identifiers:
  - "claude purge"
  - "--dry-run"
  - "--yes"
  - "--all"
  - "-i"
  - "claude project purge"
  - "/heapdump"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-directory"
    resource: "https://code.claude.com/docs/en/claude-directory"
    title: "Explore the .claude directory"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude purge [path]` deletes the state Claude Code holds for one project: transcripts and auto memory under `projects/`, per-session `tasks/`, `debug/` and `file-history/` entries, matching prompt lines in `history.jsonl`, and the project's entry in `~/.claude.json`. Before v2.1.288 the command was `claude project purge`.

# How to use it

| Invocation | Effect |
| - | - |
| `claude purge ~/work/my-repo --dry-run` | Print the deletion plan only |
| `claude purge ~/work/my-repo` | Print the plan, then ask `[y/N]` before deleting |
| `claude purge ~/work/my-repo --yes` | Skip confirmation (for scripts) |
| `claude purge` (no path) | Pick a project from an interactive list |
| `claude purge --all` | Purge every project; deletes `history.jsonl` outright instead of filtering |
| `claude purge ... -i` | Step through the plan one item at a time |

If no state matches the path, it prints an error and exits with status 1.

# Limits and defaults

- Does not touch `shell-snapshots/` and `backups/` (not project-scoped; warned about in the plan), nor images and scratchpads under the temp directory (the sweep still deletes images older than `cleanupPeriodDays`; a purged session's scratchpad stays until you delete it or the OS clears it).
- `.heapsnapshot` files written by `/heapdump` hold the full conversation and credentials and are not removed by purge or the sweep; delete them yourself.
