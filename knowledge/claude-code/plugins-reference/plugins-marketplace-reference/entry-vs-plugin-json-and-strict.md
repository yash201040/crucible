---
type: "Concept"
title: "Entry vs plugin.json, display fields and strict mode"
description: "How a marketplace entry combines with a plugin's own plugin.json, which fields users see, and what strict true or false does."
resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
tags: [marketplace, strict-mode, plugin-json, hooks]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "strict"
  - "commands"
  - "agents"
  - "skills"
  - "hooks"
  - "outputStyles"
  - "themes"
  - "mcpServers"
  - "lspServers"
  - "userConfig"
  - "channels"
  - "hooks/hooks.json"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-marketplace-reference"
    resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
    title: "Marketplace reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Rules for combining a [plugin entry](./plugin-entry-fields.md) with the fetched plugin's `.claude-plugin/plugin.json`.

# How to use it

- **No `plugin.json`**: the entry is the manifest regardless of `strict`; every field it accepts applies, including `mcpServers`, `lspServers`, `userConfig` and `channels`.
- **`plugin.json` present**: it is the manifest. `strict` decides whether the entry's six component fields (`commands`, `agents`, `skills`, `hooks`, `outputStyles`, `themes`) are merged or rejected. Entry `mcpServers`, `lspServers`, `userConfig`, `channels` do not apply; declare them in `plugin.json`.

| `strict` | `plugin.json` | Entry component fields | Result |
| :- | :- | :- | :- |
| any | absent | any | Entry is the manifest |
| `true` (default) | present | any | `plugin.json` is authority; entry component fields are appended, except `hooks`, whose matchers replace the manifest's per event |
| `false` | present | none | `plugin.json` is the manifest |
| `false` | present | one or more | Conflict: load fails with `Plugin <name> has conflicting manifests: both plugin.json and marketplace entry specify components` |

**Hooks in an entry**: write them as an inline object mapping event names to matcher arrays. A file path or an array passes `claude plugin validate` but never runs, and Claude Code reports a `not yet supported in a marketplace entry` error. Put file-based hooks in the plugin's `hooks/hooks.json` or `plugin.json`.

**Display fields**: `displayName`, `description`, `author`, `homepage`, `repository`, `license`, `keywords` can be set on both. Users see the entry's value when set, otherwise the `plugin.json` value.

# Limits and defaults

Before install, Claude Code can read `plugin.json` only for entries with a relative-path source; for any other source type, users see only the entry's own fields until install.
