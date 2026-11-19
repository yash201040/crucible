---
type: "Feature"
title: "claude plugin tag"
description: "Creates an annotated git tag <name>--v<version> for a plugin release after checking plugin.json and marketplace versions agree."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, release, git-tag]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin tag"
  - "--push"
  - "--dry-run"
  - "-f, --force"
  - "-m, --message <msg>"
  - "--remote <name>"
  - "<name>--v<version>"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude plugin tag [path] [options]` creates an annotated git tag named `<name>--v<version>`. Before tagging it checks that `plugin.json` and any marketplace entry that lists the plugin agree on the version. `[path]` defaults to the current directory; the command finds the marketplace entry by walking up to a `.claude-plugin/marketplace.json` that lists the plugin.

# How to use it

| Flag | Description |
| :- | :- |
| `--push` | Push the tag to `--remote` after creating it |
| `--dry-run` | Print what would be tagged (name, version and source file, marketplace entry, tag name, git commands) |
| `-f, --force` | Skip dirty-working-tree and tag-already-exists checks |
| `-m, --message <msg>` | Annotation; `%s` stands for the version; default `<name> <version>` |
| `--remote <name>` | Remote for `--push`; default `origin` |

Example: `claude plugin tag plugins/formatter --dry-run`. Without `--dry-run` it prints `Created tag formatter--v1.0.0` and `Pushed to origin` or the push command.

# Limits and defaults

Exits `1` with a reason when no `version` in `plugin.json` or marketplace entry, the tag exists, or the working tree is dirty. If the push fails the tag still exists locally and the command exits with an error.
