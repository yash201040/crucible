---
type: "Concept"
title: "Teammate context, communication and token cost"
description: "What a teammate loads at spawn, how messages and idle notifications flow, and the subagentPromptCacheTtl cache setting for in-process teammates."
resource: "https://code.claude.com/docs/en/agent-teams"
tags: [agent-teams, context, tokens, prompt-caching]
kind: "mixed"
maturity: "experimental"
since: "2.1.281"
surfaces: [cli]
requires: ""
identifiers:
  - "--setting-sources"
  - "subagentPromptCacheTtl"
  - "CLAUDE.md"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-teams"
    resource: "https://code.claude.com/docs/en/agent-teams"
    title: "Orchestrate teams of Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each teammate has its own context window. At spawn it loads the same project context as a regular session (CLAUDE.md, MCP servers, skills) and receives the lead's spawn prompt. The lead's conversation history does not carry over.

# How to use it

- If the lead starts with `--setting-sources`, teammates load from the same restricted list. Before v2.1.281, split-pane teammates loaded every settings source.
- Messages are delivered automatically; the lead does not poll.
- Idle notification: when a teammate finishes and stops it notifies the lead with its final answer. A teammate whose turn ends on an API error notifies the lead of the failure with the error text.
- Teammates can see and claim shared tasks if they have the Task tools. Messaging targets one teammate by name; to reach everyone send one message per recipient.
- The lead names every teammate at spawn; state names in the spawn instruction for predictable names.
- Cache: an in-process teammate's requests fall outside the main conversation's cache TTL bucket, so its cache holds five minutes by default, including on a Claude subscription. Set `subagentPromptCacheTtl` to `1h` to keep it an hour; the API bills 1-hour cache writes at a higher rate.

# Limits and defaults

Agent teams use significantly more tokens than a single session; usage scales with the number of active teammates (see "agent team token costs" on the costs page).
