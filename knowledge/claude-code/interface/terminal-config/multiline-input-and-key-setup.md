---
type: "Guide"
title: "Multiline input, Option key and tmux setup"
description: "How to get newlines (Ctrl+J, backslash-Enter, Shift+Enter), the Option key and tmux working for the Claude Code prompt in each terminal."
resource: "https://code.claude.com/docs/en/terminal-config"
tags: [terminal, shift-enter, tmux, keybindings]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/terminal-setup"
  - "chat:newline"
  - "chat:submit"
  - "terminal.integrated.gpuAcceleration"
  - "terminal.integrated.mouseWheelScrollSensitivity"
  - "terminal.integrated.macOptionIsMeta"
  - "~/.tmux.conf"
  - "allow-passthrough"
  - "CLAUDE_CODE_BS_AS_CTRL_BACKSPACE"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "terminal-config"
    resource: "https://code.claude.com/docs/en/terminal-config"
    title: "Configure your terminal for Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Enter submits. For a line break press Ctrl+J, or type `\` then Enter; both work everywhere. Shift+Enter support depends on the terminal.

# How to use it

| Terminal | Shift+Enter |
| :- | :- |
| Ghostty, Kitty, iTerm2, WezTerm, Warp, Windows Terminal 1.25+ | Works without setup |
| Other kitty-keyboard-protocol terminals (foot, Alacritty 0.16+) | Works; needs Claude Code v2.1.269+ |
| VS Code, Cursor, Devin Desktop, Alacritty before 0.16, Zed | Run `/terminal-setup` once |
| gnome-terminal, Windows Terminal before 1.25, JetBrains IDEs | Not available; use Ctrl+J or `\` Enter |

`/terminal-setup` writes a Shift+Enter binding into the terminal's config; run it in the host terminal, not inside tmux or screen. In VS Code/Cursor/Devin Desktop it also sets `terminal.integrated.gpuAcceleration` to `"off"` and `terminal.integrated.mouseWheelScrollSensitivity`. In Zed it merges into `keymap.json` after making a `.bak` backup, or leaves the file unchanged and prints the block if it cannot read, parse, back up or verify. Remap newline/submit with `chat:newline` and `chat:submit` in the keybindings file.

Option key on macOS (Option+Enter, Option+P): enable "Use Option as Meta Key" in Apple Terminal; set Left/Right Option to "Esc+" in iTerm2; set `"terminal.integrated.macOptionIsMeta": true` in VS Code. `/terminal-setup` in iTerm2 also enables clipboard access for `/copy`.

tmux: add to `~/.tmux.conf` and run `tmux source-file ~/.tmux.conf`:

```
set -g allow-passthrough on
set -g focus-events on
set -s extended-keys on
set -as terminal-features 'xterm*:extkeys'
```

The last two lines are for Shift+Enter (then detach, reattach, restart Claude Code); `allow-passthrough` is for notifications. A mod's `Image` needs `allow-passthrough` and `focus-events`.

# Notes

- On Windows a Backspace arriving as `^H` is read as Ctrl+Backspace (deletes a word) except when `TERM_PROGRAM` is `mintty` or `TERM` is `cygwin`. Set `CLAUDE_CODE_BS_AS_CTRL_BACKSPACE=0` to fix, or `1` for the reverse on macOS/Linux.
