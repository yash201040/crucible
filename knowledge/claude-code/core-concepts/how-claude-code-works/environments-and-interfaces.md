---
type: "Reference"
title: "Execution environments and interfaces"
description: "Local, cloud and Remote Control execution environments and the interfaces that reach the same agentic loop."
resource: "https://code.claude.com/docs/en/how-claude-code-works"
tags: [environments, cloud, remote-control, interfaces]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, web, ide, cloud]
requires: ""
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

The loop, tools and capabilities are the same everywhere; what changes is where code executes and how you interact.

# How to use it

| Environment | Where code runs | Use case |
| - | - | - |
| Local | Your machine | Default; full access to files, tools, environment |
| Cloud | Anthropic-managed VMs, or self-hosted environments your organization operates | Offload tasks, work on repos not held locally |
| Remote Control | Your machine, controlled from a browser | Web UI while execution and files stay local |

Interfaces: terminal, desktop app, IDE extensions, claude.ai/code, Remote Control, Slack, and CI/CD pipelines (GitHub Actions).
