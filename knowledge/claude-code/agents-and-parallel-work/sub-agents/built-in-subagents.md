---
type: "Reference"
title: "Built-in subagents"
description: "Explore, Plan, general-purpose and helper agents Claude Code uses automatically, with their models and tools, and how to disable them."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, explore, plan, built-in, disable]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.198"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "Explore"
  - "Plan"
  - "general-purpose"
  - "claude"
  - "statusline-setup"
  - "claude-code-guide"
  - "CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS"
  - "CLAUDE_AGENT_SDK_DISABLE_BUILTIN_AGENTS"
  - "Agent(Explore)"
  - "subagent_type"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Built-in subagents are registered by default in interactive sessions. Each inherits the parent's permission rules; most run with a restricted tool set. Explore and Plan start without your CLAUDE.md files and without the git status snapshot (other built-in and custom subagents load both unless `omitClaudeMd` is set).

# How to use it

| Agent | Model | Tools | Purpose |
| :- | :- | :- | :- |
| Explore | Parent's model; if parent is Fable: Opus (the `opus` alias) with a Claude subscription, Console account or LLM gateway via `ANTHROPIC_BASE_URL`; stays Fable on Bedrock, Google Agent Platform, Foundry, Claude Platform on AWS or a Claude apps gateway | Read-only (Write and Edit denied) | File discovery, code search. Claude passes a thoroughness level: quick, medium, very thorough |
| Plan | Inherits parent, unless `CLAUDE_CODE_SUBAGENT_MODEL` is forced onto all subagents | Read-only | Research during plan mode, keeping the main thread read-only |
| general-purpose | Parent's model by default (follows the model order) | Every tool available to subagents | Complex multi-step work needing exploration and action |
| claude | None of its own (follows model order) | Every tool available to subagents | Catch-all; also the default agent of a dispatched background session |
| statusline-setup | Sonnet | | Runs on `/statusline` |
| claude-code-guide | Haiku | | Answers questions about Claude Code features |

A user or project subagent named `Explore` overrides the built-in and keeps its own `model` (for example `model: haiku`).

Restricting built-ins:
- Block one type: `permissions.deny` entry such as `Agent(Explore)`.
- Block all delegation: deny the `Agent` tool.
- Remove only Explore and Plan: `CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS=1` (v2.1.198 or later).
- Non-interactive mode and the Agent SDK: `CLAUDE_AGENT_SDK_DISABLE_BUILTIN_AGENTS=1` removes all built-in types so only your own exist.

# Limits and defaults

- An Agent tool call without `subagent_type` fails with `subagent_type is required` when the session has no `general-purpose` subagent to fall back on.
- Explore and Plan are one-shot: no agent ID is returned, so they cannot be resumed.
