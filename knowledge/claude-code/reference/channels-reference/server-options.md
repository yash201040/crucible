---
type: "Reference"
title: "Channel Server constructor options"
description: "MCP Server constructor fields that make a server a channel: claude/channel, claude/channel/permission, tools and instructions."
resource: "https://code.claude.com/docs/en/channels-reference"
tags: [channels, mcp, capabilities, instructions]
kind: "api"
maturity: "research-preview"
since: "2.1.234"
surfaces: [cli]
requires: ""
identifiers:
  - "capabilities.experimental['claude/channel']"
  - "capabilities.experimental['claude/channel/permission']"
  - "capabilities.tools"
  - "instructions"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "channels-reference"
    resource: "https://code.claude.com/docs/en/channels-reference"
    title: "Channels reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Fields set in the MCP `Server` constructor. `instructions` and `capabilities.tools` are standard MCP; the two `claude/channel*` keys are channel-specific.

# How to use it

| Field | Type | Description |
| :- | :- | :- |
| `capabilities.experimental['claude/channel']` | object | Required, always `{}`; presence registers the notification listener |
| `capabilities.experimental['claude/channel/permission']` | object or `false` | Optional; `{}` declares the channel can receive permission relay requests. Omit or `false` to opt out. Before v2.1.234, `false` was treated as declared |
| `capabilities.tools` | object | Two-way only, always `{}` (standard MCP tool capability) |
| `instructions` | string | Recommended; delivered to Claude as context at connect. Say what events to expect, what tag attributes mean, whether to reply, which tool, and which attribute (like `chat_id`) to pass back |

# Notes

For a one-way channel omit `capabilities.tools`.
