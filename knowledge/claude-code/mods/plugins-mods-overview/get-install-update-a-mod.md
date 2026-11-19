---
type: "Guide"
title: "Get, install and update a mod"
description: "Install a mod as a plugin from a marketplace, reload after shell installs, and try Anthropic's sample mods with --plugin-dir."
resource: "https://code.claude.com/docs/en/plugins/mods/overview"
tags: [mods, install, marketplace, samples]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "/plugin install token-chart@your-org"
  - "claude plugin install token-chart@your-org"
  - "/reload-plugins"
  - "--plugin-dir"
  - "claude-code-playground-mods"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-overview"
    resource: "https://code.claude.com/docs/en/plugins/mods/overview"
    title: "Mods overview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Ways to get a mod: use a built-in one (e.g. `/diff`), have Claude write one, or install one.

# How to use it

A mod installs as a plugin: `/plugin install token-chart@your-org` in a session, or `claude plugin install token-chart@your-org` in a shell (plugin name, `@`, marketplace name). If you install or update from a shell while a session is open, run `/reload-plugins` there; otherwise it loads at next start.

Anthropic's samples are in the `claude-code/mods` directory of the `claude-code-playground` repository (shared as-is, without support): `token-weather` (context window forecast above the prompt), `blast-radius` (holds risky shell commands like `rm -rf` or force push and shows what they would change, with proceed/cancel buttons), `replay-theater` (a `/replay` command stepping through the last turn's file edits). Try one by cloning and loading its directory with `--plugin-dir`; keep one by adding the clone's `claude-code/mods` directory as a marketplace and installing from `claude-code-playground-mods` (stops loading if the clone moves).

# Notes

Installing and updating follows the general plugin install pages. A mod runs with your permissions; see [trust](./trust-and-what-a-mod-can-reach.md).
