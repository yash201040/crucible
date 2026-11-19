---
type: "Guide"
title: "Bundle plugins for a team"
description: "A plugin with only a name and a dependencies array installs a curated plugin set with one command."
resource: "https://code.claude.com/docs/en/plugins/dependencies"
tags: [plugins, bundles, dependencies, enterprise]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "dependencies"
  - "claude plugin install"
  - "claude plugin update"
  - "enabledPlugins"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-dependencies"
    resource: "https://code.claude.com/docs/en/plugins/dependencies"
    title: "Plugin dependencies"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Publish a plugin whose manifest holds a `name` and `dependencies` array (only `name` is required in a manifest); installing it installs every dependency. Example: `backend-standard` depending on `secrets-vault`, `deploy-kit`, `{ "name": "db-migrate", "version": "^3.0" }`, `oncall-runbook`.

# How to use it

To add a plugin to the set, publish a new bundle version. If the marketplace does not auto-update by default, engineers turn on auto-update for it, or run `claude plugin update backend-standard` then `/reload-plugins` in an open session to install the newly added dependencies. To deploy a bundle org-wide an administrator adds it to `enabledPlugins` in managed settings.
