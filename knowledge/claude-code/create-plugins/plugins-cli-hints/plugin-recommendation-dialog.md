---
type: "Feature"
title: "Plugin recommendation dialog"
description: "The dialog users see for a hint and the effect of each answer, including a 30-second timeout counting as No."
resource: "https://code.claude.com/docs/en/plugins/cli-hints"
tags: [plugins, hints, ui, install]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Plugin recommendation"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-hints"
    resource: "https://code.claude.com/docs/en/plugins/cli-hints"
    title: "Recommend your plugin from your CLI"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When the prompt conditions pass, a **Plugin recommendation** dialog shows the plugin name, marketplace and description and the options: 1 Yes, install; 2 No; 3 No, and don't show plugin installation hints again. It names the first word of the shell command Claude ran, so users can spot a mismatch.

# How to use it

- Yes, install: installs the plugin at user scope.
- No, and don't show again: turns off future hint prompts for that user.
- No answer for 30 seconds: counts as No.
