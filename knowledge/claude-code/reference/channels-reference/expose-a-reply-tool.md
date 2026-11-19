---
type: "Guide"
title: "Expose a reply tool (two-way channels)"
description: "A two-way channel declares tools, registers a standard MCP reply tool and tells Claude via instructions how to route replies."
resource: "https://code.claude.com/docs/en/channels-reference"
tags: [channels, reply-tool, two-way, mcp-tools]
kind: "tool"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "reply"
  - "chat_id"
  - "ListToolsRequestSchema"
  - "CallToolRequestSchema"
  - "capabilities.tools"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "channels-reference"
    resource: "https://code.claude.com/docs/en/channels-reference"
    title: "Channels reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Nothing about the tool registration is channel-specific. A reply tool needs: `tools: {}` in `Server` capabilities, handlers defining the tool schema and send logic, and `instructions` telling Claude when and how to call it.

# How to use it

- Add `tools: {}` next to `experimental: { 'claude/channel': {} }`.
- Register handlers with `ListToolsRequestSchema` (tool `reply`, input `chat_id` and `text`, both required strings) and `CallToolRequestSchema` (send, return `{ content: [{ type: 'text', text: 'sent' }] }`).
- Instructions example: messages arrive as `<channel source="webhook" chat_id="...">`; reply with the reply tool passing the `chat_id` from the tag.
- In the walkthrough, outbound replies stream over `GET /events` (SSE) so `curl -N localhost:8788/events` can watch them; the SSE server sets `idleTimeout: 0`.

# Notes

The fakechat server shows a fuller example with attachments and message editing.
