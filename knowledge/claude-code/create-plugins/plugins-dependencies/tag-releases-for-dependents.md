---
type: "Feature"
title: "Tag plugin releases with claude plugin tag"
description: "Constraints resolve against git tags named <plugin-name>--v<version>; claude plugin tag validates and creates them."
resource: "https://code.claude.com/docs/en/plugins/dependencies"
tags: [plugins, git-tags, releases, versioning]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin tag"
  - "--push"
  - "--dry-run"
  - "<plugin-name>--v<version>"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-dependencies"
    resource: "https://code.claude.com/docs/en/plugins/dependencies"
    title: "Plugin dependencies"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Version ranges resolve against git tags on the repository that hosts the plugin: for `github`, `url`, `git-subdir` sources, the plugin's own repo; for a relative path such as `./plugins/secrets-vault`, the marketplace repo. Tag each release `<plugin-name>--v<version>` where the version matches `plugin.json` in that commit.

# How to use it

From the plugin directory (with an `origin` remote): `claude plugin tag --push`. Before tagging it validates the plugin, checks `plugin.json` and marketplace entry agree on version (inside a marketplace checkout), requires a clean working tree under the plugin directory, and refuses if the tag exists. Success prints `Created tag secrets-vault--v2.1.0` and, with `--push`, `Pushed to origin`; without `--push` it prints the `git push` command. `--dry-run` shows the plan. A plain `git tag secrets-vault--v2.1.0` also works if you keep versions in sync yourself.
