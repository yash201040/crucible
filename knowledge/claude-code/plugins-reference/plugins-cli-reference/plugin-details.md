---
type: "Feature"
title: "claude plugin details"
description: "Shows a loaded plugin's component inventory and projected always-on token cost."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, token-cost, inventory]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin details"
  - "Component inventory"
  - "Projected token cost"
  - "Per-component (rounded)"
  - "@builtin"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude plugin details <name>` shows what a plugin contributes. The plugin must be loaded: installed, in a skills directory, or passed with `--plugin-dir` or `--plugin-url` in the same command. `<name>` is `name` or `name@marketplace`. It takes no flags beyond `--help`.

# How to use it

It prints name, version, description, source, then: `Component inventory` (skills, agents, hooks, MCP servers, LSP servers), `Projected token cost` (always-on tokens added to every session), and `Per-component (rounded)` (always-on and on-invoke estimates per skill, agent and command; omitted when none). The two figures are explained in the Measure plugin cost and usage page.

# Limits and defaults

An unloaded plugin prints `Plugin "formatter" not found. Run \`claude plugin list\` to see installed plugins, or pass --plugin-dir <path> to load one from disk.` and exits `1`. An id ending `@builtin` names a plugin built into Claude Code; if not found the message says built-ins do not appear in `claude plugin list` and to open the Installed tab of `/plugin`.
