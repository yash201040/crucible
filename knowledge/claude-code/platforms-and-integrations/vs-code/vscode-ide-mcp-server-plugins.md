---
type: "Concept"
title: "VS Code IDE MCP server, MCP and plugin management"
description: "The built-in ide and claude-vscode MCP servers, their two model-visible tools and auth, plus /mcp and /plugins management and install links."
resource: "https://code.claude.com/docs/en/vs-code"
tags: [vscode, mcp, ide-server, plugins, hooks]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [ide, cli]
requires: ""
identifiers:
  - "mcp__ide__getDiagnostics"
  - "mcp__ide__executeCode"
  - "mcp__claude-vscode__getDiagnostics"
  - "X-Claude-Code-Ide-Authorization"
  - "~/.claude/ide/<port>.lock"
  - "CLAUDE_CONFIG_DIR"
  - "claude mcp add"
  - "/mcp"
  - "/plugins"
  - "ms-toolsai.jupyter"
  - "NODE_EXTRA_CA_CERTS"
  - "permissions.deny"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "vs-code"
    resource: "https://code.claude.com/docs/en/vs-code"
    title: "Use Claude Code in VS Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When active, the extension runs a local MCP server named `ide` (hidden from `/mcp`) that the CLI connects to for native diffs, selection for `@` mentions and notebook execution. It binds `127.0.0.1` on a random port 10000-65535 (not configurable) over unencrypted `ws://`; each activation writes a fresh auth token to a lock file at `~/.claude/ide/<port>.lock` (`$CLAUDE_CONFIG_DIR/ide/` if set; mode 0600 in a 0700 directory), and the CLI must send it as the `X-Claude-Code-Ide-Authorization` header.

Only two tools reach the model:

| Tool (as seen by hooks) | What it does | Read-only |
|---|---|---|
| `mcp__ide__getDiagnostics` | Language-server errors and warnings from the Problems panel, optionally for one file | Yes |
| `mcp__ide__executeCode` | Runs Python in the active Jupyter notebook kernel; inserts a cell and a Quick Pick must confirm Execute or Cancel; refuses with no active notebook, no `ms-toolsai.jupyter`, or a non-Python kernel | No |

In the chat panel (v2.1.285+) diagnostics come from a separate built-in server `claude-vscode` (tool `mcp__claude-vscode__getDiagnostics`). Hooks and rules must name both tools; a `Read` deny rule covers neither, so use `permissions.deny` entries for both. The Quick Pick is separate from `PreToolUse` hooks: an allowlist entry only lets Claude propose a run.

# How to use it

- `/mcp` in the panel adds, removes (local/user/project scope; v2.1.261+), enables, disables, reconnects servers and manages OAuth. Same config as `claude mcp add` in the terminal; the command does not validate credentials.
- `/plugins` opens Manage plugins: Plugins and Marketplaces tabs, install scope (for you, for this project, locally), config form on install, uninstall prompts, restart notice. Same commands as the CLI, shared config.
- Install link: `vscode://anthropic.claude-code/install-plugin?plugin=code-review&marketplace=anthropics/claude-plugins-official`. `plugin` required (max 100 chars, ASCII letters/digits/`.`/`_`/`-`); `marketplace` is a GitHub `owner/repo`, an `https://` URL without credentials or query, or a git SSH address, default `anthropics/claude-plugins-official`; pin a ref with `%23`. Invalid links show `Invalid plugin installation URL`.
- Plugins containing mods can draw in the panel (extension 2.1.299+; 2.1.304+ when flags are not fetched, e.g. Bedrock); labels such as "From the token-chart plugin" mark plugin-drawn content.

# Limits and defaults

Selection and open-file context come with each prompt in the CLI too (transcript line `Selected N lines from <file>`); queued messages keep the selection at send time. For TLS-inspecting proxies set `NODE_EXTRA_CA_CERTS` in `env` of `~/.claude/settings.json` (extension 2.1.307+) for dictation and the Web tab.
