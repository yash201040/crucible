---
type: "Reference"
title: "Render sites: props, requestId and surfaces"
description: "Each ui.render e.component value with its e.props fields, e.requestId meaning and the apps that render it, plus viewport sizing."
resource: "https://code.claude.com/docs/en/plugins/mods/reference"
tags: [mods, render-sites, props, surfaces]
kind: "ui"
maturity: "unlabelled"
since: "2.1.299"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "Pane"
  - "AbovePrompt"
  - "AbovePromptList"
  - "Placed"
  - "Backdrop"
  - "UserMessage"
  - "AssistantMessage"
  - "ToolUse"
  - "ToolResult"
  - "ToolGroup"
  - "CommandOutput"
  - "AskUserQuestion"
  - "ToolProgress"
  - "Spinner"
  - "TurnDuration"
  - "InfoNotice"
  - "SessionMode"
  - "PromptHint"
  - "e.viewport"
  - "e.props.bodyColumns"
  - "e.props.scroll.bodyRows"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-reference"
    resource: "https://code.claude.com/docs/en/plugins/mods/reference"
    title: "Mods reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`e.surface` is `terminal`, `desktop` or `vscode`. VS Code rendering needs extension 2.1.299+ (2.1.304+ without feature-flag fetch).

| Site | `e.props` | `e.requestId` | Rendered on |
| :- | :- | :- | :- |
| `Pane` | `title`, `isFocused`, `bodyColumns`, `placement`, `scroll`, `view` | pane `id` | Terminal, Desktop, VS Code |
| `AbovePrompt` | `hasSurvey`, `isCollapsed`, `isWorking`, `maxRows`, `bodyColumns`, `scroll`, `view` | one instance | Terminal, Desktop |
| `AbovePromptList` | `rows` (list of `{ plugin, tree }`) plus AbovePrompt props | one instance | Terminal, Desktop; v2.1.323+ |
| `Placed` | `id`, `plugin`, `onScreen` | `requestId` from `$.ui.place` | Terminal |
| `Backdrop` | `scene`, `plugin`, `glass`, `overrideColorScheme` (before v2.1.323: `id`, `colorScheme`) | `backdrop` | desktop and mobile |
| `UserMessage` | `text`, `origin`, `isExpanded`, `task` or `from` | row id | Terminal, Desktop, VS Code |
| `AssistantMessage` | reply text | row id | Terminal, Desktop, VS Code |
| `ToolUse`, `ToolResult`, `ToolGroup` | tool name, input, result | tool call id | Terminal, Desktop, VS Code |
| `CommandOutput` | `command`, `text` | row id | Terminal, Desktop |
| `AskUserQuestion` | question and options | tool call id | Terminal, Desktop, VS Code |
| `ToolProgress` | `kind` | tool call id | Terminal |
| `Spinner` | `word`, `message`, `suffix`, `mode` | agent id | Terminal, Desktop, VS Code |
| `TurnDuration` | `word`, `durationMs` | row id | Terminal |
| `InfoNotice` | `text`, `command` | notice text prefixed `notice:` | Terminal |
| `SessionMode` | `modes` | one instance | Terminal, Desktop |
| `PromptHint` | `isDraft`, `isWorking`, `hint` | one instance | Terminal, Desktop |

# How to use it

`e.viewport` holds `columns`, `rows`, `isFullscreen`; in terminal and Desktop it is absent until the window is measured and `rows` is the whole window height; in VS Code always present. Draw a Pane or band to `e.props.bodyColumns`. Pane beside transcript (`placement` `'dock'`): `e.props.scroll.bodyRows` is the rows for your tree. Pane above prompt (`'inline'`): grows with the tree to a limit `bodyRows`; request another via the `rows` field of `$.ui.open`. A tree taller than the pane scrolls as a whole.
