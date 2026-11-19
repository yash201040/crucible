---
type: "Feature"
title: "Channels"
description: "A channel is an MCP server that pushes events (chat, webhooks, CI) into a running session; two-way, research preview."
resource: "https://code.claude.com/docs/en/channels"
tags: [channels, mcp, push-events, research-preview]
kind: "mixed"
maturity: "research-preview"
since: ""
surfaces: [cli, headless]
requires: "Anthropic auth via claude.ai or Console API key; not on Bedrock, Google Cloud's Agent Platform or Microsoft Foundry; Team/Enterprise must enable"
identifiers:
  - "--channels"
  - "--dangerously-load-development-channels"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "channels"
    resource: "https://code.claude.com/docs/en/channels"
    title: "Push events into a running session with channels"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A channel is an MCP server that pushes events into your running Claude Code session so Claude can react while you are away. Channels can be two-way: Claude replies through the same channel (a chat bridge). Events arrive only while the session is open, so for always-on use run Claude in a background process or persistent terminal. Unlike integrations that spawn a fresh cloud session or wait to be polled, the event lands in the session you already have open.

You install a channel as a plugin and configure it with your own credentials. Telegram, Discord and iMessage are in the preview. When Claude replies, the terminal shows the inbound message and the tool call plus a confirmation like "sent", not the reply text.

# How to use it

Enable per session: `claude --channels plugin:<name>@<marketplace>` (several, space-separated). Being listed in `.mcp.json` is not enough: a server must also be named in `--channels`. See [supported channels](./supported-channel-plugins.md), [quickstart](./fakechat-quickstart.md), [security](./channel-security.md), [enterprise controls](./channel-enterprise-controls.md).

# Limits and defaults

- Non-interactive `-p`: tools needing terminal input (multiple-choice questions, plan mode approval) are disabled so the session never stalls.
- Permission prompts while away pause the session, unless the channel declares the permission relay capability. `--dangerously-skip-permissions` bypasses most prompts (trusted environments only); actions no mode auto-approves still apply.

# Notes

Comparison: cloud sessions (fresh sandbox, async work), Claude in Slack (spawns a cloud session from an `@Claude` mention), standard MCP server (Claude queries; nothing pushed), Remote Control (you drive a local session from claude.ai or mobile). Channels push non-Claude events into your already-running local session: chat bridge and webhook receiver. Related: session-scoped scheduled tasks poll on a timer instead.
