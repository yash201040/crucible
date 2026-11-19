---
type: "Feature"
title: "Authenticate archive downloads with headers and headersHelper"
description: "Send static headers or a headersHelper command output with archive and marketplace URL downloads, with trust, acceptance and removal rules."
resource: "https://code.claude.com/docs/en/plugins/host-marketplace"
tags: [plugins, archive, authentication, headers, security]
kind: "setting"
maturity: "unlabelled"
since: "2.1.238"
surfaces: [cli, ide]
requires: "Entry-level headers and headersHelper need Claude Code v2.1.238 or later; VS Code needs extension 2.1.290 or later to accept"
identifiers:
  - "headers"
  - "headersHelper"
  - "strict"
  - "CLAUDE_CODE_MARKETPLACE_URL"
  - "CLAUDE_CODE_MARKETPLACE_NAME"
  - "CLAUDE_CODE_PLUGIN_NAME"
  - "CLAUDE_CODE_PLUGIN_ARCHIVE_URL"
  - "--yes"
  - "--accept-command"
  - "--json"
  - "disableCommandPluginSources"
  - "allowManagedHooksOnly"
  - "CLAUDE_CONFIG_DIR"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-host-marketplace"
    resource: "https://code.claude.com/docs/en/plugins/host-marketplace"
    title: "Host and maintain a marketplace"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`headers` (static) or `headersHelper` (a command printing short-lived headers) authenticate `archive` downloads. Set them on the marketplace's `url` source (for example an `extraKnownMarketplaces` entry) or, on v2.1.238+, on the plugin's own `marketplace.json` entry beside `source`. An entry with `headersHelper` must set `"strict": false`. Where both set a header, the entry's value wins; a command's output overrides `headers` of the same name in one place.

# How to use it

| Place | Downloads that get headers | When the command runs |
|---|---|---|
| Marketplace `url` source | archives on the marketplace URL's origin | before each `marketplace.json` fetch and archive download on that origin; one run reused up to 60 s |
| Plugin entry | that entry's download only | only on single-plugin install or update after user accepts |

Command requirements: at most 500 printable ASCII characters, no run of four or more spaces; print one JSON object of string values on stdout and exit 0 within 10 seconds; run through `sh` (or `cmd.exe`) with working directory `~/.claude` or `CLAUDE_CONFIG_DIR`; use absolute path or PATH command. From a `marketplace.json` entry or project settings, credential-looking env variables are removed (e.g. `ANTHROPIC_API_KEY`); not from user, `--settings` or managed settings. Claude Code sets `CLAUDE_CODE_MARKETPLACE_URL`/`CLAUDE_CODE_MARKETPLACE_NAME` (url source; name unset on first fetch) or `CLAUDE_CODE_PLUGIN_NAME`/`CLAUDE_CODE_PLUGIN_ARCHIVE_URL` (entry).

Acceptance: users accept an entry command on each single-plugin install or update (terminal `/plugin`, shell `claude plugin install`/`update`, or VS Code Manage plugins). In a non-interactive shell pass `--yes`, or `--accept-command` with the `sha256` a prior `--json` run reported. If command or archive URL changed in between, the install is refused (query-string-only change does not count except in VS Code or with `--accept-command`).

# Limits and defaults

The command is skipped or output dropped when: it exits non-zero, runs over 10 s, or prints non-JSON-string-object (the fetch does not happen); marketplace URL is not `https://`; a redirect leaves the origin; routing/identity headers (`Host`, `Cookie`, `X-Forwarded-*`) are dropped while `Authorization` stays; the command is in an `--add-dir` directory's settings; managed `disableCommandPluginSources: true` (or `allowManagedHooksOnly` unless `disableCommandPluginSources` is explicitly `false`) blocks it, except for marketplaces managed settings declare. Bulk installs, suggestions, dependencies, background auto-update and session start never run an entry command; the plugin is refused or listed in the `/plugin` Errors tab.

# Notes

A `url` source command runs without asking from user settings, `--settings` or managed files; from a project `.claude/settings.json` only after trust dialog acceptance for that exact folder (`-p`/SDK does not count, nor does parent trust); from server-managed settings only after the security approval dialog.
