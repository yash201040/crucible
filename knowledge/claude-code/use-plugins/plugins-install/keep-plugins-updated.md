---
type: "Feature"
title: "Plugin auto-update and manual update"
description: "Auto-update defaults per marketplace kind, manual update paths, and marketplace listing refresh."
resource: "https://code.claude.com/docs/en/plugins/install"
tags: [plugins, auto-update, marketplace, updates]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin update"
  - "claude plugin marketplace update"
  - "claude plugin marketplace remove"
  - "/plugin marketplace update"
  - "/plugin marketplace remove"
  - "/plugin marketplace list"
  - "/reload-plugins"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-install"
    resource: "https://code.claude.com/docs/en/plugins/install"
    title: "Install and manage plugins"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

After a session starts, Claude Code refreshes marketplaces that have auto-update on and updates the on-disk copies of plugins installed from them. On `Plugin updated: <name> · Run /reload-plugins to apply`, run `/reload-plugins`; new versions load at next launch either way.

# How to use it

| Marketplace | Auto-update default |
| :- | :- |
| `claude-plugins-official` and other official names except `knowledge-work-plugins` and `first-party-plugins`, plus marketplaces added from claude.ai | On |
| Every other (community, third-party, local development) | Off |

- Toggle per marketplace on the **Marketplaces** tab of `/plugin`.
- Update one plugin: **Update now** on the **Installed** tab or `claude plugin update <plugin>@<marketplace>`. There is no command updating every plugin at once.
- **Update marketplace** (Marketplaces tab) refreshes the listing and updates plugins installed from it, reporting any left for you. Plugins with a `command` source or with an entry `headersHelper` are not updated this way.
- `claude plugin marketplace update` with no name refreshes every listing but leaves installed plugins at their versions.

| Action | Shell | Session |
| :- | :- | :- |
| List | `claude plugin marketplace list` | `/plugin marketplace list` |
| Update listing | `claude plugin marketplace update <name>` | `/plugin marketplace update <name>` |
| Remove | `claude plugin marketplace remove <name>` | `/plugin marketplace remove <name>` |

# Notes

Removing a marketplace uninstalls every plugin installed from it and removes their `enabledPlugins` entries. Auto-update timing, skips and the environment variables that turn it off are on the plugin loading page; private-marketplace auto-update credentials are on the host-marketplace page.
