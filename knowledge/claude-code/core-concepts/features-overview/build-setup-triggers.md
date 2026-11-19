---
type: "Guide"
title: "When to add each extension"
description: "Table of recognizable triggers that tell you which extension to add next, and when to update an existing one."
resource: "https://code.claude.com/docs/en/features-overview"
tags: [extensions, claude-md, skills, hooks, setup]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers: []
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "features-overview"
    resource: "https://code.claude.com/docs/en/features-overview"
    title: "Extend Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

You do not configure everything up front. Each feature has a recognizable trigger, and most teams add them in roughly this order.

# How to use it

| Trigger | Add |
| :- | :- |
| Claude gets a convention or command wrong twice | CLAUDE.md |
| You keep asking Claude to be shorter, explain more, or use one format | An output style |
| You keep typing the same prompt to start a task | A user-invocable skill |
| You paste the same playbook into chat for the third time | A skill |
| You keep copying data from a browser tab Claude cannot see | An MCP server |
| Claude reads many files to find where a symbol is defined or used | A code intelligence plugin |
| A side task floods the conversation with output you will not reference again | A subagent |
| You want something to happen every time without asking | A hook |
| A second repository needs the same setup | A plugin |

# Notes

The same triggers say when to update what you have: a repeated mistake or recurring review comment is a CLAUDE.md edit, not a one-off chat correction. A workflow you keep tweaking by hand is a skill needing another revision.
