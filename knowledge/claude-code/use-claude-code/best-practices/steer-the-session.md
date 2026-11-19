---
type: "Guide"
title: "Steering and rewinding a session"
description: "Esc, /rewind, /clear, /btw, /rename and resume by name, plus the checkpoint limit for Bash-only changes."
resource: "https://code.claude.com/docs/en/best-practices"
tags: [steering, rewind, checkpoints, clear, resume]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Esc"
  - "/rewind"
  - "/clear"
  - "/btw"
  - "/rename"
  - "claude --resume"
  - "claude --continue"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "best-practices"
    resource: "https://code.claude.com/docs/en/best-practices"
    title: "Best practices for Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Watch the first minute, press `Esc` when Claude drifts, and after two failed corrections run `/clear` and write a better prompt instead of a third.

# How to use it

- `Esc` stops mid-action keeping everything so far.
- `/rewind` or `Esc` twice on an empty prompt opens the rewind menu to roll back code, conversation or both; it can also summarize stale parts.
- `/clear` starts over.
- `/btw` answers a quick question without adding to history.
- `/rename oauth-migration` names a session so `claude --resume oauth-migration` resumes it later with checkpoints; `claude --continue` resumes the most recent.

# Limits and defaults

Checkpoints cover files edited with Claude's own file tools in the main conversation; a file touched only by a Bash command is not restored. They work alongside git, not as a replacement.
