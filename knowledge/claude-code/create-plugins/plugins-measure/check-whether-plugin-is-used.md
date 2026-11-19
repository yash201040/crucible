---
type: "Feature"
title: "Check whether a plugin is used"
description: "Usage is recorded per machine; users can see it in /plugin, /skill-doctor, /doctor and /usage, and admins via telemetry."
resource: "https://code.claude.com/docs/en/plugins/measure"
tags: [plugins, usage, skill-doctor, doctor]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "/usage breakdown on Pro, Max, Ultra, Team or Enterprise plan"
identifiers:
  - "/plugin"
  - "/skill-doctor"
  - "/doctor"
  - "/usage"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-measure"
    resource: "https://code.claude.com/docs/en/plugins/measure"
    title: "Measure plugin cost and usage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code does not report a plugin's usage back to its author. Usage is recorded on each installer's machine. Administrators can count installs and activations fleet-wide via telemetry or the Analytics API. Teammates can check in four user-run commands.

# How to use it

| Command | What it shows |
| :- | :- |
| `/plugin` Installed tab | Enabled marketplace plugin moves under **Not used recently** after at least 14 days and 10 sessions unused; details show last-used time |
| `/skill-doctor` | Cost and usage of each skill, flags skills in the listing never invoked (including plugin skills); opens in the `/plugin` Stats tab in interactive sessions |
| `/doctor` | Lists user-installed skills, MCP servers and plugins and recommends disabling unused ones |
| `/usage` | Attributes recent usage to skills, subagents, plugins and MCP servers as share of total (Pro, Max, Ultra, Team, Enterprise) |

# Limits and defaults

The **Not used recently** header never appears for plugins loaded with `--plugin-dir` or from a skills directory, plugins enabled via managed settings or a seed directory, or plugins that include a theme, output style, monitor or workflow. An LSP server counts as used when it delivers diagnostics or answers navigation requests. With `strictKnownMarketplaces` set by the organization, neither the header nor last-used time appears.
