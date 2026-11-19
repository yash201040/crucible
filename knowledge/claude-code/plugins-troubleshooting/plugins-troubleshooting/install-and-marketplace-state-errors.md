---
type: "Reference"
title: "Errors when installing plugins or loading marketplaces"
description: "Install-time and load-time messages: not found, archive integrity, reserved or ignored marketplaces, source conflicts, manifest and cache errors."
resource: "https://code.claude.com/docs/en/plugins/troubleshooting"
tags: [plugins, troubleshooting, install, errors, marketplace]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.287"
surfaces: [cli]
requires: ""
identifiers:
  - "sha256"
  - "claude plugin marketplace update"
  - "claude plugin marketplace remove"
  - "claude plugin marketplace list"
  - "claude plugin list --json"
  - "known_marketplaces.json"
  - "extraKnownMarketplaces"
  - "--marketplace"
  - "Plugin archive integrity check failed"
  - "An npm plugin source must name a registry package"
  - "is registered from an untrusted source"
  - "is added but ignored"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-troubleshooting"
    resource: "https://code.claude.com/docs/en/plugins/troubleshooting"
    title: "Troubleshoot plugins"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Messages from `claude plugin install` / `/plugin` and the `/plugin` Errors tab when a plugin or its marketplace cannot be found, read, or trusted.

# How to use it

| Message | Cause / fix |
|---|---|
| `Plugin "<name>" not found in marketplace "<marketplace>"` | stale catalog (run `/plugin marketplace update <marketplace>`), wrong name (copy from Discover), or marketplace not added; before v2.1.232 refresh happened only after a miss with auto-update on |
| `Plugin "<name>" not found in any marketplace` | no `@marketplace` given; `claude plugin install <name>` does not refresh and `/plugin install` refreshes only auto-update marketplaces; name the marketplace |
| `Plugin '<name>@<marketplace>' is already installed globally` | already at user scope or by managed settings; shell prints `... is already installed (scope: user)` and exits 0 |
| `"<plugin>" was not installed: it would share its folder with "<other>"` (or `its saved data`) | ids that map to the same folder (`.` and `@` become `-`; capitals also on macOS/Windows); uninstall the other or rename in the marketplace |
| `This plugin uses a source type your Claude Code version does not support` | run `claude update` |
| `Plugin archive integrity check failed` | `sha256` pin mismatch; publisher recomputes (`shasum -a 256`, `Get-FileHash -Algorithm SHA256`) |
| `An npm plugin source must name a registry package` | `package` must be `name`, `name@version` or an http(s) tarball link; git deps use `github`/`url`/`git-subdir` |
| `Marketplace "<name>" is registered from an untrusted source` | reserved official name from a non-`github.com/anthropics/` source; re-checked on every load since v2.1.205; remove and re-add from official source or rename |
| `Marketplace "<name>" is added but ignored` | entry in `known_marketplaces.json` failed a re-check: network-drive/`.`/`..` location, bad git or URL, source mismatching `extraKnownMarketplaces` in user/managed settings (repo settings do not count), or refused name; fix: `claude plugin marketplace remove <name>` and re-add |
| `Plugin <name> has a corrupt manifest file` / `has an invalid manifest file` | `plugin.json` invalid JSON or schema; author runs `claude plugin validate <dir>` |
| `Plugin directory not found at path: <path>` / `Marketplace directory not found at path: <path>` | relative entry path missing, or local marketplace dir moved |
| `No plugins available` / `No marketplaces configured` | add `anthropics/claude-plugins-official` |
| `Marketplace "<name>" is already added from a different source` | with `--marketplace <source>`; `/plugin marketplace remove <name>` first |
| `Cannot add marketplace "<name>": its source doesn't match its extraKnownMarketplaces entry in user or managed settings` | sources match only with same type and all fields (a `ref` counts; `https://github.com/` URL is a `git` source); use declared source (e.g. `acme-corp/claude-plugins#v1.2.0`); wording changed in v2.1.287 |
| `Couldn't install: <plugin> (<reason>)` / `Failed to install: ...` | reasons may be shortened; Enter on the plugin in Discover shows the full error |
| `Could not move the new copy of this plugin version into <path>` | cache dir busy (scanner, other session); message says whether the previous copy was moved back; close other sessions and retry |

# Notes

`claude plugin install` exits 1 with `Failed to install plugin "<name>@<marketplace>":` for manifest errors.
