---
type: "Concept"
title: "Plugin install scopes and loading layers"
description: "User, project and local install scopes, and the settings, disk and session layers a plugin must pass to be usable."
resource: "https://code.claude.com/docs/en/plugins/overview"
tags: [plugins, scopes, settings, cloud]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide, cloud, web]
requires: ""
identifiers:
  - "~/.claude/plugins/"
  - ".claude/settings.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-overview"
    resource: "https://code.claude.com/docs/en/plugins/overview"
    title: "Plugins overview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Install scope decides who a plugin is enabled for:
- User scope: you, in every project on this computer.
- Project scope: everyone in the repository via committed `.claude/settings.json`; each collaborator still installs it on their own machine.
- Local scope: you, in this repository only.

A user-scope plugin installed in the terminal, the desktop app's local sessions or the VS Code extension is available in the other two, since they read the same settings files. A cloud session (including claude.ai/code) does not load plugins from your local settings. The same format also installs on claude.ai and Cowork, which load a different set of components.

# How to use it

For a plugin to give a runnable skill it must be present at three layers: Settings (marketplaces added, plugins enabled), Disk (`~/.claude/plugins/` holds what was fetched), Session (plugins load at startup or when plugins are reloaded). The Plugin loading reference covers settings precedence and file locations.

# Notes

Related pages: install, create, publish, measure, evals, org management, troubleshooting.
