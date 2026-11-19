---
type: "Guide"
title: "Project troubleshooting messages"
description: "Common project thread messages and fixes, including stuck threads, guessed assumptions and setup failures."
resource: "https://code.claude.com/docs/en/claude-projects"
tags: [projects, troubleshooting, errors, threads]
kind: "behavior"
maturity: "beta"
since: ""
surfaces: [web, desktop]
requires: ""
identifiers: []
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-projects"
    resource: "https://code.claude.com/docs/en/claude-projects"
    title: "Let Claude coordinate ongoing work with Projects"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Fixes for recurring project problems.

# How to use it

- Thread looks stuck: Claude does not post each step; open the thread; it may be provisioning or waiting on a permission prompt there.
- Threads guessed or stalled: ask Claude "For every open thread, list what you asked it to do, what it assumed or couldn't reach, and what it's waiting on"; mark wrong-assumption threads resolved or redirect them (branches and PRs stay on GitHub); fix the gap once in instructions or the environment; send one thread before the rest.
- Setup-time advice: write project instructions, send one small real piece of work first, check thread model and effort, and ask Claude to propose threads and run a few at a time.

| Message | Action |
| - | - |
| "Unable to connect to repository" (couldn't reach GitHub) | wait, ask for a new thread |
| "Unable to connect to repository" (couldn't access repository or environment) | check push access and that the environment exists |
| "Couldn't show the setup proposal" | refresh or restart the app, or ask Claude to propose again |
| "The project's environment was removed" | pick another environment; new threads only |
| "Setup script failed" | fix the script, then run the task in a new thread |
| "Claude ran out of context on this turn" | continues itself if it says fresh session; else start a new thread |
