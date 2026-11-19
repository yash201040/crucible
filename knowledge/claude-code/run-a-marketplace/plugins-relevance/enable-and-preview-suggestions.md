---
type: "Feature"
title: "Enable plugin suggestions and what users see"
description: "Allowlist a marketplace for suggestions in managed settings and the frequency rules for spinner tips, session-start notices and the Discover pin."
resource: "https://code.claude.com/docs/en/plugins/relevance"
tags: [plugins, suggestions, managed-settings, spinner-tips]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, cloud]
requires: "Managed settings; terminal suggestions need the marketplace allowlisted"
identifiers:
  - "pluginSuggestionMarketplaces"
  - "extraKnownMarketplaces"
  - "strictKnownMarketplaces"
  - "spinnerTipsEnabled"
  - "spinnerTipsOverride"
  - "excludeDefault"
  - "claude-plugins-official"
  - "~/.claude.json"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-relevance"
    resource: "https://code.claude.com/docs/en/plugins/relevance"
    title: "Recommend plugins for your org"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

In the terminal, users see no suggestions from a marketplace until an admin allowlists it, even if its `marketplace.json` declares `relevance`.

# How to use it

Add the marketplace name to `pluginSuggestionMarketplaces` in managed settings. For any marketplace other than the official one, also declare its source as the name's `extraKnownMarketplaces` entry or as a `strictKnownMarketplaces` entry. If the marketplace is unregistered or registered under that name from a different source, no suggestions appear. The official marketplace needs only the name: `{"pluginSuggestionMarketplaces": ["claude-plugins-official"]}`.

Where suggestions appear: spinner tip (`Working with Terraform? Install the terraform-helpers plugin: /plugin install terraform-helpers@your-marketplace`), session-start notification when a `cwd` signal matches (`plugin suggestion: terraform-helpers@your-marketplace · /plugin`), and the `/plugin` Discover tab pinned to top with an annotation such as `suggested for this directory`.

# Limits and defaults

- At most once every three sessions across spinner tip and session-start notice combined.
- Session-start notice stops after the tip and notice have shown a combined two times.
- Neither repeats once installed.
- The Discover pin happens the first time the tab is opened while signals match, recorded in `~/.claude.json`.
- Spinner tip and session-start notice stop when `spinnerTipsEnabled` is `false` or a `spinnerTipsOverride` with `excludeDefault` replaces built-in tips; the Discover pin is unaffected.

# Notes

In a cloud session's conversation Claude can suggest plugins regardless; turning that off is covered under Claude Code on the web.
