---
type: "Reference"
title: "Marketplace source fields and policy-only values"
description: "Per-type marketplace source fields (ref, path, sparsePaths, skipLfs, headers) and values valid only in strictKnownMarketplaces and blockedMarketplaces."
resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
tags: [marketplace, ref-pinning, policy, sparse-checkout]
kind: "setting"
maturity: "unlabelled"
since: "2.1.324"
surfaces: []
requires: ""
identifiers:
  - "headers"
  - "headersHelper"
  - "repo"
  - "ref"
  - "path"
  - "sparsePaths"
  - "skipLfs"
  - "name"
  - "plugins"
  - "hostPattern"
  - "pathPattern"
  - "skills-dir"
  - "owner/*"
  - "strictPluginOnlyCustomization"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-marketplace-reference"
    resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
    title: "Marketplace reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Fields of a [marketplace source](./marketplace-source-types.md) that have a default, constraint or type-specific meaning, plus values valid only in policy lists.

# How to use it

| Field | Types | Meaning |
| :- | :- | :- |
| `url` | `url` | Link to `marketplace.json`; only that file is downloaded so relative-path plugin sources cannot be used |
| `url` | `git` | Repository to clone |
| `headers` | `url` | HTTP headers sent with the fetch |
| `headersHelper` | `url` | Command printing short-lived headers. Needs v2.1.238 or later |
| `repo` | `github` | Must name one repo in `marketplace add` and `extraKnownMarketplaces`; `owner/*` is rejected by add and taken literally (clone fails) in settings |
| `ref` | `github`, `git` | Branch, tag, or full lowercase commit SHA; default is the repo default branch. A SHA needs v2.1.324 or later and is refused for a reserved-name marketplace such as `claude-plugins-official` |
| `path` | `github`, `git` | Marketplace file path in repo; default `.claude-plugin/marketplace.json` |
| `path` | `file` | The file itself, read in place; root is two directories up, so keep it at `<root>/.claude-plugin/marketplace.json` |
| `path` | `directory` | The marketplace root |
| `sparsePaths` | `github`, `git` | Directories for sparse checkout, e.g. `[".claude-plugin", "plugins"]`; set by `marketplace add --sparse` |
| `skipLfs` | `github`, `git` | Accepted, no effect |
| `name` | `settings` | Must equal the `extraKnownMarketplaces` key; cannot be reserved |
| `plugins` | `settings` | Inline catalog; each item takes `name`, `source`, `description`, `version`, `strict`, `headers`, `headersHelper`; item `source` must be an object type |

# Limits and defaults

Valid only in `strictKnownMarketplaces` and `blockedMarketplaces`: `hostPattern` and `pathPattern` (regular expressions tested before fetching), `skills-dir`, and `owner/*` as a `github` `repo` (matches every repo under exactly that owner; needs v2.1.223 or later). If `strictKnownMarketplaces` is set without a `{"source": "skills-dir"}` entry, skills-directory plugins stop loading; locking any customization type with `strictPluginOnlyCustomization` stops them whether or not the entry exists.

# Notes

To keep refreshes and auto-updates from moving a marketplace off a reviewed commit, set `ref` to the full SHA, e.g. `{ "source": "github", "repo": "acme-corp/plugins", "ref": "<40-char sha>" }`. Update Claude Code on every machine first: versions before v2.1.324 cannot load a marketplace pinned this way. Entries with their own remote source can still update, so pin them too (e.g. `sha`).
