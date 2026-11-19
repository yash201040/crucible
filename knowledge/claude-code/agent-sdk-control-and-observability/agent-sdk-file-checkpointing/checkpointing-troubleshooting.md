---
type: "Reference"
title: "Checkpointing errors and fixes"
description: "Causes and fixes for unrecognized options, missing UUIDs, no checkpoint found, rewinding not enabled and ProcessTransport errors."
resource: "https://code.claude.com/docs/en/agent-sdk/file-checkpointing"
tags: [checkpointing, troubleshooting, errors, resume]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [sdk, cli]
requires: ""
identifiers:
  - "No file checkpoint found for this message"
  - "File rewinding is not enabled"
  - "ProcessTransport is not ready for writing"
  - "CLAUDE_CODE_ENABLE_SDK_FILE_CHECKPOINTING"
  - "replay-user-messages"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-file-checkpointing"
    resource: "https://code.claude.com/docs/en/agent-sdk/file-checkpointing"
    title: "Rewind file changes with checkpointing"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

| Symptom | Cause | Fix |
| - | - | - |
| `enableFileCheckpointing` or `rewindFiles()` unavailable | older SDK | `pip install --upgrade claude-agent-sdk` or `npm install @anthropic-ai/claude-agent-sdk@latest` |
| `message.uuid` missing | `replay-user-messages` not set | add `extra_args` / `extraArgs` option |
| `No file checkpoint found for this message` | checkpointing not enabled on the original session; session not completed before resume; UUID came from a tool-result user message | enable it on the original session, capture the first user message UUID, finish the session, resume with an empty prompt, call rewind once |
| `File rewinding is not enabled` | non-interactive rewind without checkpointing: bare `claude -p --rewind-files`, or an SDK session (even resumed) not enabling it | bare CLI: set `CLAUDE_CODE_ENABLE_SDK_FILE_CHECKPOINTING=true`; SDK: set the enable option on the resumed session (the SDK sets the variable internally only then) |
| `ProcessTransport is not ready for writing` | rewind called after the response loop finished (connection closed) | resume with an empty prompt, call rewind on the new query |
