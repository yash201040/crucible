---
type: "Guide"
title: "Checkpoint before risky operations and multiple restore points"
description: "Two patterns: keep only the latest checkpoint UUID to revert mid-stream, or store every prompt's UUID to rewind to any turn."
resource: "https://code.claude.com/docs/en/agent-sdk/file-checkpointing"
tags: [checkpointing, patterns, revert, restore-points]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "tool_use_result"
  - "parent_tool_use_id"
  - "isReplay"
  - "rewind_files()"
  - "rewindFiles()"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-file-checkpointing"
    resource: "https://code.claude.com/docs/en/agent-sdk/file-checkpointing"
    title: "Rewind file changes with checkpointing"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two ways to use checkpoint UUIDs.

# How to use it

- Checkpoint before risky operations: update one `safe_checkpoint` variable at each prompt you send. In Python a checkpoint message is a `UserMessage` with `uuid`, `tool_use_result is None` and `parent_tool_use_id is None`; in TypeScript it is `message.type === "user"` with `isReplay` and `uuid`. If your own revert condition (error detection, validation failure, user input) trips, call rewind with the saved UUID and break out of the loop; no session ID is needed because the connection is still open.
- Multiple restore points: store every checkpoint UUID with metadata (description, timestamp) in an array. After the session, resume with an empty prompt and rewind to any of them, for example to keep a refactor from the first prompt and undo tests added by the second.
