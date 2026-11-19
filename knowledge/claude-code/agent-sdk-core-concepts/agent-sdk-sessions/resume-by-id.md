---
type: "Feature"
title: "Resume by session ID"
description: "Resume a specific session with full prior context; where transcripts are stored and how directory lookup works."
resource: "https://code.claude.com/docs/en/agent-sdk/sessions"
tags: [resume, transcripts, storage, cross-directory]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.223"
surfaces: [sdk]
requires: ""
identifiers:
  - "resume"
  - "~/.claude/projects/<encoded-cwd>/*.jsonl"
  - "CLAUDE_CONFIG_DIR"
  - "CLAUDE_CODE_PROJECT_DIR_NAME"
  - "error_max_turns"
  - "error_max_budget_usd"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-sessions"
    resource: "https://code.claude.com/docs/en/agent-sdk/sessions"
    title: "Work with sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Pass a session ID to `resume` to return to that session with full context. Reasons: follow up on a completed task, recover from `error_max_turns` or `error_max_budget_usd` (resume with a higher limit; in a single-shot `query()` catch the raised error first), restart your process.

# How to use it

Transcripts live under `~/.claude/projects/<encoded-cwd>/*.jsonl`, or `$CLAUDE_CONFIG_DIR/projects/`. Encode the working directory by replacing every non-alphanumeric character with `-` (`/Users/me/proj` becomes `-Users-me-proj`); names over 200 characters are truncated with a hash appended, so match the first 200 characters. `CLAUDE_CODE_PROJECT_DIR_NAME` set beside `CLAUDE_CONFIG_DIR` replaces the name (needs TypeScript Agent SDK v0.3.234 or later, or Python Agent SDK v0.2.140 or later).

# Limits and defaults

- Resume works from any working directory (cross-directory lookup) but the session file must exist on the current machine.
- Before v2.1.223 the lookup was limited to the current project directory and its git worktrees; SDK versions bundling an older CLI still behave that way.
