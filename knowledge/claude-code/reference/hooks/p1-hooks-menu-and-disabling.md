---
type: "Feature"
title: "The /hooks menu and disabling hooks"
description: "Read-only /hooks browser and the disableAllHooks setting, including its precedence and managed-hook behavior."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, disable, settings, menu]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/hooks"
  - "disableAllHooks"
  - "--settings"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/hooks` opens a read-only browser of configured hooks, labeled by source (user, project, local, plugin, session). Selecting one shows the full command and where it is defined; `All events` at the end lists every event including unconfigured ones.

# How to use it

- Remove a hook by deleting its entry from the settings file. File-watcher picks up direct edits normally.
- Disable all temporarily: `"disableAllHooks": true`. The value after settings precedence applies is used, so a project `"disableAllHooks": false` overrides a user `true`. For one run regardless of project settings: `--settings '{"disableAllHooks": true}'`.
- There is no way to disable a single hook while keeping it in config.

# Limits and defaults

`disableAllHooks` set in user, project or local settings cannot disable managed policy hooks; only the managed level can.
