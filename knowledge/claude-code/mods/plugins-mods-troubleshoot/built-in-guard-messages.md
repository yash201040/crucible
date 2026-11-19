---
type: "Reference"
title: "Built-in guard messages"
description: "Messages from the built-in guard that refuses a mod or one of its answers, with where each appears."
resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
tags: [mods, guard, permissions, deny-rules]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "mods are limited to your organization's by policy (allowManagedModsOnly)"
  - "tried to lift a deny rule in your settings"
  - "the rules and hooks in your settings could not be checked for this call, so it is refused"
  - "tool.check"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-troubleshoot"
    resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
    title: "Troubleshoot a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Where the built-in guard loads, it can refuse a mod or one of its answers. Some messages name the option the administrator sets to change the rule.

# How to use it

| Message contains | Meaning | Where it appears |
| :- | :- | :- |
| `mods are limited to your organization's by policy (allowManagedModsOnly)` | Only the organization's own mods are allowed, so yours was refused | Debug log, and the transcript in a session that hot-reloads a plugin directory |
| `tried to lift a deny rule in your settings` | A mod's `tool.check` hook approved a call that a `deny` rule refuses; the call stays denied | Transcript and debug log, once per mod per session; in `claude -p`, the debug log |
| `the rules and hooks in your settings could not be checked for this call, so it is refused` | The guard failed while checking a call a mod approved, so it refused it | The reason Claude reads for the denied call |

# Notes

A mod cannot override a settings `deny` rule through `tool.check`.
