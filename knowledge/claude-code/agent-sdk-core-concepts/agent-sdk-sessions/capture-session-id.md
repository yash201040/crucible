---
type: "Guide"
title: "Capture the session ID"
description: "Where to read the session ID: result message in both SDKs, init message earlier in TypeScript."
resource: "https://code.claude.com/docs/en/agent-sdk/sessions"
tags: [sessions, session-id, result-message]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "session_id"
  - "ResultMessage"
  - "SDKResultMessage"
  - "SystemMessage.data"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-sessions"
    resource: "https://code.claude.com/docs/en/agent-sdk/sessions"
    title: "Work with sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Resume and fork need a session ID. Read `session_id` from the result message (`ResultMessage` in Python, `SDKResultMessage` in TypeScript); it is present on every result, success or error. In TypeScript it is also a direct field on the init `SystemMessage`; in Python it is nested in `SystemMessage.data`.

# Limits and defaults

If the process fails before any result (connection or process failure), no ID is captured. A single-shot `query()` raises after an error result, so catch the error after capturing the ID.
