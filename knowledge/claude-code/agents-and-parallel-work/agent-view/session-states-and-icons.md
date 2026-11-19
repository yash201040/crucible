---
type: "Reference"
title: "Agent view session states and icons"
description: "State icons, row shapes, notifications and persistence of background sessions across sleep and updates."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, states, notifications, persistence]
kind: "ui"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "preferredNotifChannel"
  - "Notification"
  - "agent_needs_input"
  - "agent_completed"
  - "~/.claude/jobs/"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each row begins with an icon whose colour and animation give the session state. Rows are grouped by state, with pinned sessions and those needing you at top; each shows name (tinted by `/color`), activity, and age (counted from creation; frozen at run duration when finished).

# How to use it

| State | Icon | Meaning |
| :- | :- | :- |
| Working | Animated | Running tools or generating |
| Needs input | Yellow | Waiting on something only you can give: an answer, a permission decision, a sandbox prompt, an MCP elicitation. Commands needing an attached terminal (`/install-github-app`, the `/mcp` list) also hold an unattended session here |
| Idle | Dimmed | Nothing to do, ready for next prompt |
| Completed | Green | Finished successfully |
| Failed | Red | Ended with an error |
| Stopped | Grey | Stopped with `Ctrl+X` or `claude stop`, process killed externally, or ended while the background service was off |

| Shape | Meaning |
| :- | :- |
| `✻` or animated `✽` | Process running, or session needs input |
| `∙` | Process exited; peek still works; a reply or `Enter` restarts it from the saved conversation |
| `✢` | A `/loop` session sleeping between iterations; row shows run count and countdown |

A `#N` or `!N` label at the right edge links to the pull or merge request. Terminal tab title shows `2 awaiting input · claude agents` when sessions need input. While agent view is open, a notification goes through the configured terminal channel (`preferredNotifChannel`) when a local background session needs input, finishes or fails, and the `Notification` hook fires with type `agent_needs_input` or `agent_completed`. Scheduled sessions such as `/loop` notify only when they need input.

# Limits and defaults

For scripts use `claude agents --json`, not the files under `~/.claude/jobs/`. State persists on disk through auto-updates and supervisor restarts and survives machine sleep (processes resume on wake). A session mid-response at sleep can come back unresponsive; opening it makes the supervisor restart the process and continue the response. Shutdown still stops running sessions.
