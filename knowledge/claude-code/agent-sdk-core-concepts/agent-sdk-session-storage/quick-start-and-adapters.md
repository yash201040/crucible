---
type: "Guide"
title: "Session store quick start, adapters, conformance"
description: "InMemorySessionStore example, writing an adapter, reference S3/Redis/Postgres adapters and the conformance suite."
resource: "https://code.claude.com/docs/en/agent-sdk/session-storage"
tags: [session-store, adapters, conformance, s3]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "InMemorySessionStore"
  - "run_session_store_conformance"
  - "claude_agent_sdk.testing"
  - "examples/session-stores/"
  - "examples/session_stores/"
  - "S3SessionStore"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-session-storage"
    resource: "https://code.claude.com/docs/en/agent-sdk/session-storage"
    title: "Persist sessions to external storage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The SDK ships `InMemorySessionStore` for development and testing. Run a query with `options: { sessionStore: store }` (Python `ClaudeAgentOptions(session_store=store)`), capture `session_id` from the result, then call `query()` again with the same store and `resume`; the transcript loads from the store.

# How to use it

Write an adapter by implementing `append` and `load`; add the optional methods for listing, summaries, deletion and subagent resume. Treat entries as opaque JSON-safe values, persist in order, return them in the same order; `load` must return entries deep-equal to those appended (byte-equal not required).

| Storage type | Model | Example adapter |
| :- | :- | :- |
| Object store | One part file per `append()`; `load()` lists, sorts, concatenates | S3 |
| Key-value store | List per transcript plus sorted session index | Redis |
| Relational or document | One row/document per entry, ordered by key assigned on insert | Postgres |

Reference adapters live in the SDK repos' `examples/session-stores/` (TypeScript) and `examples/session_stores/` (Python); they are not published packages, so copy one. Each takes a pre-configured client.

# Limits and defaults

Conformance suite: TypeScript copy `shared/conformance.ts`; Python ships `claude_agent_sdk.testing.run_session_store_conformance` (needs pytest installed; takes a zero-argument factory that returns a fresh, empty store each call). Optional-method tests skip automatically.
