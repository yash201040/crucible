---
type: "Feature"
title: "Hold a tool call until the user decides ($.ui.ask)"
description: "A tool.call hook can await $.ui.ask to put a question dialog to the user while the tool call stays pending."
resource: "https://code.claude.com/docs/en/plugins/mods/events"
tags: [mods, ask, dialog, headless]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "$.ui.ask"
  - "Chat about this"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-events"
    resource: "https://code.claude.com/docs/en/plugins/mods/events"
    title: "React to events with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A `tool.call` hook can `await` before calling `next`; the call stays pending. `$.ui.ask(question, options)` shows the question over a numbered list of options in Claude's question dialog and resolves to the chosen label. The dialog adds a row for typing another answer and a **Chat about this** row.

# How to use it

`answer = await $.ui.ask('Run this command? ' + e.command, ['Run it', 'Refuse'])`. Start from a safe default (`let answer = 'Refuse'`) and wrap in try/catch.

Outcomes: pick "Run it" then call `next(e)` (permission check still runs); pick "Refuse" then return `{ deny }`; a typed answer resolves to the typed text; `$.ui.ask` rejects when the user dismisses it or picks **Chat about this**, and in a `claude -p` run (no one to ask), so the catch leaves the safe default.

# Limits and defaults

- Time waiting inside a mods API call such as `$.ui.ask` does not count against the hook's time limit; time awaiting your own promise does.
- A timed-out hook is skipped and the held command would run; chain a `.catch` on the registration to refuse instead.
