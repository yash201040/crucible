---
type: "Feature"
title: "allowManagedHooksOnly"
description: "Managed-scope switch that restricts hook execution to managed, SDK and force-enabled plugin hooks."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, hooks, managed, policy]
kind: "setting"
maturity: "unlabelled"
since: "2.1.310"
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "allowManagedHooksOnly"
  - "allowManagedModsOnly"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Managed-scope Boolean (default unset, so hooks from every scope and plugin run). When `true`, only approved hooks load.

# How to use it

`{ "allowManagedHooksOnly": true }` in managed settings.

What runs or is blocked when `true`:

- Run: hooks in managed settings; Agent SDK in-process hooks; hooks of plugins force-enabled in managed `enabledPlugins` (matched on full `plugin@marketplace` id).
- Mods in a force-enabled plugin load only when they count as the organization's. Built-in mods keep running; to block only users' mods use `allowManagedModsOnly`.
- Blocked: user, project and local hooks, hooks and mods from other plugins, hooks in agent frontmatter, and monitors from other plugins (needs v2.1.310+).
- Command-sourced plugins are disabled, including force-enabled ones, unless `disableCommandPluginSources` is explicitly `false`.
- Marketplace `headersHelper` commands are blocked under the same condition, except for a marketplace managed settings declare (needs v2.1.238+).
- `statusLine` and `fileSuggestion` are read from managed settings only.

# Limits and defaults

The `/goal` command cannot run while this key is set, because it depends on hooks.
