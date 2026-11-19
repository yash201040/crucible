---
type: "Feature"
title: "claude plugin eval init"
description: "Creates an eval suite in the current plugin directory via an interactive authoring interview, or a blank template with --bare or no terminal."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, evals, scaffold]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.269"
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin eval init"
  - "--bare"
  - "-i, --interactive"
  - "--eval-dir <dir>"
  - "prompt.md"
  - "graders/criteria.md"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude plugin eval init [name] [options]` creates an eval suite. Requires v2.1.269 or later. Run it from the plugin root (the directory with `.claude-plugin/plugin.json` or the skill's `SKILL.md`).

# How to use it

In a terminal it opens an interactive Claude Code session: Claude reads the plugin, asks what it should do well, proposes cases and graders, writes the case files, then runs the cases and reviews the grades with you. With `--bare`, or without a terminal, it writes a blank single-case template. When Claude runs the command inside a Claude Code session, it prints the interview instructions for that session instead of writing a template.

| Option | Description | Default |
| :- | :- | :- |
| `--bare` | Write blank `prompt.md` and `graders/criteria.md` for `<name>` | |
| `-i, --interactive` | Require the interview; fails without a terminal | |
| `--eval-dir <dir>` | Directory below the current directory for cases | Manifest `experimental.evals`, else `evals` |

# Limits and defaults

`name` is a case name, required with `--bare` or without a terminal. It starts with a letter or digit and contains only letters, digits, `.`, `_`, `-`. Names Windows cannot store (e.g. `con`, or ending in `.`) are refused on every platform.
