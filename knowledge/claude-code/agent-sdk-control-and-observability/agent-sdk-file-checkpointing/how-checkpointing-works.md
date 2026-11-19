---
type: "Feature"
title: "File checkpointing and rewind"
description: "SDK backs up files before Write, Edit or NotebookEdit changes so files on disk can be rewound to the state at any prompt."
resource: "https://code.claude.com/docs/en/agent-sdk/file-checkpointing"
tags: [checkpointing, rewind, files, undo]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.216"
surfaces: [sdk]
requires: ""
identifiers:
  - "rewindFiles()"
  - "rewind_files()"
  - "RewindFilesResult"
  - "skippedLinks"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-file-checkpointing"
    resource: "https://code.claude.com/docs/en/agent-sdk/file-checkpointing"
    title: "Rewind file changes with checkpointing"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

With checkpointing enabled, the SDK backs up files before the Write, Edit or NotebookEdit tools modify them. Each prompt that starts a turn is a checkpoint, and its user message UUID is the restore point. Rewinding deletes files Claude Code created and restores modified files to their content at that point.

# Limits and defaults

- Rewinding restores files on disk only; the conversation history and context stay intact.
- Claude Code skips a tracked path that is a symlink, hard link or other non-regular file, a tracked file whose parent directory no longer resolves to its checkpoint-time location, and one whose backup it cannot read safely. `RewindFilesResult` counts skipped paths in `skippedLinks`. Skipping needs Claude Code v2.1.216 or later; before it, a rewind wrote and deleted through links at tracked paths.
- `rewindFiles()` does not undo `sed -i` or other Bash changes unless Write or Edit had modified that file in the main conversation. Subagent edits are not tracked; edits from a skill with `context: fork` running in the foreground are.
