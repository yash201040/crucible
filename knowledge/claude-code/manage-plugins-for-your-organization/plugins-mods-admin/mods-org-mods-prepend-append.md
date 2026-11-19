---
type: "Feature"
title: "Install organization mods and set order"
description: "Make a mod count as the organization's with enabledPlugins, extraKnownMarketplaces and prependPlugins or appendPlugins."
resource: "https://code.claude.com/docs/en/plugins/mods/admin"
tags: [mods, prependplugins, appendplugins, marketplace, managed-settings]
kind: "setting"
maturity: "unlabelled"
since: "2.1.324"
surfaces: [cli]
requires: "managed settings; Claude Code v2.1.324 or later for remote-marketplace org mods"
identifiers:
  - "enabledPlugins"
  - "extraKnownMarketplaces"
  - "prependPlugins"
  - "appendPlugins"
  - "strictKnownMarketplaces"
  - "tier prepend"
  - "tier user"
  - ".claude-plugin/marketplace.json"
  - ".claude-plugin/plugin.json"
  - "hooks/hooks.json"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-admin"
    resource: "https://code.claude.com/docs/en/plugins/mods/admin"
    title: "Manage mods for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

A mod counts as the organization's (runs before user mods, is not refused by `allowManagedModsOnly`) when, in managed settings, its plugin is `true` in `enabledPlugins`, its marketplace is declared in `extraKnownMarketplaces` (pin marketplace and entry to control code changes), and its id (`name@marketplace`, e.g. `acme-guard@acme-tools`) is in `prependPlugins` or `appendPlugins` (v2.1.324+ for remote marketplaces). A mod in a local directory counts only when managed `enabledPlugins` is true, managed settings name the marketplace as an absolute directory path (an `extraKnownMarketplaces` entry with `"source": {"source": "directory", "path": ...}`), and the marketplace lists the plugin by relative path so it loads in place. Copy the directory to every machine and make it admin-writable only; the admin console can carry the keys but cannot place the directory.

Example:

```json
{ "extraKnownMarketplaces": { "acme-tools": { "source": { "source": "directory", "path": "/opt/acme/claude-plugins" } } },
  "enabledPlugins": { "acme-guard@acme-tools": true },
  "prependPlugins": ["acme-guard@acme-tools", "sec-default@builtin"] }
```

- `prependPlugins`: your mod sees an event before any user mod and the result after them; it can change, refuse, or skip user mods.
- `appendPlugins`: runs after every user mod; sees only events they pass on.

# Limits and defaults

- The list replaces the default: name `sec-default@builtin` in `prependPlugins` to keep the guard (it needs no `enabledPlugins` entry).
- A plugin not meeting the conditions counts as a user's: `prependPlugins`/`appendPlugins` skip it (debug line `prependPlugins names ..., which is not an enabled managed plugin with a hooks module; skipped`), `allowManagedModsOnly` refuses it, `allowManagedHooksOnly` keeps it from loading.
- Repository settings cannot set either list. User settings in `~/.claude/settings.json` can order the user's own mods only on a machine with no managed settings or `managed-mcp.json` and a non-Team/Enterprise `/login` credential.
- Verify with `claude --debug`: `hooks module acme-guard@acme-tools loaded` with `tier prepend`; `tier user` means treated as a user's mod.
- Plugin controls (strictKnownMarketplaces, update policy, audit, CI seeding) apply to mods as plugins; a mod copied from a GitHub, git, URL or npm source counts as a user's unless installed as the org's.
