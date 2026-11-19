---
type: "Feature"
title: "Marketplace updates, versions and release channels"
description: "How users receive plugin updates, how version strings gate them, pinning, command-source changes and stable/early-access channels."
resource: "https://code.claude.com/docs/en/plugins/host-marketplace"
tags: [plugins, versions, auto-update, release-channels, pinning]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "version"
  - "plugin.json"
  - "ref"
  - "sha"
  - "autoUpdate"
  - "/plugin marketplace update <name>"
  - "claude plugin update <plugin>@<name>"
  - "<plugin>--v<version>"
  - "allowCrossMarketplaceDependenciesOn"
  - "relevance"
  - "pluginSuggestionMarketplaces"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-host-marketplace"
    resource: "https://code.claude.com/docs/en/plugins/host-marketplace"
    title: "Host and maintain a marketplace"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Changes reach users through background auto-update (off by default for your marketplace, and `marketplace.json` has no field to turn it on) or manual update. A user gets a new copy only when the plugin's computed version changes.

# How to use it

- Turn on: users toggle auto-update under Marketplaces in `/plugin`, or an admin sets `"autoUpdate": true` on the managed `extraKnownMarketplaces` entry. Manual: `/plugin marketplace update <name>` or `claude plugin update <plugin>@<name>`.
- Release: change `version` (from `plugin.json` first, then the entry). Either bump on each release (otherwise pushed commits are not received) or omit `version` in both places so users track commits. Setting both makes `plugin.json` win silently; `validate` warns `Entry declares version "<a>" but <path>/plugin.json says "<b>"`. In-place local loads ignore `version`.
- Hold a version: `ref`/`sha` on `github`, `url` or `git-subdir` entries; `#<ref>` on the add command; `<plugin>--v<version>` tags for dependency ranges.
- `command` source: if the command or `mode` changes, background runs stop for the user and an Errors-tab entry shows the new command and the `claude plugin update` to run; the user must accept the new command.
- Release channels: two marketplaces with different `name` values pointing at different refs (e.g. `stable-tools` with `ref: "stable"`, `latest-tools` with `ref: "latest"`). Give refs different `plugin.json` versions or omit `version`, else a moved ref leaves users on the cached copy. Admins can assign channels to groups.
- Dependencies: entries can declare plugin dependencies with semver ranges; cross-marketplace dependencies install only if the marketplace lists the other in `allowCrossMarketplaceDependenciesOn`. A `relevance` block lets Claude Code suggest the plugin (needs `pluginSuggestionMarketplaces`).
