---
type: "Reference"
title: "Band, pane and ui.render problems"
description: "Causes for a missing band row, empty pane, refused ui.render, key errors and render exceptions, with the log lines to search."
resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
tags: [mods, ui, render, band]
kind: "ui"
maturity: "unlabelled"
since: "2.1.323"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "ui.render hook skipped"
  - "does not validate"
  - "past the limits of the band"
  - "a hook returned a tree that does not validate"
  - "ui.render (<site>) refused:"
  - "ui.render (<site>): the chain settled on a tree that does not validate"
  - "hooks: ui.render (AbovePrompt) refused: a row past the limits of the band; nothing was drawn"
  - "<Input> needs a key"
  - "<Select> needs a key"
  - "<Button> needs a key"
  - "is drawn twice; each takes its own key"
  - "key each once"
  - "threw while drawn"
  - "the engine drew its own"
  - "the module failed without a message"
  - "Claude Code exited after an unrecoverable interface error"
  - "isPlaced"
  - "$.ui.open"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-troubleshoot"
    resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
    title: "Troubleshoot a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Problems where the mod loaded but its pane or band does not draw or respond.

# How to use it

- **Another mod's band shows and yours does not** (each mod above the prompt gets its own row): check for a tree that does not validate (search debug log for `ui.render hook skipped` or `does not validate`), rows together exceeding limits (search `past the limits of the band`; rows share one tree's limits), or another mod hiding your row (turn other mods off one at a time). Before v2.1.323 all mods shared one band drawing, and an earlier mod replaced yours if its tree lacked the `await next(e)` result; keep it among a `Box`'s children and give no `Box` a `width`, `height`, `minWidth`, `minHeight`, `position`, `top`, `left`, `right`, `bottom`, `display` or `overflow` prop.
- **Pane or band empty or shows usual content**: the tree did not validate; a `hook skipped` line names the reason, e.g. `first-mod: ui.render hook skipped: returned the wrong shape (a tree Pane refuses: Box prop "flexDirection" must be one of row, column, row-reverse, column-reverse)`. If cut short, search the debug log for `a hook returned a tree that does not validate`.
- **`ui.render (<site>) refused:`** or `ui.render (<site>): the chain settled on a tree that does not validate`: the tree at that site exceeds a size limit; make the mods' trees smaller. If the transcript line starts with `hooks`, several mods draw at that site. For AbovePrompt rows the line reads `hooks: ui.render (AbovePrompt) refused: a row past the limits of the band; nothing was drawn`, though rows that fit still draw. Before v2.1.307 a `refused:` line covered any invalid tree and for `Pane` and `AbovePrompt` ended `; the engine drew its own`.
- **Key errors**: `<Input> needs a key` / `<Select> needs a key` / `<Button> needs a key` (key missing, empty or not a string, e.g. `key: 3`); `is drawn twice; each takes its own key` (duplicate key); `key each once` from `press` in a test (several buttons with that key; buttons with the same label and no `key` share the label as key).
- **`threw while drawn:`**: e.g. `first-mod: ui.render (ToolUse) threw while drawn: <error>; the engine drew its own`; the site shows usual content. Before v2.1.289 this in a transcript row ended the session with `Claude Code exited after an unrecoverable interface error`.
- **`the module failed without a message`**: a `Client` threw an error with no message (e.g. `throw new Error()`), shown as `my-mod: Client client/spinner.js: the module failed without a message`. Before v2.1.289 it showed `Error`.
- **`$.ui.open` runs and no pane appears**: the call did not come from a user action and the terminal is narrower than the pane needs; open from a command or button, or check the `isPlaced` result.

# Notes

See [toasts, hotkeys and app support](./toast-hotkey-and-surface-problems.md).
