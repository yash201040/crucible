---
type: "Concept"
title: "Agent SDK compared with CLI, Client SDK and Managed Agents"
description: "Which Claude tool to use: Agent SDK library, CLI, Client SDK or hosted Managed Agents."
resource: "https://code.claude.com/docs/en/agent-sdk/overview"
tags: [sdk, comparison, managed-agents, headless]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk, cli, headless]
requires: ""
identifiers:
  - "-p"
  - "--output-format json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-overview"
    resource: "https://code.claude.com/docs/en/agent-sdk/overview"
    title: "Agent SDK overview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The Agent SDK gives the same tools, agent loop and context management that power Claude Code, programmable in Python and TypeScript. An agent plans its own steps and calls tools that read files, run commands or edit code.

# How to use it

| You want to | Use | What you get |
| - | - | - |
| Embed Claude Code's agent in your own Python or TypeScript app, in a process you operate | Agent SDK | A library that runs the Claude Code binary, with built-in tools, permissions, sessions, hooks |
| Interactive development or one-off tasks from a terminal | Claude Code CLI | Terminal interface for daily use |
| Call the Claude API directly | Client SDK | Direct API access in any client SDK language; you write the tool loop or use the client SDK's beta tool runner |
| Have Anthropic host the agent via the Claude API | Managed Agents | Hosted harness running the agent loop, with sessions in an Anthropic-managed cloud sandbox or a self-hosted sandbox on your infrastructure; use via the language SDK, the `ant` CLI or REST |

To drive the same agent loop from another language, run the CLI as a subprocess with the `-p` flag and `--output-format json` (the headless page).

# Notes

A related blog post on agent harness design describes how the Claude Code team uses dynamic workflows to orchestrate many subagents at once.
