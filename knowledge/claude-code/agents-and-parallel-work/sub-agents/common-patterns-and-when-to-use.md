---
type: "Guide"
title: "Common subagent patterns and when to use them"
description: "Isolating high-volume output, parallel research, chaining, and choosing between subagents, main conversation, skills and /btw."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, patterns, parallel, chaining, context]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/btw"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Patterns: isolate high-volume operations (test runs, docs fetches, logs) so only a summary returns; run parallel research with several subagents on independent areas; chain subagents in sequence with Claude passing context between them.

# How to use it

Use the main conversation for: back-and-forth refinement, phases sharing context, quick targeted changes, latency-sensitive work (a non-fork subagent starts fresh). Use subagents for: verbose output, enforced tool restrictions or permissions, self-contained work returning a summary. Skills instead for reusable prompts running in the main context. For a question about what is already in the conversation use `/btw` (no tool access, answer not added to history).

# Limits and defaults

Warning from the page: many subagents returning detailed results can consume significant context, and each spends tokens of its own. For work that must keep running in parallel or exceeds one context window use separate sessions with cross-session messaging.
