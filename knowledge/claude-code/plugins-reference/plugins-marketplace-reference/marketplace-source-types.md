---
type: "Reference"
title: "Marketplace source types"
description: "Marketplace source objects (url, github, git, npm, file, directory, settings, skills-dir, hostPattern, pathPattern) and how each behaves in three settings keys."
resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
tags: [marketplace, marketplace-source, policy, settings]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "extraKnownMarketplaces"
  - "strictKnownMarketplaces"
  - "blockedMarketplaces"
  - "url"
  - "github"
  - "git"
  - "npm"
  - "file"
  - "directory"
  - "settings"
  - "skills-dir"
  - "hostPattern"
  - "pathPattern"
  - "claude plugin marketplace add"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-marketplace-reference"
    resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
    title: "Marketplace reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A marketplace source says where a `marketplace.json` is fetched from. It is built by `claude plugin marketplace add`, written by hand in `extraKnownMarketplaces`, or listed by administrators in `strictKnownMarketplaces` (allowlist) and `blockedMarketplaces` (blocklist).

# How to use it

Type names `url`, `git`, `github` differ from plugin sources: marketplace `url` is a direct link to a `marketplace.json` (fields `url`, `headers`, `headersHelper`); marketplace `git` clones a repo (`url`, `ref`, `path`, `sparsePaths`) and does not exist as a plugin source; marketplace `github` has `repo`, `ref`, `path`, `sparsePaths`.

| Type | Fields | `marketplace add` input | `extraKnownMarketplaces` | `strictKnownMarketplaces` | `blockedMarketplaces` |
| :- | :- | :- | :- | :- | :- |
| `url` | `url`, `headers`, `headersHelper` | `http(s)://` URL not matching a git form | Loads | Allows same URL | Blocks same URL |
| `github` | `repo`, `ref`, `path`, `sparsePaths` | `owner/repo`, `owner/repo@ref`, `owner/repo#ref` | Loads | Allows same `repo`, `ref`, `path`; `repo` may be `owner/*` | Blocks same, and a `git` URL to the same repo |
| `git` | `url`, `ref`, `path`, `sparsePaths` | `user@host:path`, or `http(s)://` URL ending `.git`, containing `/_git/`, or naming a github.com or gitlab.com repo; `#ref` pins | Loads | Allows same URL, `ref`, `path` | Blocks same, and other spellings of the same github.com repo |
| `npm` | `package` | Not produced | Fails: `NPM marketplace sources not yet implemented` | Parses, matches nothing | Parses, matches nothing |
| `file` | `path` | Path to a `.json` file | Loads | Allows same path | Blocks same path |
| `directory` | `path` | Path to a directory | Loads | Allows same path | Blocks same path |
| `settings` | `name`, `plugins`, `owner` | Not produced | Loads | Allows same `name` and identical `plugins` | Blocks same `name` |
| `skills-dir` | none | Not produced | Fails: `Unsupported marketplace source type` | Allows skills-directory plugins | Stops skills-directory plugins loading |
| `hostPattern` | `hostPattern` | Not produced | Fails: `Unsupported marketplace source type` | Allows `github`, `git`, `url` sources whose host matches | Blocks them |
| `pathPattern` | `pathPattern` | Not produced | Fails: `Unsupported marketplace source type` | Allows `file`/`directory` sources whose `path` matches | Blocks them |

# Notes

Source object examples: `extraKnownMarketplaces` maps a marketplace name to `{ "source": { "source": "git", "url": "...", "ref": "main" } }`; the two policy keys are arrays such as `[{ "source": "github", "repo": "your-org/*" }, { "source": "hostPattern", "hostPattern": "^git\\.example\\.com$" }]`.
