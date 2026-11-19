---
type: "Feature"
title: "claude plugin uninstall"
description: "Removes a plugin from one scope; deletes stored options, secrets and data directory when removed from the last scope unless --keep-data."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, uninstall, data, cleanup]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.281"
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin uninstall"
  - "claude plugin remove"
  - "claude plugin rm"
  - "--keep-data"
  - "--prune"
  - "-y, --yes"
  - "--json"
  - "~/.claude/plugins/data/<id>/"
  - "~/.claude/plugins/mcpb/"
  - "cleanupPeriodDays"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude plugin uninstall <plugin> [options]` (aliases `remove`, `rm`) removes an installed plugin from one scope.

# How to use it

| Flag | Description |
| :- | :- |
| `-s, --scope <scope>` | `user`, `project` or `local`; default `user` |
| `--keep-data` | Preserve `~/.claude/plugins/data/<id>/` |
| `--prune` | Also remove auto-installed dependencies no remaining plugin needs |
| `-y, --yes` | Skip the `--prune` confirmation; required with `--prune` when stdin/stdout is not a TTY |
| `--json` | JSON result like [install](./plugin-json-result.md); cannot combine with `--prune`. v2.1.268 or later |

Example: `claude plugin uninstall formatter@my-marketplace --scope project` prints `Successfully uninstalled plugin: formatter (scope: project)`. A plugin not installed there prints `Failed to uninstall plugin "...":` and exits `1`. If the failure says `"formatter" was not uninstalled:` and names a settings file, the scope's settings still switch it on, the plugin stays installed, and `--json` gives `failureCode: "settings_still_on"` (check needs v2.1.282 or later).

# Limits and defaults

Uninstalling from the last scope also deletes stored options and secrets and the data directory. Data stays with `--keep-data`; when another installed plugin uses the same folder (id differs only in letter case); or when the installed-plugin list cannot be read back (options, secrets and data all stay, uninstall still succeeds, `--json` carries `savedKept: "install_records_unreadable"`; v2.1.282 or later). `--json` `keptData` reports whether the directory stayed (v2.1.281 or later for the no-`--keep-data` case), and `/plugin` shows `· data preserved`. Deleting options also deletes files that v2.1.326 or later extracted into `~/.claude/plugins/mcpb/` from the plugin's MCP bundles, unless another plugin uses an identical bundle; leftover files are cleaned once unused for `cleanupPeriodDays`.
