---
type: "Guide"
title: "Enable contribution metrics"
description: "Four-step setup connecting a GitHub organization so the Teams/Enterprise dashboard shows PR and line contribution metrics."
resource: "https://code.claude.com/docs/en/analytics"
tags: [analytics, github, contribution-metrics, setup, admin]
kind: "behavior"
maturity: "beta"
since: ""
surfaces: [web]
requires: "Claude for Teams or Enterprise; Owner role; GitHub admin to install the app; not Zero Data Retention"
identifiers:
  - "github.com/apps/claude"
  - "claude.ai/admin-settings/claude-code"
  - "GitHub analytics"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "analytics"
    resource: "https://code.claude.com/docs/en/analytics"
    title: "Track team usage with analytics"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Contribution metrics (labelled public beta) count PRs and lines of code shipped with Claude Code assistance. They need your GitHub organization connected.

# How to use it

1. A GitHub admin installs the Claude GitHub app at github.com/apps/claude.
2. A Claude Owner opens claude.ai/admin-settings/claude-code and enables the Claude Code analytics feature.
3. On the same page, enable the "GitHub analytics" toggle.
4. Complete the GitHub authentication flow and choose which GitHub organizations to include.

Data typically appears within 24 hours, with daily updates. Messages you may see: "GitHub app required" (install the app) and "Data processing in progress" (check back in a few days, confirm the app is installed).

# Limits and defaults

- Only users inside your claude.ai organization are covered. Claude Console API usage and third-party integrations are not included.
- Not available for organizations with Zero Data Retention enabled: the dashboard shows usage metrics only.
- Covers repositories on github.com only. For GitHub Enterprise Server repositories, only usage metrics appear.
- Owner role is needed to configure analytics settings.
