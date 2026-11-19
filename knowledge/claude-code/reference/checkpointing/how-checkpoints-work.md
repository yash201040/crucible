---
type: "Feature"
title: "Automatic checkpoints"
description: "Each turn-starting prompt creates a checkpoint of Claude's file edits; 100 kept per session, saved with the conversation, swept after about 30 days."
resource: "https://code.claude.com/docs/en/checkpointing"
tags: [checkpointing, rewind, snapshots, retention]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide]
requires: ""
identifiers:
  - "/rewind"
  - "/undo"
  - "cleanupPeriodDays"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "checkpointing"
    resource: "https://code.claude.com/docs/en/checkpointing"
    title: "Checkpointing"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code automatically tracks changes made by its file editing tools. Before every prompt you send that starts a turn, a new checkpoint captures code state. `/rewind` (alias `/undo`) opens the rewind menu.

# Limits and defaults

- Snapshots kept for the 100 most recent checkpoints per session. Discarding an older one deletes snapshot files no remaining checkpoint references, except each file's first snapshot, which the VS Code extension uses as the baseline for session diffs.
- Checkpoints are saved with the conversation, so `/rewind` works after resuming a session.
- File snapshots are deleted in the retention sweep, by default about 30 days after the session last saved one. Rewinding to a checkpoint whose snapshots are gone can fail with `No files were restored`. Set `cleanupPeriodDays` to keep them longer.
- Only files edited within the current session are tracked.

# Notes

Common uses: exploring alternatives, recovering from mistakes, iterating on features, freeing context by summarizing a verbose debugging session.
