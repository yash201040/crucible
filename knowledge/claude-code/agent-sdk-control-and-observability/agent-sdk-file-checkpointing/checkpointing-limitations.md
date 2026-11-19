---
type: "Limit"
title: "Checkpointing limitations"
description: "What rewinding does not cover: Bash changes, subagent edits, other sessions, directories and remote files."
resource: "https://code.claude.com/docs/en/agent-sdk/file-checkpointing"
tags: [checkpointing, limitations, subagents, bash]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers: []
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-file-checkpointing"
    resource: "https://code.claude.com/docs/en/agent-sdk/file-checkpointing"
    title: "Rewind file changes with checkpointing"
stale_after: "2027-01-19T00:00:00Z"
---

# Limits and defaults

| Limitation | Description |
| - | - |
| Bash command changes | not undone, except in files the main conversation had already edited with Write or Edit |
| Subagent edits | not tracked, except a skill with `context: fork` in the foreground; a rewind reverts them only in files the main conversation already edited; use git for the rest |
| Same session | checkpoints are tied to the session that created them |
| File content only | creating, moving or deleting directories is not undone |
| Local files | remote or network files are not tracked |
