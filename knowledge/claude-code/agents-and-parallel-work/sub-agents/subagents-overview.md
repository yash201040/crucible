---
type: "Concept"
title: "Subagents overview"
description: "Subagents run in their own context window with their own prompt, tools and permissions, and return only a summary to the parent."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, context, delegation, overview]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers: []
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A subagent is a specialized assistant with its own context window, custom system prompt, specific tool access and independent permissions. It does a side task (searches, logs, file reads) and returns only a summary, keeping the main conversation small. Its requests count toward the same usage limits as the main conversation. Claude delegates automatically when a task matches the subagent's `description`.

# How to use it

Benefits the page lists: preserve context, enforce tool constraints, reuse configs across projects (user-level), specialize with focused prompts, control cost by routing to lower-cost models such as Haiku.

Related primitives the page points to:
- Many independent sessions monitored together: background agents (agent view).
- Sessions that message each other: cross-session messaging.
- A coordinated team Claude spawns and supervises: agent teams.
- Subagents work within a single session.

# Limits and defaults

- Combined `description` fields of non-built-in subagents above 15,000 tokens trigger a startup warning with the total token count; every subagent still loads. Trim descriptions, move detail into the system prompt (loaded only when the subagent runs).
