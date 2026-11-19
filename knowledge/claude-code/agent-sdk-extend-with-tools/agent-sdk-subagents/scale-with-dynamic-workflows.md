---
type: "Feature"
title: "Workflow tool for large agent runs"
description: "For dozens to hundreds of agents, the Workflow tool moves orchestration into a script run outside the conversation context."
resource: "https://code.claude.com/docs/en/agent-sdk/subagents"
tags: [workflows, orchestration, scale, typescript]
kind: "tool"
maturity: "unlabelled"
since: "0.3.149"
surfaces: [sdk]
requires: "TypeScript Agent SDK v0.3.149 or later"
identifiers:
  - "Workflow"
  - "allowedTools"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-subagents"
    resource: "https://code.claude.com/docs/en/agent-sdk/subagents"
    title: "Subagents in the SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Subagents suit a few delegated tasks per turn. For runs that coordinate dozens to hundreds of agents, the `Workflow` tool runs orchestration in a script the runtime executes outside the conversation context. The docs point to the dynamic workflows page for how this differs from turn-by-turn delegation.

# How to use it

Available in the TypeScript Agent SDK v0.3.149 and later. Include `Workflow` in `allowedTools` to auto-approve workflow runs. Input and output schemas are in the TypeScript reference.
