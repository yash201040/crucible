---
type: "Feature"
title: "Plugin userConfig values"
description: "Declare values users must supply in userConfig; the dialog appears in interactive /plugin flows, and shell installs take --config or --values-stdin."
resource: "https://code.claude.com/docs/en/plugins/components"
tags: [plugins, userconfig, secrets, install]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide]
requires: ""
identifiers:
  - "userConfig"
  - "sensitive"
  - "title"
  - "description"
  - "/plugin configure <plugin>@<marketplace>"
  - "claude plugin install --config KEY=VALUE"
  - "claude plugin configure --values-stdin"
  - "${user_config.*}"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-components"
    resource: "https://code.claude.com/docs/en/plugins/components"
    title: "Add components to a plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The `userConfig` manifest key declares values the plugin needs from the user, so users do not edit `settings.json`. Each option is a dialog row with `title` as label and `description` beneath. `"sensitive": true` masks input and stores the value in secure storage instead of `settings.json`.

# How to use it

Example options: `api_url` (type string) and `api_token` (type string, sensitive).

The dialog is part of the interactive `/plugin` interface and opens for unset options when the user installs in `/plugin`, runs `/plugin install <plugin>@<marketplace>` in a session, or enables the plugin from the Installed tab. `/plugin configure <plugin>@<marketplace>` reopens it any time. The VS Code Manage plugins dialog asks as a form, with a gear icon to reopen.

From a shell, `claude plugin install` never prompts: pass `--config KEY=VALUE` at install, or pipe a JSON object to `claude plugin configure --values-stdin`. Unset options print a `userConfig options not yet set` line.

# Notes

Loading with `--plugin-dir` does not show the dialog (see create page). Components reference saved values as `${user_config.*}` (not allowed in monitors); hooks get `CLAUDE_PLUGIN_OPTION_<KEY>`.
