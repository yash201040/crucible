---
type: "Guide"
title: "Add a marketplace"
description: "Sources accepted by /plugin marketplace add, private marketplaces, and adding claude.ai marketplaces with --claudeai."
resource: "https://code.claude.com/docs/en/plugins/install"
tags: [marketplace, add, claudeai, private]
kind: "slash_command"
maturity: "unlabelled"
since: "2.1.273"
surfaces: [cli]
requires: ""
identifiers:
  - "/plugin marketplace add"
  - "/plugin market"
  - "claude plugin marketplace add"
  - "claude plugin marketplace list"
  - "--claudeai"
  - "claudeai-"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-install"
    resource: "https://code.claude.com/docs/en/plugins/install"
    title: "Install and manage plugins"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code must know a marketplace before you install from it. After adding, install with `/plugin install <plugin>@<marketplace>` or `claude plugin install <plugin>@<marketplace>`. `claude plugin marketplace add` takes the same sources from the shell.

# How to use it

| Source | Type | Example |
| :- | :- | :- |
| GitHub repo | `owner/repo`, optional `#ref` | `/plugin marketplace add your-org/plugins#v1.2.0` |
| Any git host | full clone URL, optional `#ref` | `/plugin marketplace add https://gitlab.example.com/your-group/your-marketplace.git#v1.0.0` |
| Local dir or file | path to dir with `.claude-plugin/marketplace.json` or the JSON; relative paths start `./` or `../` (a bare `name/name` is read as GitHub) | `/plugin marketplace add ./my-marketplace` |
| Hosted file | `https://` URL | `/plugin marketplace add https://example.com/marketplace.json` |

`/plugin market` is a shorter form. Include `https://` or use `git@host:path`; a bare `gitlab.example.com/...` is read as GitHub shorthand and rejected. Verify on the **Marketplaces** tab.

**From claude.ai (needs v2.1.273 or later, terminal sessions with claude.ai plugin sync)**: in `/plugin` use the **Marketplaces** tab, or run `claude plugin marketplace list` (shows a `From claude.ai:` section) then `claude plugin marketplace add --claudeai claudeai-organization-library`. The local name starts with `claudeai-`, derived from the claude.ai name ("Organization library" becomes `claudeai-organization-library`). Signing out or switching organizations leaves the marketplace configured but empty; installed plugins keep loading. Git-based marketplaces in that section print a source and are added by source, not `--claudeai`.

# Notes

Managed settings can register a marketplace for you. GitHub Enterprise Server credentials are covered on the GHES page.
