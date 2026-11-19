---
type: "Concept"
title: "MCP overview and finding servers"
description: "What MCP gives Claude Code, where to find reviewed servers, and how the mcp-server-dev plugin scaffolds one."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, overview, directory, plugin]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide, desktop]
requires: ""
identifiers:
  - "/plugin install mcp-server-dev@claude-plugins-official"
  - "/mcp-server-dev:build-mcp-server"
  - "/plugin marketplace add anthropics/claude-plugins-official"
  - "/plugin marketplace update claude-plugins-official"
  - "/reload-plugins --force"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The Model Context Protocol (MCP) is an open standard. MCP servers give Claude Code access to external tools, databases and APIs (issue trackers, monitoring, databases, designs, email). A server can also act as a [channel](./mcp-channels.md) that pushes events into a session.

# How to use it

- Browse reviewed connectors in the Anthropic Directory (claude.ai/directory). Any remote server listed there can be added with `claude mcp add`.
- To scaffold your own server, install the official `mcp-server-dev` plugin: `/plugin install mcp-server-dev@claude-plugins-official`, then run `/mcp-server-dev:build-mcp-server`. Claude asks about the use case and scaffolds a remote HTTP or local stdio server.
- If install fails with `Marketplace "claude-plugins-official" not found`, run `/plugin marketplace add anthropics/claude-plugins-official`. If it fails with `Plugin "<name>" not found in marketplace`, run `/plugin marketplace update claude-plugins-official`.
- If the install summary says `Run /reload-plugins to apply.`, Claude Code runs the reload itself; if it warns the next message would re-read the conversation, use `/reload-plugins --force`.

# Notes

- The docs warn to trust each server before connecting: servers that fetch external content can expose you to prompt injection.
- In the VS Code extension and desktop app, follow the plugin install flow of that surface instead of the terminal command.
