---
type: "Feature"
title: "strictKnownMarketplaces and blockedMarketplaces"
description: "Managed allowlist and blocklist of plugin marketplace sources, with source types, owner wildcards and exact-match rules."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, plugins, marketplaces, policy]
kind: "setting"
maturity: "unlabelled"
since: "2.1.223"
surfaces: [cli]
requires: "Managed settings"
identifiers:
  - "strictKnownMarketplaces"
  - "allowedMarketplaces"
  - "blockedMarketplaces"
  - "hostPattern"
  - "pathPattern"
  - "skills-dir"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Managed-scope arrays of marketplace source objects. `strictKnownMarketplaces` (alias `allowedMarketplaces`, v2.1.232+) restricts what can be added; `blockedMarketplaces` blocks sources. Both are checked on marketplace add and on plugin install, update, refresh and auto-update, before any network or filesystem operation. Set in the claude.ai admin console they also apply to adding marketplaces from git repos on claude.ai.

# How to use it

`strictKnownMarketplaces` default: unset allows any marketplace; an empty array blocks every source including the official one.

| Source | Fields |
| :- | :- |
| `github` | `repo` required; `ref` (branch, tag or SHA); `path` (marketplace file path) |
| `git` | `url` required; `ref`, `path` |
| `url` | `url` required; `headers` |
| `file` | `path` to a `marketplace.json` |
| `directory` | `path` to a dir containing `.claude-plugin/marketplace.json` |
| `hostPattern` | regex matched anywhere in host; anchor with `^` `$` |
| `pathPattern` | regex matched in `path` of file and directory sources |
| `skills-dir` | no fields |

Rules: exact matching includes `ref` and `path` (both must match or both be undefined). A `url` marketplace downloads only `marketplace.json`, so its plugins cannot use relative-path sources. For git sources `hostPattern` takes the host from URLs with a scheme, or from `user@host:path`; other forms have no host. Any allowlist, even empty, stops `@skills-dir` plugins loading from `~/.claude/skills/` and `.claude/skills/`; add `{ "source": "skills-dir" }` and leave `strictPluginOnlyCustomization` unset to keep them.

Owner wildcards (v2.1.223+): `{ "source": "github", "repo": "acme-corp/*" }` in these two keys only; `*`, `*/plugins`, `acme-corp/tools-*` are invalid.

| Rule | strictKnownMarketplaces | blockedMarketplaces |
| - | - | - |
| Spellings | `owner/repo` only | any spelling resolving to the repo |
| Owner case | sensitive | insensitive |
| `ref` | exact rule | entry without ref blocks all refs |
| `path` | entry without path matches any path | entry without path blocks all paths |

# Notes

- Allow only the official marketplace: `{ "source": "github", "repo": "anthropics/claude-plugins-official" }`. It is auto-registered on first interactive terminal session, but not in non-interactive environments before that, VS Code-only machines, or machines that previously ran under a blocking policy; add it to `extraKnownMarketplaces` or run `claude plugin marketplace add anthropics/claude-plugins-official`.
- `blockedMarketplaces` with `{ "source": "skills-dir" }` stops `@skills-dir` loading without restricting marketplaces.
- Before v2.1.223 owner wildcards matched nothing; before v2.1.234 `hostPattern` also matched some non-SSH git forms.
- Strict vs `extraKnownMarketplaces`: strict is managed-only policy, highest precedence, enforced before network; extra is any file, registers missing marketplaces, can be overridden. Set both to restrict and pre-register.
