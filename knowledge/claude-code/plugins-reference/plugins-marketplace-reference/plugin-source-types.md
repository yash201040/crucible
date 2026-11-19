---
type: "Reference"
title: "Plugin source types"
description: "The seven plugin source types (relative path, github, url, git-subdir, npm, archive, command) with fields and the shared ref and sha pins."
resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
tags: [marketplace, plugin-source, git, pinning]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "source"
  - "github"
  - "url"
  - "git-subdir"
  - "npm"
  - "archive"
  - "command"
  - "repo"
  - "ref"
  - "sha"
  - "path"
  - "package"
  - "version"
  - "registry"
  - "sha256"
  - "timeout"
  - "mode"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-marketplace-reference"
    resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
    title: "Marketplace reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A plugin entry's `source` is a relative-path string or an object whose own `source` key names the type, e.g. `"source": { "source": "github", "repo": "your-org/formatter" }`.

# How to use it

| Type | Fields | Notes |
| :- | :- | :- |
| Relative path | the string itself | Directory inside the marketplace, resolved from the root; must start with `./` unless a bare name under `metadata.pluginRoot`; `"."` means the root |
| `github` | `repo`, `ref`, `sha` | `owner/repo` form |
| `url` | `url`, `ref`, `sha` | Any git repository by URL |
| `git-subdir` | `url`, `path`, `ref`, `sha` | One subdirectory, via sparse checkout |
| `npm` | `package`, `version`, `registry` | npm package or tarball; unpacked without running install scripts |
| `archive` | `url`, `sha256` | Zip over HTTPS |
| `command` | `command`, `timeout`, `mode` | Directory printed by a command run on the user's machine |

`git` exists only as a marketplace source, `npm` is both, and `git-subdir`, `archive`, `command` are plugin-only. `url` and `github` also exist as marketplace sources with different meanings (see [marketplace source types](./marketplace-source-types.md)). Use a relative path for a subdirectory of the marketplace repo itself, `git-subdir` for another repo.

# Limits and defaults

`github`, `url` and `git-subdir` share:

- `ref`: branch or tag; defaults to the repo's default branch.
- `sha`: full 40-character lowercase commit SHA. With both set, `sha` is checked out; on most hosts (GitHub, GitLab, Bitbucket) install succeeds even if the `ref` was deleted upstream while the commit is reachable. Some servers (AWS CodeCommit) cannot fetch by SHA, so `ref` must still exist.

# Notes

Fetching, caching and versioning are described on the plugin loading reference page.
