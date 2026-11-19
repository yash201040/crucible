---
type: "Reference"
title: "SessionStore interface"
description: "Required append and load plus four optional methods, SessionKey shape and when each method is called."
resource: "https://code.claude.com/docs/en/agent-sdk/session-storage"
tags: [session-store, interface, append, load]
kind: "api"
maturity: "unlabelled"
since: "0.3.234"
surfaces: [sdk]
requires: ""
identifiers:
  - "SessionStore"
  - "SessionKey"
  - "SessionStoreEntry"
  - "SessionSummaryEntry"
  - "append"
  - "load"
  - "listSessions"
  - "listSessionSummaries"
  - "delete"
  - "listSubkeys"
  - "foldSessionSummary"
  - "fold_session_summary"
  - "projectKey"
  - "sessionId"
  - "subpath"
  - "CLAUDE_CODE_PROJECT_DIR_NAME"
  - "sessionStore"
  - "session_store"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-session-storage"
    resource: "https://code.claude.com/docs/en/agent-sdk/session-storage"
    title: "Persist sessions to external storage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A `SessionStore` adapter mirrors session transcripts (default: JSONL under `~/.claude/projects/`) to your own backend so another host with a matching working directory can resume. Reasons: multi-host deployments, durability, compliance and audit.

`SessionKey` = `{ projectKey, sessionId, subpath? }` (Python `project_key`, `session_id`, `subpath`). `projectKey` is a filesystem-safe encoding of the working directory; `subpath` is set for subagent transcripts or sidecars (for example `subagents/agent-<id>`); undefined means the main transcript. Treat `subpath` as opaque.

# How to use it

| Method | Required | Called when |
| :- | :- | :- |
| `append` | Yes | After each batch of entries is written locally |
| `load` | Yes | Before subprocess spawns for `resume` or `continue: true`; return `null` if unknown |
| `listSessions` | No | By `listSessions({ sessionStore })` and `query()`/`startup()` with `continue: true`; if undefined, `continue: true` throws |
| `listSessionSummaries` | No | One-call metadata reads; maintain summaries in `append`; fallback is `listSessions` plus per-session `load` |
| `delete` | No | By `deleteSession({ sessionStore })`; deleting the main key must cascade to subkeys and the summary; undefined means no-op |
| `listSubkeys` | No | On resume to find subagent transcripts; without it only the main transcript is restored |

Summaries: call `foldSessionSummary` / `fold_session_summary` per batch inside `append`, skipping batches with a `subpath`. The fold never sets `mtime`; stamp it at persist time (`options.mtime` in TypeScript). `mtime` must share a clock with `listSessions` values. Serialize read-fold-write per session (transaction, compare-and-swap, or lock).

# Limits and defaults

- Resume from a working directory matching the original run. In TypeScript, `CLAUDE_CODE_PROJECT_DIR_NAME` beside `CLAUDE_CONFIG_DIR` in a query's `env` changes the key; standalone helpers (`listSessions`, `deleteSession`) read the process environment, so set both there too. Requires Agent SDK v0.3.234 or later.
