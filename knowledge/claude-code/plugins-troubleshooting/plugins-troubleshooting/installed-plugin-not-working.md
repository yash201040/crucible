---
type: "Reference"
title: "Plugin installed but not working: reload, state files, hooks, MCP, LSP"
description: "Messages and fixes after a successful install: /reload-plugins, cache and records files, settings, hooks, MCP servers and language servers."
resource: "https://code.claude.com/docs/en/plugins/troubleshooting"
tags: [plugins, troubleshooting, hooks, mcp, reload]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.268"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "/reload-plugins"
  - "/reload-plugins --force"
  - "installed_plugins.json"
  - "install_records_unreadable"
  - "failureCode"
  - "claude plugin update"
  - "claude plugin uninstall"
  - "claude update"
  - "claude --debug"
  - "~/.claude/debug/<session-id>.txt"
  - "/mcp"
  - "/plugin configure"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "${CLAUDE_PLUGIN_ROOT}"
  - "PostToolUse"
  - "matcher"
  - "cleanupPeriodDays"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-troubleshooting"
    resource: "https://code.claude.com/docs/en/plugins/troubleshooting"
    title: "Troubleshoot plugins"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Diagnostics for a plugin that installed but does nothing. First check `/plugin` Installed and the Errors tab, then run `/reload-plugins`, which prints `Reloaded:` with counts of plugins, skills, agents, hooks and servers (and `N errors during load. Run /plugin for details.`).

# How to use it

- `Run /reload-plugins to apply.`: the install did not activate (prompt-cache cost or failure); Claude Code runs the reload for you or queues it after the streaming response. Since v2.1.268 this is automatic (before, it stayed pending). A reload that adds/removes a plugin MCP server or the `LSP` tool warns `your next message will re-read the whole conversation instead of using the cache. Run /reload-plugins --force to apply.` Before v2.1.246 the skills count included only `commands/` entries.
- `The packages it lists are not installed` (retry with `claude plugin update <plugin>@<marketplace>`; skipped under `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`) vs `were not installed, because ...` (Yarn/pnpm/`bun.lockb`, or missing manager).
- `Plugin "<name>" not cached at <path>`: `claude plugin install <name>@<marketplace> [--scope project]`, then `/reload-plugins`; before v2.1.323 it could also appear for repo-enabled uninstalled plugins.
- `installed_plugins.json holds a record under "<id>" that this version of Claude Code cannot read`: commands refuse with `Plugin "<name>" was not installed|uninstalled|updated:` and, with `--json`, `failureCode: "install_records_unreadable"`. Fix: `claude update`, else uninstall with the writing version, else delete the record by hand. A rebuilt unreadable file leaves `installed_plugins.unreadable.<date>.<hash>.kept`; unusable keys go to `installed_plugins.set-aside.<date>.<hash>.json`; both age out per `cleanupPeriodDays`.
- `does not load (...), so Claude Code ignores the whole file`: a settings file with an invalid value or non-object top level is ignored entirely, including what the command just wrote.
- `Plugin "<name>" is on in project settings but isn't installed here`: run `claude plugin install <name>@<marketplace> --scope project`, then reload.
- Windows project/local uninstall can leave a second record with a differently spelled path: rerun the same uninstall; before v2.1.295 the rerun failed.
- `Version: unknown` for git plugins: v2.1.302 or later, then `claude plugin marketplace update` and `claude plugin update <plugin>@<marketplace> [--scope ...]`.

Hooks: `Couldn't load hooks from <path>: <reason>`, `Failed to load hooks from <path>: <reason>`, `hooks path not found: <path>`, `hooks path escapes plugin directory: <path>`; `... hook error: Failed with non-blocking status code: <stderr>` means the command failed (e.g. `node` not on PATH; an unquoted `${CLAUDE_PLUGIN_ROOT}` with a space in the path needs quotes or exec form). A hook exiting 2 blocks the action and, since v2.1.281, the error ends `This hook comes from the <plugin> plugin.` A loaded hook that never fires: check same-name plugin note (`Its hooks.json hooks do not run`), event name case (e.g. `PostToolUse`), the `matcher`, then use debug logging. `Plugin directory does not exist: <path>` hook failure: run `/reload-plugins` (or `--force` when it says so); shown once per session per event and command.

MCP: `Invalid MCP server config for "<server>": <error>` (`Missing environment variables: <names>`, `URL is unset or invalid` fixed by `/plugin configure <plugin>`, invalid `url` or `headersHelper` referencing `${user_config.*}`); `Bundled MCP server "<name>" was not started: it needs configuration` (Configure on Installed tab; message added v2.1.285). Check `/mcp`; read the server error in `~/.claude/debug/<session-id>.txt` from `claude --debug` (log only, not terminal). A plugin stdio server whose connection failed less than 15 minutes earlier is not started (use Reconnect in `/mcp`). An invalid `.mcp.json` entry is dropped and logged only in the debug log; `claude plugin validate` reports it (since v2.1.281). Works with `--plugin-dir` but fails installed: use `${CLAUDE_PLUGIN_ROOT}` paths.

LSP: failure shows `Executable not found in $PATH: "<binary>"` and `LSP server <name> failed to start: <reason>` in the debug log; install the binary on PATH. High memory (rust-analyzer, pyright): `/plugin disable <plugin>`.
