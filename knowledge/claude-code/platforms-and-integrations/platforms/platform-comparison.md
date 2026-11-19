---
type: "Reference"
title: "Platforms and integrations overview"
description: "Where Claude Code runs (CLI, Desktop, VS Code, JetBrains, web, mobile), which integrations connect it, and ways to work away from the terminal."
resource: "https://code.claude.com/docs/en/platforms"
tags: [platforms, surfaces, integrations, remote, comparison]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide, web, mobile]
requires: "Varies by surface; Dispatch, Slack and computer use need Pro, Max or Ultra; Claude Tag and self-hosted environments need Team or Enterprise"
identifiers:
  - "claude remote-control"
  - "/remote-control"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "platforms"
    resource: "https://code.claude.com/docs/en/platforms"
    title: "Platforms and integrations"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code runs the same engine on every surface; surfaces differ in interface and what runs where. Configuration, project memory and MCP servers are shared across local surfaces.

| Platform | Best for |
| - | - |
| CLI | terminal, scripting, remote servers; full feature set, Agent SDK, computer use on macOS (Pro, Max, Ultra), third-party providers |
| Desktop | visual review, parallel sessions, managed setup; computer use and Dispatch on Pro, Max, Ultra |
| VS Code | working inside VS Code |
| JetBrains | IntelliJ, PyCharm, WebStorm and others |
| Web | long-running tasks, work that continues offline (cloud, Anthropic-managed by default) |
| Mobile | start and monitor tasks; cloud sessions, Remote Control, Dispatch |

Scripting and the Agent SDK are CLI-only. Third-party providers work in the CLI, VS Code and JetBrains; Desktop supports Google Cloud's Agent Platform for Enterprise and gateway providers, and Bedrock or Foundry via the CLI, IDE extensions or Claude Desktop on 3P.

# How to use it

Integrations: Chrome (your logged-in browser), GitHub Actions, GitLab CI/CD, Code Review (every PR), Slack (`@Claude`, own account, Pro, Max, Ultra), Claude Tag (shared org identity, Team and Enterprise), MCP servers and connectors.

Working away from the terminal:

| Option | Trigger | Runs on |
| - | - | - |
| Dispatch | message from mobile app | your machine (Desktop) |
| Remote Control | drive a session from claude.ai/code or mobile | your machine (CLI, Desktop, VS Code) |
| Channels | events from Telegram, Discord or your own server | your machine (CLI) |
| Slack | `@Claude` mention | Anthropic cloud |
| Self-hosted environments | cloud session on your org's environment | your organization's infrastructure (Team, Enterprise) |
| Scheduled tasks | a schedule | CLI, Desktop or cloud |

# Limits and defaults

Desktop and IDE extensions trade some CLI-only features for visual review and editor integration.
