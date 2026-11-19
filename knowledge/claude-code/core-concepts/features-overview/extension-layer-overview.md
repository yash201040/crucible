---
type: "Concept"
title: "The extension layer"
description: "Overview of the features that extend Claude Code: CLAUDE.md, output styles, skills, MCP, subagents, workflows, hooks, plugins."
resource: "https://code.claude.com/docs/en/features-overview"
tags: [extensions, overview, skills, hooks, plugins]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers: []
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "features-overview"
    resource: "https://code.claude.com/docs/en/features-overview"
    title: "Extend Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Built-in tools (file operations, search, execution, web) cover most coding tasks. The extension layer is what you add to change what Claude knows, connect it to services and automate work. Each extension plugs into a different part of the agentic loop.

# How to use it

| Feature | What it does | Use when |
| - | - | - |
| CLAUDE.md | Persistent context loaded every session | Project conventions, "always do X" rules |
| Output style | Sets role, tone and response format for a whole session | A voice or format wanted in every response |
| Skill | Markdown file of knowledge or workflows; invoked as `/name` or loaded automatically | Reusable content, repeatable tasks |
| Subagent | Isolated context that returns a summary | Context isolation, parallel tasks, specialized workers |
| Dynamic workflow | Script Claude writes that runs many subagents in the background and returns one result | Work that outgrows a handful of subagents, or findings to cross-check |
| Cross-session messaging | Claude delivers a message from one of your sessions to another | Sessions you run yourself that need each other's findings mid-task |
| Code intelligence | Language-server navigation and diagnostics (LSP) | Typed languages, large codebases |
| MCP | Connects external services and tools | External data or actions |
| Hook | Script, HTTP request, MCP tool call, prompt or subagent run on a lifecycle event | Automation on every matching event |
| Artifact | Publishes session output as a private, interactive web page | Output to see or share visually |
| Plugin / marketplace | Packages skills, hooks, subagents and MCP servers into one installable unit | Reuse across repositories or distribute to others |

Plugin skills are namespaced (for example `/my-plugin:review`) so several plugins can coexist.

# Notes

Skills are described as the most flexible extension. They can run in the current conversation or in an isolated context via subagents. For other ways to run several Claude instances at once, the page points to the "Run agents in parallel" page.
