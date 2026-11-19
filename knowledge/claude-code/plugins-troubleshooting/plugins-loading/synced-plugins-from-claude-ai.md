---
type: "Feature"
title: "Plugins synced from claude.ai"
description: "Plugins turned on for a claude.ai account load in Claude Code as name@synced, with sync timing, sign-in requirements and controls."
resource: "https://code.claude.com/docs/en/plugins/loading"
tags: [plugins, synced, claude-ai, cowork, sync]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.273"
surfaces: [cli, cloud]
requires: "Terminal sync needs Claude Code v2.1.273 or later and a claude.ai sign-in"
identifiers:
  - "syncClaudeAiPlugins"
  - "<name>@synced"
  - "claude plugin disable <name>@synced"
  - "ANTHROPIC_AUTH_TOKEN"
  - "CLAUDE_CODE_OAUTH_TOKEN"
  - "apiKeyHelper"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "--safe-mode"
  - "--setting-sources"
  - "/login"
  - "~/.claude/plugins/.trash/"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-loading"
    resource: "https://code.claude.com/docs/en/plugins/loading"
    title: "Plugin loading reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A plugin turned on for your claude.ai account (including by your org) also loads in Claude Code as `<name>@synced`, with no marketplace and no install record. In terminal sessions skills, agents, hooks, MCP servers and LSP servers load with the same trust as an installed marketplace plugin. Cowork downloads them into the session environment at start.

# How to use it

Terminal sync runs once in the background at each start, downloading new/updated plugins and removing those turned off; if it finishes after the session started you see `Plugins changed. Run /reload-plugins to activate.`. A toggle made during a terminal session applies at next start. In cloud Cowork sessions, if nothing changes after a few messages start a new session.

Controls:
- One plugin: `claude plugin disable <name>@synced` or the `/plugin` Installed tab saves `"<name>@synced": false` in user `enabledPlugins`; put it in committed `.claude/settings.json` to keep it out of a project.
- All: `syncClaudeAiPlugins: false` in user or managed settings; Claude Code stops downloading and at next start moves synced plugins to `~/.claude/plugins/.trash/`. Turning off Skills on claude.ai also stops sync.
- Org-required plugins load even if disabled; `claude plugin disable` refuses with `Plugin "<name>@synced" is required by your organization and can't be disabled here. Contact your admin to change it.` and `claude plugin list` marks `required by your org`.

# Limits and defaults

Not downloaded or loaded in terminal sessions where: `ANTHROPIC_AUTH_TOKEN`, `CLAUDE_CODE_OAUTH_TOKEN` or an `apiKeyHelper` supplies the credential; feature flags are not fetched (e.g. `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`); bare mode or `--safe-mode`; a `--setting-sources` list omits `user`. A sign-in from an earlier version needs a background renewal, or run `/login` again.
