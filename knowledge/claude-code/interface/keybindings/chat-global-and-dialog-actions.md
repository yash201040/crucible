---
type: "Reference"
title: "Keybinding actions: app, chat, dialogs and lists"
description: "Action names, contexts and defaults for Global, Chat, Autocomplete, Confirmation, Transcript, HistorySearch, Task, Theme, Help, Tabs, Attachments, Select and Settings."
resource: "https://code.claude.com/docs/en/keybindings"
tags: [keybindings, actions, shortcuts, chat, defaults]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "app:interrupt"
  - "app:exit"
  - "app:redraw"
  - "app:toggleTodos"
  - "app:toggleTranscript"
  - "history:search"
  - "history:previous"
  - "history:next"
  - "chat:cancel"
  - "chat:clearInput"
  - "chat:clearScreen"
  - "chat:killAgents"
  - "chat:cycleMode"
  - "chat:modelPicker"
  - "chat:fastMode"
  - "chat:thinkingToggle"
  - "chat:submit"
  - "chat:queueSubmit"
  - "chat:sendNow"
  - "chat:newline"
  - "chat:undo"
  - "chat:externalEditor"
  - "chat:stash"
  - "chat:imagePaste"
  - "autocomplete:accept"
  - "autocomplete:dismiss"
  - "autocomplete:previous"
  - "autocomplete:next"
  - "confirm:yes"
  - "confirm:no"
  - "confirm:previous"
  - "confirm:next"
  - "confirm:nextField"
  - "confirm:previousField"
  - "confirm:toggle"
  - "confirm:cycleMode"
  - "confirm:toggleExplanation"
  - "permission:toggleDebug"
  - "transcript:toggleShowAll"
  - "transcript:exit"
  - "historySearch:next"
  - "historySearch:accept"
  - "historySearch:cancel"
  - "historySearch:execute"
  - "historySearch:cycleScope"
  - "task:background"
  - "theme:toggleSyntaxHighlighting"
  - "help:dismiss"
  - "tabs:next"
  - "tabs:previous"
  - "attachments:next"
  - "attachments:previous"
  - "attachments:remove"
  - "attachments:exit"
  - "select:next"
  - "select:previous"
  - "select:pageUp"
  - "select:pageDown"
  - "select:first"
  - "select:last"
  - "select:accept"
  - "select:cancel"
  - "settings:search"
  - "settings:retry"
  - "settings:fixUsage"
  - "voice:pushToTalk"
  - "plugin:toggle"
  - "plugin:install"
  - "plugin:favorite"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "keybindings"
    resource: "https://code.claude.com/docs/en/keybindings"
    title: "Customize keyboard shortcuts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Rebindable actions grouped by context, with defaults.

# How to use it

| Context | Action: default |
| :- | :- |
| `Global` | `app:interrupt` Ctrl+C; `app:exit` Ctrl+D (twice within 800 ms); `app:redraw` unbound; `app:toggleTodos` Ctrl+T (the to-do checklist, not `/tasks`); `app:toggleTranscript` Ctrl+O; `history:search` Ctrl+R; `history:previous` Up; `history:next` Down |
| `Chat` | `chat:cancel` Escape; `chat:clearInput` Ctrl+L and `chat:clearScreen` Cmd+K (both full redraw keeping input and conversation); `chat:killAgents` Ctrl+X Ctrl+K (stops all running background subagents and turns off artifact auto-replies for the session; press twice within 3 s; usable while a background subagent permission prompt is open); `chat:cycleMode` Shift+Tab (Meta+M on Windows without VT mode); `chat:modelPicker` Meta+P; `chat:fastMode` Meta+O; `chat:thinkingToggle` Meta+T; `chat:submit` Enter; `chat:queueSubmit` Ctrl+X Enter (v2.1.247+, queues without interrupting even with autocomplete highlighted); `chat:sendNow` Ctrl+Enter or Ctrl+X Ctrl+S (v2.1.275+, sends queued messages and draft at once); `chat:newline` Ctrl+J; `chat:undo` Ctrl+_ or Ctrl+Shift+-; `chat:externalEditor` Ctrl+G, Ctrl+X Ctrl+E; `chat:stash` Ctrl+S; `chat:imagePaste` Ctrl+V (Alt+V on Windows and WSL); `command:<name>` unbound |
| `Autocomplete` | `autocomplete:accept` Tab; `:dismiss` Escape; `:previous` Up; `:next` Down |
| `Confirmation` | `confirm:yes` Enter; `confirm:no` Escape; `confirm:previous` Up; `confirm:next` Down; `confirm:nextField` Tab (toggles fast mode in `/fast` dialog); `confirm:previousField` unbound and ignored; `confirm:toggle` Space; `confirm:cycleMode` Shift+Tab (closes a permission comment field, else allows for the session when offered); `permission:toggleDebug` unbound and ignored |
| `Transcript` | `transcript:toggleShowAll` Ctrl+E (classic renderer only); `transcript:exit` q, Ctrl+C, Escape |
| `HistorySearch` | `historySearch:next` Ctrl+R; `:accept` Escape, Tab; `:cancel` Ctrl+C; `:execute` Enter; `:cycleScope` Ctrl+S (fullscreen only: session, project, everywhere) |
| `Task` | `task:background` Ctrl+B, Ctrl+X Ctrl+B |
| `ThemePicker`, `Help` | `theme:toggleSyntaxHighlighting` Ctrl+T; `help:dismiss` Escape |
| `Tabs` | `tabs:next` Tab, Right; `tabs:previous` Shift+Tab, Left |
| `Attachments` | `attachments:next` Right; `:previous` Left; `:remove` Backspace, Delete; `:exit` Down, Escape |
| `Select` | `select:next` Down, J, Ctrl+N; `:previous` Up, K, Ctrl+P; `:pageUp`; `:pageDown`; `:first` Home; `:last` End; `:accept` Enter; `:cancel` Escape |
| `Settings` | `settings:search` /; `settings:retry` R; `settings:fixUsage` F (v2.1.305+); `select:accept` Enter, Space; `confirm:no` Escape (changes already saved) |
| `Chat` (voice) | `voice:pushToTalk` Space, when voice dictation is enabled |
| `Plugin` | `plugin:toggle` Space; `plugin:install` I; `plugin:favorite` F |

# Notes

- `MessageSelector` (rewind menu) has no actions of its own and uses `Select` actions; before v2.1.283 it had `messageSelector:up`, `:down`, `:top`, `:bottom`, `:select`, which still work as the matching Select actions.
- `confirm:toggleExplanation` (Ctrl+E) was removed before v2.1.257. Before v2.1.280 `y` and `n` were default `confirm:yes`/`confirm:no`; older generated files keep them until deleted. Binding bare letters in `Confirmation` also acts on dialogs that do not show them; text fields still type the letters.
- `Select` paging/first/last bindings apply in list panels such as `/skills`, `/mcp`, `/tasks`; before v2.1.280 other lists ignored Home/End bindings.
- Ctrl+C or Ctrl+D pressed twice closes most dialogs rather than exiting.
