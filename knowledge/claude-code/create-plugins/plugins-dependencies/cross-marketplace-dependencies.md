---
type: "Limit"
title: "Cross-marketplace dependency allowlist"
description: "A dependency from another marketplace is installed only if the root marketplace lists it in allowCrossMarketplaceDependenciesOn or it is already enabled."
resource: "https://code.claude.com/docs/en/plugins/dependencies"
tags: [plugins, dependencies, marketplace, security]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "allowCrossMarketplaceDependenciesOn"
  - "marketplace.json"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-dependencies"
    resource: "https://code.claude.com/docs/en/plugins/dependencies"
    title: "Plugin dependencies"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

By default a dependency from a different marketplace than the declaring plugin's is not installed, unless the user already has it installed and enabled at the same scope. This prevents one marketplace silently installing plugins from an unreviewed source.

# How to use it

Add the target marketplace name to `allowCrossMarketplaceDependenciesOn` (array) in the root marketplace's `marketplace.json`. The root marketplace is the one hosting the plugin being installed; only its allowlist applies.

# Limits and defaults

- Missing from the allowlist, with the dependency declared in the marketplace entry: the install is refused with a message beginning `Dependency "audit-logger@your-shared-marketplace" (required by deploy-kit@your-marketplace) is in marketplace "your-shared-marketplace", which is not in the allowlist`.
- Declared in `plugin.json`: the install completes without the dependency and the plugin then fails to load.
- The check does not apply to an already enabled dependency at the same scope.
