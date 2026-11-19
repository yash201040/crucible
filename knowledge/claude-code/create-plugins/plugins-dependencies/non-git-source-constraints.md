---
type: "Limit"
title: "Version constraints on non-git sources"
description: "For npm, archive and command plugin sources the constraint is only checked at load time, and command or headersHelper dependencies are never installed by Claude Code."
resource: "https://code.claude.com/docs/en/plugins/dependencies"
tags: [plugins, dependencies, limits, sources]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "npm"
  - "archive"
  - "command"
  - "headersHelper"
  - "/reload-plugins"
  - "claude plugin marketplace add"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-dependencies"
    resource: "https://code.claude.com/docs/en/plugins/dependencies"
    title: "Plugin dependencies"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Tag-based resolution applies only to git-backed sources. For `npm`, `archive` or `command` sources the constraint does not control which version is fetched; it is still checked at plugin load and the dependent plugin is disabled if the installed version does not satisfy it. The version checked is `version` in the dependency's `plugin.json`; one that sets no version satisfies no constraint.

# Limits and defaults

- Claude Code never installs a dependency with a `command` source itself; users install it first.
- It never runs a dependency's `headersHelper`; users install such a dependency before your plugin.
- These limits also apply to the other operations that install missing dependencies: `/reload-plugins`, auto-update of the dependent plugin's marketplace, re-running `claude plugin install`, and `claude plugin marketplace add`.
