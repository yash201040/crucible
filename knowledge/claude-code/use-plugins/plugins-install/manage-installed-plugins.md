---
type: "Guide"
title: "Manage installed plugins"
description: "The Installed tab, uninstalling project-enabled plugins, dependencies behavior, synced plugins and unused-plugin detection."
resource: "https://code.claude.com/docs/en/plugins/install"
tags: [plugins, manage, dependencies, synced]
kind: "ui"
maturity: "unlabelled"
since: "2.1.273"
surfaces: [cli]
requires: ""
identifiers:
  - "/plugin enable"
  - "/plugin disable"
  - "/plugin uninstall"
  - "<name>@synced"
  - "claude plugin details"
  - "claude plugin prune"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-install"
    resource: "https://code.claude.com/docs/en/plugins/install"
    title: "Install and manage plugins"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The **Installed** tab in `/plugin` (reach it with Tab, or via `/plugin enable`, `/plugin disable`, `/plugin uninstall`) lists plugins with enable, disable, update and uninstall actions.

# How to use it

- List keys: type to filter, Space to enable or disable, `f` to favorite, Enter for details. Disabled plugins sit under a collapsed header. A **Managed** scope (installed through managed settings) cannot be changed here.
- Details menu: **Disable plugin** / **Enable plugin**, **Update now**, **Uninstall**; **Configure options** appears for manifest `userConfig` options; **Configure** for a bundled MCP server's own `user_config`.
- Closing the panel with pending changes runs `/reload-plugins`; if that would invalidate the prompt cache it warns and leaves changes pending (`/reload-plugins --force` applies anyway).
- **Uninstalling a project-enabled plugin** asks: **y** (Disable for me: writes `false` in `.claude/settings.local.json`) or **u** (Uninstall for everyone: removes it from `.claude/settings.json`).
- **Synced plugins** (source `synced`, shown as `<name>@synced`; terminal sessions on v2.1.273 or later): enable or disable on the **Installed** tab unless the organization requires it; remove by turning it off on claude.ai. Changes show `Plugins changed. Run /reload-plugins to activate.`
- **Cost**: `claude plugin details <name>` shows the `Always-on` token count per session and per-component rows. **Not used recently** header flags unused plugins.
- **Dependencies**: install also installs and enables declared dependencies at the same scope; enable also enables installed-but-disabled dependencies (fails if one is not installed); disable is refused when another enabled plugin needs it (a chained command is printed); uninstall leaves auto-installed dependencies until `claude plugin prune`.

# Notes

Plugins you install with `/plugin` or `claude plugin install` stay on the machine and are not added to your claude.ai account. Plugins from claude.ai sync in the background at each start while signed in, and in Cowork sessions at session start.
