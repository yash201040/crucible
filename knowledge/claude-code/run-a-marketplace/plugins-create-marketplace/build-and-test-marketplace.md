---
type: "Guide"
title: "Build and test a local marketplace"
description: "Create a .claude-plugin/marketplace.json, validate it, register it, install a plugin and confirm it loaded."
resource: "https://code.claude.com/docs/en/plugins/create-marketplace"
tags: [plugins, marketplace, validate, local-testing]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - ".claude-plugin/marketplace.json"
  - "claude plugin validate"
  - "claude plugin marketplace add"
  - "claude plugin marketplace remove"
  - "claude plugin install"
  - "claude plugin list"
  - "claude plugin details"
  - "/plugin marketplace add"
  - "/reload-plugins"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-create-marketplace"
    resource: "https://code.claude.com/docs/en/plugins/create-marketplace"
    title: "Create a marketplace"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A marketplace is a directory or repository with `.claude-plugin/marketplace.json` listing plugins and where to fetch each. Push it to a git host and others register it with one command. It can be private, list any number of plugins, and an admin can require it on every machine.

# How to use it

1. `mkdir -p my-marketplace/.claude-plugin my-marketplace/plugins`, copy the plugin under `plugins/`, and check it with `claude plugin validate ./my-marketplace/plugins/my-first-plugin`.
2. Write `.claude-plugin/marketplace.json` with required `name`, `owner` (object with `name`) and `plugins` array; optional `description`. Each plugin entry needs `name` and `source` (path from the marketplace root, e.g. `"./plugins/my-first-plugin"`).
3. `claude plugin validate ./my-marketplace`; ends with `Validation passed`.
4. `claude plugin marketplace add ./my-marketplace` (recorded in user settings), then `claude plugin install my-first-plugin@my-marketplace` (install id is entry name `@` marketplace name). In-session equivalents: `/plugin marketplace add`, `/plugin install`.
5. `claude plugin list` shows `Status: ✔ enabled`; `claude plugin details <plugin>` shows the component inventory. Plugin skills are prefixed with the plugin name (`/my-first-plugin:hello`).

Test edits: for a local-directory marketplace with relative-path sources, files are read directly, and edits apply at next session start or `/reload-plugins` without a version change. Hosted installs use a cached copy. Start over with `claude plugin marketplace remove my-marketplace` (also uninstalls its plugins).

# Notes

Before pushing, choose a distinctive top-level `name`: a user cannot have two marketplaces with the same name. Users add a GitHub one with `claude plugin marketplace add <owner>/<repo>`. Sharing one plugin with few people or offering to everyone are covered by the publish page.
