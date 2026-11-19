---
type: "Guide"
title: "Convert a .claude/ setup into a plugin"
description: "Copy commands, agents, skills and the settings hooks object into a plugin; originals stay loaded alongside and hooks run twice."
resource: "https://code.claude.com/docs/en/plugins/create"
tags: [plugins, migration, hooks, skills]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - ".claude/commands"
  - ".claude/agents"
  - ".claude/skills"
  - ".claude/settings.json"
  - ".claude/settings.local.json"
  - "hooks/hooks.json"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-create"
    resource: "https://code.claude.com/docs/en/plugins/create"
    title: "Create a Claude Code plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

Create `my-plugin/.claude-plugin/plugin.json`, then `cp -r` `.claude/commands`, `.claude/agents`, `.claude/skills` to the plugin root. Copy the `hooks` object from `.claude/settings.json` or `.claude/settings.local.json` into `my-plugin/hooks/hooks.json` (same format). Test with `claude --plugin-dir ./my-plugin` and check components under new names (`/my-plugin:deploy`, `my-plugin:reviewer`).

# Limits and defaults

While originals remain under `.claude/` they stay loaded: skills and agents do not collide (prefix `my-plugin:`), but hooks have no prefix, so a hook in both the settings file and `hooks/hooks.json` runs twice per event. After confirming, delete the originals and the settings `hooks` object.
