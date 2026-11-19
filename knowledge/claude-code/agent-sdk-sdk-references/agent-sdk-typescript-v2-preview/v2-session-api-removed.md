---
type: "Feature"
title: "TypeScript SDK V2 session API (removed)"
description: "The experimental unstable_v2 session API (createSession, resumeSession, prompt) was removed in TypeScript Agent SDK 0.3.142; use query() instead."
resource: "https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview"
tags: [agent-sdk, typescript, sessions, deprecated, migration]
kind: "api"
maturity: "deprecated"
since: "0.3.142"
surfaces: [sdk]
requires: "TypeScript 5.2+ for `await using`; Agent SDK 0.2.x to use it"
identifiers:
  - "unstable_v2_createSession"
  - "unstable_v2_resumeSession"
  - "unstable_v2_prompt"
  - "SDKSession"
  - "SDKSessionOptions"
  - "session.send()"
  - "session.stream()"
  - "session.close()"
  - "@anthropic-ai/claude-agent-sdk@0.2"
  - "forkSession"
  - "options.resume"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-typescript-v2-preview"
    resource: "https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview"
    title: "TypeScript SDK V2 session API (removed)"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

V2 was an experimental TypeScript Agent SDK session interface that replaced async generators and yield coordination with a separate send and stream cycle per turn. TypeScript Agent SDK 0.3.142 removes `unstable_v2_createSession`, `unstable_v2_resumeSession`, `unstable_v2_prompt` and the `SDKSession` and `SDKSessionOptions` types. The page is kept only for people maintaining code on Agent SDK 0.2.x or earlier.

# How to use it

Migration: use the `query()` API and its session options. For multi-turn conversations pass an `AsyncIterable<SDKUserMessage>` as the prompt; to continue a saved session pass `options.resume` with the session ID.

| V2 name | What it did |
| :- | :- |
| `unstable_v2_createSession(options)` | Create a session; `options.model` is required, other options accepted. Returns `SDKSession`. |
| `unstable_v2_resumeSession(sessionId, options)` | Resume a session by ID. |
| `unstable_v2_prompt(prompt, options)` | One-shot single-turn query; returns `Promise<SDKResultMessage>` (check `result.subtype === "success"`). |
| `session.send(message)` | Send a string or `SDKUserMessage`. |
| `session.stream()` | `AsyncGenerator<SDKMessage>` of the response. |
| `session.close()` | Close the session; `await using session = ...` (TypeScript 5.2+) closes it automatically. |
| `session.sessionId` | Read-only ID; also available as `msg.session_id` on any streamed message. |

To keep using V2, install the last compatible release: `npm install @anthropic-ai/claude-agent-sdk@0.2`.

# Limits and defaults

- Agent SDK 0.2.x is the last version with V2; the package version jumped from 0.2.x directly to 0.3.142.
- V2 did not support session forking (`forkSession` option) or some advanced streaming input patterns; those need the V1 `query()` API.
- The SDK bundles a native Claude Code binary as an optional dependency, so most installs need no separate Claude Code install.
