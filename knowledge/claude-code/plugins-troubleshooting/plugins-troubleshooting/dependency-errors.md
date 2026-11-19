---
type: "Reference"
title: "Plugin dependency error messages"
description: "Dependency messages at install or load time, their meanings, fixes, and the errorDetails types in claude plugin list --json."
resource: "https://code.claude.com/docs/en/plugins/troubleshooting"
tags: [plugins, dependencies, errors, semver]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin list --json"
  - "errorDetails"
  - "dependency-unsatisfied"
  - "dependency-version-unsatisfied"
  - "<name>--v*"
  - "/reload-plugins"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-troubleshooting"
    resource: "https://code.claude.com/docs/en/plugins/troubleshooting"
    title: "Troubleshoot plugins"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A plugin with unsatisfied dependencies fails to install, or installs and stays disabled; the problem shows in the install error or the `/plugin` Errors tab.

# How to use it

| Message | Fix |
|---|---|
| `Dependency "<dep>" is not installed` | `claude plugin install <dep>@<marketplace>`, or add the marketplace and run `/reload-plugins` (installs resolvable missing deps) |
| `"<name>@synced" is loaded from your claude.ai account but meets a marketplace dependency only for other claude.ai plugins` | install the dependency from its marketplace; that copy then loads |
| `Dependency "<dep>" is disabled` | enable it or uninstall the plugin |
| `Requires "<dep>" <range>, installed <version>` | update dependency into range |
| `... has conflicting version requirements` | uninstall/update one plugin or widen constraint |
| `... too complex to intersect` / `has an invalid version requirement` | fix invalid semver or simplify `\|\|` chains |
| `... has no git tag satisfying <range>` | upstream must tag `<name>--v*` releases or relax range |
| `Dependency "<dep>" (required by <plugin>) is in marketplace "<marketplace>", which is not in the allowlist` | cross-marketplace resolution is off by default; install dependency yourself at the same `--scope` |

`claude plugin list --json` gives plugins with problems an `errors` field and `errorDetails` with a `type`: first three rows are `dependency-unsatisfied`, the fourth `dependency-version-unsatisfied`.
