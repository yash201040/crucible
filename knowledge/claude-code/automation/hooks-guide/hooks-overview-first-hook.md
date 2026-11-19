---
type: "Guide"
title: "Hooks overview and first hook"
description: "Hooks are user-defined handlers run at lifecycle points for deterministic control; how to add and verify a Notification hook."
resource: "https://code.claude.com/docs/en/hooks-guide"
tags: [hooks, setup, settings, lifecycle]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "hooks"
  - "/hooks"
  - "~/.claude/settings.json"
  - "Notification"
  - "type"
  - "command"
  - "matcher"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks-guide"
    resource: "https://code.claude.com/docs/en/hooks-guide"
    title: "Automate actions with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Hooks are user-defined handlers Claude Code runs at specific lifecycle points, giving deterministic control: certain actions always happen instead of relying on the model. Use them to enforce project rules, automate repetitive tasks and integrate existing tools. For judgment-based decisions use prompt-based or agent-based hooks. Other extension routes: skills, subagents, plugins. The full event schemas live in the Hooks reference.

# How to use it

1. Add a `hooks` block to a settings file, for example in `~/.claude/settings.json`:
```json
{"hooks":{"Notification":[{"matcher":"","hooks":[{"type":"command","command":"osascript -e 'display notification \"Claude Code needs your attention\" with title \"Claude Code\"'"}]}]}}
```
2. If a `hooks` key exists, add the event as a sibling key; do not replace the object. Each event name is a key inside the single `hooks` object.
3. Verify with `/hooks` (the hooks browser lists it under `Notification`).
4. Test: `Shift+Tab` until the status bar shows `⏸ manual mode on`, ask for something needing permission, switch away.

You can also ask Claude to write the hook from a description.

# Notes

Production example of hooks running a separate model review and feeding findings back: the `security-guidance` plugin.
