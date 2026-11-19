---
type: "Feature"
title: "Plugin update policy and release channels"
description: "Set marketplace auto-update per marketplace or fleet-wide and give user groups stable or early-access marketplaces."
resource: "https://code.claude.com/docs/en/plugins/org"
tags: [plugins, auto-update, release-channels, managed-settings]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Per-group server-managed settings need an Enterprise plan"
identifiers:
  - "autoUpdate"
  - "DISABLE_AUTOUPDATER"
  - "FORCE_AUTOUPDATE_PLUGINS"
  - "env"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-org"
    resource: "https://code.claude.com/docs/en/plugins/org"
    title: "Manage Claude Code plugins for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Plugin auto-update runs in the background after startup for marketplaces that have it on. Admins can fix it per marketplace or for the whole fleet, and can hand different groups different marketplaces.

# How to use it

- Per marketplace: set `"autoUpdate": true` or `false` on a managed `extraKnownMarketplaces` entry. When set, the user's `/plugin` toggle is refused with an error starting `Auto-update for '<name>' is set by`. When unset, the user's toggle persists.
- Whole fleet: managed `env` block `{"env": {"DISABLE_AUTOUPDATER": "1"}}` (also stops Claude Code's own updates). Add `"FORCE_AUTOUPDATE_PLUGINS": "1"` to keep plugin auto-update while stopping Claude Code updates.
- `DISABLE_AUTOUPDATER` does not cover `command`-source plugins; Claude Code re-runs each enabled one's command every session and installs the output if it changed.
- Release channels: host two marketplaces (e.g. `stable-tools`, `latest-tools`) pointing at different refs, then assign per group via separate endpoint-managed settings (file or MDM), one Claude apps gateway policy per group (first matching policy wins; its `extraKnownMarketplaces` map does not merge, so list every marketplace needed), or on Enterprise per-group configuration in the admin console (does not merge with org-wide config).

# Notes

Which marketplaces auto-update by default is in the plugin loading reference.
