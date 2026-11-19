---
type: "Concept"
title: "What an enabled plugin adds to every session"
description: "Context tokens, processes and permissions an enabled plugin brings, and how to check or stop its footprint."
resource: "https://code.claude.com/docs/en/plugins/overview"
tags: [plugins, context, cost, mcp, permissions]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin disable"
  - "/plugin"
  - "Context cost"
  - "Not used recently"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-overview"
    resource: "https://code.claude.com/docs/en/plugins/overview"
    title: "Plugins overview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An enabled plugin is part of every session, not only those that use it.

- Context and usage: for each skill, agent and command Claude can invoke on its own, the name and description sit in context every turn and count toward usage even if nothing runs. Full text of a skill or agent loads only when used. MCP servers' per-turn cost follows MCP tool search.
- Processes: its MCP servers run alongside each session where it is enabled; its hooks fire at their events.
- Permissions: what the plugin runs, it runs as you.

# How to use it

- Before install: open the plugin from the **Marketplaces** tab in `/plugin`; plugins in Anthropic's official marketplace show a **Context cost** estimate.
- After install: the Measure plugin cost page shows how to read the footprint; the **Installed** tab's **Not used recently** group lists plugins you could turn off.
- Stop without uninstalling: disable via `/plugin` or `claude plugin disable`.
