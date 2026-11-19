---
type: "Concept"
title: "Marketplaces and Anthropic marketplace tiers"
description: "A marketplace is a catalog file listing plugins; names fall into official, community or third-party tiers."
resource: "https://code.claude.com/docs/en/plugins/overview"
tags: [marketplace, plugins, security, official]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - ".claude-plugin/marketplace.json"
  - "/plugin marketplace add"
  - "claude-plugins-official"
  - "claude-code-plugins"
  - "claude-community"
  - "commit-commands@claude-plugins-official"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-overview"
    resource: "https://code.claude.com/docs/en/plugins/overview"
    title: "Plugins overview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A marketplace is a repository or directory with `.claude-plugin/marketplace.json` listing plugins and where to fetch each. It is a catalog, not a hosted store. Add one once, then install by name, e.g. `commit-commands@claude-plugins-official`. It is not Claude Marketplace (claude.com/marketplace), which cannot be added with `/plugin marketplace add`.

Claude Code adds Anthropic's official marketplace the first time you start an interactive terminal session, unless managed policy blocks it. It does not add the community marketplace on its own.

# Limits and defaults

Three tiers by name; official and community names are accepted only for marketplaces sourced from `github.com/anthropics/` repositories:
- Official: Anthropic's official names, including `claude-plugins-official` and `claude-code-plugins`.
- Community: e.g. `claude-community`.
- Third-party: everything else, including your coworker's or organization's.

Whatever the tier, a plugin can run code with your user privileges. Through managed settings an organization can allowlist or block marketplaces, force-install plugins and turn off session-only loading.
