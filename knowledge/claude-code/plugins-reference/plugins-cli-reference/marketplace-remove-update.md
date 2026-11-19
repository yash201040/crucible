---
type: "Feature"
title: "claude plugin marketplace remove and update"
description: "remove deletes a marketplace declaration and, from the last scope, its cache and installed plugins; update refreshes one or all marketplaces."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, marketplace, remove, update]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.287"
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin marketplace remove"
  - "claude plugin marketplace rm"
  - "claude plugin marketplace update"
  - "--scope <scope>"
  - "--json"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

**remove**: `claude plugin marketplace remove <name> [options]` (alias `rm`) removes a marketplace declaration. WARNING: removing it from the last scope that declares it also deletes its cache and uninstalls every plugin installed from it, and deletes their saved options, secrets and data where it can. `<name>` is the name `marketplace list` shows, not the source passed to `add`.

**update**: `claude plugin marketplace update [name] [options]` refreshes one marketplace or all from source. A marketplace added with a branch or tag `ref` updates to the latest commit of that ref, not the default branch. Use update instead of remove/add to refresh without losing plugins.

# How to use it

| Flag | Command | Description |
| :- | :- | :- |
| `--scope <scope>` | remove | Remove from one scope (`user`, `project`, `local`); without it, from every scope |
| `--json` | remove, update | JSON result on the last stdout line. v2.1.287 or later. For update, without a name the command refuses `--json` and exits `1` |

Output: `Successfully removed marketplace: your-marketplace` plus `Also uninstalled 2 plugins from this marketplace:` when applicable; `Successfully updated marketplace: your-marketplace` or `Successfully updated 2 marketplaces`.

# Limits and defaults

A scope that does not declare it fails with `Marketplace 'your-marketplace' is not declared in project settings. Omit --scope to remove it from all scopes.`
