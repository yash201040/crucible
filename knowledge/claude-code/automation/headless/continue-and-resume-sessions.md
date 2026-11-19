---
type: "Feature"
title: "Continue and resume in -p mode"
description: "--continue, --resume with session ID or transcript path, and background-session behavior from v2.1.257."
resource: "https://code.claude.com/docs/en/headless"
tags: [headless, sessions, resume, continue]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.257"
surfaces: [headless]
requires: ""
identifiers:
  - "--continue"
  - "--resume"
  - "session_id"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "headless"
    resource: "https://code.claude.com/docs/en/headless"
    title: "Run Claude Code programmatically"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`--continue` continues the most recent conversation; `--resume <session-id>` continues a specific one. From v2.1.257, `--continue` opens a background session that has finished, but not one still running.

# How to use it

```bash
claude -p "Review this codebase for performance issues"
claude -p "Now focus on the database queries" --continue
session_id=$(claude -p "Start a review" --output-format json | jq -r '.session_id')
claude -p "Continue that review" --resume "$session_id"
```

Run the commands from different directories if needed: Claude Code finds the session by ID in any project on the machine. `--resume` also accepts the absolute path of a session's `.jsonl` transcript file.

# Notes

Cost totals reported with `--continue` or `--resume` cover the whole conversation, earlier runs included.
