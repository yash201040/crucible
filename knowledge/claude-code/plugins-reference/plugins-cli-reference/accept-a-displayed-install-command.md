---
type: "Feature"
title: "Accept a displayed install command"
description: "A failed --json install carries a shownCommand with sha256 that --accept-command accepts in a later run from your own terminal."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, security, install, ci]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.271"
surfaces: [cli]
requires: ""
identifiers:
  - "shownCommand"
  - "acceptCommandMatched"
  - "--accept-command"
  - "sha256"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When a `--json` run displays a marketplace-declared command and does not run it, the `failed` result also carries a `shownCommand` object: the command as displayed, the plugin it belongs to, and its `sha256`.

# How to use it

Re-run with that `sha256` as `--accept-command` from your own terminal; the flag has no effect inside a Claude Code session. Requires v2.1.271 or later.

# Limits and defaults

The `sha256` counts as acceptance for exactly that command, plugin and marketplace catalog. If any changed since display (including a change fetched by the run's own marketplace refresh), Claude Code does not accept it and shows the command again. If `shownCommand.acceptCommandMatched` is `false`, the `sha256` you passed does not match the command now displayed; review it before re-running.
