---
type: "Reference"
title: "Built-in tool categories"
description: "The five categories of built-in tools and what Claude can do with each, plus tools for orchestration."
resource: "https://code.claude.com/docs/en/how-claude-code-works"
tags: [tools, file-operations, search, execution, web]
kind: "tool"
maturity: "unlabelled"
since: ""
surfaces: []
requires: "Code intelligence needs a code intelligence plugin"
identifiers: []
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "how-claude-code-works"
    resource: "https://code.claude.com/docs/en/how-claude-code-works"
    title: "How Claude Code works"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Tools let Claude act instead of only replying with text. Each result feeds back into the loop.

# How to use it

| Category | What Claude can do |
| - | - |
| File operations | Read files, edit code, create files, rename and reorganize |
| Search | Find files by pattern, search content with regex, explore codebases |
| Execution | Run shell commands, start servers, run tests, use git |
| Web | Search the web, fetch documentation, look up errors |
| Code intelligence | See type errors and warnings after edits, jump to definitions, find references (requires code intelligence plugins) |

# Notes

Claude also has tools for spawning subagents, asking you questions and other orchestration tasks; the complete list is on the Tools reference page. Extensions (skills, MCP, hooks, subagents) sit on top of the core loop.
