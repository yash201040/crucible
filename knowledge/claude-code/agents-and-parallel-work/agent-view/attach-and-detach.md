---
type: "Feature"
title: "Attach to and detach from a session"
description: "Attach with Enter or claude attach for the full session; detach keys never stop the session."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, attach, detach, fullscreen]
kind: "ui"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude attach <id>"
  - "/exit"
  - "/stop"
  - "/mcp"
  - "/install-github-app"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Attaching replaces agent view with the full interactive session; on attach Claude posts a short recap of what happened. Attached sessions always render in fullscreen mode regardless of the `tui` setting. An attached session does not report status to your terminal.

# How to use it

| Key | Effect |
| :- | :- |
| `←` on empty prompt, or `/exit` | Detach to agent view (also for `claude attach <id>`; also while the `/btw` overlay is open, v2.1.257+) |
| `Ctrl+Z` | Detach to where you started (agent view or shell); use when a dialog ignores `←` |
| `Ctrl+C` | Interrupts a response or `!` command; twice on an empty prompt detaches |
| `/stop` | Ends the session from inside |

Detaching, double `Ctrl+C`/`Ctrl+D` never stop the session; a waiting `/loop` keeps running on schedule. On Windows, `←` within about half a second of attaching shows `Ambiguous ←, press again to detach`.

`/install-github-app` and the `/mcp` list work when a human is attached; unattended they put the session under `Needs input` (`open this session to manage MCP servers`) until you attach and re-run. `/mcp reconnect <server>`, `/mcp enable`, `/mcp disable` work either way.
