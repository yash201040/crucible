---
type: "Feature"
title: "enabledPlugins and extraKnownMarketplaces"
description: "Per-plugin on/off switches and named marketplace registration, with source types, headersHelper and key aliases."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, plugins, marketplaces, headers]
kind: "setting"
maturity: "unlabelled"
since: "2.1.232"
surfaces: [cli]
requires: ""
identifiers:
  - "enabledPlugins"
  - "extraKnownMarketplaces"
  - "additionalMarketplaces"
  - "autoUpdate"
  - "headersHelper"
  - "skipLfs"
  - "defaultEnabled"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`enabledPlugins` (any file): object mapping `plugin-name@marketplace-name` to a Boolean; no entry means the plugin's `defaultEnabled`. `/plugin` and `claude plugin enable` write it. `extraKnownMarketplaces` (any file): named marketplaces registered for everyone the file reaches, each with a `source` object and optional `autoUpdate`.

# How to use it

Scopes of `enabledPlugins`: user (personal), project (turned on for the repo but not installed), local (gitignored per-machine), managed (a `false` blocks install at every scope and hides it). Project beats user, so opt out of a project-enabled plugin in `.claude/settings.local.json`; managed force-enables cannot be disabled that way.

`extraKnownMarketplaces` source types: `github` (`repo`), `git` (`url`), `url` (`url`, optional `headers`, `headersHelper`), `file` (`path`), `directory` (`path`), `settings` (inline, with `name` and `plugins`; plugins must reference external sources such as GitHub or npm; `name` must match the key; enable each separately). `autoUpdate`: omitted defaults to `true` for `claude-plugins-official` and most official marketplaces, `false` for third-party.

# Limits and defaults

- Entries in a repo's `.claude/settings*.json` are honored only after the workspace trust dialog; untrusted (including `-p`) ignores them silently.
- Same-name entries: the highest-precedence file's entry wins whole (before v2.1.228 fields merged).
- `headersHelper` (needs v2.1.238+): command printing headers, run before each `marketplace.json` fetch and each plugin archive download on the same origin; output reused up to 60 seconds. Ignored in `--add-dir` directories' settings. An inline plugin entry with an `archive` source may set `headers` and `headersHelper`; run only when a user installs or updates that plugin alone; project-file entries need folder trust and have routing and client-identity header names dropped.
- Git LFS content is never downloaded for `github` and `git` sources; `skipLfs` accepted but has no effect (before v2.1.274 LFS was downloaded unless `"skipLfs": true`).
- Aliases (v2.1.232+): `additionalMarketplaces` for `extraKnownMarketplaces`, `allowedMarketplaces` for `strictKnownMarketplaces`; earlier versions ignore them; both spellings in one file means canonical wins; Claude Code may rewrite the alias.
