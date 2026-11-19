---
type: "Concept"
title: "Dual-write architecture and conflicts"
description: "The subprocess writes locally first and the SDK mirrors to the store; which copy survives and unsupported option combinations."
resource: "https://code.claude.com/docs/en/agent-sdk/session-storage"
tags: [session-store, local-disk, auth, persistsession]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "CLAUDE_CONFIG_DIR"
  - "persistSession"
  - "enableFileCheckpointing"
  - "enable_file_checkpointing"
  - "CLAUDE_CODE_OAUTH_TOKEN"
  - "ANTHROPIC_API_KEY"
  - "apiKeyHelper"
  - "Not logged in"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-session-storage"
    resource: "https://code.claude.com/docs/en/agent-sdk/session-storage"
    title: "Persist sessions to external storage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The Claude Code subprocess always writes each batch to local disk first, then the SDK forwards it to the store's `append()`; the store mirrors, not replaces.
- Fresh session, or resume when the store has nothing: the local transcript outlives the run; the store gets a copy.
- Run resumed from the store: the local copy is deleted at run end, so the store holds the only durable copy.

# How to use it

To keep a fresh session off local disk, set `CLAUDE_CONFIG_DIR` to a new private temp directory in `options.env` (TypeScript: spread `process.env` too). If you do that and authenticate via a claude.ai login or an `apiKeyHelper` in user `settings.json`, the run fails with `Not logged in`. Fixes: set `CLAUDE_CODE_OAUTH_TOKEN` (from `claude setup-token`; model requests only, so claude.ai connectors are unavailable), set `ANTHROPIC_API_KEY`, or copy config files into the temp directory.

# Limits and defaults

The SDK throws at startup if a store is combined with:
- `persistSession: false` (TypeScript; Python has no equivalent)
- file checkpointing (`enableFileCheckpointing` / `enable_file_checkpointing`), whose backups go to local disk and are not mirrored
