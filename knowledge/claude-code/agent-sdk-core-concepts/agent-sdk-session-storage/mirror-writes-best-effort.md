---
type: "Limit"
title: "Mirror writes are best-effort"
description: "append retries up to three attempts, then drops the batch and emits a mirror_error system message."
resource: "https://code.claude.com/docs/en/agent-sdk/session-storage"
tags: [session-store, retry, errors, monitoring]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "mirror_error"
  - "entry.uuid"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-session-storage"
    resource: "https://code.claude.com/docs/en/agent-sdk/session-storage"
    title: "Persist sessions to external storage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

If `append()` rejects, the SDK retries the batch up to two more times with short backoff (three attempts total). A call that times out is not retried since the original may still land. Retries can re-deliver entries, so deduplicate by `entry.uuid` in `append()` and keep every entry without a `uuid`.

# How to use it

After the final failure the SDK logs the error, emits `{ type: "system", subtype: "mirror_error" }` into the iterator, drops the batch and continues the query. Monitor `mirror_error` to detect store data loss.

# Limits and defaults

A store outage does not interrupt the agent, since the subprocess writes locally first. On a run resumed from the store, a dropped batch has no surviving copy after the run ends.
