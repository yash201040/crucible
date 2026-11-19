---
type: "Reference"
title: "marketplace.json top-level fields"
description: "Every top-level key Claude Code reads from marketplace.json, with types and version requirements."
resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
tags: [marketplace, marketplace-json, fields, reference]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "name"
  - "owner"
  - "plugins"
  - "$schema"
  - "description"
  - "version"
  - "metadata.description"
  - "metadata.version"
  - "metadata.pluginRoot"
  - "forceRemoveDeletedPlugins"
  - "allowCrossMarketplaceDependenciesOn"
  - "renames"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-marketplace-reference"
    resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
    title: "Marketplace reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The keys Claude Code reads from `marketplace.json`. `name`, `owner` and `plugins` are required.

# How to use it

| Field | Type | What it does |
| :- | :- | :- |
| `name` | string | Marketplace id: letters, digits, `.`, `_`, `-`, starts with letter or digit, no `..`. Users type it after `@` (`my-plugin@my-marketplace`). `claude plugin validate` fails other names |
| `owner` | object | `name` required; `email` and `url` optional |
| `plugins` | array | Plugin entries; each validated on its own, so one invalid entry does not fail the marketplace |
| `$schema` | string | JSON Schema URL for editors; ignored at load |
| `description` | string | Shown to users; validate warns if missing |
| `version` | string | Marketplace manifest version |
| `metadata.description`, `metadata.version` | string | Alternate location for `description` and `version` |
| `metadata.pluginRoot` | string | Directory that bare plugin source names resolve under. Needs v2.1.239 or later |
| `forceRemoveDeletedPlugins` | boolean | When `true`, a plugin removed from `plugins` is uninstalled on users' machines |
| `allowCrossMarketplaceDependenciesOn` | array of strings | Marketplace names whose plugins may be installed as dependencies of this marketplace's plugins. Only the list in the installed plugin's own marketplace applies, for its whole dependency chain |
| `renames` | object | Map from a former plugin name to its current name, or `null` for a removed plugin |

# Notes

See [plugin entry fields](./plugin-entry-fields.md) for the items of `plugins`.
