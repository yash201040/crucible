---
type: "Feature"
title: "Validate: README install-line advice"
description: "An Advice block means a plugin README lacks a marketplace install line; it never changes the verdict or exit code."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, validate, readme, advice]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.295"
surfaces: [cli]
requires: ""
identifiers:
  - "Advice"
  - "/plugin install <plugin> --marketplace <source>"
  - "<owner>/<repo>"
  - "plugin i"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An `Advice` block in `claude plugin validate` output means a plugin's README has no line that installs it from a marketplace, and gives a line to add (e.g. `/plugin install deploy-helper --marketplace acme/tools`, which works in one step on Claude Code 2.1.275 or later). Requires v2.1.295 or later. It is not an error or warning and changes neither the verdict nor the exit code, with or without `--strict`.

# How to use it

Paste the suggested line into the README it names and rerun validate. A placeholder `<owner>/<repo>` must be replaced first: when you validated the plugin's own directory and the marketplace lists it from a directory inside its own, validate that directory instead, otherwise fill it in yourself; when you validated the marketplace directory, the source is taken from the `origin` remote of the top-level `.git` (replace manually if unusable).

# Limits and defaults

An existing line counts when `plugin install` or `plugin i` (either `/plugin` or `claude plugin` spelling) is followed on the same line by `<plugin>@<marketplace>`, or by the plugin name and `--marketplace <source>`.
