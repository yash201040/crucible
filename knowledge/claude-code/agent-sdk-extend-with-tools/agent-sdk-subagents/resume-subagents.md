---
type: "Feature"
title: "Resume a subagent"
description: "Resume a finished or partial subagent by passing resume with the session ID and naming the agentId in the prompt."
resource: "https://code.claude.com/docs/en/agent-sdk/subagents"
tags: [subagents, resume, sessions, agentid]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.246"
surfaces: [sdk]
requires: ""
identifiers:
  - "resume"
  - "agentId"
  - "session_id"
  - "cleanupPeriodDays"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-subagents"
    resource: "https://code.claude.com/docs/en/agent-sdk/subagents"
    title: "Subagents in the SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A resumed subagent keeps its full conversation history (tool calls, results, reasoning). When a subagent stops at `maxTurns`, the Agent tool result marks output as partial (Claude Code v2.1.246 or later) so it can be continued.

# How to use it

1. Capture `session_id` from messages (e.g. the `ResultMessage`) of the first query.
2. Parse `agentId: <id>` from the text of the Agent tool result.
3. Run a second query with `resume: sessionId` and put the agent ID in the prompt (e.g. "Resume agent <id> and ...").

For a custom agent pass the same definition in `agents` for both queries.

# Limits and defaults

- Each `query()` starts a new session by default; you must resume the same session to reach the subagent transcript.
- Built-in `Explore` and `Plan` agents are one-shot and return no `agentId`; use a custom agent or `general-purpose` to resume.
- Subagent transcripts are stored in separate files, persist independently of the main conversation; compaction behavior and the `cleanupPeriodDays` cleanup period are in the Claude Code subagents docs.
