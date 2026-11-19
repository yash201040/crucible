---
type: "Reference"
title: "File checkpointing and Bash output limit"
description: "fileCheckpointingEnabled (rewind snapshots, ignored in -p and SDK) and bashOutputMaxChars (inline output cap, 4000 to 128000)."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [checkpointing, rewind, bash-output, limits]
kind: "setting"
maturity: "unlabelled"
since: "2.1.261"
surfaces: [cli, headless, sdk]
requires: "bashOutputMaxChars v2.1.261"
identifiers:
  - "fileCheckpointingEnabled"
  - "bashOutputMaxChars"
  - "CLAUDE_CODE_DISABLE_FILE_CHECKPOINTING"
  - "CLAUDE_CODE_ENABLE_SDK_FILE_CHECKPOINTING"
  - "enableFileCheckpointing"
  - "BASH_MAX_OUTPUT_LENGTH"
  - "/rewind"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`fileCheckpointingEnabled` (Boolean, default `true`, scope `Any file`) snapshots files before each edit so `/rewind` can restore them; `/config` **Rewind code (checkpoints)** writes it to user settings. `bashOutputMaxChars` (scope `Any file`) sets how many characters of a successful Bash or PowerShell command's output Claude receives inline.

# How to use it

```json
{ "fileCheckpointingEnabled": false, "bashOutputMaxChars": 100000 }
```

# Limits and defaults

- `CLAUDE_CODE_DISABLE_FILE_CHECKPOINTING` turns checkpointing off for a session; whichever of the two turns it off, the other cannot turn it back on.
- In a `-p` run or an Agent SDK session `fileCheckpointingEnabled` is ignored. The SDK turns checkpointing on with its `enableFileCheckpointing` option and a bare `-p` run needs `CLAUDE_CODE_ENABLE_SDK_FILE_CHECKPOINTING=true`.
- `bashOutputMaxChars`: positive integer, clamped into `4000` to `128000`; default unset means up to 30,000 characters inline. Beyond the limit the output is saved to a file and Claude gets a short preview plus the path. When the key is set the `BASH_MAX_OUTPUT_LENGTH` variable is ignored.
