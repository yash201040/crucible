---
type: "Guide"
title: "Choosing an extension feature in the SDK"
description: "Maps goals to CLAUDE.md, skills, subagents, agent teams, hooks and MCP with the SDK surface for each."
resource: "https://code.claude.com/docs/en/agent-sdk/claude-code-features"
tags: [subagents, agent-teams, mcp, hooks]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [sdk, cli]
requires: ""
identifiers:
  - "agents"
  - "allowedTools: [\"Agent\"]"
  - "mcpServers"
  - "hooks"
  - "skills"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-claude-code-features"
    resource: "https://code.claude.com/docs/en/agent-sdk/claude-code-features"
    title: "Use Claude Code features in the SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Goal | Use | SDK surface |
| :- | :- | :- |
| Project conventions always followed | CLAUDE.md | `settingSources: ["project"]` |
| Reference material loaded when relevant | Skills | `settingSources` + `skills` |
| Reusable workflow (deploy, review, release) | User-invocable skills | `settingSources` + `skills` |
| Isolated subtask in a fresh context | Subagents | `agents` parameter + `allowedTools: ["Agent"]` |
| Multiple Claude Code instances with shared task lists and direct messaging | Agent teams | Not configured via SDK options; a CLI feature where one session is team lead |
| Deterministic logic on tool calls | Hooks | `hooks` callbacks, or shell scripts via `settingSources` |
| Structured tool access to an external service | MCP | `mcpServers` |

# Notes

Every enabled feature adds to the context window.
