---
type: "Guide"
title: "Fakechat quickstart"
description: "Try channels with the officially supported localhost demo channel before connecting a real platform."
resource: "https://code.claude.com/docs/en/channels"
tags: [channels, fakechat, quickstart]
kind: "behavior"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: "Bun; claude.ai account or Console API key; admin enablement on Team/Enterprise"
identifiers:
  - "/plugin install fakechat@claude-plugins-official"
  - "plugin:fakechat@claude-plugins-official"
  - "http://localhost:8787"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "channels"
    resource: "https://code.claude.com/docs/en/channels"
    title: "Push events into a running session with channels"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Fakechat runs a chat UI on localhost with nothing to authenticate. A message typed in the browser arrives in your session; Claude replies and the reply shows in the browser.

# How to use it

1. `/plugin install fakechat@claude-plugins-official` (user scope).
2. Exit and restart: `claude --channels plugin:fakechat@claude-plugins-official`. The startup screen shows a channels notice that messages from that plugin inject directly into the session; a warning line appears if the plugin is not installed or not on the approved allowlist.
3. Open `http://localhost:8787` and type a message.

The terminal shows an inbound line like `← fakechat · web: what's in my working directory?`; the model receives a `<channel source="plugin:fakechat:fakechat">` event (plugin's scoped server name). Claude calls fakechat's `reply` tool; approve the first reply permission prompt if asked.

# Notes

Check Bun with `bun --version`. For unattended use, permission relay or `--dangerously-skip-permissions` are the options (see [overview](./channels-overview.md)).
