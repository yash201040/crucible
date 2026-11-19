---
type: "Reference"
title: "Official and community marketplaces"
description: "The two general-purpose Anthropic marketplaces, their repos, names and how each is obtained."
resource: "https://code.claude.com/docs/en/plugins/anthropic-marketplaces"
tags: [marketplace, official, community, plugins]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "claude-plugins-official"
  - "claude-community"
  - "anthropics/claude-plugins-official"
  - "anthropics/claude-plugins-community"
  - "anthropics/skills"
  - "anthropics/knowledge-work-plugins"
  - "CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL"
  - "/plugin marketplace add"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-anthropic-marketplaces"
    resource: "https://code.claude.com/docs/en/plugins/anthropic-marketplaces"
    title: "Anthropic's marketplaces"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Anthropic publishes two general-purpose marketplaces, each a GitHub repository with `.claude-plugin/marketplace.json`. Topic-specific ones such as `anthropics/skills` and `anthropics/knowledge-work-plugins` are added with `/plugin marketplace add <owner>/<repo>`.

# How to use it

| | Official | Community |
| :- | :- | :- |
| Repository | `anthropics/claude-plugins-official` | `anthropics/claude-plugins-community` |
| Marketplace name (after `@`) | `claude-plugins-official` | `claude-community` (not the repo name) |
| Contents | Plugins Anthropic maintains plus partner and other authors' plugins | Third-party plugins submitted to Anthropic |
| How you get it | Added automatically on first interactive terminal session, unless a managed policy or `CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL` blocks it | `/plugin marketplace add anthropics/claude-plugins-community`, then install with `@claude-community` |

Example: `/plugin install commit-commands@claude-plugins-official`. If the official marketplace is missing from the **Marketplaces** tab, add it with `/plugin marketplace add anthropics/claude-plugins-official`.

# Notes

Third-party marketplaces are not reviewed by Anthropic; add one with `/plugin marketplace add <owner>/<repo>` and install `<plugin>@<marketplace-name>`, where the name is the `name` field of its `marketplace.json`. See [security and trust](../plugins-security/trust-and-review.md).
