---
type: "Feature"
title: "claude plugin enable and disable"
description: "Enable or disable a plugin at a scope (auto-detected local, project, user); --all disables everything; dependencies are enforced."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, enable, disable, dependencies]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.268"
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin enable"
  - "claude plugin disable"
  - "-a, --all"
  - "-s, --scope <scope>"
  - "--json"
  - "<name>@synced"
  - "<name>@inline"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude plugin enable <plugin>` and `claude plugin disable [plugin]` switch a plugin on or off without uninstalling. For a plugin synced from claude.ai pass `<name>@synced`.

# How to use it

| Flag | enable | disable |
| :- | :- | :- |
| `-s, --scope <scope>` | `user`, `project`, `local`; auto-detected when omitted | same |
| `--json` | JSON result, v2.1.268 or later | same |
| `-a, --all` | n/a | Disable every enabled plugin; cannot combine with a name or `--scope` |

Without `--scope` the scope is detected in order local, project, user (first scope that mentions the plugin). Passing a scope where the plugin is not declared writes an override if that scope takes precedence over the declaring one (e.g. `claude plugin disable formatter --scope local` turns off a project-enabled plugin for you alone); otherwise it fails with `Plugin "formatter" is installed at project scope, not user. Use --scope project or omit --scope to auto-detect.`

# Limits and defaults

- Already enabled: `Plugin "formatter" is already enabled`, exit `1`; with `--json` `"failureCode": "already_in_goal_state"` and `"alreadyInGoalState": true` so a script can treat it as success. Already disabled likewise (`Plugin "formatter" is already disabled`, exit `1`).
- `disable` with no name and no `--all`: `Please specify a plugin name or use --all to disable all plugins`, exit `1`.
- enable also enables dependencies; fails if a dependency is not installed (prints install command per dependency), is blocked by organization policy, or is `false` at a higher-precedence scope.
- disable fails if another enabled plugin depends on it (names the dependents) or the organization requires it as a synced plugin (nothing saved).
