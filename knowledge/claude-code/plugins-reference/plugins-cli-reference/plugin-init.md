---
type: "Feature"
title: "claude plugin init"
description: "Scaffolds a plugin at ~/.claude/skills/<name>/ that loads next session as <name>@skills-dir with no install step."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, scaffold, skills-dir]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin init"
  - "claude plugin new"
  - "--description <text>"
  - "--author <name>"
  - "--author-email <email>"
  - "--with <components...>"
  - "-f, --force"
  - "~/.claude/skills/<name>/"
  - "<name>@skills-dir"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude plugin init <name> [options]` (alias `new`) scaffolds a plugin at `~/.claude/skills/<name>/`. Unless an administrator blocked skills-directory plugins, it loads in your next session as `<name>@skills-dir`. `<name>` becomes the directory name and the manifest `name`. There is no flag for another location.

# How to use it

| Flag | Description |
| :- | :- |
| `--description <text>` | Manifest description |
| `--author <name>` | Author name; defaults to `git config user.name` |
| `--author-email <email>` | Author email; defaults to `git config user.email` |
| `--with <components...>` | Also scaffold starter files for `skills`, `agents`, `hooks`, `mcp`, `lsp`, `output-style` or `channel` |
| `-f, --force` | Overwrite an existing `.claude-plugin/` at the target |

Example: `claude plugin init my-helper --with skills hooks`. It validates what it wrote and prints `Created plugin "my-helper" at ~/.claude/skills/my-helper` plus the load id and the `claude plugin disable` command.

# Limits and defaults

Exits `1` without writing for: an unknown `--with` value; an existing scaffold without `--force`; a managed marketplace allowlist without the `skills-dir` source, or a blocklist that names it (`Plugins from ~/.claude/skills/ are blocked by your organization's managed settings`).
