---
type: "Feature"
title: "claude plugin marketplace add"
description: "Adds a marketplace from GitHub, git, URL, local directory or file, or claude.ai and declares it in a settings scope."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, marketplace, sources, add]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.273"
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin marketplace add"
  - "--scope <scope>"
  - "--sparse <paths...>"
  - "--claudeai"
  - "--json"
  - "extraKnownMarketplaces"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude plugin marketplace add <source> [options]` adds a marketplace and declares it in a settings file. Afterwards Claude Code installs dependencies your installed plugins were missing. Marketplace subcommands follow the same exit codes; their `--scope` has no `-s` short form.

# How to use it

| Flag | Description |
| :- | :- |
| `--scope <scope>` | Settings file: `user`, `project` or `local`; default `user` |
| `--sparse <paths...>` | Limit the git checkout to directories (monorepos); `github` and `git` sources only |
| `--claudeai` | Treat the argument as the name of a marketplace hosted on claude.ai. v2.1.273 or later |
| `--json` | Result as JSON on the last stdout line; no effect with `--claudeai`. v2.1.287 or later |

| You type | Source type | Fetch |
| :- | :- | :- |
| `owner/repo`, `owner/repo#ref`, `owner/repo@ref` | `github` | Clone, pinned to `ref` if given |
| `user@host:path[.git][#ref]` | `git` | Clone over SSH |
| `http(s)` URL ending `.git[#ref]` or containing `/_git/` | `git` | Clone (including Azure DevOps) |
| `https://github.com/owner/repo` or `https://gitlab.com/namespace/project` (also http) | `git` | Clone after appending `.git` |
| Any other `http(s)` URL (including self-hosted git host without `.git`) | `url` | Fetch as a `marketplace.json`; append `.git` to clone instead |
| `./path`, `../path`, `/path`, `~/path` to a directory | `directory` | Read in place (Windows `.\`, `..\`, `C:\` work) |
| Same forms to a `.json` file | `file` | Read in place |

For hosts without the `.git` suffix (e.g. AWS CodeCommit) use a git entry in `extraKnownMarketplaces`. `gitlab.com` URLs with nested subgroups clone too.

# Limits and defaults

- Output: `Successfully added marketplace: your-marketplace (declared in project settings)`; repeat add: `Marketplace 'your-marketplace' already on disk — declared in project settings`, exit `0`; unrecognized source: `Invalid marketplace source format. Try: owner/repo, https://..., or ./path`, exit `1`; a bare host like `gitlab.example.com/team/plugins` fails as invalid `owner/repo` shorthand.
- With `--claudeai` (name taken from the `From claude.ai:` section of `marketplace list`), `--scope` and `--sparse` are refused; the marketplace is hosted for your account, not declared in settings, so it cannot be shared through project `.claude/settings.json`.
