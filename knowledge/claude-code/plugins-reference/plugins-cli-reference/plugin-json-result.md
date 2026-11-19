---
type: "Reference"
title: "Plugin --json result format"
description: "With --json the last stdout line is one JSON object with command, outcome and message; marketplace commands use the same shape."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, json, scripting, ci]
kind: "api"
maturity: "unlabelled"
since: "2.1.268"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "--json"
  - "command"
  - "outcome"
  - "message"
  - "pluginId"
  - "scope"
  - "failureCode"
  - "marketplace"
  - "marketplace-add"
  - "marketplace-remove"
  - "marketplace-update"
  - "invalid_source"
  - "anthropic-plugin-directory"
  - "already_in_goal_state"
  - "alreadyInGoalState"
  - "settings_still_on"
  - "keptData"
  - "savedKept"
  - "install_records_unreadable"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`--json` on `plugin install`, `uninstall`, `update`, `enable`, `disable` (v2.1.268 or later) prints one JSON object as the last line of stdout. Parse only that line, because a marketplace-declared command is printed ahead of it.

# How to use it

Always present: `command` (subcommand that ran, e.g. `install`), `outcome` (`ok` or `failed`), `message`. Others appear only when they apply: `pluginId`, `scope`, `failureCode`, plus each subcommand's own fields.

Marketplace commands (`marketplace add`, `remove`, `update` with `--json`, v2.1.287 or later) print `command` as `marketplace-add`, `marketplace-remove` or `marketplace-update`, plus `outcome`, `message`, and when applicable `marketplace` and `failureCode` (e.g. `invalid_source`). Example: `{"command":"marketplace-remove","outcome":"ok","marketplace":"your-marketplace","message":"Successfully removed marketplace: your-marketplace"}`.

Other fields mentioned: `already_in_goal_state` / `alreadyInGoalState: true` (enable/disable already in the target state), `settings_still_on` (uninstall could not confirm settings off), `keptData`, `savedKept: "install_records_unreadable"`.

# Limits and defaults

- A usage error such as an invalid `--scope` prints no result line, exits `1`, reason on stderr.
- `marketplace add` and `remove` can print no result line when the argument is the reserved name `anthropic-plugin-directory`, so check the exit code.
