---
type: "Concept"
title: "Cache scope: machine and directory"
description: "The Claude Code cache is effectively scoped to one machine and directory; parallel same-directory sessions can share it."
resource: "https://code.claude.com/docs/en/prompt-caching"
tags: [prompt-caching, scope, parallel-sessions, sdk]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers: []
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "prompt-caching"
    resource: "https://code.claude.com/docs/en/prompt-caching"
    title: "How Claude Code uses prompt caching"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The system prompt embeds auto memory paths and the conversation opens with the working directory, platform, shell and OS version. Sessions in different directories build different prefixes and miss each other's cache.

# Limits and defaults

- Parallel sessions in the same directory build matching prefixes and can read each other's cache.
- Sequential sessions share a prefix only when the startup git status snapshot (branch and recent commits) matches.
- The underlying API cache: isolated between organizations, and on some providers between workspaces; two requests share only when model, speed and prefix match.

# Notes

For Agent SDK fleets, the Agent SDK page on modifying system prompts describes "improve prompt caching across users and machines" by moving the auto memory location out of the system prompt.
