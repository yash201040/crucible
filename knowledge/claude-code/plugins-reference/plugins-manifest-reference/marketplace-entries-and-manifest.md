---
type: "Concept"
title: "Marketplace entries versus plugin.json"
description: "How a marketplace entry and plugin.json combine under strict true/false, and metadata precedence between them."
resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
tags: [plugins, marketplace, strict, precedence]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "strict"
  - "Plugin <name> has conflicting manifests"
  - "not yet supported in a marketplace entry"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-manifest-reference"
    resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
    title: "Plugin manifest reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A marketplace entry accepts its own fields, including `strict`, and every field on the manifest page except the directory listing fields. `strict` decides whether the entry may add components to a plugin that has its own `plugin.json`; default `true`.

# How to use it

- **No `plugin.json`**: the entry is the manifest regardless of `strict`. Entry `hooks` loads only in inline object form; a file path or array shows a `not yet supported in a marketplace entry` error on the `/plugin` Errors tab.
- **`plugin.json` present, `strict` unset or `true`**: the manifest loads and the entry's `commands`, `agents`, `skills`, `outputStyles` and `themes` are appended. For `hooks`, the entry's matchers for an event replace the manifest's for that event; events only the manifest declares keep theirs.
- **`plugin.json` present, `strict: false`**: an entry declaring any of `commands`, `agents`, `skills`, `hooks`, `outputStyles` or `themes` is a conflict; the plugin fails with `Plugin <name> has conflicting manifests`.
- When an entry whose `source` is the marketplace root lists specific `skills` subdirectories, only those load and the default `skills/` is not scanned; a manifest `skills` key adds to the default instead.

# Limits and defaults

Metadata precedence regardless of `strict`: the entry's `defaultEnabled` and display fields (e.g. `displayName`) override the manifest's; the manifest's `version` overrides the entry's; when the entry lists the plugin under a different `name`, `enabledPlugins` uses the entry name and components are namespaced under the manifest name.
