---
type: "Feature"
title: "Rename or remove marketplace plugins safely"
description: "Use displayName, a renames map and forceRemoveDeletedPlugins so renames and removals migrate users instead of breaking installs."
resource: "https://code.claude.com/docs/en/plugins/host-marketplace"
tags: [marketplace, renames, removal, migration]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "renames"
  - "forceRemoveDeletedPlugins"
  - "displayName"
  - "enabledPlugins"
  - "pluginConfigs"
  - "claude plugin validate"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-host-marketplace"
    resource: "https://code.claude.com/docs/en/plugins/host-marketplace"
    title: "Host and maintain a marketplace"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A plugin `name` is its identifier used in `enabledPlugins`, `pluginConfigs` and `/plugin install`, so changing it breaks installs. To change only the label in `/plugin`, set `displayName` in `plugin.json`.

# How to use it

Add a top-level `renames` map to `marketplace.json`: former name to current name, or `null` when removed (e.g. `"formatter": "code-formatter"`, `"legacy-linter": null`).
- Renamed: plugin loads under the new name, a one-time notice shows `Renamed to "code-formatter" in the "your-marketplace" marketplace`, and old keys in `enabledPlugins` and `pluginConfigs` are rewritten in user, project and local scopes.
- `null`: old key dropped from those scopes, notice `Removed from the "your-marketplace" marketplace`.
- Managed settings cannot be rewritten, so the notice recurs until an admin updates managed `enabledPlugins`.
- Git/URL marketplaces: a renamed plugin shows `Plugin "<name>" not cached at <path>` until the user runs `/plugin install code-formatter@your-marketplace` once.
- Treat `renames` as append-only; Claude Code follows the chain from the oldest name. `claude plugin validate .` rejects cycles or chains not ending at `null` or a listed plugin (`renames.<name>: chain does not resolve`).

`"forceRemoveDeletedPlugins": true` (top level): at each session start Claude Code treats plugins neither listed nor renamed as removed, uninstalls them from user, project and local scopes (managed-only installs stay), and lists them under Needs attention on the Installed tab. Without it, a removed plugin stays installed and reports `Plugin "<name>" not found in marketplace`.
