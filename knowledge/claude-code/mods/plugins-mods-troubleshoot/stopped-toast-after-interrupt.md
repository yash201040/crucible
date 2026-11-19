---
type: "Concept"
title: "Stopped toast after an interrupted turn"
description: "The 'stopped · type a message to continue' toast means a mod tried to start work on its own after the user stopped a turn."
resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
tags: [mods, interrupt, toast, background-work]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "stopped · type a message to continue"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-troubleshoot"
    resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
    title: "Troubleshoot a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

After you stop a turn (e.g. with Esc), a mod tried to start work on its own and Claude Code did not allow it. Nothing needs fixing.

# How to use it

After your next message mods can start work again, and some of that work comes back on its own. If what you expected does not return, ask again or rerun the mod's command. Authors should read the mods API section on calls and background work after the user interrupts a turn.
