---
type: "Reference"
title: "claude plugin list and its JSON fields"
description: "Lists installed plugins with version, scope and status; --json gives per-installation objects, --available adds uninstalled marketplace plugins."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, list, json, inventory]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "claude plugin list"
  - "--json"
  - "--available"
  - "--data-size [plugin]"
  - "--plugin-dir"
  - "--plugin-url"
  - "id"
  - "version"
  - "scope"
  - "enabled"
  - "installPath"
  - "readFromFolder"
  - "folderVersion"
  - "installedAt"
  - "lastUpdated"
  - "projectPath"
  - "mcpServers"
  - "errors"
  - "notes"
  - "errorDetails"
  - "noteDetails"
  - "hasUserConfig"
  - "projectEnabled"
  - "dataDirSize"
  - "dataDirUnreadable"
  - "installed"
  - "available"
  - "pluginId"
  - "name"
  - "marketplaceName"
  - "source"
  - "description"
  - "installCount"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude plugin list [options]` lists installed plugins. Human output groups by load route: `Installed plugins:`, `Session-only plugins (--plugin-dir / --plugin-url):` (shown only if the flag precedes the subcommand, e.g. `claude --plugin-dir ./my-plugin plugin list`), `Skills-directory plugins (.claude/skills/*):`, `Synced from claude.ai`. With none: ``No plugins installed. Use `claude plugin install` to install a plugin.``

# How to use it

| Flag | Description |
| :- | :- |
| `--json` | Print as JSON |
| `--available` | Also list uninstalled marketplace plugins; no effect without `--json` |
| `--data-size [plugin]` | Measure saved data directories (or the one named `name@marketplace`); no effect without `--json`. An unknown name prints `--data-size names a plugin that is not installed`, exit `1`. v2.1.285 or later |

`--json` prints an array, one object per installation. Always present: `id`, `version`, `scope`, `enabled`, `installPath`.

| Field | Description |
| :- | :- |
| `id` | `name@marketplace`; `name@inline` session-only; `name@skills-dir`; `name@synced` |
| `version` | Computed at install for marketplace installs; else manifest `version` or `unknown` |
| `scope` | `user`, `project`, `local`, `managed` for installs; `user`/`project` for skills-dir; `session`; `synced` |
| `enabled` | Enabled in merged settings |
| `installPath` | Directory loaded from (except load-in-place plugins) |
| `readFromFolder`, `folderVersion` | For plugins loaded in place from the marketplace folder (v2.1.289 or later) |
| `installedAt`, `lastUpdated` | ISO timestamps, marketplace installs only |
| `projectPath` | `project` and `local` scope only |
| `mcpServers` | MCP definitions of a marketplace-installed plugin |
| `errors`, `notes` | Load errors; non-error warnings |
| `errorDetails`, `noteDetails` | Detail objects per entry (v2.1.268 or later) |
| `hasUserConfig` | `true` when loaded and manifest declares `userConfig` (v2.1.285 or later) |
| `projectEnabled` | Project `.claude/settings.json` turns it on; marketplace installs (v2.1.285 or later) |
| `dataDirSize`, `dataDirUnreadable` | With `--data-size`: `bytes` and `human`; marketplace installs (v2.1.285 or later) |

With `--json --available` the output is one object: `installed` (array above) and `available`, one object per uninstalled plugin with `pluginId`, `name`, `marketplaceName`, `source`, optional `description`, `version`, `installCount`.
