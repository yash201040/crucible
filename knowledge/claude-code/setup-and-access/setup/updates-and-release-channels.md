---
type: "Feature"
title: "Updates, release channels and version pinning"
description: "Auto-update behavior, autoUpdatesChannel, minimumVersion, DISABLE_AUTOUPDATER vs DISABLE_UPDATES and claude update."
resource: "https://code.claude.com/docs/en/setup#update-claude-code"
tags: [updates, release-channel, versions, enterprise]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "autoUpdatesChannel"
  - "minimumVersion"
  - "requiredMinimumVersion"
  - "requiredMaximumVersion"
  - "DISABLE_AUTOUPDATER"
  - "DISABLE_UPDATES"
  - "CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE"
  - "claude update"
  - "claude install"
  - "~/.local/bin/claude"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "setup"
    resource: "https://code.claude.com/docs/en/setup"
    title: "Advanced setup"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Native installs check for updates at startup and periodically, install in the background, and take effect on next start. `claude doctor` shows the last attempt.

# How to use it

| Name | What it does |
| :- | :- |
| `autoUpdatesChannel` | `"latest"` (default) or `"stable"` (about a week old, skips releases with major regressions); also `/config` > Auto-update channel |
| `minimumVersion` | updates and `claude update` refuse versions below it; in managed settings it is an org-wide floor; set it with stable to avoid a downgrade |
| `requiredMinimumVersion`, `requiredMaximumVersion` | managed settings; Claude Code refuses to start outside the range |
| `DISABLE_AUTOUPDATER` (`"1"` in `env`) | stops only the background check; `claude update` and `claude install` still work; `claude doctor` shows `disabled (set by env: DISABLE_AUTOUPDATER)` |
| `DISABLE_UPDATES` | blocks all update paths, including manual; for self-distributed installs |
| `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE` | `1` makes Claude Code run the Homebrew or WinGet upgrade in the background |
| `claude update` | applies an update now; reports `Claude Code is up to date (<version>)` |

# Limits and defaults

- Homebrew casks: `claude-code` = stable, `claude-code@latest` = latest. apt/dnf/apk choose channel by repository. Homebrew, WinGet and package managers do not auto-update by default; apt/dnf/apk always need manual upgrade (elevated privileges).
- A new model can need a version newer than stable serves; move to latest.
- A custom launcher replacing `~/.local/bin/claude` is left alone; versions stay under `~/.local/share/claude/versions/` and all are kept. Remove the launcher and run `claude update` to restore management.
