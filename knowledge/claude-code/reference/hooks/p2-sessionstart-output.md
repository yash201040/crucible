---
type: "Reference"
title: "SessionStart output fields and skill reload"
description: "Fields a SessionStart hook can return: additionalContext, initialUserMessage, sessionTitle, watchPaths, reloadSkills."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, sessionstart, output, skills]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "additionalContext"
  - "initialUserMessage"
  - "sessionTitle"
  - "watchPaths"
  - "reloadSkills"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A SessionStart hook can add context, supply the first user message, set the session title, register watched files and trigger a skill re-scan. Return these inside `hookSpecificOutput` with `hookEventName: "SessionStart"`. Plain-text stdout on exit 0 is also added to Claude's context.

# How to use it

| Field | Description |
| :- | :- |
| `additionalContext` | String added to context at conversation start, before the first prompt |
| `initialUserMessage` | String used as the first user message in non-interactive mode (`-p`); becomes the first turn even with no prompt; a prompt you pass follows as the next turn |
| `sessionTitle` | Sets the title like `/rename`; applies when `source` is `startup`, `resume` or `fork` |
| `watchPaths` | Array of absolute paths watched for [FileChanged](./p2-filechanged-event.md) events |
| `reloadSkills` | Boolean; `true` makes Claude Code re-scan skill and command directories after SessionStart hooks finish |

Example: `echo '{"hookSpecificOutput": {"hookEventName": "SessionStart", "reloadSkills": true}}'` after syncing a skills repo into `~/.claude/skills/`.

# Limits and defaults

- Skill discovery normally runs before SessionStart hooks finish, so skills a hook writes to `~/.claude/skills/` or `.claude/skills/` can be missing at the first prompt unless `reloadSkills` is returned.
- A plugin SessionStart hook's `initialUserMessage` and `sessionTitle` are ignored if the plugin finishes installing after SessionStart hooks have run; install before the session starts.
