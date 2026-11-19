---
type: "Reference"
title: "Plugin admin and trust settings"
description: "Managed keys for command-source plugins, contextual plugin suggestions and the plugin trust message."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, plugins, managed, trust]
kind: "setting"
maturity: "unlabelled"
since: "2.1.229"
surfaces: [cli]
requires: "Managed settings"
identifiers:
  - "disableCommandPluginSources"
  - "pluginSuggestionMarketplaces"
  - "pluginTrustMessage"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Three managed-scope keys.

# How to use it

| Name | Type | Default | What it does |
| :- | :- | :- | :- |
| `disableCommandPluginSources` | Boolean | unset: follows `allowManagedHooksOnly` | `true`: never runs a marketplace-declared command, does not install or update command-sourced plugins and stops loading installed ones. `false` allows explicitly. Whenever command sources are blocked it also blocks marketplace `headersHelper` commands, except marketplaces managed settings declare. Needs v2.1.229+; `headersHelper` block needs v2.1.238+. Passing `disableAllHooks: true` in the SDK `managedSettings` does not by itself disable command sources |
| `pluginSuggestionMarketplaces` | array of marketplace names | unset | Marketplaces whose plugins may appear as contextual install suggestions (spinner tips, top of `/plugin` Discover tab) via each plugin's `relevance` declaration. A name works only if registered and its source is declared in the same managed settings (`extraKnownMarketplaces` entry or `strictKnownMarketplaces`); the official marketplace is exempt. Built-in frontend-design tip unaffected |
| `pluginTrustMessage` | string | unset | Extra text added to the plugin trust warning before install |
