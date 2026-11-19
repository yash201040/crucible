---
type: "Feature"
title: "Teammate plan mode and plan approval"
description: "Teammates spawned while the lead is in plan mode plan first and send a plan approval request; approval is automatic unless the mode was changed."
resource: "https://code.claude.com/docs/en/agent-teams"
tags: [agent-teams, plan-mode, approval, permissions]
kind: "behavior"
maturity: "experimental"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Shift+Tab"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-teams"
    resource: "https://code.claude.com/docs/en/agent-teams"
    title: "Orchestrate teams of Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

For complex or risky tasks, teammates can plan before implementing. A teammate Claude spawns while the lead is in plan mode also works in plan mode until its plan is ready.

# How to use it

Switch the lead into plan mode first, then ask, for example, "Spawn an architect teammate to refactor the authentication module." When the teammate finishes planning it sends a plan approval request to the lead. If you have not changed that teammate's permission mode since spawn, Claude Code approves the plan as soon as the request arrives, without lead review. Once approved the teammate leaves plan mode and implements; Claude Code gives it the lead's current permission mode, or Manual if that is plan mode.

# Limits and defaults

If you put a running in-process teammate in plan mode with `Shift+Tab` while viewing it, the lead reviews that run's plan instead; you are not asked to approve, the lead approves or sends it back for revision.
