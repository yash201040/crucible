---
type: "Reference"
title: "Index: ~/.claude.json global config keys"
description: "Keys kept in ~/.claude.json rather than settings files, including IDE, copy, agent view and removed keys (index rows only)."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [global-config, claude-json, settings, ide]
kind: "setting"
maturity: "unlabelled"
since: "2.1.257"
surfaces: [cli, ide]
requires: ""
identifiers:
  - "autoConnectIde"
  - "autoInstallIdeExtension"
  - "claudeInChromeDefaultEnabled"
  - "copyFullResponse"
  - "copyOnSelect"
  - "defaultToAgentsView"
  - "diffTool"
  - "externalEditorContext"
  - "leftArrowOpensAgents"
  - "prStatusFooterEnabled"
  - "permissionExplainerEnabled"
  - "teammateDefaultModel"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The short group of keys scope `Global config`, stored in `~/.claude.json`. Detailed sections are in other parts of the page.

# How to use it

| Key | What it does |
| :- | :- |
| `autoConnectIde` | Connect to a running VS Code or JetBrains IDE automatically from an external terminal |
| `autoInstallIdeExtension` | Let `/ide` install the IDE extension from an external terminal |
| `claudeInChromeDefaultEnabled` | Turn on Chrome integration at session start in the interactive CLI and VS Code extension |
| `copyFullResponse` | Make `/copy` copy the full response without the picker |
| `copyOnSelect` | Turn off automatic copying of mouse selections in fullscreen rendering and agent view |
| `defaultToAgentsView` | Open agent view instead of a new conversation when running `claude` with no arguments |
| `diffTool` | Open proposed changes in the VS Code or JetBrains diff viewer or keep them in the terminal |
| `externalEditorContext` | Show Claude's last response as comments when pressing Ctrl+G to edit |
| `leftArrowOpensAgents` | Turn off the left-arrow shortcut that backgrounds the session and opens agent view |
| `prStatusFooterEnabled` | Turn off the prompt footer's PR review status badge and the PR check behind it |
| `permissionExplainerEnabled` | Removed in v2.1.257, together with the `Ctrl+E` command explanation on shell permission prompts |
| `teammateDefaultModel` | Removed in v2.1.234; see the agent-teams page for how a teammate's model is picked |
