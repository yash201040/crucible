---
type: "Feature"
title: "/reload-plugins"
description: "Applies pending plugin changes to the running session, with a summary line, a cache guard for MCP changes, and limits in non-interactive sessions."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, reload, prompt-cache, headless]
kind: "slash_command"
maturity: "unlabelled"
since: "2.1.260"
surfaces: [cli, headless, sdk, desktop]
requires: ""
identifiers:
  - "/reload-plugins"
  - "--force"
  - "force"
  - "Reloaded: N plugins · N skills · N agents · N hooks · N plugin MCP servers · N plugin LSP servers"
  - "This reload changes MCP tools"
  - "/reload-plugins isn't available over a remote connection in this session."
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/reload-plugins [--force]` applies pending plugin changes (installed, updated, enabled, disabled or edited on disk since session start) without restarting. Closing the `/plugin` panel with pending changes runs it for you; run it yourself after changes made outside the panel, such as a `claude plugin` command in another terminal.

# How to use it

- `--force` (or `force`) applies the reload even when it would invalidate the prompt cache.
- Summary line: `Reloaded: N plugins · N skills · N agents · N hooks · N plugin MCP servers · N plugin LSP servers` (the MCP server count is omitted in a session without an interactive terminal). Errors add `N errors during load. Run /plugin for details.` The skills count includes `commands/` entries and `SKILL.md` skills; the agents count is all agents loaded in the session. Missing dependencies are installed, reloaded again, and `(+ N dependencies: <names>) resolved` is appended.
- **MCP tool changes**: if the reload would add or remove a plugin MCP server or the `LSP` tool and thereby invalidate the prompt cache, it is not applied; it prints `This reload changes MCP tools (<server>) — your next message will re-read the whole conversation instead of using the cache. Run /reload-plugins --force to apply.`

# Limits and defaults

- **Sessions without an interactive terminal** (desktop app, Agent SDK, `-p` non-interactive mode): runs too, v2.1.260 or later, but only when typed into the session yourself (the `-p` prompt, the desktop prompt box). Arriving through Remote Control or a relayed Slack message, it replies `/reload-plugins isn't available over a remote connection in this session.` and reloads nothing.
- In those sessions the reload does not connect or disconnect plugin MCP servers; those changes take effect next session.
