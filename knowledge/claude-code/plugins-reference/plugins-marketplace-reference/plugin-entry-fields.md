---
type: "Reference"
title: "Plugin entry fields"
description: "Fields of an item in the marketplace plugins array, including strict, engines, defaultEnabled, headers and headersHelper."
resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
tags: [marketplace, plugin-entry, fields, engines]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "plugins[].name"
  - "source"
  - "strict"
  - "category"
  - "tags"
  - "relevance"
  - "dependencies"
  - "engines"
  - "engines.claude-code"
  - "defaultEnabled"
  - "displayName"
  - "metadata"
  - "headers"
  - "headersHelper"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-marketplace-reference"
    resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
    title: "Marketplace reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each object in `plugins` names a plugin and where to fetch it. `name` and `source` are required. An entry also accepts every `plugin.json` field (such as `description`, `version`, `author`, `commands`, `hooks`) besides the directory listing fields.

# How to use it

| Field | Type | What it does |
| :- | :- | :- |
| `name` | string | Plugin id (letters, digits, `.`, `_`, `-`; starts with letter or digit). Users type it before `@`, even if `plugin.json` sets a different `name` |
| `source` | string or object | Where to fetch the plugin; see [plugin source types](./plugin-source-types.md) |
| `description` | string | Shown in `/plugin` listings |
| `version` | string | When `plugin.json` also sets `version`, `plugin.json` wins and validate warns |
| `category` | string | Free-form catalog category |
| `tags` | array of strings | Free-form search tags |
| `strict` | boolean | Default `true`; see [strict mode](./entry-vs-plugin-json-and-strict.md) |
| `relevance` | object | Signals for when to suggest the plugin |
| `dependencies` | array | Plugins that must be enabled; each item `"name"`, `"name@marketplace"` or an object |
| `engines` | object | Claude Code versions the plugin works on, as a semver range under `claude-code`, e.g. `"engines": { "claude-code": ">=2.1.400" }`. Needs v2.1.323 or later |
| `defaultEnabled` | boolean | Default `true`; whether the plugin starts enabled when the user has not set it in `enabledPlugins`. Entry value beats `plugin.json` |
| `displayName` | string | UI name; falls back to `name` |
| `metadata` | object | Free-form; Claude Code does not read it |
| `headers` | object | HTTP headers sent when downloading this entry's archive; replaces a same-named header from the marketplace source's `headers`. Needs v2.1.238 or later |
| `headersHelper` | string | Command printing the entry's archive-download headers as one JSON object, for expiring credentials. Entry must also set `"strict": false`. Needs v2.1.238 or later |

# Limits and defaults

- To keep a marketplace working on Claude Code v2.0.15 through v2.1.75, omit `engines` from every entry: those versions reject the whole `marketplace.json` when any entry has it.
