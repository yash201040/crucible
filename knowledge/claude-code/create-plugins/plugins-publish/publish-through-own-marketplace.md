---
type: "Guide"
title: "Publish through your own marketplace"
description: "Add a .claude-plugin/marketplace.json with a source of ./ and tell users the add and install commands, with version requirements for one-command forms."
resource: "https://code.claude.com/docs/en/plugins/publish"
tags: [plugins, marketplace, install, updates]
kind: "file"
maturity: "unlabelled"
since: "2.1.275"
surfaces: [cli]
requires: ""
identifiers:
  - ".claude-plugin/marketplace.json"
  - "claude plugin marketplace add"
  - "claude plugin install"
  - "/plugin install <name> --marketplace <source>"
  - "claude plugin install <name> --marketplace <source>"
  - "claude plugin update <name>@<marketplace>"
  - "claude plugin validate ."
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-publish"
    resource: "https://code.claude.com/docs/en/plugins/publish"
    title: "Publish and distribute a plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A marketplace is a `.claude-plugin/marketplace.json` listing your plugin, added to a git repository (the plugin's own or a separate one). Once in the repo the plugin is published; no submission form. Minimal file: `name`, `owner: { name }`, `plugins: [{ "name": "deploy-helper", "source": "./" }]`; entry `name` must match `plugin.json`. Pick a marketplace name other authors are unlikely to use: a user cannot have two marketplaces with the same name. Run `claude plugin validate .` before pushing.

# How to use it

Access follows the repo: anyone who can clone it can install, so a private repo means a private marketplace.

| Step | Command |
| :- | :- |
| Add once | `claude plugin marketplace add your-org/your-marketplace` (GitHub `owner/repo`, URL or path) |
| Install | `claude plugin install deploy-helper@your-marketplace` |
| Add and install in a session | `/plugin install deploy-helper --marketplace your-org/your-marketplace` (v2.1.275 or later) |
| Add and install from shell | `claude plugin install deploy-helper --marketplace your-org/your-marketplace` (v2.1.292 or later) |

# Limits and defaults

Updates: `claude plugin update deploy-helper@your-marketplace` refreshes the marketplace and installs when the version changed. Auto-update is off by default for your marketplace; when on it does the same on a delay after session start.
