---
type: "Feature"
title: "API trigger and /fire endpoint"
description: "Start a scheduled task by POSTing to its own /fire endpoint with a per-task bearer token and optional text context."
resource: "https://code.claude.com/docs/en/routines"
tags: [api, trigger, fire, bearer-token, beta-header]
kind: "api"
maturity: "research-preview"
since: ""
surfaces: [cloud, web]
requires: "claude.ai users only; not part of the Claude Platform API"
identifiers:
  - "/v1/claude_code/routines/<trigger_id>/fire"
  - "anthropic-beta: experimental-cc-routine-2026-04-01"
  - "anthropic-version: 2023-06-01"
  - "Authorization: Bearer"
  - "text"
  - "<routine-fire-payload>"
  - "routine_fire"
  - "claude_code_session_id"
  - "claude_code_session_url"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "routines"
    resource: "https://code.claude.com/docs/en/routines"
    title: "Automate work with scheduled tasks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An API trigger gives a task a dedicated HTTP endpoint. A POST with the task's bearer token starts a new session and returns its URL. Use it for alerting, deploy pipelines or internal tools. Added on the web only (edit dialog > Trigger row > + > API); the Fire URL and token are shown, the token appears once and cannot be retrieved. Each task has its own token scoped to that task. It takes effect when generated, without Save changes. Delete token removes the trigger; Regenerate invalidates the previous token.

# How to use it

```bash
curl -X POST https://api.anthropic.com/v1/claude_code/routines/trig_01ABCDEFGHJKLMNOPQRSTUVW/fire \
  -H "Authorization: Bearer sk-ant-oat01-xxxxx" \
  -H "anthropic-beta: experimental-cc-routine-2026-04-01" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{"text": "Sentry alert SEN-4521 fired in prod. Stack trace attached."}'
```

Response JSON: `{"type": "routine_fire", "claude_code_session_id": "...", "claude_code_session_url": "..."}`. Wrong token gives `401`.

`text` is optional, freeform and unparsed (JSON arrives as a literal string). It reaches the task wrapped in a `<routine-fire-payload>` block labeled as untrusted data with an instruction not to follow it unless the saved prompt says to. The same wrapping applies to text given with Run now. The saved prompt must therefore reference the payload explicitly (for example "Investigate the alert described in the routine-fire-payload block").

# Limits and defaults

- Endpoint ships under the `experimental-cc-routine-2026-04-01` beta header; shapes, rate limits and token semantics may change in research preview. Breaking changes ship under new dated headers and the two most recent previous header versions keep working.
- Rate limits: see the usage-limits concept (30 per hour per task shared with Run now; 100 per hour per account for API fires).
- Full reference: platform.claude.com "Trigger a routine through the API".
