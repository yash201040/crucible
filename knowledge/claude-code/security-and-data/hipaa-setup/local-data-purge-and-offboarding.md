---
type: "Feature"
title: "Purge local session data and offboard developers"
description: "claude purge (v2.1.288+) and claude project purge delete local transcripts and memory; retention sweep runs only at start; removing a seat deletes nothing."
resource: "https://code.claude.com/docs/en/hipaa-setup"
tags: [purge, retention, local-data, offboarding, cleanup]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.288"
surfaces: [cli, desktop]
requires: "claude purge needs v2.1.288 or later; claude project purge works on v2.1.126 through v2.1.287"
identifiers:
  - "claude purge"
  - "claude project purge"
  - "--all"
  - "--yes"
  - "cleanupPeriodDays"
  - "~/.claude/projects/"
  - "paste-cache/"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hipaa-setup"
    resource: "https://code.claude.com/docs/en/hipaa-setup"
    title: "Set up Claude Code (local mode) for a HIPAA-ready organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Local session data is the organization's responsibility. The retention sweep deleting data older than `cleanupPeriodDays` runs only when someone starts Claude Code, so an unused computer keeps its data.

# How to use it

- v2.1.288 or later: `claude purge --all --yes`. v2.1.126 through v2.1.287: `claude project purge --all --yes` (same flags). Run as that developer. Without `--yes` it prints the plan and asks.
- Deletes every project's transcripts and auto memory, entries in `tasks/`, `debug/`, `file-history/`, `history.jsonl`, and project entries in `~/.claude.json`. It leaves other paths such as `paste-cache/`.
- Code tab data lives in `~/.claude/projects/` plus the Claude Desktop data folder (`~/Library/Application Support/Claude` on macOS; `%APPDATA%\Claude` or `%LOCALAPPDATA%\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude` on Windows). With HIPAA applied, Desktop deletes local Code tab sessions inactive longer than `cleanupPeriodDays` (including starred), only while running; the worktree is removed only if no uncommitted changes, not starred or pinned, and unused by other sessions.

# Limits and defaults

Removing a seat or account, or `/logout`, deletes nothing on the computer; wipe the device with device management to remove all of it.
