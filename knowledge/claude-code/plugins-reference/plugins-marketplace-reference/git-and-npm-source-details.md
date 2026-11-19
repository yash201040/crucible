---
type: "Reference"
title: "github, url, git-subdir and npm source details"
description: "Field rules and refusals for github, url, git-subdir and npm plugin sources, with examples."
resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
tags: [marketplace, npm, git-subdir, plugin-source]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "github"
  - "url"
  - "git-subdir"
  - "npm"
  - "package"
  - "version"
  - "registry"
  - "repo"
  - "path"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-marketplace-reference"
    resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
    title: "Marketplace reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Details of four of the [plugin source types](./plugin-source-types.md).

# How to use it

| Type | Rules |
| :- | :- |
| `github` | `repo` takes `owner/repo`; `ref`, `sha` optional |
| `url` | Full git URL: `https://`, `http://`, `file://` or `git@`. No `.git` suffix needed (Azure DevOps, AWS CodeCommit work). No `owner/repo` shorthand |
| `git-subdir` | `url` is a full git URL or GitHub `owner/repo`; `path` is the subdirectory; only it is checked out. Over `https` or SSH, a partial clone is requested, so large monorepos need not be fully downloaded on supporting hosts |
| `npm` | `package`: name, name with `@version`, or `https` tarball link. `version`: version, semver range or dist-tag when `package` has no version (omit for `latest`). `registry`: URL for a non-default registry |

# Limits and defaults

npm sources are fetched with the user's npm client; `preinstall`/`postinstall` scripts never run and dependencies are not installed during fetch. With a supported lockfile beside `package.json`, Node.js dependencies are installed in a separate step, also with scripts disabled.

Refused `package` values (install fails naming the value): a git address, folder or `file:` path, or `npm:` alias; a tarball link on github.com, gist.github.com, gitlab.com, bitbucket.org or git.sr.ht (even GitHub release downloads), except a GitLab npm registry link under `gitlab.com/api/v4/`; a tarball link over `http` unless it points at the user's own default npm registry. `registry` must be `https` unless it is the user's own default registry.
