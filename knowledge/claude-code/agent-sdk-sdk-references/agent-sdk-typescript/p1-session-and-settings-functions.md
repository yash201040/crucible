---
type: "Reference"
title: "Session, settings and model helper functions"
description: "Top-level functions to list, read, rename, tag and fork sessions, resolve effective settings, and test deniedModels."
resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
tags: [sessions, fork, settings, resolve, list]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: "resolveSettings() and matchDeniedModels() are alpha; matchDeniedModels needs v0.3.323+"
identifiers:
  - "listSessions()"
  - "getSessionMessages()"
  - "getSessionInfo()"
  - "renameSession()"
  - "tagSession()"
  - "forkSession()"
  - "resolveSettings()"
  - "matchDeniedModels()"
  - "SDKSessionInfo"
  - "SessionMessage"
  - "upToMessageId"
  - "includeWorktrees"
  - "includeSystemMessages"
  - "serverManagedSettings"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-typescript"
    resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
    title: "Agent SDK reference - TypeScript"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Standalone functions that work on stored sessions and settings without starting a query.

# How to use it

| Function | Parameters | Returns / behavior |
| :- | :- | :- |
| `listSessions({ dir?, limit?, includeWorktrees? })` | `includeWorktrees` default `true` | `SDKSessionInfo[]` sorted by `lastModified` desc; all projects if `dir` omitted |
| `getSessionMessages(sessionId, { dir?, limit?, offset?, includeSystemMessages? })` | `includeSystemMessages` default `false` | `SessionMessage[]` with `type`, `uuid`, `session_id`, `message`, `parent_tool_use_id`, `parent_agent_id` (nested subagent; Claude Code v2.1.202+) |
| `getSessionInfo(sessionId, { dir? })` | | `SDKSessionInfo` or `undefined`, no directory scan |
| `renameSession(sessionId, title, { dir? })` | title non-empty after trim | Appends custom-title entry; last wins |
| `tagSession(sessionId, tag|null, { dir? })` | `null` clears | Last wins |
| `forkSession(sessionId, { dir?, upToMessageId?, title? })` | | `{ sessionId }`; pass as `resume`. Fork lacks original's file checkpoints. Throws if not a UUID, session missing/empty, or `upToMessageId` unmatched. Default title is original plus `(fork)` |
| `resolveSettings({ cwd?, settingSources?, managedSettings?, serverManagedSettings? })` | alpha | `{ effective, provenance, sources }` using the CLI merge engine without spawning it |
| `matchDeniedModels(models, deniedModels)` | alpha | `{ denied: boolean[]; warnings: string[] }`; `false` does not mean allowed (aliases and overrides also checked) |

`SDKSessionInfo` fields: `sessionId`, `summary`, `lastModified`, `fileSize` (local JSONL only), `customTitle`, `firstPrompt`, `gitBranch`, `cwd`, `tag`, `createdAt`.

# Limits and defaults

`resolveSettings()` differs from a live session: it reads MDM sources but does not run the `policyHelper` subprocess; it does not fetch server-managed settings (pass `serverManagedSettings`); it returns `permissions.defaultMode` as-is, including `auto` and `bypassPermissions` from project/local settings that a live session ignores. Passing `settingSources: []` skips user/project/local but endpoint-managed policy still loads.
