---
type: "Feature"
title: "Background subagents and forks"
description: "By default spawned subagents run in the background (async_launched); Claude can wait, and from v2.1.302 it can start forked subagents."
resource: "https://code.claude.com/docs/en/agent-sdk/subagents"
tags: [subagents, background, fork, async]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.302"
surfaces: [sdk]
requires: "Claude Code v2.1.302 for forks"
identifiers:
  - "async_launched"
  - "completed"
  - "background"
  - "subagent_type: \"fork\""
  - "Agent(fork)"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-subagents"
    resource: "https://code.claude.com/docs/en/agent-sdk/subagents"
    title: "Subagents in the SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

By default a subagent the main agent spawns runs in the background: the Agent tool result has `status: "async_launched"` and the report arrives in a later turn. Claude blocks (result `status: "completed"`) when its next action needs the report.

A fork is a subagent that copies the conversation so far instead of starting fresh. From Claude Code v2.1.302, Claude can start forks with nothing configured by calling the Agent tool with `subagent_type: "fork"`.

# How to use it

- Make Claude wait: say so in the prompt ("run the test-runner agent and wait for it").
- Keep an agent in the background: set `background: true` in its definition.
- Stop forks: add a deny rule `Agent(fork)` via `disallowedTools` / `disallowed_tools`; other subagent types still run.

# Notes

A fork does not get the named-agents list that a `SendMessage`-capable subagent receives, since it inherits the parent conversation.
