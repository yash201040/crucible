---
type: "Reference"
title: "Deep link handler registration and platforms"
description: "When and where Claude Code registers the claude-cli:// handler, terminal selection per OS, disableDeepLinkRegistration, VS Code and Desktop links."
resource: "https://code.claude.com/docs/en/deep-links"
tags: [deep-links, registration, platforms, settings]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide, desktop]
requires: ""
identifiers:
  - "disableDeepLinkRegistration"
  - "~/Applications/Claude Code URL Handler.app"
  - "claude-code-url-handler.desktop"
  - "HKEY_CURRENT_USER\\Software\\Classes\\claude-cli"
  - "$XDG_DATA_HOME/applications"
  - "$TERMINAL"
  - "x-terminal-emulator"
  - "claude agents"
  - "vscode://anthropic.claude-code/open"
  - "claude://"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "deep-links"
    resource: "https://code.claude.com/docs/en/deep-links"
    title: "Launch sessions from links"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code registers the handler on macOS, Linux and Windows when you either send anything to an interactive `claude` session (a message or `/help`; starting and sending nothing does not register) or start Claude Code in agent view (such as `claude agents`) in a trusted folder. No install command; user-level locations only.

# How to use it

| Platform | Handler location |
| --- | --- |
| macOS | `~/Applications/Claude Code URL Handler.app` |
| Linux | `claude-code-url-handler.desktop` under `$XDG_DATA_HOME/applications` (default `~/.local/share/applications`) |
| Windows | `HKEY_CURRENT_USER\Software\Classes\claude-cli` |

Terminal choice: macOS reuses the terminal of your most recent interactive session (iTerm2, Ghostty, kitty, Alacritty, WezTerm, Terminal.app). Linux honors `$TERMINAL`, then `x-terminal-emulator`, then common emulators. Windows prefers Windows Terminal, then PowerShell, then `cmd.exe` (order fixed).

Prevent registration: set `disableDeepLinkRegistration` to `"disable"` in `settings.json`; set it in managed settings to enforce it. It covers `claude-cli://` only.

# Notes

- VS Code extension has its own handler `vscode://anthropic.claude-code/open` that opens an editor tab. Claude Desktop handles its own `claude://` links (SSH sessions).
- Troubleshooting: link does nothing means handler not registered (send a prompt in an interactive session, exit, retry); Linux without a desktop environment may have nothing for `xdg-open` to dispatch to; session in home means the `repo` clone was not seen.
