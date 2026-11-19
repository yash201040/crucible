---
type: "Reference"
title: "Claude Code capabilities available in the Agent SDK"
description: "Built-in tools, hooks, subagents, MCP, permissions, sessions, skills/commands/memory and plugins in the SDK."
resource: "https://code.claude.com/docs/en/agent-sdk/overview"
tags: [sdk, capabilities, subagents, hooks, sessions]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - ".claude/"
  - "~/.claude/"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-overview"
    resource: "https://code.claude.com/docs/en/agent-sdk/overview"
    title: "Agent SDK overview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The Claude Code capabilities exposed in the SDK.

# How to use it

| Capability | What it does |
| - | - |
| Built-in tools | Read, write, edit files, run commands, search the web |
| Hooks | Run custom code at key points in the agent lifecycle |
| Subagents | Spawn specialized agents for focused subtasks |
| MCP | Connect external tools and data sources via the Model Context Protocol |
| Permissions | Control which tools run automatically and which need approval |
| Sessions | Maintain context across exchanges; resume or fork later |
| Skills, commands, memory | Load automatically from the project's `.claude/` and `~/.claude/`, same as Claude Code |
| Plugins | Package skills, agents, hooks and MCP servers; load them by local path |

# Notes

Each capability has its own Agent SDK page (hooks, subagents, mcp, permissions, sessions, skills, plugins, claude-code-features, modifying-system-prompts). Release notes live in the CHANGELOG.md of the `claude-agent-sdk-typescript` and `claude-agent-sdk-python` GitHub repositories, where bugs are also reported.
