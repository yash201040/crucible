---
type: "Reference"
title: "Vim editor mode"
description: "Vim-style editing in the prompt: modes, motions, operators, text objects, visual mode and INSERT remaps."
resource: "https://code.claude.com/docs/en/interactive-mode"
tags: [vim, editor, keyboard, settings]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "editorMode"
  - "vimInsertModeRemaps"
  - "Ctrl+["
  - "gg"
  - "dd"
  - "%"
  - "d0"
  - "d%"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "interactive-mode"
    resource: "https://code.claude.com/docs/en/interactive-mode"
    title: "Interactive mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Optional vim keybindings in the prompt box. Enable through `/config` then Editor mode, or `"editorMode": "vim"` in settings.

# How to use it

- Enter NORMAL with `Esc` or `Ctrl+[` (in Kitty keyboard protocol terminals `Ctrl+[` needs v2.1.242+). Enter INSERT with `i I a A o O`; visual with `v` (character) or `V` (line).
- Motions: `h j k l`, `Space`, `w e b`, `0 $ ^`, `gg`, `G`, `f/F/t/T{char}`, `;` and `,` to repeat, `%` bracket jump (v2.1.301+), `/` opens reverse history search like `Ctrl+R`.
- Edits: `x`, `r{char}`, `dd`, `D`, `dw/de/db`, `df/dt{char}`, `dj/dk`, `dgg/dG`, `cc`, `C`, `cw/ce/cb`, `s`, `S`, `yy/Y`, `yw/ye/yb`, `p/P`, `>>`, `<<`, `J`, `u`, `.`. `d0/c0/y0` need v2.1.281+; `d%/c%/y%` need v2.1.301+.
- Text objects with `d c y`: `iw aw`, `iW aW`, `i" a"`, `i' a'`, `i( a(`, `i[ a[`, `i{ a{`.
- Visual mode: `d/x`, `y`, `c/s`, `p/P`, `r{char}`, `~ u U`, `> <`, `J`, `o`, text objects, `v/V` toggle or exit.

INSERT remap, in `~/.claude/settings.json`:

```json
{ "editorMode": "vim", "vimInsertModeRemaps": { "jj": "<Esc>" } }
```

# Limits and defaults

- Block-wise visual mode (`Ctrl+V`) is not supported.
- `vimInsertModeRemaps` keys are exactly two printable characters, and `"<Esc>"` is the only target; other entries are ignored. The second key must follow within one second.
- The setting is read only from user settings, `--settings` and managed settings; project `.claude/settings.json` and `.claude/settings.local.json` are ignored.
- At the start or end of input in NORMAL mode `j/k` and arrows navigate history; `Left` on an empty prompt opens agent view.
- When typing in the `Other` row of an AskUserQuestion, press `Esc` twice to cancel (single-key cancel is bindable in keybindings).
