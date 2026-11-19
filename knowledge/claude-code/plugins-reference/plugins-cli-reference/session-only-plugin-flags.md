---
type: "Feature"
title: "--plugin-dir and --plugin-url"
description: "Two repeatable claude flags load a plugin from a directory, .zip or URL for one session without installing it; admins can block them."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, plugin-dir, session-only, sideload]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "--plugin-dir <path>"
  - "--plugin-url <url>"
  - "CLAUDE_CODE_PLUGIN_DIRS"
  - "disableSideloadFlags"
  - "plugins"
  - "claude plugin disable <name>@inline"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two `claude` flags load a plugin for one session only, without installing it. Both are repeatable. Plugin authors use them to test before publishing.

# How to use it

| Flag | Description | Example |
| :- | :- | :- |
| `--plugin-dir <path>` | Load from a directory or a `.zip` archive. A folder of plugins loads each child folder holding `.claude-plugin/plugin.json`. One path per flag | `claude --plugin-dir ./my-plugin --plugin-dir ./other.zip` |
| `--plugin-url <url>` | Fetch a plugin `.zip` from a URL; repeat the flag or pass several URLs space-separated in one quoted value | `claude --plugin-url "https://example.com/a.zip https://example.com/b.zip"` |

A plugin loaded this way is session-only; `claude plugin list` shows it only when the same flag precedes the subcommand, as `<name>@inline` under `Session-only plugins`, `--json` `scope` `session`. From the Agent SDK, the `plugins` option is the equivalent of `--plugin-dir`.

# Limits and defaults

- A session-only plugin sharing a name with an installed one wins for that session and the installed copy is skipped; the installed copy loads instead if you disabled the session-only copy with `claude plugin disable <name>@inline`, or managed settings lock that plugin name.
- An administrator can reject both flags, and folders in the `CLAUDE_CODE_PLUGIN_DIRS` variable, with the managed `disableSideloadFlags` setting; Claude Code then prints that the flag is disabled by managed settings and exits `1` without starting.
