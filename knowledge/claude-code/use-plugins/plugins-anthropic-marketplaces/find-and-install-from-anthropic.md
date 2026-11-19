---
type: "Guide"
title: "Find and install from Anthropic's marketplaces"
description: "Ways to browse the official catalog (Discover tab, install by name, web, GitHub) and how claude.ai directory plugins reach Claude Code."
resource: "https://code.claude.com/docs/en/plugins/anthropic-marketplaces"
tags: [plugins, discovery, marketplace, install]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/plugin"
  - "/plugin install <name>"
  - "commit-commands"
  - "code-review"
  - "feature-dev"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-anthropic-marketplaces"
    resource: "https://code.claude.com/docs/en/plugins/anthropic-marketplaces"
    title: "Anthropic's marketplaces"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Most of the official marketplace comes from partners and other authors; Anthropic maintains a smaller set (such as `commit-commands`, `code-review`, `feature-dev` and the language server plugins). The catalog changes often and is not listed on the page.

# How to use it

- **Browse**: run `/plugin` in an interactive session; the **Discover** tab is searchable.
- **By name**: `/plugin install <name>` looks the name up in your marketplaces and opens its details in the `/plugin` panel; nothing installs until you choose a scope and confirm. Otherwise you see `Plugin "<name>" not found in any marketplace`.
- **Web**: Claude Marketplace (claude.com/marketplace/plugins) shows install counts and marks some plugins **Anthropic verified**.
- **GitHub**: open `.claude-plugin/marketplace.json` in the marketplace repo.

# Notes

Anthropic's directory (the catalog on claude.ai) is separate. A plugin added from it on claude.ai reaches Claude Code through account sync.
