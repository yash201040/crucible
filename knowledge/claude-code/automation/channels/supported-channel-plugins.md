---
type: "Reference"
title: "Telegram, Discord and iMessage plugins"
description: "Setup steps, config files, env vars and access commands for the three supported channel plugins (all need Bun)."
resource: "https://code.claude.com/docs/en/channels"
tags: [channels, telegram, discord, imessage]
kind: "mixed"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: "Bun; iMessage needs macOS"
identifiers:
  - "plugin:telegram@claude-plugins-official"
  - "plugin:discord@claude-plugins-official"
  - "plugin:imessage@claude-plugins-official"
  - "/plugin install telegram@claude-plugins-official"
  - "/plugin install discord@claude-plugins-official"
  - "/plugin install imessage@claude-plugins-official"
  - "/telegram:configure"
  - "/telegram:access"
  - "/discord:configure"
  - "/discord:access"
  - "/imessage:access"
  - "TELEGRAM_BOT_TOKEN"
  - "DISCORD_BOT_TOKEN"
  - "~/.claude/channels/telegram/.env"
  - "~/.claude/channels/discord/.env"
  - "/plugin marketplace add anthropics/claude-plugins-official"
  - "/plugin marketplace update claude-plugins-official"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "channels"
    resource: "https://code.claude.com/docs/en/channels"
    title: "Push events into a running session with channels"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each supported channel is a plugin from the `claude-plugins-official` marketplace that requires Bun.

# How to use it

| Channel | Steps | Config / access |
| --- | --- | --- |
| Telegram | Create bot with BotFather `/newbot`; `/plugin install telegram@claude-plugins-official`; `/telegram:configure <token>`; restart with `claude --channels plugin:telegram@claude-plugins-official`; message the bot for a pairing code | Token saved to `~/.claude/channels/telegram/.env` or set `TELEGRAM_BOT_TOKEN`; `/telegram:access pair <code>` then `/telegram:access policy allowlist` |
| Discord | Developer Portal: New Application, Bot, Reset Token; enable Message Content Intent (Privileged Gateway Intents); OAuth2 URL Generator with `bot` scope and permissions View Channels, Send Messages, Send Messages in Threads, Create Public Threads, Read Message History, Attach Files, Add Reactions; install plugin; `/discord:configure <token>`; restart with `--channels plugin:discord@claude-plugins-official`; DM bot for code | Token to `~/.claude/channels/discord/.env` or `DISCORD_BOT_TOKEN`; `/discord:access pair <code>`, `/discord:access policy allowlist` |
| iMessage | macOS only, no token: reads `~/Library/Messages/chat.db`, replies via AppleScript. Grant Full Disk Access to the terminal (else server exits with `authorization denied`); install plugin; restart with `--channels plugin:imessage@claude-plugins-official` | Texting yourself bypasses access control; first reply triggers a macOS Automation prompt; allow others with `/imessage:access allow +15551234567` (phone `+country` format or Apple ID email) |

# Notes

- If the bot does not respond, Claude Code must be running with `--channels`.
- Install failures: `Marketplace "claude-plugins-official" not found` means add it with `/plugin marketplace add anthropics/claude-plugins-official`; `Plugin "<name>" not found in marketplace "claude-plugins-official"` means refresh with `/plugin marketplace update claude-plugins-official`.
- Choose user scope at install so the plugin works across projects. If the summary says `Run /reload-plugins to apply.`, reload, or just restart.
