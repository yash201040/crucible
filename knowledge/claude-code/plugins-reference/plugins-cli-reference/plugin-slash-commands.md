---
type: "Reference"
title: "/plugin session commands"
description: "Forms of /plugin inside an interactive session (aliases /plugins, /marketplace) and which shell subcommands have no session form."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, slash-commands, interactive]
kind: "slash_command"
maturity: "unlabelled"
since: "2.1.275"
surfaces: [cli]
requires: ""
identifiers:
  - "/plugin"
  - "/plugins"
  - "/marketplace"
  - "/plugin help"
  - "/plugin list [--enabled|--disabled]"
  - "/plugin install"
  - "/plugin install <plugin> --marketplace <source>"
  - "/plugin manage"
  - "/plugin stats"
  - "/plugin enable <plugin>"
  - "/plugin disable <plugin>"
  - "/plugin uninstall <plugin>"
  - "/plugin configure <plugin>"
  - "/plugin validate <path>"
  - "/plugin tag"
  - "/plugin marketplace"
  - "/plugin marketplace add [source]"
  - "/plugin marketplace list"
  - "/plugin marketplace update [name]"
  - "/plugin marketplace remove [name]"
  - "/skill-doctor"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/plugin` opens the plugin panel in an interactive session; `/plugins` and `/marketplace` are aliases. They run only in an interactive terminal session; in a non-interactive run such as `claude -p` Claude Code replies that `/plugin` is not available in this environment. The shell subcommands `init`, `update`, `details`, `prune`, `eval`, `eval init` and `test` have no session form. Plugin argument is `name` or `name@marketplace`.

# How to use it

| Command | Aliases | What it does |
| :- | :- | :- |
| `/plugin` | | Opens **Discover** tab; any unrecognized first word does the same |
| `/plugin help` | `--help`, `-h` | Usage list |
| `/plugin list [--enabled\|--disabled]` | `ls` | Prints marketplace-installed plugins inline; unapplied enable state marked `run /reload-plugins to apply` |
| `/plugin install` | `i` | Opens Discover |
| `/plugin install <plugin>` | `i` | Opens plugin details in Discover (`name@marketplace` opens that marketplace's list) |
| `/plugin install <source>` | `i` | Path, URL or `owner/repo` reports a marketplace-not-found error and installs nothing, even for an added source |
| `/plugin install <plugin> --marketplace <source>` | `i` | Adds the marketplace after confirmation if needed, opens details. v2.1.275 or later |
| `/plugin manage` | | Opens **Installed** tab |
| `/plugin stats` | | Opens **Stats** tab where `/skill-doctor` is available, else Discover |
| `/plugin enable <plugin>` / `disable` / `uninstall` | | Opens Installed at the plugin and does it |
| `/plugin configure <plugin>` | `config` | Opens the `userConfig` dialog or reports none declared |
| `/plugin validate <path>` | | Same report as `claude plugin validate`, inline |
| `/plugin tag [path] [--push] [--dry-run] [--force]` | | Creates the release tag; `-f` accepted; other flags or extra args print usage |
| `/plugin marketplace` | `market` | Does nothing visible; pass `add`, `list`, `update` or `remove` |
| `/plugin marketplace add [source]` | `market add` | With a source adds it; without opens **Add marketplace** input |
| `/plugin marketplace list` | `market list` | Prints marketplace names |
| `/plugin marketplace update [name]` | `market update` | Opens **Marketplaces** tab; with name refreshes it |
| `/plugin marketplace remove [name]` | `market remove`, `market rm`, `marketplace rm` | Opens **Marketplaces** tab; with name removes it |

# Limits and defaults

Naming a plugin not on the Installed tab in `enable`, `disable`, `uninstall` or `configure` prints a message ending `installed in this project`.
