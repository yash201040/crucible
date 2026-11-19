---
type: "Reference"
title: "Agent view keyboard shortcuts"
description: "Shortcuts for navigating, dispatching, pinning, renaming and stopping sessions in agent view."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, keyboard, shortcuts, keybindings]
kind: "ui"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Ctrl+Enter"
  - "Alt+1"
  - "Ctrl+S"
  - "Ctrl+T"
  - "Ctrl+F"
  - "Ctrl+R"
  - "Ctrl+G"
  - "Ctrl+J"
  - "Ctrl+X"
  - "Ctrl+Y"
  - "keybindings.json"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

`?` shows shortcuts in context.

| Shortcut | Action |
| :- | :- |
| `↑`/`↓`, `PgUp`/`PgDn`, `Home`/`End` | Move between rows |
| `Enter` | Attach, or submit input if not a filter |
| `Space` | Open or close peek |
| `Shift+Enter`, `Ctrl+J` | Newline in dispatch input |
| `Ctrl+Enter` | Dispatch and attach immediately (where `?` lists `ctrl+enter to start and open`) |
| `→` | Attach |
| `Alt+1`..`Alt+9` | Attach to session 1-9 in focused session's directory |
| `Tab` | Empty input: browse subagents; otherwise apply suggestion |
| `Ctrl+S` | Switch grouping state/directory |
| `Ctrl+T` | Pin or unpin |
| `Ctrl+F` | Find by name (`n:` filter) |
| `Alt+↑`/`Alt+↓` | Previous or next group header |
| `Ctrl+R` | Rename |
| `Ctrl+G` | Edit dispatch prompt in `$VISUAL`/`$EDITOR` |
| `Ctrl+X` | Stop; again within two seconds to delete |
| `Shift+↑`/`Shift+↓` | Reorder |
| `Esc` | Close peek, clear input, or exit (v2.1.323+: clearing a prompt takes two presses; final `Esc` returns to the conversation if opened via `←`; vim mode: INSERT to NORMAL) |
| `Ctrl+Y` | Restore last cleared text in dispatch input |
| `Ctrl+C` | Clear input; twice to exit; clears a selection first |

Shortcuts with an action in the `Agents` context follow `keybindings.json`; `Ctrl+G` follows `chat:externalEditor` in the `Chat` context. Actions `agents:switchView` and `agents:togglePin` map to `Ctrl+S`, `Ctrl+T`.
