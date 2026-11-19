---
type: "Reference"
title: "Store-backed helpers, forks, subagents, retention"
description: "How getSessionMessages, forkSession, subagent transcripts and retention behave with a store, and which functions accept sessionStore."
resource: "https://code.claude.com/docs/en/agent-sdk/session-storage"
tags: [session-store, fork, subagents, retention]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "getSessionMessages"
  - "forkSession"
  - "listSubagents"
  - "getSubagentMessages"
  - "listSessions"
  - "getSessionInfo"
  - "renameSession"
  - "tagSession"
  - "deleteSession"
  - "startup"
  - "query"
  - "cleanupPeriodDays"
  - "list_sessions_from_store"
  - "get_session_info_from_store"
  - "get_session_messages_from_store"
  - "list_subagents_from_store"
  - "get_subagent_messages_from_store"
  - "rename_session_via_store"
  - "tag_session_via_store"
  - "delete_session_via_store"
  - "fork_session_via_store"
  - "subagents/agent-<id>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-session-storage"
    resource: "https://code.claude.com/docs/en/agent-sdk/session-storage"
    title: "Persist sessions to external storage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

TypeScript functions accepting `sessionStore`: `query()`, `startup()`, `listSessions()`, `getSessionInfo()`, `getSessionMessages()`, `renameSession()`, `tagSession()`, `deleteSession()`, `forkSession()`, `listSubagents()`, `getSubagentMessages()`.

Python: set `session_store` in `ClaudeAgentOptions` for `query()`; other operations have store-backed functions: `list_sessions_from_store()`, `get_session_info_from_store()`, `get_session_messages_from_store()`, `list_subagents_from_store()`, `get_subagent_messages_from_store()`, `rename_session_via_store()`, `tag_session_via_store()`, `delete_session_via_store()`, `fork_session_via_store()`. `startup()` has no Python equivalent; the standalone `list_sessions()` etc. read local files.

# How to use it

- `getSessionMessages({ sessionStore })` returns the post-compaction linked chain the agent would see on resume (503 raw entries might yield 18 messages); use `store.load(key)` for the full raw history.
- `forkSession({ sessionStore })` reads entries, rewrites every `sessionId`, remaps message UUIDs and appends under a new key; it is not a byte copy and adapters must not shortcut with a copy.
- Subagent transcripts mirror under `subpath: "subagents/agent-<id>"`. `listSubagents` requires `listSubkeys`; `getSubagentMessages` uses it when available, else falls back to the direct subpath.

# Limits and defaults

Retention: the SDK never deletes from your store; use backend expiry or scheduled cleanup. Local transcripts under `CLAUDE_CONFIG_DIR` are swept by `cleanupPeriodDays`. A run resumed from the store leaves no local transcript, so your store's retention is the only one.
