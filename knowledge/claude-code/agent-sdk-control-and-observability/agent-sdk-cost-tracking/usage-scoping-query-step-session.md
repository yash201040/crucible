---
type: "Concept"
title: "Usage scope: query, step, session"
description: "How token usage is scoped per query() call, per step with shared message IDs, and per resumed session."
resource: "https://code.claude.com/docs/en/agent-sdk/cost-tracking"
tags: [usage, tokens, sessions, deduplication]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "modelUsage"
  - "model_usage"
  - "message.message.id"
  - "message.message.usage"
  - "message.usage"
  - "message.message_id"
  - "input_tokens"
  - "output_tokens"
  - "resume"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-cost-tracking"
    resource: "https://code.claude.com/docs/en/agent-sdk/cost-tracking"
    title: "Track cost and usage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Both SDKs expose the same usage data with different names. TypeScript: per-step usage on each assistant message (`message.message.id`, `message.message.usage`), per-model cost via `modelUsage` on the result, cumulative total on the result. Python: `message.usage` and `message.message_id` per step, `model_usage` on the result, `total_cost_usd` on the result.

Scopes:
- `query()` call: one invocation, many steps; produces one `result` message at the end, except in streaming input mode where each user turn emits its own result.
- Step: one request/response cycle; produces assistant messages with token usage. When Claude uses several tools in one turn, all those messages share the same ID, so deduplicate by ID.
- Session: `query()` calls linked by a session ID through `resume`. A resumed call's results report the whole session's spend.

# How to use it

If you only need the estimated total, ignore per-step usage and read the single result value. Independent `query()` calls each report only their own cost; a call that resumes a session also counts the session's earlier spend.
