---
type: "Feature"
title: "Reducing transcript exposure"
description: "Transcripts and history are unencrypted; options to shorten retention or skip writing them, including no-session-persistence for headless and SDK runs."
resource: "https://code.claude.com/docs/en/claude-directory"
tags: [privacy, transcripts, headless, sdk, persistence]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "cleanupPeriodDays"
  - "desktopSessionCleanupPeriodDays"
  - "CLAUDE_CODE_SKIP_PROMPT_HISTORY"
  - "--no-session-persistence"
  - "persistSession: false"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-directory"
    resource: "https://code.claude.com/docs/en/claude-directory"
    title: "Explore the .claude directory"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Transcripts and history are not encrypted at rest; OS file permissions are the only protection. A credential printed by a command or read from a `.env` file is written to `projects/<project>/<session>.jsonl`.

# How to use it

- Lower `cleanupPeriodDays` to shorten transcript retention.
- Set `desktopSessionCleanupPeriodDays` to age-limit Claude Desktop and Cowork transcripts.
- Set the `CLAUDE_CODE_SKIP_PROMPT_HISTORY` environment variable to skip writing transcripts and prompt history in any mode.
- Non-interactive mode: pass `--no-session-persistence` alongside `-p`, or set `persistSession: false` in the TypeScript Agent SDK. The Python SDK has no equivalent option.
- Use permission rules to deny reads of credential files.

# Limits and defaults

Deleting `~/.claude/projects/` loses resume, continue and rewind for past sessions and auto memory for every project.
