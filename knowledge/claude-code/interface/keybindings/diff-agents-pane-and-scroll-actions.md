---
type: "Reference"
title: "Keybinding actions: diff, agent view, panes and scroll"
description: "Actions and defaults for diff dialog and panel, model and effort pickers, footer, above-prompt band, mod panes, agent view and fullscreen scroll/selection."
resource: "https://code.claude.com/docs/en/keybindings"
tags: [keybindings, actions, agent-view, panes, scrolling]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.257"
surfaces: [cli]
requires: ""
identifiers:
  - "diff:dismiss"
  - "diff:previousSource"
  - "diff:nextSource"
  - "diff:previousFile"
  - "diff:nextFile"
  - "diff:back"
  - "diff:viewDetails"
  - "app:toggleReplTab"
  - "app:cycleDiffBase"
  - "app:diffFileListUp"
  - "app:diffFileListDown"
  - "app:toggleDiffNoiseFilter"
  - "app:toggleDiffPreSession"
  - "modelPicker:decreaseEffort"
  - "modelPicker:increaseEffort"
  - "modelPicker:thisSessionOnly"
  - "effortSlider:decreaseEffort"
  - "effortSlider:increaseEffort"
  - "effortSlider:toggleUltracode"
  - "effortSlider:thisSessionOnly"
  - "footer:next"
  - "footer:previous"
  - "footer:up"
  - "footer:down"
  - "footer:openSelected"
  - "footer:clearSelection"
  - "footer:close"
  - "footer:dismiss"
  - "abovePrompt:toggle"
  - "abovePrompt:focus"
  - "abovePrompt:next"
  - "abovePrompt:previous"
  - "abovePrompt:press"
  - "abovePrompt:leave"
  - "abovePrompt:highlightNext"
  - "abovePrompt:highlightPrevious"
  - "pane:scrollUp"
  - "pane:scrollDown"
  - "pane:pageUp"
  - "pane:pageDown"
  - "pane:top"
  - "pane:bottom"
  - "pane:grow"
  - "pane:shrink"
  - "pane:close"
  - "pane:next"
  - "pane:previous"
  - "agents:switchView"
  - "agents:togglePin"
  - "agents:find"
  - "agents:rename"
  - "agents:previousGroup"
  - "agents:nextGroup"
  - "scroll:lineUp"
  - "scroll:lineDown"
  - "scroll:pageUp"
  - "scroll:pageDown"
  - "scroll:top"
  - "scroll:bottom"
  - "scroll:halfPageUp"
  - "scroll:halfPageDown"
  - "scroll:fullPageUp"
  - "scroll:fullPageDown"
  - "selection:copy"
  - "selection:clear"
  - "selection:extendLeft"
  - "selection:extendRight"
  - "selection:extendUp"
  - "selection:extendDown"
  - "selection:extendLineStart"
  - "selection:extendLineEnd"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "keybindings"
    resource: "https://code.claude.com/docs/en/keybindings"
    title: "Customize keyboard shortcuts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The remaining actions by context. Continues [chat and dialog actions](./chat-global-and-dialog-actions.md).

# How to use it

| Context | Action: default |
| :- | :- |
| `DiffDialog` | `diff:dismiss` Escape; `diff:previousSource` Left; `diff:nextSource` Right; `diff:previousFile` Up, K; `diff:nextFile` Down, J; `diff:back` unbound (Left default removed v2.1.203). Reaches only the earlier diff viewer shown after disabling the `cc-plugin-diff` mod in `/plugin`. The detail view also binds `scroll:*` pager keys (PageUp, PageDown, Shift+Space/B, Space, G/Home, Shift+G/End). File list uses `Select` actions; `diff:viewDetails` (pre-v2.1.283) maps to `select:accept` |
| `DiffPanel`/`Global` | `app:cycleDiffBase` Ctrl+X B (session, uncommitted, branch); `app:diffFileListUp` Ctrl+Up, Meta+Up; `app:diffFileListDown` Ctrl+Down, Meta+Down; `app:toggleReplTab`, `app:toggleDiffNoiseFilter`, `app:toggleDiffPreSession` unbound and reach only the earlier panel |
| `ModelPicker` | `modelPicker:decreaseEffort` Left; `:increaseEffort` Right; `:thisSessionOnly` s |
| `EffortSlider` | `effortSlider:decreaseEffort` Left and `:increaseEffort` Right (v2.1.284+); `:toggleUltracode` Tab (v2.1.284+, when offered); `:thisSessionOnly` s (v2.1.257+). Enter and Escape fixed |
| `Footer` | `footer:next` Right; `:previous` Left; `:up` Up, Ctrl+P; `:down` Down, Ctrl+N; `:openSelected` Enter; `:clearSelection` Escape; `:close` x (stops the selected agent or workflow, or dismisses a finished row); `footer:dismiss` unbound, no effect |
| `AbovePrompt` band | `abovePrompt:toggle` Ctrl+X Ctrl+A; `:focus` Ctrl+X Tab; `:next` Tab; `:previous` Shift+Tab; `:press` Enter; `:leave` Escape; `:highlightNext` Down; `:highlightPrevious` Up (Right/Left/Space also work in `AbovePrompt`) |
| `Pane` | `pane:scrollUp` Up; `:scrollDown` Down; `:pageUp`; `:pageDown`; `:top` Home; `:bottom` End; `:grow` Ctrl+X Left/Up; `:shrink` Ctrl+X Right/Down; `:close` Ctrl+X X (also in `PaneField`); `pane:next`, `pane:previous` unbound (Global, when more than one pane is open) |
| `Agents` (v2.1.257+) | `agents:switchView` Ctrl+S; `:togglePin` Ctrl+T; `:find` Ctrl+F (v2.1.288+); `:rename` Ctrl+R (v2.1.288+); `:previousGroup` Ctrl+Up, Meta+Up (v2.1.288+); `:nextGroup` Ctrl+Down, Meta+Down (v2.1.288+) |
| `Scroll` (fullscreen) | `scroll:lineUp` wheelup; `:lineDown` wheeldown; `:pageUp` PageUp; `:pageDown` PageDown; `:top` Ctrl+Home; `:bottom` Ctrl+End; `:halfPageUp`, `:halfPageDown`, `:fullPageUp`, `:fullPageDown` unbound; `selection:copy` Ctrl+Shift+C / Cmd+C; `selection:clear` unbound (v2.1.234+); `selection:extendLeft/Right/Up/Down` Shift+arrows; `selection:extendLineStart` Shift+Home; `selection:extendLineEnd` Shift+End |

# Limits and defaults

- In agent view (`claude agents`) an `Agents` binding takes precedence over `Chat` or `Global` on the same key (Ctrl+S switches grouping, not `chat:stash`). Bindings fire on single keystrokes there, so the `Ctrl+X Ctrl+E` chord does not open the editor; `chat:externalEditor` single-key bindings (Ctrl+G) do.
- Footer: while an item is selected, Enter opens it even if `Chat` Enter is rebound to `chat:queueSubmit` or `chat:newline`; other `Chat` bindings such as `Shift+Tab` keep working.
- `footer:dismiss` and the Backspace/Delete default were removed in v2.1.281.
