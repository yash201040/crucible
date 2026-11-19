---
type: "Reference"
title: "Policy refusal messages for plugins"
description: "User-facing messages when managed settings block marketplaces, plugins, sideload flags, skills-dir or command sources, and the setting behind each."
resource: "https://code.claude.com/docs/en/plugins/troubleshooting"
tags: [plugins, policy, managed-settings, errors, enterprise]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: "Managed settings"
identifiers:
  - "blockedMarketplaces"
  - "strictKnownMarketplaces"
  - "disableSideloadFlags"
  - "disableCommandPluginSources"
  - "allowManagedHooksOnly"
  - "CLAUDE_CODE_PLUGIN_SEED_DIR"
  - "--plugin-dir"
  - "--plugin-url"
  - "--agents"
  - "--mcp-config"
  - "claude plugin init"
  - "claude plugin enable"
  - "skills-dir"
  - "hostPattern"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-troubleshooting"
    resource: "https://code.claude.com/docs/en/plugins/troubleshooting"
    title: "Troubleshoot plugins"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Messages users see when organization policy refuses an action, and the setting responsible.

# How to use it

| Message | Setting behind it |
|---|---|
| `Marketplace source '<source>' is blocked by enterprise policy` | `blockedMarketplaces` or `strictKnownMarketplaces`; `Allowed sources: <list>` means allowlist; `No external marketplaces are allowed.` means empty allowlist; a `Tip:` says `owner/repo` assumes github.com, so use the full URL such as `git@your-git-host.com:owner/repo.git`. Applies on every refresh too |
| `Marketplace "<name>" is not in the allowed marketplace list` / `... is blocked by enterprise policy` (Errors tab) | same policy applied at load; guidance `Contact your administrator to configure allowed marketplace sources` or `This marketplace source is explicitly blocked by your administrator` |
| `Plugin "<name>" is blocked by your organization's policy and cannot be installed` (`cannot be enabled`, or naming its marketplace or a blocked dependency) | managed settings block the plugin, its marketplace or a dependency |
| `--plugin-dir is disabled by your organization's managed settings (disableSideloadFlags)` | `disableSideloadFlags` blocks `--plugin-dir`, `--plugin-url`, `--agents`, `--mcp-config`; exits with `Plugins, custom agents, and MCP servers can only be loaded from sources your administrator has approved.` Related: `--plugin-dir copy of "<name>" ignored: plugin is locked by managed settings` |
| `Plugins from ~/.claude/skills/ are blocked by your organization's managed settings` (`claude plugin init` or `claude plugin enable`) | `skills-dir` missing from `strictKnownMarketplaces` or present in `blockedMarketplaces` |
| `Command-sourced plugins are disabled by your organization's managed settings` | `disableCommandPluginSources` (or `allowManagedHooksOnly` when unset); plugin not installed and command not run |
| `Marketplace '<name>' is seed-managed (<dir>)` | marketplace pre-populated through `CLAUDE_CODE_PLUGIN_SEED_DIR` is read-only; bulk `marketplace update` skips it |
