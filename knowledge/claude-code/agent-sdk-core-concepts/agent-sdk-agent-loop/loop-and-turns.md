---
type: "Concept"
title: "The agent loop and turns"
description: "Prompt, evaluate, execute tools, repeat, return result; what a turn is and how max_turns counts."
resource: "https://code.claude.com/docs/en/agent-sdk/agent-loop"
tags: [agent-loop, turns, max-turns, lifecycle]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "max_turns"
  - "maxTurns"
  - "error_max_turns"
  - "SystemMessage"
  - "AssistantMessage"
  - "ResultMessage"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-agent-loop"
    resource: "https://code.claude.com/docs/en/agent-sdk/agent-loop"
    title: "How the agent loop works"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The SDK runs the same loop as Claude Code: Claude evaluates the prompt, calls tools, gets results, repeats until a response has no tool calls. Both TypeScript and Python SDKs bundle a native Claude Code binary.

Cycle: (1) receive prompt, SDK yields a `SystemMessage` subtype `"init"`; (2) Claude responds, one `AssistantMessage` per content block; (3) SDK runs tools; hooks can intercept; (4) repeat; (5) final `AssistantMessage` with text, then a `ResultMessage` (final text, token usage, cost, session ID).

# How to use it

A turn is one pass: output, and if it has tool calls, execution and feedback without returning control to your code. Example "Fix the failing tests in auth.ts" took four turns: three with tool calls, one final text-only.

Cap with `max_turns` / `maxTurns`: count each turn with tool calls plus one for the final text-only response. Hitting the cap ends with a `ResultMessage` of subtype `error_max_turns` and no final response.

# Limits and defaults

Without limits the loop runs until Claude finishes, which can run long on open-ended prompts. Setting a budget is a good default for production agents. See [turns and budget](./turns-and-budget.md).
