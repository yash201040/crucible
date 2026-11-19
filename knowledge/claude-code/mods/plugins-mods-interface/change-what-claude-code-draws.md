---
type: "Reference"
title: "Change what Claude Code already draws (render sites)"
description: "Claude Code's own messages, tool rows, spinner and notices are render sites a mod can restyle, replace or leave alone."
resource: "https://code.claude.com/docs/en/plugins/mods/interface"
tags: [mods, render-sites, spinner, restyle]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "UserMessage"
  - "AssistantMessage"
  - "ToolUse"
  - "ToolResult"
  - "ToolGroup"
  - "CommandOutput"
  - "AskUserQuestion"
  - "Spinner"
  - "ToolProgress"
  - "TurnDuration"
  - "InfoNotice"
  - "SessionMode"
  - "PromptHint"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-interface"
    resource: "https://code.claude.com/docs/en/plugins/mods/interface"
    title: "Draw in the interface with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Site | What it is |
| :- | :- |
| `UserMessage`, `AssistantMessage` | A message in the transcript |
| `ToolUse`, `ToolResult`, `ToolGroup` | A tool call row, its result, a collapsed group of calls |
| `CommandOutput` | The row a command printed |
| `AskUserQuestion` | The dialog Claude opens to ask a question |
| `Spinner`, `ToolProgress`, `TurnDuration` | Status lines: animated line, running tool progress, line closing a turn |
| `InfoNotice`, `SessionMode`, `PromptHint` | Lines under the logo, mode labels in the footer, hint under the prompt |

`Pane`, `AskUserQuestion`, `Spinner`, `UserMessage`, `AssistantMessage` and the tool call sites work in terminal, Desktop and VS Code.

# How to use it

At such a site: change a detail with `next({ ...e, props: { ...e.props, suffix: '...' } })`; replace by returning a tree without `next`; leave alone with `next(e)`. `next(e)` returns `{ type: 'engine', ref }`, a reference to Claude Code's drawing, which can be returned or put in a `Box` beside your elements. For `AskUserQuestion`, a tree must hold the reference exactly once with your elements above it, otherwise Claude Code draws its own dialog.

# Limits and defaults

The permission prompt is not a render site: a mod cannot change what it shows.
