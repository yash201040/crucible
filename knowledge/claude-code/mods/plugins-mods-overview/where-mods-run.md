---
type: "Reference"
title: "Where mods run (surfaces and headless)"
description: "Mod hooks run in every session that loads the plugin, including claude -p, the Agent SDK and cloud sessions, but drawing only in terminal, Desktop and VS Code."
resource: "https://code.claude.com/docs/en/plugins/mods/overview"
tags: [mods, surfaces, headless, sdk]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk, desktop, ide, cloud]
requires: ""
identifiers:
  - "claude -p"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-overview"
    resource: "https://code.claude.com/docs/en/plugins/mods/overview"
    title: "Mods overview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Hooks run in every kind of session that loads the plugin, whichever provider serves the model (including Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry). Drawing is narrower.

| Where | Hooks run | Drawing appears |
| :- | :- | :- |
| `claude` in a terminal (incl. editor terminal, JetBrains plugin) | Yes | Yes |
| Desktop Code tab (not WSL) | Yes | Yes, except terminal-only elements |
| Desktop WSL session | No (plugins not available in WSL sessions) | No |
| VS Code chat panel | Yes | Yes, extension 2.1.299+ (2.1.304+ if no feature-flag fetch, e.g. Bedrock) |
| `claude -p` and the Agent SDK | Yes | No |
| Remote Control from claude.ai or mobile | Yes, in the session on your machine | In the terminal on your machine |
| Cloud session | Yes, for a plugin that reaches the cloud session | No |

# Notes

A mod that draws can check which app it runs in and fall back to a transcript line or a command's text reply where nothing draws. In `claude -p`, `$.ui.ask` rejects (nobody to ask).
