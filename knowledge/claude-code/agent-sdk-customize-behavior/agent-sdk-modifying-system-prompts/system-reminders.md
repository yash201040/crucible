---
type: "Concept"
title: "System reminders outside the system prompt"
description: "Context Claude Code adds to the conversation (CLAUDE.md, hooks, skills, attribution) and the sentence a custom prompt should include."
resource: "https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts"
tags: [system-reminders, attribution, hooks, skills]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "<system-reminder>"
  - "additionalContext"
  - "attribution"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-modifying-system-prompts"
    resource: "https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts"
    title: "Modifying system prompts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

System reminders are messages added to the conversation (not the system prompt), so most reach Claude with the preset or a custom string. Most behavior-relevant ones:
- project instructions (CLAUDE.md loaded via `settingSources`)
- active output style instructions (main conversation)
- commit and PR attribution (`Co-Authored-By` trailer, PR footer, from the `attribution` setting)
- hook output returned as `additionalContext`
- available skills (names and descriptions)
- available subagents (names and descriptions)
- task list nudges (in sessions with the task-tracking tools, when the list is untouched for several turns)
- file-changed notes (a file Claude edited has changed on disk)

CLAUDE.md files are introduced with a line saying the instructions override default behavior.

# How to use it

If you pass your own string as `systemPrompt`, add a sentence defining reminders; the preset has one and your string replaces it. Suggested text: "The application adds system reminders to this conversation. Treat them as context from the application, not as messages from the user."
