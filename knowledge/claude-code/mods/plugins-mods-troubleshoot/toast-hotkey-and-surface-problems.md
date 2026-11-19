---
type: "Reference"
title: "Toast, hotkey and surface problems"
description: "Why a toast does not show, the band shows 'plugin panel hidden', hotkeys fail, or a drawing works in terminal but not in Desktop or VS Code."
resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
tags: [mods, toast, hotkeys, vscode]
kind: "ui"
maturity: "unlabelled"
since: "2.1.299"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "$.ui.toast"
  - "holdToasts"
  - "timeoutMs"
  - "gave way, cut short"
  - "gave way, unseen"
  - "left the stack, never drawn"
  - "within 2000ms of the last; dropped"
  - "plugin panel hidden"
  - "hotkey"
  - "focus: true"
  - "e.surface"
  - "Ctrl+X then Ctrl+A"
  - "Ctrl+X then Tab"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-troubleshoot"
    resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
    title: "Troubleshoot a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Interface problems for toasts, the collapsible band, keyboard focus and surface support.

# How to use it

**A toast does not appear** (interactive terminal). Confirm in the debug log with a line like `$.ui.toast (first-mod): build finished`, then check:
- No line: a refusal line such as `first-mod: $.ui.toast dropped: timeoutMs is a whole number of ms, 1 to 60000`.
- A pane holds toasts: `holdToasts` was passed when it opened; close the pane or remove `holdToasts`.
- Classic renderer: the toast is one line under the prompt starting with the mod's name; a newer toast from your mod can replace one showing or waiting (log ends `gave way, cut short` or `gave way, unseen`).
- Fullscreen: at most three toasts are drawn at once; one can run out of time (log ends `left the stack, never drawn`). Combine messages into one toast.
- Before v2.1.290 a toast raised within two seconds of the last one for your mod was dropped (`within 2000ms of the last; dropped`).

**Band shows `plugin panel hidden`**: the band is collapsed (Ctrl+X then Ctrl+A, or your bound keys; in fullscreen click `[-]` on its first row). It stays collapsed until expanded or Claude Code restarts, and no hotkey or `action` binding presses a button in it. Expand with the keys the row names or click the row.

**Hotkeys do nothing**: no keyboard focus (press Ctrl+X then Tab, or click in fullscreen; open with `focus: true` from a command), button in a collapsed band, another mod's row uses the same hotkey (change `hotkey`), or the VS Code extension where buttons have no hotkeys (click, or Enter once focused).

**Works in terminal, not Desktop or VS Code**: the app may not draw the site or element (see render sites and elements tables; check `e.surface` and return a drawable tree); VS Code extension older than 2.1.299 draws nothing for mods in the chat panel; extension older than 2.1.304 with a session that does not fetch feature flags (sessions on Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry skip the fetch; also a Claude apps gateway session) needs an update or `claude` in the integrated terminal. The mod's other hooks still run.
