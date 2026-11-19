---
type: "Feature"
title: "claude plugin update"
description: "Updates a plugin to the latest marketplace version, loaded next session or after /reload-plugins; scope auto-detected including managed."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, update, scopes, managed]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.246"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "claude plugin update"
  - "-s, --scope <scope>"
  - "-y, --yes"
  - "--accept-command <sha256>"
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

`claude plugin update <plugin> [options]` updates to the latest version the marketplace offers. The new version loads in the next session, or after `/reload-plugins` in a running one.

# How to use it

| Flag | Description |
| :- | :- |
| `-s, --scope <scope>` | `user`, `project`, `local` or `managed`; auto-detected when omitted |
| `-y, --yes` | Accept a changed install command from a command-source plugin without the prompt; required when stdin/stdout is not a TTY unless `--accept-command` |
| `--accept-command <sha256>` | Accept the command whose `sha256` a previous `--json` run reported; instead of `-y`. v2.1.271 or later |
| `--json` | JSON result. v2.1.268 or later |

Prints `Checking for updates for plugin "formatter@my-marketplace"…`; when nothing is newer: `formatter is already at the latest version (1.0.0).`, exit `0`.

# Limits and defaults

- **Scope**: omitted `--scope` picks the most specific scope installed for the current project, checking local, project, user, then managed. Before v2.1.281 it used `user`, failing with `Plugin "<name>" is not installed at scope user` for project/local-only installs; pass `--scope` on those versions. `managed` is the one scope you can update but not install to.
- **Bare name**: matched against installed plugins; if several marketplaces share it, the update is refused and qualified commands listed. Needs v2.1.246 or later.
- **Dependency retry**: at the latest version it can retry an unfinished dependency install in the cached copy; failure prints `Failed to update plugin "formatter@my-marketplace"` with reason, exit `1`. Before v2.1.287 it did not retry.
