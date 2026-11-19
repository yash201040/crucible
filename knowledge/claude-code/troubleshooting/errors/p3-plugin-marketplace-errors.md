---
type: "Reference"
title: "Plugin and marketplace errors"
description: "Errors for claude plugin eval, reserved or impersonating marketplace names, archive sha256 pins, required plugins, uninstall failures, user_config shell refusal."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, plugins, marketplaces, security]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.269"
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin eval"
  - "claude plugin eval init"
  - "claude plugin marketplace add"
  - "claude plugin marketplace remove"
  - "claude plugin marketplace update"
  - "claude plugin install"
  - "claude plugin update"
  - "claude plugin uninstall"
  - "claude plugin disable"
  - "claude plugin list"
  - "/plugin"
  - "/reload-plugins"
  - "~/.claude/plugins/known_marketplaces.json"
  - "extraKnownMarketplaces"
  - "enabledPlugins"
  - "installed_plugins.json"
  - "sha256"
  - "${user_config.KEY}"
  - "CLAUDE_PLUGIN_OPTION_<KEY>"
  - "--marketplace"
  - "failureCode"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors from plugin and marketplace configuration and the `claude plugin` subcommands. Plugins are a packaging route for skills, hooks, monitors and MCP servers.

# How to use it

| Error | Cause | Fix |
|---|---|---|
| `plugin eval is currently in early access` / `currently unavailable` | `claude plugin eval` (and `init`) exits 1. First: build older than v2.1.269 (first generally available version). Second: switched off server-side | `claude update`; try later |
| `Marketplace "x" is registered from an untrusted source` | Reserved name (official Anthropic names) registered from a source other than a `github.com/anthropics` repo; re-checked at every load (before v2.1.205 earlier entries kept loading) | `claude plugin marketplace remove <name>` and re-add from official source |
| `... is another spelling of "<reserved>"` | Spelling variants such as `claude.code.plugins`; ignored entries warn from `/plugin`, `claude plugin install`, `claude plugin update` | Rename, or `claude plugin marketplace remove` |
| `Claude Code refuses the marketplace name "..."` | Name impersonates an official marketplace; marketplace and its plugins stop loading. Settings-declared (`"source": "settings"`) marketplaces: rename key and `source.name` in `extraKnownMarketplaces` first (v2.1.292+ lists steps); removal also uninstalls plugins and deletes their data, options, secrets | `claude plugin marketplace remove` or wait for maintainer rename then `claude plugin marketplace update <name>` |
| `Marketplace "x" is already added from a different source` | `--marketplace <source>` on install; existing marketplace kept, plugin not installed | `/plugin install <plugin>@<name>`, or remove first |
| `Plugin command references user_config in a shell command` | A hook, monitor or MCP `headersHelper` references `${user_config.KEY}` in a shell-parsed command; component refused to start even with no value set (before v2.1.207 substituted) | Hooks: exec form `{"command": "<exe>", "args": ["${user_config.KEY}"]}` or read `$CLAUDE_PLUGIN_OPTION_<KEY>`; monitors: read a config file; `headersHelper`: use the server `headers` field or read inside the script |
| `Plugin archive integrity check failed` | `archive` source with a `sha256` pin did not match; nothing installed | Maintainer recomputes digest (`shasum -a 256`, PowerShell `Get-FileHash -Algorithm SHA256`); user runs `/plugin marketplace update <name>` |
| `Failed to load marketplace configuration` / `Marketplace configuration file is corrupted` | `~/.claude/plugins/known_marketplaces.json` invalid, empty, or schema mismatch (`claude plugin install` reports it since v2.1.246) | Repair or replace with `{}` and re-add; user/managed `extraKnownMarketplaces` re-register on next start in a trusted folder |
| `Plugin "<name>@synced" is required by your organization` | `claude plugin disable` on a required plugin synced from claude.ai | Admin changes required status |
| `"<plugin>" was not uninstalled: ...` | After removing from `enabledPlugins`, a settings file still enables it or cannot be read; uninstall stops so data is not lost. `claude plugin uninstall` exits 1; `--json` result has `failureCode: "settings_still_on"` | Fix the named settings file, retry |

# Notes

Path and symlink refusals for plugin components are in [plugin path errors](./p3-plugin-path-errors.md).
