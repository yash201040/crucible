---
type: "Feature"
title: "Mods and asking Claude to write one"
description: "A mod is a plugin with a hooks module; Claude writes one from a description using the plugin-authoring skill into the session's dev-mods folder."
resource: "https://code.claude.com/docs/en/plugins/mods/create"
tags: [mods, plugin-authoring, hot-reload, dev-mods]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.287"
surfaces: [cli]
requires: "Claude Code v2.1.287 or later"
identifiers:
  - "plugin-authoring"
  - "/plugin-authoring"
  - "~/.claude/dev-mods/<session-id>/"
  - "cleanupPeriodDays"
  - "--plugin-dir"
  - "/plugin"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-create"
    resource: "https://code.claude.com/docs/en/plugins/mods/create"
    title: "Create a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A mod is a Claude Code plugin with an entry file, the hooks module: a JavaScript or TypeScript file whose functions Claude Code calls on events. No Node.js, bundler or build step is needed; `.js` and `.ts` load directly. Use v2.1.287 or later.

# How to use it

Describe the mod in an interactive session (for example "make a mod that shows the current git branch above the prompt"). Claude works from the built-in skill `plugin-authoring` (also loadable with `/plugin-authoring`) and writes into `~/.claude/dev-mods/<session-id>/<mod>/`. In `default` and `acceptEdits` modes you approve each file (the folder is a protected path). On the first file saved Claude Code asks whether to enable hot reloading: **Turn them on** loads the session's mods at end of turn and reloads after each turn that changes them (answer lasts the session, including resume); **Not now** loads nothing now but the mods load next time that session starts. Check the **Installed** tab of `/plugin`. If a transcript line from the mod says its change did not load, paste it into your next message; Claude does not see it otherwise.

# Limits and defaults

A mod Claude wrote loads only in its session; the session's mods folder is deleted after `cleanupPeriodDays`. To keep one, copy it out (e.g. `~/mods/git-branch`) and load with `claude --plugin-dir ~/mods/git-branch` or add it to a marketplace.
