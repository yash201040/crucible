---
type: "Concept"
title: "Hook vs skill and MCP vs skill"
description: "Hooks are deterministic lifecycle automation; skills are instructions Claude interprets; MCP supplies tools while skills supply knowledge."
resource: "https://code.claude.com/docs/en/features-overview"
tags: [hooks, skills, mcp, guardrails, comparison]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "PreToolUse"
  - "PostToolUse"
  - "SessionStart"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "features-overview"
    resource: "https://code.claude.com/docs/en/features-overview"
    title: "Extend Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A hook runs at a lifecycle event; a skill is loaded into context for Claude to apply. MCP connects Claude to external services; skills teach Claude how to use them well.

# How to use it

| Aspect | Hook | Skill |
| - | - | - |
| Runs | Shell command, HTTP request, MCP tool call, LLM prompt, or subagent | Instructions Claude reads |
| Triggered by | Lifecycle events such as `PostToolUse` or `SessionStart` | `/<name>`, or Claude matching the description |
| Determinism | Fires without Claude deciding | Outcome can vary |
| Context cost | Zero unless the hook returns output | Description each session; full content when used |

- Guardrails belong in hooks: "never edit `.env`" in CLAUDE.md or a skill is a request; a `PreToolUse` hook that blocks the edit is enforcement.
- Pair them: a `PostToolUse` hook runs the linter and sends errors to Claude; a skill such as `/fix-lint` gives fixing rules.
- MCP provides tools and data access (Slack, database queries, browser control); a skill carries schema, query patterns or a `/post-to-slack` workflow. They work together.

# Notes

Combination patterns listed: Skill + MCP, Skill + Subagent (an `/audit` skill kicks off security, performance and style subagents in isolated context), CLAUDE.md + Skills, Hook + MCP (post-edit hook sends a Slack notification).
