---
type: "Feature"
title: "Changing the prompt of a resumed session"
description: "The system prompt is recorded on a session's first request; how to update instructions mid-session and the snapshot option."
resource: "https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts"
tags: [system-prompt, resume, snapshot, additional-context]
kind: "setting"
maturity: "unlabelled"
since: "2.1.265"
surfaces: [sdk]
requires: "Claude Code v2.1.265 or later; @anthropic-ai/claude-agent-sdk v0.3.257 or later or claude-agent-sdk v0.2.153 or later for snapshot"
identifiers:
  - "snapshot"
  - "additionalContext"
  - "UserPromptSubmit"
  - "PostToolUse"
  - "--bare"
  - "extraArgs"
  - "CLAUDE_CODE_SIMPLE"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-modifying-system-prompts"
    resource: "https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts"
    title: "Modifying system prompts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code records the system prompt on a session's first request and reuses it until the session is compacted. If you pass a different `append` or custom prompt on `resume` or `continue`, Claude does not see it on the next turn; it takes effect after compaction or in a new session.

# How to use it

To change instructions mid-session, send them in the conversation: in the next user message, or return `additionalContext` from a `UserPromptSubmit` or `PostToolUse` hook callback, phrased as a factual statement (for example "The workspace is now read-only"). The recorded prompt stays unchanged.

While iterating on wording, set `snapshot: false` on the object form of the system prompt (preset and custom forms): Claude Code then rebuilds the prompt every request. Needs `@anthropic-ai/claude-agent-sdk` v0.3.257 or later, or `claude-agent-sdk` v0.2.153 or later.

# Limits and defaults

- Keep recording on in production: with it off, a changed prompt on a resumed session reaches Claude next turn but the request cannot reuse the session's prompt cache, and where the API enforces preserved thinking Claude loses its earlier thinking.
- Outside cloud sessions, bare mode (`--bare` via `extraArgs` or `CLAUDE_CODE_SIMPLE=1`) leaves recording off unless `snapshot: true`.
- Recording by default needs Claude Code v2.1.265 or later (TypeScript SDK bundles from v0.3.265, Python from v0.2.153). Before v2.1.268, sessions that do not fetch feature flags (including Bedrock, Google Cloud's Agent Platform, Microsoft Foundry) rebuilt the prompt every request and `snapshot` had no effect.
