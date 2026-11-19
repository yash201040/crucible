---
type: "Feature"
title: "claude plugin configure"
description: "Shows an installed plugin's userConfig options or saves JSON values piped on stdin, scriptable with --json."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, userconfig, scripting, secrets]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "claude plugin configure"
  - "--values-stdin"
  - "--json"
  - "refused"
  - "schema"
  - "choices"
  - "inputs"
  - "configured"
  - "unconfigured"
  - "saved"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude plugin configure <plugin>` shows an installed plugin's `userConfig` options and which are set, or saves values. Requires v2.1.285 or later. Pass the full `name@marketplace` id; a bare `name` is not accepted. With no loaded plugin of that id: `No installed plugin has the id "<plugin>".`, exit `1`.

# How to use it

| Flag | Description |
| :- | :- |
| `--values-stdin` | Read option values from stdin as a JSON object of single-line strings and save them; options left out keep saved values |
| `--json` | One JSON object on stdout. Without `--values-stdin`: `schema`, `choices`, starting `inputs`, `configured` and `unconfigured` names. With it: `saved` names and, when readable, `unconfigured` |

Example: `claude plugin configure formatter@my-marketplace --values-stdin < values.json` with `{"api_url": "https://example.com"}`. Output without flags lists each option with labels `required`/`optional`, `sensitive`, `set`/`not set`, never values. `--json` includes saved values of non-sensitive options only.

# Limits and defaults

Each value is validated against the declared type, then `Configuration saved. Restart Claude Code to apply it.` An undeclared key or failing value saves nothing, prints `Failed to save configuration:` and exits `1`; with `--json` a `refused` field carries `message` and, when one option is at fault, its `option` key. For a bundled MCP server's settings see `plugin install --config` or the **Configure** item in `/plugin`.
