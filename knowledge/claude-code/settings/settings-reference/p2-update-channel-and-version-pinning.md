---
type: "Reference"
title: "Update channel and version pinning settings"
description: "Settings that choose the auto-update channel and set minimum or maximum Claude Code versions."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, updates, versioning, managed]
kind: "setting"
maturity: "unlabelled"
since: "2.1.163"
surfaces: [cli]
requires: ""
identifiers:
  - "autoUpdatesChannel"
  - "minimumVersion"
  - "requiredMinimumVersion"
  - "requiredMaximumVersion"
  - "DISABLE_AUTOUPDATER"
  - "claude update"
  - "claude install"
  - "claude doctor"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Keys for update behavior and version bounds.

# How to use it

| Name | Scope | Type / default | What it does |
| :- | :- | :- | :- |
| `autoUpdatesChannel` | any file | `"latest"` or `"stable"`; unset follows `"latest"` | `stable` is typically about one week old and skips releases with major regressions. `/config` Auto-update channel writes `"stable"` and removes the key for latest; `claude install stable`/`latest` also save it. Switching latest to stable in `/config` asks about a downgrade; staying sets `minimumVersion`. Homebrew ignores it (cask `claude-code` tracks stable, `claude-code@latest` tracks latest; `claude update` defers to `brew upgrade`). Turn auto-updates off with `DISABLE_AUTOUPDATER` in `env` |
| `minimumVersion` | any file (managed to pin) | version string such as `"2.1.323"`; invalid ignored | Background updates and `claude update` never install below it; constrains updates only. Cleared when switching back to latest |
| `requiredMinimumVersion` | managed; ignored silently elsewhere. Needs v2.1.163+ | version string | Claude Code exits at startup if older (startup check only; running sessions continue). `claude update`, `claude install`, `claude doctor` still work |
| `requiredMaximumVersion` | managed; needs v2.1.163+ | version string | Exits at startup if newer; on native and npm installs auto-update and `claude update` skip versions above it. Desktop app's bundled Claude Code can exceed it, and then Code tab local sessions do not start; turn off desktop auto-updates on macOS and Windows (Microsoft Store still updates its install) |

# Notes

Pair `requiredMinimumVersion` and `requiredMaximumVersion` to enforce a range.
