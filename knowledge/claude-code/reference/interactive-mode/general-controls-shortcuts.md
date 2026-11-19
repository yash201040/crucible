---
type: "Reference"
title: "General keyboard shortcuts"
description: "Keys for interrupting, backgrounding, stashing, switching model or mode, and sending queued messages in the interactive prompt."
resource: "https://code.claude.com/docs/en/interactive-mode"
tags: [keyboard, shortcuts, interrupt, background, permission-mode]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Ctrl+C"
  - "Ctrl+X Ctrl+K"
  - "Ctrl+D"
  - "Ctrl+G"
  - "Ctrl+X Ctrl+E"
  - "Ctrl+L"
  - "Ctrl+O"
  - "Ctrl+R"
  - "Ctrl+V"
  - "Ctrl+B"
  - "Ctrl+T"
  - "Ctrl+S"
  - "Ctrl+Z"
  - "Tab"
  - "Esc"
  - "Esc + Esc"
  - "Ctrl+Enter"
  - "Ctrl+X Ctrl+S"
  - "Shift+Tab"
  - "Option+P"
  - "Alt+P"
  - "Option+T"
  - "Alt+T"
  - "Option+O"
  - "Alt+O"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "interactive-mode"
    resource: "https://code.claude.com/docs/en/interactive-mode"
    title: "Interactive mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The general-controls table of the interactive terminal prompt. Shortcuts vary by platform and terminal. On macOS the Option/Alt shortcuts (`Alt+B`, `Alt+F`, `Alt+D`, `Alt+Y`, `Alt+P`) need Option configured as Meta in the terminal.

# How to use it

| Shortcut | What it does |
| :- | :- |
| `Ctrl+C` | Interrupts a running operation. With nothing running, first press clears the prompt, second exits. |
| `Ctrl+X Ctrl+K` | Stops all running background subagents in the session and turns off artifact auto-replies for the rest of it. Press twice within 3 seconds to confirm; works while a background subagent permission prompt is open. |
| `Ctrl+D` | Exit: first press shows a hint, second within 800ms exits. With text in the prompt it deletes the character after the cursor. |
| `Ctrl+G` or `Ctrl+X Ctrl+E` | Edit the prompt in the default text editor. `/config` option **Show last response in external editor** prepends Claude's last reply as `#` comments (stripped on save). |
| `Ctrl+L` | Full terminal redraw, keeps input and history. |
| `Ctrl+O` | Toggle transcript viewer (tool usage detail, timestamp and model per assistant message; expands collapsed MCP call lines and cross-session message previews). |
| `Ctrl+R` | Reverse search of command history. |
| `Ctrl+V` / `Cmd+V` (iTerm2) / `Alt+V` (Windows, WSL) | Paste an image from the clipboard as an `[Image #N]` chip. |
| `Ctrl+B` | Background running Bash commands and agents. Tmux users press twice. |
| `Ctrl+T` | Toggle Claude's task checklist (not the `/tasks` background view). |
| `Ctrl+S` | Stash the prompt, or restore the stash (text, cursor, pasted content, input mode) on an empty prompt. |
| `Ctrl+Z` | Suspend the process (Unix only); `fg` resumes. |
| `Tab` | Accept an autocomplete suggestion, or open a comment field on a permission prompt answer. |
| `Esc` | Interrupt the current response or tool call (work done is kept; queued messages are then sent); closes a dialog; on a permission prompt declines. |
| `Esc` + `Esc` | With text: clear the draft and save it to history. With empty input: open the rewind menu. |
| `Ctrl+Enter` or `Ctrl+X Ctrl+S` | Send queued messages now. Needs Claude Code v2.1.275 or later. |
| `Shift+Tab` (`Alt+M` on Windows without VT input) | Cycle permission modes: `default` (labeled Manual), `acceptEdits`, `plan`, then `bypassPermissions` and `auto` where available. |
| `Option+P` / `Alt+P` | Switch model without clearing the prompt. |
| `Option+T` / `Alt+T` | Toggle extended thinking. No effect on Opus 5.5, Sonnet 5.5, Haiku 5.5 or the Fable models, which always use extended thinking. |
| `Option+O` / `Alt+O` | Toggle fast mode. |

Other keys in the same table: `Left/Right arrows` switch dialog tabs, `Up/Down` or `Ctrl+P`/`Ctrl+N` move the cursor or navigate history (with messages queued, `Up` from the first row takes them back).

# Notes

Cleared drafts can be recovered, see [command history](./command-history.md). Queue behaviour is in [queue messages](./queue-messages-while-working.md).
