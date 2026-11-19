---
type: "Feature"
title: "LSP plugin recommendation dialog"
description: "A dialog that offers a language server plugin when its binary is on PATH, with four choices and a five-ignore cutoff."
resource: "https://code.claude.com/docs/en/plugins/code-intelligence"
tags: [lsp, recommendation, dialog, plugins]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "lspRecommendationDisabled"
  - "lspRecommendationIgnoredCount"
  - "lspRecommendationNeverPlugins"
  - "~/.claude.json"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-code-intelligence"
    resource: "https://code.claude.com/docs/en/plugins/code-intelligence"
    title: "Code intelligence plugins"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When a language server binary is on `PATH` and the plugin using it is not installed, Claude Code can show a dialog titled **LSP plugin recommendation** after Claude edits a file.

# How to use it

Appearance conditions: a marketplace you added (or the registered official one) lists a plugin for the file's extension and its binary is installed; the official marketplace's plugin is offered first; at most once per session, for the first matching file; never when the terminal is attached to a cloud session (such as `claude --cloud`).

Choices: **Yes, install** (installs for your user account, prints `<plugin> installed · restart to apply`), **No, not now** (also Esc), **Never for this plugin**, **Disable all LSP recommendations**.

# Limits and defaults

The dialog closes after 30 seconds and counts as ignored; the count persists across sessions. After five ignored dialogs recommendations stop, same as disabling them all.

# Notes

To turn recommendations back on, remove `lspRecommendationDisabled` and `lspRecommendationIgnoredCount` from `~/.claude.json`. To re-offer a plugin you chose Never for, remove its `name@marketplace` id from `lspRecommendationNeverPlugins` in the same file.
