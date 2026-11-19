---
type: "Reference"
title: "Marketplace-level validation messages and URL-marketplace pitfalls"
description: "Marketplace validate errors and warnings, relative-path failures in URL marketplaces, and submodule gaps for root plugins."
resource: "https://code.claude.com/docs/en/plugins/troubleshooting"
tags: [plugins, marketplace, validation, errors]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.247"
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin validate ."
  - "Duplicate plugin name"
  - "Plugin source path refused"
  - "its marketplace entry path does not stay inside the marketplace directory"
  - "org"
  - "org-provisioned"
  - "unknown"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-troubleshooting"
    resource: "https://code.claude.com/docs/en/plugins/troubleshooting"
    title: "Troubleshoot plugins"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Messages `claude plugin validate .` prints for the marketplace file, plus owner-side pitfalls. Entry-level problems print as `plugins[N] plugin.json → ...`. It also warns when a local-path entry's `version` disagrees with the plugin's manifest.

# How to use it

| Message | Kind |
|---|---|
| `Duplicate plugin name "<name>" found in marketplace` | Error |
| `Path contains "..": <path>` under `plugins[N].source` | Error |
| Marketplace or plugin name contains control or bidirectional-formatting characters | Error |
| `Claude Code cannot install plugins from marketplace "<name>"...` / `... plugin "<name>"...` (id parts: a-z A-Z digits `.` `_` `-`, start with letter or digit) | Error |
| `Marketplace has no plugins defined` / `No marketplace description provided` | Warning |
| `Plugin name "<name>" is not kebab-case` (claude.ai sync requires it) | Warning |
| `Entry declares version "<a>" but <path>/plugin.json says "<b>"` (`plugin.json` authoritative) | Warning |
| `Marketplace name "<name>" is reserved in Claude Desktop` (rejects `org`, `org-provisioned`, `unknown` in any casing) | Warning |
| `... is not accepted by Claude Desktop` (max 128 chars of letters, digits, `.`, `_`, `-`) | Warning |

Before v2.1.247 control/bidi names were reported only as impersonation of an official marketplace.

URL-hosted marketplaces download only `marketplace.json`, so relative-path entries fail (`its marketplace entry path does not stay inside the marketplace directory`; installed ones `Plugin source path refused`); use `github` sources or a git-hosted marketplace. A plugin at the marketplace root that uses a submodule file finds the directory empty after install since v2.1.295 (before, every submodule was fetched); write the path literally, e.g. `${CLAUDE_PLUGIN_ROOT}/vendor/tool/run.sh`.
