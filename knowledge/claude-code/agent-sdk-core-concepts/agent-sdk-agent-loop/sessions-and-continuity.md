---
type: "Concept"
title: "Sessions and continuity in the loop"
description: "Capturing the session ID, resume and fork, and pointers to session storage for stateless hosts."
resource: "https://code.claude.com/docs/en/agent-sdk/agent-loop"
tags: [sessions, resume, fork, session-id]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "session_id"
  - "session_store"
  - "sessionStore"
  - "ClaudeSDKClient"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-agent-loop"
    resource: "https://code.claude.com/docs/en/agent-sdk/agent-loop"
    title: "How the agent loop works"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each interaction creates or continues a session. Capture the ID from `ResultMessage.session_id` (both SDKs). TypeScript also exposes it directly on the init `SystemMessage`; in Python it is nested in `SystemMessage.data`.

# How to use it

On resume, full prior context returns. A session can be forked to branch without modifying the original. To resume across stateless containers or serverless hosts, pass a `session_store` / `sessionStore` adapter so transcripts mirror to your backend; the subprocess still writes to local disk first. In Python, `ClaudeSDKClient` handles session IDs across calls.

See [sessions](../agent-sdk-sessions/continue-resume-fork.md) and [session storage](../agent-sdk-session-storage/dual-write-architecture.md).
