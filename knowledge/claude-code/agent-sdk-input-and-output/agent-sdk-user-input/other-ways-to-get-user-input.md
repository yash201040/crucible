---
type: "Concept"
title: "Other ways to get user input"
description: "Streaming input and custom tools as alternatives to canUseTool and AskUserQuestion."
resource: "https://code.claude.com/docs/en/agent-sdk/user-input"
tags: [agent-sdk, streaming-input, custom-tools, user-input]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers: []
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-user-input"
    resource: "https://code.claude.com/docs/en/agent-sdk/user-input"
    title: "Handle approvals and user input"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two options beyond `canUseTool` and `AskUserQuestion`.

# How to use it

- Streaming input: interrupt the agent mid-task, give extra context without waiting to be asked, and build chat UIs for follow-ups during long runs. See [streaming input](../agent-sdk-streaming-vs-single-mode/single-shot-vs-streaming-input.md).
- Custom tools: collect structured input (forms, wizards, multi-step flows beyond multiple choice), integrate external approval systems (ticketing, workflow platforms), and build domain-specific interactions. They give full control but need more implementation work than the built-in `canUseTool` callback.
