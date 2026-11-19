---
type: "Guide"
title: "Example subagent definitions"
description: "Four sample subagents: code-reviewer, debugger, data-scientist and a db-reader with a read-only SQL hook."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, examples, hooks, tools]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "code-reviewer"
  - "debugger"
  - "data-scientist"
  - "db-reader"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Sample files on the page:

| Name | Tools | Model | Point |
| :- | :- | :- | :- |
| `code-reviewer` | Read, Grep, Glob, Bash | `inherit` | Read-only reviewer, output by priority |
| `debugger` | Read, Edit, Bash, Grep, Glob | default | Analyzes and fixes |
| `data-scientist` | Bash, Read, Write | `sonnet` | Non-coding domain (SQL, BigQuery) |
| `db-reader` | Bash | default | `PreToolUse` hook script blocks INSERT, UPDATE, DELETE, DROP, CREATE, ALTER, TRUNCATE, REPLACE, MERGE with exit code 2 |

# Notes

Best practices listed: design focused subagents, write descriptions that single out one subagent (within the 15,000-token budget), limit tool access, check project subagents into version control. The system prompt tells db-reader to refuse writes; the hook is the backstop.
