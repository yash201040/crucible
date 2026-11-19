---
type: "Feature"
title: "Permission relay for channels"
description: "A two-way channel can receive tool-approval prompts, sanitized and credential-masked, and return allow or deny verdicts by request ID."
resource: "https://code.claude.com/docs/en/channels-reference"
tags: [channels, permissions, relay, remote-approval]
kind: "api"
maturity: "research-preview"
since: "2.1.234"
surfaces: [cli]
requires: "Channel registered via --channels or the development flag; server declares claude/channel/permission"
identifiers:
  - "notifications/claude/channel/permission_request"
  - "notifications/claude/channel/permission"
  - "claude/channel/permission"
  - "request_id"
  - "tool_name"
  - "description"
  - "input_preview"
  - "behavior"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "channels-reference"
    resource: "https://code.claude.com/docs/en/channels-reference"
    title: "Channels reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When Claude calls a tool needing approval, the local dialog opens and a permission-relay channel receives the same prompt in parallel. Whichever answer arrives first is applied and the other is closed. Relay covers tool-use approvals such as `Bash`, `Write`, `Edit`; project trust and MCP server consent dialogs do not relay. From v2.1.234, permission requests go only to servers registered as channels for the session (behind the same session opt-in and org controls as message delivery) and the server must declare the capability.

# How to use it

Flow: Claude Code makes a short request ID and sends `notifications/claude/channel/permission_request`; the server forwards prompt and ID to the chat app; the user replies yes or no with the ID; the inbound handler emits `notifications/claude/channel/permission` with `request_id` (echoed) and `behavior` of `'allow'` or `'deny'`. Claude Code applies it only if the ID matches an open request. A verdict affects only that call.

| Field | Meaning |
| :- | :- |
| `request_id` | Five lowercase letters a-z without `l`; not shown in the local dialog, so only the outbound handler can learn it |
| `tool_name` | e.g. `Bash`, `Write` |
| `description` | Human-readable summary, never the command itself; for Bash without a model description it is the constant `Run shell command` |
| `input_preview` | Tool arguments as JSON-shaped text (Bash: the command; Write: path and content) |

Adding relay: declare `claude/channel/permission: {}` under `experimental`; register a notification handler (zod schema with `z.literal('notifications/claude/channel/permission_request')`) that formats the prompt; in the inbound handler (after sender gating) match `/^\s*(y|yes|n|no)\s+([a-km-z]{5})\s*$/i`, lowercase the ID, and emit the verdict instead of forwarding as chat. Declare the capability only if the channel authenticates the sender.

# Limits and defaults

- From v2.1.211, `description` and `input_preview` are sanitized: direction-override, invisible and quote or angle-bracket lookalike characters neutralized; whitespace runs folded to one space; text relayed whole up to 3,500 code points, otherwise start and end around `⋯ N code points elided ⋯`. For `input_preview` the limit applies per top-level field. Earlier clients relay `description` raw and cut `input_preview` to 200 UTF-16 units with an ellipsis.
- From v2.1.234, unserializable values appear as `(value unserializable)` and recognizable provider credentials as `[REDACTED]`; key names in `input_preview` can be masked too; spans with shell syntax, path or URL characters are never masked; secrets without a recognizable prefix or spanning whitespace (private-key blocks) arrive unmasked. Treat both fields as untrusted.
- Auto mode: the classifier decides instead of a dialog, so no relay occurs; the example uses manual mode (`Shift+Tab` until `⏸ manual mode on`).

# Notes

A remote reply with no effect while the local dialog stays open means: wrong format (e.g. `yes` without ID falls through as chat), unknown ID (dropped silently), or an ID repeated by an earlier prompt (once an ID repeats, channel verdicts carrying it are dropped; answer at the terminal). Full assembled example serves `GET /events` (SSE) and `POST /` gated by an `X-Sender` header allowlist.
