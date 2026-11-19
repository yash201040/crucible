---
type: "Reference"
title: "Channel notification format and delivery"
description: "notifications/claude/channel params (content, meta), the resulting channel tag, and how events are queued without acknowledgement."
resource: "https://code.claude.com/docs/en/channels-reference"
tags: [channels, notification, meta, delivery]
kind: "api"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "notifications/claude/channel"
  - "content"
  - "meta"
  - "<channel>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "channels-reference"
    resource: "https://code.claude.com/docs/en/channels-reference"
    title: "Channels reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The server calls `mcp.notification()` with method `notifications/claude/channel`. The event reaches Claude wrapped in a `<channel>` tag whose `source` attribute is set automatically from the server's configured name.

# How to use it

| Param | Type | Description |
| :- | :- | :- |
| `content` | string | Event body, becomes the tag body |
| `meta` | `Record<string, string>` | Optional; each entry becomes a tag attribute (chat ID, sender, severity). Keys must be letters, digits and underscores; keys with hyphens or other characters are silently dropped |

Example: `meta: { severity: 'high', run_id: '1234' }` gives `<channel source="your-channel" severity="high" run_id="1234">body</channel>`.

# Limits and defaults

- No acknowledgement: the `await` resolves when the message is written to the transport, not when Claude has processed it. If the session did not load the server as a channel, or org policy blocks it, events are dropped silently with no error to the server.
- For delivery confirmation, track state in the server and expose a reply tool for Claude to report status.
- Events queue in order; notifications arriving while Claude is busy are delivered together on the next turn and handled as a group. To process independent streams concurrently, run separate sessions.
