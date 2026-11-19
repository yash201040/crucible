---
type: "Reference"
title: "claude plugin marketplace list"
description: "Lists added marketplaces with source; --json gives an array with name, source, repo, url, path, ref and installLocation."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, marketplace, list, json]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.273"
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin marketplace list"
  - "--json"
  - "name"
  - "source"
  - "repo"
  - "url"
  - "path"
  - "ref"
  - "installLocation"
  - "marketplaceId"
  - "organizationUuid"
  - "scope"
  - "status"
  - "From claude.ai:"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude plugin marketplace list [options]` prints `Configured marketplaces:` with one `Source:` line each, or `No marketplaces configured`.

# How to use it

`--json` prints an array, one object per marketplace, every field a string:

| Field | Description |
| :- | :- |
| `name` | Marketplace name |
| `source` | `github`, `git`, `url`, `directory`, `file` or `claudeai` |
| `repo` | `owner/repo`, `github` only |
| `url` | Clone or fetch URL, `git` and `url` only |
| `path` | Local path, `directory` and `file` only |
| `ref` | Pinned branch, tag or commit SHA, only when pinned |
| `installLocation` | Where Claude Code cached it |

An added claude.ai marketplace has no local clone: its entry carries `marketplaceId` and `organizationUuid` instead of `installLocation`, plus `scope` when recorded and `status`.

# Limits and defaults

If terminal sessions sync plugins from your claude.ai account, the text listing ends with a `From claude.ai:` section naming marketplaces claude.ai lists that you have not added (git-based and hosted); requires v2.1.273 or later. `--json` covers configured marketplaces only and omits that section.
