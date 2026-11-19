---
type: "Reference"
title: "Where /plugin runs and command spellings"
description: "Surfaces where /plugin is unavailable, shell mistakes, and the table of nonexistent plugin command spellings with real equivalents."
resource: "https://code.claude.com/docs/en/plugins/troubleshooting"
tags: [plugins, troubleshooting, cli, headless, commands]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk, desktop, ide, web]
requires: ""
identifiers:
  - "/plugin"
  - "/plugins"
  - "/marketplace"
  - "claude plugin install"
  - "claude plugin marketplace add"
  - "claude plugin uninstall"
  - "claude plugin remove"
  - "claude plugins"
  - "--scope project"
  - "/plugin isn't available in this environment"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-troubleshooting"
    resource: "https://code.claude.com/docs/en/plugins/troubleshooting"
    title: "Troubleshoot plugins"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/plugin` is typed inside a running terminal session and opens an interactive panel. It replies `/plugin isn't available in this environment` in non-interactive mode (`claude -p`), the Agent SDK, the desktop app Code tab, the VS Code extension panel (only with trailing arguments; bare `/plugin` or `/plugins` opens Manage plugins) and the browser at claude.ai/code. In those, use the surface's own Install a plugin tab, or run `claude plugin install <plugin>@<marketplace>` in a shell. Cloud sessions have no plugin browser.

# How to use it

Typing `/plugin ...` at a shell gives `zsh: no such file or directory: /plugin` (Bash: `bash: /plugin: No such file or directory`; PowerShell: not recognized as a cmdlet); start `claude` first or use `claude plugin ...`. `claude: command not found` is a PATH problem (Verify your PATH).

| You typed | Result | Use instead |
|---|---|---|
| `claude plugin add <source>` | `unknown command 'add'` | `claude plugin marketplace add <source>` or `claude plugin install <plugin>@<marketplace>` |
| `claude plugin install <plugin> --project` | `unknown option '--project'` | `... --scope project` |
| `/install <plugin>` | `Unknown command: /install` | `/plugin install <plugin>@<marketplace>` |
| `/plugin add <source>` | panel opens on Discover | `/plugin marketplace add <source>` |
| `marketplace.anthropic.com` as source | invalid marketplace source | `anthropics/claude-plugins-official` |

Aliases that work: `claude plugins` = `claude plugin`; `claude plugin remove` = `claude plugin uninstall`; `/plugins` and `/marketplace` open the `/plugin` panel.
