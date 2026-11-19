---
type: "Concept"
title: "What subagents inherit and output scanning"
description: "A non-fork subagent starts with a fresh context; only the Agent tool prompt passes down, and its final report is scanned for instruction-shaped patterns."
resource: "https://code.claude.com/docs/en/agent-sdk/subagents"
tags: [subagents, context, inheritance, security]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.210"
surfaces: [sdk]
requires: ""
identifiers:
  - "settingSources"
  - "omitClaudeMd"
  - "SendMessage"
  - "[harness: ...]"
  - "<system-reminder>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-subagents"
    resource: "https://code.claude.com/docs/en/agent-sdk/subagents"
    title: "Subagents in the SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Unless it is a fork, a subagent's context starts fresh with no parent conversation. The only content passed parent to subagent is the Agent tool's prompt string, so put file paths, error messages and decisions in it.

# How to use it

| Receives | Does not receive |
| --- | --- |
| Its own system prompt (`AgentDefinition.prompt`) and the Agent tool prompt | Parent conversation history or tool results |
| Project CLAUDE.md (via `settingSources`), unless `omitClaudeMd` | Preloaded skill content, unless in `AgentDefinition.skills` |
| Tool definitions (parent's or the `tools` subset, filtered for background runs) | The parent's system prompt |

Also: it inherits the main session's extended thinking configuration; a subagent with the `SendMessage` tool starts with a list of other named agents running in the session.

# Limits and defaults

From v2.1.210, Claude Code scans a subagent's final message before the parent reads it:
- Control-tag imitation (a harness-only tag such as `<system-reminder>`): neutralized in place with a backslash after the opening bracket.
- Permission-configuration mentions (`.claude/settings.json`, `bypassPermissions`, `--dangerously-skip-permissions`): kept as written.
- Turn markers (a line starting `Human:` or `Assistant:`): backslash inserted before the colon.
Control-tag or permission matches get a `[harness: ...]` marker line prepended; a turn-marker match does not. Text is never removed or reworded.

# Notes

The parent gets the final report but may summarize it; to preserve it verbatim, say so in the prompt or `systemPrompt`. An API error that ends a subagent early (e.g. rate limit) is never delivered as its result.
