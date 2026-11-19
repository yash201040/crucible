---
type: "Feature"
title: "claude plugin install"
description: "Installs a plugin from a configured marketplace with scope, userConfig, non-interactive acceptance of command sources and JSON output."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, install, marketplace, non-interactive]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.268"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "claude plugin install"
  - "claude plugin i"
  - "-s, --scope <scope>"
  - "--config <key=value>"
  - "-y, --yes"
  - "--accept-command <sha256>"
  - "--json"
  - "--marketplace <source>"
  - "Run this command now? [y/N]"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude plugin install <plugin> [options]` (alias `i`) installs a plugin from one of your marketplaces. Most plugins install without a prompt. If the marketplace entry runs a command to install it, or sets a `headersHelper` for its download, Claude Code prints the command and asks `Run this command now? [y/N]`.

# How to use it

| Flag | Description |
| :- | :- |
| `-s, --scope <scope>` | `user`, `project` or `local`; default `user` |
| `--config <key=value>` | Set a `userConfig` option; repeat per option. `<server>.<key>` sets a setting that a bundled MCP server declares in its own `user_config` (bundle shipped in the plugin); that form needs v2.1.285 or later |
| `-y, --yes` | Accept the displayed install command without the prompt. Ignored when run inside a Claude Code session (Bash tool or hook) |
| `--accept-command <sha256>` | Accept the displayed command whose `sha256` a previous `--json` run reported in `shownCommand`, instead of `-y`; cannot combine with `-y`. v2.1.271 or later |
| `--json` | Print the result as one JSON object on the last line of stdout. v2.1.268 or later |
| `--marketplace <source>` | Install the bare-named plugin from the marketplace at `<source>`, adding it first if needed. v2.1.292 or later |

Share with a project: `claude plugin install formatter@my-marketplace --scope project`, commit `.claude/settings.json`, and have each person add the marketplace and run the same command in their clone.

# Limits and defaults

- stdin or stdout not a TTY and neither `-y` nor `--accept-command`: install is refused (command only displayed), exit `1`.
- Claude running the command via its Bash tool: `-y` is ignored; run it from your own terminal.
- Success prints `Successfully installed plugin: formatter@my-marketplace (scope: project)`. Already installed: `Plugin "..." is already installed (scope: project)`, exit `0`. Declined command prompt: `Aborted.`, exit `1`. Declined or unconfirmable `headersHelper` prompt: `Aborted — the command was not run.`, exit `1`.

# Notes

See [JSON result format](./plugin-json-result.md) and [accepting a displayed command](./accept-a-displayed-install-command.md).
