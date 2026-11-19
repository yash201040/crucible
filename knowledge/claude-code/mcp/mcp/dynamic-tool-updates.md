---
type: "Feature"
title: "Dynamic tool updates and list_changed"
description: "How list_changed notifications refresh tools, prompts and resources, and the v2 notification stream reopen limits."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, list-changed, refresh, headless]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "list_changed"
  - "-p"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A connected server may change its tools, prompts or resources and send `list_changed`.

# How to use it

- Interactive terminal: the updated list is fetched from that server without reconnecting.
- Non-interactive `-p` and the Agent SDK: only the tool list is refreshed on these notifications.
- If a refresh fails, the previously discovered tools, prompts and resources are kept until a later refresh succeeds.

# Limits and defaults

On the v2 runtime the notification stream is reopened when it closes: if it closes again within 10 seconds, up to three reopens, then it stops for that connection; if it stayed open longer than 10 seconds then closed, after five reopens in an hour Claude Code waits about six hours before the next. Until reopened you keep the last fetched lists; reconnect from `/mcp` to refresh sooner.
