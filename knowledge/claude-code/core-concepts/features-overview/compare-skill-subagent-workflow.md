---
type: "Concept"
title: "Skill vs subagent vs dynamic workflow"
description: "How skills, subagents and dynamic workflows differ in context, who decides what runs next, and how they combine."
resource: "https://code.claude.com/docs/en/features-overview"
tags: [skills, subagents, workflows, comparison, context]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "skills:"
  - "context: fork"
  - "omitClaudeMd"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "features-overview"
    resource: "https://code.claude.com/docs/en/features-overview"
    title: "Extend Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Skills are reusable content loaded into any context. Subagents are isolated workers with their own context window (own input and output tokens); only a summary returns. Dynamic workflows are scripts Claude writes that run many subagents in the background and return one result.

# How to use it

| Aspect | Skill | Subagent | Dynamic workflow |
| - | - | - | - |
| Who decides what runs next | Claude interprets instructions | Claude, turn by turn | The script |
| Context impact | Adds to main window | Separate window | Runs outside main conversation |
| Output | Content in context | Summary to the spawning conversation | One result |
| Best for | Reference material, invocable workflows | Reading many files, parallel work, specialized workers | Codebase-wide audit, large migration, plan drafted from several angles, cross-checked findings |

Combining: a subagent can preload skills with the `skills:` field; a skill can run in isolated context with `context: fork`. Subagents that Claude named when spawning can message each other. To start a workflow, ask for one in the prompt. To pass a finding between your own sessions, Claude uses cross-session messaging.

# Notes

Skills can be reference (knowledge used throughout) or action (do something specific, like `/deploy`). Use a subagent when the context window is filling or intermediate work need not stay visible. An agent whose definition sets `omitClaudeMd` starts without user, project and local CLAUDE.md files.
