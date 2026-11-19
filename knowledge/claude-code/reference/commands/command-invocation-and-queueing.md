---
type: "Concept"
title: "How slash commands are invoked and queued"
description: "Commands work only at message start, can chain up to six skills, and queue behind a running turn except for a few that run immediately."
resource: "https://code.claude.com/docs/en/commands"
tags: [slash-commands, queueing, skills]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.234"
surfaces: [cli]
requires: ""
identifiers:
  - "/"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "commands"
    resource: "https://code.claude.com/docs/en/commands"
    title: "Commands"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Rules for how typed commands are recognized and when they run relative to a response in progress.

# How to use it

A command is recognized only at the start of the message; text after the name becomes its arguments. At the terminal prompt one message can start several skills: `/skill-a /skill-b do XYZ` loads both and passes the trailing text to each as arguments.

# Limits and defaults

- Up to six skills can be chained in one message.
- A command sent while Claude is responding is queued and runs after the current turn.
- Some commands run immediately without interrupting the response: `/status`, `/tasks`, `/usage`.
- In fullscreen rendering, dialog commands such as `/theme` and `/help` also open immediately; before v2.1.234 they queued until the turn ended.
- In the table of commands `<arg>` is required and `[arg]` is optional. Availability varies by platform, plan and environment (for example `/desktop` only on macOS and x64 Windows with a Claude subscription; `/upgrade` not shown on Enterprise plans).
- Commands are marked Skill (bundled skill, a prompt handed to Claude) or Workflow (bundled dynamic workflow that fans work out across many subagents in the background).
- MCP servers can expose prompts that appear as commands.
