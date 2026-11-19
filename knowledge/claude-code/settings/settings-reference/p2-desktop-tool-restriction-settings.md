---
type: "Reference"
title: "Desktop tool restriction settings"
description: "Managed keys that stop Claude's tools in the desktop app's Browser pane and iOS Simulator pane."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, desktop, browser, managed]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [desktop]
requires: "Claude Desktop"
identifiers:
  - "browserExternalPageTools"
  - "disableBrowserExternalNavigation"
  - "disableMobileSimulatorTools"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Managed-scope keys for the desktop app only; the terminal CLI ignores them.

# How to use it

| Name | Values | What it does |
| :- | :- | :- |
| `browserExternalPageTools` | `"disabled"` (desktop also accepts `"disable"`, either case) | Claude's tools cannot read or act on external pages in the Browser pane; people can still browse and local dev previews work. Other values leave tools on; a non-empty unrecognized string logs a warning |
| `disableBrowserExternalNavigation` | Boolean, only `true` takes effect | Turns off external browsing for people and Claude; localhost previews work; HTML previews in SSH and WSL sessions open but run no scripts. If the machine receives no other managed settings also set `parentSettingsBehavior` to `"merge"`; on Windows a managed file removes WSL sessions until allowed |
| `disableMobileSimulatorTools` | Boolean, only `true` takes effect | Blocks Claude's tools for the iOS Simulator pane; manual use stays; nobody can re-enable from inside the app. Unset: tools follow each person's settings toggle |

# Notes

Non-Boolean values such as `"true"` or `1` for the Boolean keys log a warning and are ignored. Default for all: unset.
