---
type: "Feature"
title: "ElicitationResult hook event"
description: "Runs after the user answers an MCP elicitation; can pass, rewrite, decline or cancel the response."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, mcp, elicitation, redaction]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "ElicitationResult"
  - "mcp_server_name"
  - "action"
  - "content"
  - "mode"
  - "elicitation_id"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs after a user responds to an MCP elicitation, to observe, modify or block the response before it reaches the server. Matcher is the MCP server name. It does not run when an [Elicitation](./p2-elicitation-event.md) hook already answered the request. Input adds `mcp_server_name`, `action`, and optional `mode`, `elicitation_id`, `content`.

# How to use it

| To | Return | Server receives |
| :- | :- | :- |
| Let through | No output, exit 0 | The user's response unchanged |
| Change values | `"action": "accept"` with new `content` | `accept` with your `content` |
| Block | `"action": "decline"` | `decline`, without the user's values |
| Cancel | `"action": "cancel"` | `cancel`, along with the submitted values (return `decline` to withhold them) |

Exit code 2 and a top-level `"decision": "block"` also block (see the other-ways-to-decline notes under [Elicitation](./p2-elicitation-event.md)).

# Limits and defaults

- Your `content` replaces the user's whole `content` object, so include unchanged fields. A `hookSpecificOutput` without `action` is ignored.
- The hook also runs when the user declines or cancels, and your `action` replaces theirs: check the input `action` is `accept` before returning `accept`, or you turn a declined request into an accepted one.
- `reason`, `systemMessage` and `continue` are discarded.
