---
type: "Guide"
title: "Export transcripts and access sessions from scripts"
description: "Use /export for readable text, and claude -p JSON output, --resume, hooks' transcript_path or the Agent SDK for structured access."
resource: "https://code.claude.com/docs/en/sessions"
tags: [export, scripts, headless, transcripts, hooks]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "/export"
  - "claude -p"
  - "--output-format json"
  - "--output-format stream-json"
  - "claude -p --resume <session-id>"
  - "transcript_path"
  - "SessionEnd"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sessions"
    resource: "https://code.claude.com/docs/en/sessions"
    title: "Manage sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/export` opens a menu to copy the conversation to the clipboard or save it as plain text (messages and tool outputs rendered readable); pass a filename to write directly. For machine use, pick by what triggers the script.

# How to use it

- Run once and capture the result: `claude -p` with `--output-format json` or `stream-json` returns result, session ID, usage and cost.
- Ask an existing session a question: `claude -p --resume <session-id>` with a follow-up prompt, e.g. `claude -p --resume <session-id> --output-format json "summarize what we changed" | jq -r '.result'`.
- React to events: hooks and status line commands receive a `transcript_path` field; a `SessionEnd` hook can archive the transcript.
- Embed in a TypeScript or Python app: the Agent SDK receives each message programmatically.

# Notes

The transcript entry format is internal and changes between versions; parsing the files directly can break on any release.
