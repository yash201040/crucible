---
type: "Reference"
title: "Transcript storage, retention and deletion"
description: "Where session transcripts live, the settings and env vars that move, limit or suppress them, and how to delete them."
resource: "https://code.claude.com/docs/en/sessions"
tags: [transcripts, storage, retention, environment]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "~/.claude/projects/<project>/<session-id>.jsonl"
  - "CLAUDE_CONFIG_DIR"
  - "CLAUDE_CODE_PROJECT_DIR_NAME"
  - "cleanupPeriodDays"
  - "desktopSessionCleanupPeriodDays"
  - "CLAUDE_CODE_TRANSCRIPT_LOCAL_GC"
  - "CLAUDE_CODE_SKIP_PROMPT_HISTORY"
  - "--no-session-persistence"
  - "claude purge"
  - "claude rm <id>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sessions"
    resource: "https://code.claude.com/docs/en/sessions"
    title: "Manage sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Transcripts are JSONL at `~/.claude/projects/<project>/<session-id>.jsonl`. `<project>` is the working directory path with non-alphanumeric characters replaced by `-`; if the converted name exceeds 200 characters it is truncated to 200 and a hash of the full path appended. Each line is a message, tool use or result, a record of a request sent to the model, or a metadata entry. The format is internal and changes between versions.

# How to use it

| To | Set | Where |
| - | - | - |
| Move storage off `~/.claude` | `CLAUDE_CONFIG_DIR` | env var |
| Name the `<project>` directory yourself | `CLAUDE_CODE_PROJECT_DIR_NAME` | env var |
| Change the 30-day retention | `cleanupPeriodDays` | `settings.json` |
| Age limit for Claude Desktop and Cowork transcripts | `desktopSessionCleanupPeriodDays` | user settings, managed settings or `--settings` |
| Limit how large a `-p` or Agent SDK transcript file grows | `CLAUDE_CODE_TRANSCRIPT_LOCAL_GC` | env var |
| Suppress transcript writes in all modes | `CLAUDE_CODE_SKIP_PROMPT_HISTORY` | env var |
| Suppress writes for one non-interactive run | `--no-session-persistence` | CLI flag with `claude -p` |

Delete: transcripts age out under the retention sweep; `claude purge` deletes a project's transcripts and related state sooner. Deleting a background session with `claude rm <id>` leaves its transcript on disk and available through `claude --resume`.
