---
type: "Reference"
title: "Drawing in the VS Code extension"
description: "How mod drawing behaves in the VS Code chat panel: versions, pane docking, focus rules, labels and text limits."
resource: "https://code.claude.com/docs/en/plugins/mods/interface"
tags: [mods, vscode, panel, surface]
kind: "ui"
maturity: "unlabelled"
since: "2.1.299"
surfaces: [ide]
requires: "VS Code extension 2.1.299 or later (2.1.304 for sessions that do not fetch feature flags, such as Amazon Bedrock)"
identifiers:
  - "e.surface === 'vscode'"
  - "e.props.placement"
  - "e.viewport.isFullscreen"
  - "$.prompt.suggest"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-interface"
    resource: "https://code.claude.com/docs/en/plugins/mods/interface"
    title: "Draw in the interface with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

What a mod draws appears in the VS Code chat panel; `e.surface` is `vscode`.

# Limits and defaults

- Panes: in a panel 800 px or wider they dock beside the conversation (`e.props.placement` `'dock'`, `e.viewport.isFullscreen` true); narrower they draw above the prompt box (`'inline'`), 12 rows before scrolling.
- Toasts and status lines sit in one stack above the prompt box (with panes when narrow), one status line per mod; hidden during a permission request or dialog.
- The panel frames mod output with a label such as "From the token-chart plugin" or "Edited by the token-chart plugin".
- Buttons have no hotkeys: click, or Enter once focused.
- `focus: true` is granted only when the panel has focus, Claude is idle with no question waiting, and the prompt box is empty.
- `AskUserQuestion`: the panel keeps its own question card and draws your elements above it; props passed to `next` do not change the card.
- `$.prompt.suggest` resolves with `isShown: false` and shows nothing.
- A status line is cut at 200 characters or two rows; a toast at 500 characters.
