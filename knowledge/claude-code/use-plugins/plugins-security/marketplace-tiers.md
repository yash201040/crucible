---
type: "Reference"
title: "Marketplace tiers and official names"
description: "Official, community and third-party marketplace tiers, the official name list, and the SHA-pin rule for the community catalog."
resource: "https://code.claude.com/docs/en/plugins/security"
tags: [marketplace, trust, official-names, tiers]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "claude-plugins-official"
  - "claude-code-marketplace"
  - "claude-code-plugins"
  - "anthropic-marketplace"
  - "anthropic-plugins"
  - "agent-skills"
  - "anthropic-agent-skills"
  - "life-sciences"
  - "knowledge-work-plugins"
  - "claude-for-legal"
  - "claude-for-financial-services"
  - "financial-services-plugins"
  - "first-party-plugins"
  - "claude-tag-plugins"
  - "claude-community"
  - "claude-plugins-community"
  - "healthcare"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-security"
    resource: "https://code.claude.com/docs/en/plugins/security"
    title: "Plugin security and trust"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A marketplace's name places it in one of three tiers. Official and community names are accepted only for marketplaces sourced from `github.com/anthropics/` repositories, so third parties cannot impersonate them. A marketplace published by a coworker or your organization is third-party.

# How to use it

| Tier | Marketplaces |
| :- | :- |
| Official | `claude-plugins-official`, `claude-code-marketplace`, `claude-code-plugins`, `anthropic-marketplace`, `anthropic-plugins`, `agent-skills`, `anthropic-agent-skills`, `life-sciences`, `knowledge-work-plugins`, `claude-for-legal`, `claude-for-financial-services`, `financial-services-plugins`, `first-party-plugins`, `claude-tag-plugins` |
| Community | `claude-community`, `claude-plugins-community`, `healthcare` |
| Third-party | every other |

# Notes

Where the `claude-community` catalog pins a plugin to a commit SHA (nearly every entry), Claude Code refuses to install a different commit.
