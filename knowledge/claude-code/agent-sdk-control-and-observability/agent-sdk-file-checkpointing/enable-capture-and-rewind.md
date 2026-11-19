---
type: "Guide"
title: "Enable, capture UUIDs and rewind"
description: "Options to enable checkpointing, receive checkpoint UUIDs, and rewind by resuming with an empty prompt or via the CLI flag."
resource: "https://code.claude.com/docs/en/agent-sdk/file-checkpointing"
tags: [checkpointing, resume, cli-flag, uuid]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [sdk, cli]
requires: ""
identifiers:
  - "enable_file_checkpointing"
  - "enableFileCheckpointing"
  - "extra_args"
  - "extraArgs"
  - "replay-user-messages"
  - "rewind_files()"
  - "rewindFiles()"
  - "--rewind-files"
  - "CLAUDE_CODE_ENABLE_SDK_FILE_CHECKPOINTING"
  - "isReplay"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-file-checkpointing"
    resource: "https://code.claude.com/docs/en/agent-sdk/file-checkpointing"
    title: "Rewind file changes with checkpointing"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Enable checkpointing, capture checkpoint UUIDs from the stream, then rewind.

# How to use it

| Option | Python | TypeScript | Purpose |
| - | - | - | - |
| Enable | `enable_file_checkpointing=True` | `enableFileCheckpointing: true` | tracks file changes |
| Receive UUIDs | `extra_args={"replay-user-messages": None}` | `extraArgs: { "replay-user-messages": null }` | required to get user message UUIDs in the stream |

1. With `replay-user-messages` set, the user message for each prompt that starts a turn has a UUID that is a checkpoint. User messages carrying tool results have a UUID that is not a checkpoint. Capture the first user message UUID to restore the original state; the session ID (`message.session_id`) is only needed to rewind after the stream completes.
2. Rewind after the stream: resume the session (`resume=session_id`) with checkpointing enabled and an empty prompt `""`, then call `rewind_files(checkpoint_id)` / `rewindFiles(checkpointId)` from inside the response loop. You can also rewind during the stream.
3. From the CLI (needs the `claude` executable): `CLAUDE_CODE_ENABLE_SDK_FILE_CHECKPOINTING=true claude -p --resume <session-id> --rewind-files <checkpoint-uuid>`. The SDK sets the variable for you; bare `claude -p` does not. `--rewind-files` does not appear in `claude --help` but works; success prints `Files rewound to state at message <checkpoint-uuid>` and exits without sending a prompt.

# Notes

The examples use `permission_mode="acceptEdits"` so edits are auto-approved.
