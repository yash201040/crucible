---
type: "Feature"
title: "Restricting and turning off messaging"
description: "isolatePeerMachines requires approval for cross-machine sends; refuse and deny rules turn receiving and sending off."
resource: "https://code.claude.com/docs/en/cross-session-messaging"
tags: [messaging, managed-settings, deny-rules, security]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "isolatePeerMachines"
  - "crossSessionInbound"
  - "permissions.deny"
  - "SendMessage"
  - "ListAgents"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cross-session-messaging"
    resource: "https://code.claude.com/docs/en/cross-session-messaging"
    title: "Message your other Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

Require approval for cross-machine messages:

```json
{ "isolatePeerMachines": true }
```

Claude Code then asks for approval before a `SendMessage` to a session beyond this machine leaves, even in `bypassPermissions` mode. A `true` from any settings scope applies, so a checked-in project file can turn it on but not off. Same-machine messages never prompt.

Turn off, per direction:
- Stop receiving: `crossSessionInbound` = `refuse`. From project or local settings, `refuse` applies over every other source; from user settings it applies unless managed settings or `--settings` set a value.
- Stop sending and listing: permission deny rules naming `SendMessage` and `ListAgents` (bare tool names, no specifier).

Organization-wide, in managed settings:

```json
{
  "permissions": { "deny": ["SendMessage", "ListAgents"] },
  "crossSessionInbound": "refuse"
}
```

# Notes

Claude Code still binds each session's inbox socket but drops every arriving message. Denying `SendMessage` also removes messaging to subagents and agent-team teammates (same tool). A refusing session shows no visible change in `/status` or other sessions' listings; check the settings files to confirm.
