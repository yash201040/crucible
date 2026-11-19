---
type: "Guide"
title: "JetBrains plugin setup and settings"
description: "The Claude Code (Beta) JetBrains plugin: features, install, /ide connection, plugin settings, WSL and remote development fixes."
resource: "https://code.claude.com/docs/en/jetbrains"
tags: [jetbrains, ide, plugin, wsl, diff]
kind: "mixed"
maturity: "beta"
since: ""
surfaces: [ide]
requires: "Claude Code CLI on PATH; paid Claude subscription or Console account"
identifiers:
  - "/ide"
  - "/config"
  - "diffTool"
  - "Cmd+Esc"
  - "Ctrl+Esc"
  - "Cmd+Option+K"
  - "Alt+Ctrl+K"
  - "networkingMode=mirrored"
  - ".wslconfig"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "jetbrains"
    resource: "https://code.claude.com/docs/en/jetbrains"
    title: "JetBrains IDEs"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A plugin (Marketplace "Claude Code [Beta]") for IntelliJ IDEA, PyCharm, Android Studio, WebStorm, PhpStorm, GoLand and most JetBrains IDEs. It runs `claude` in the IDE's integrated terminal and connects to it; it does not bundle the CLI. Anthropic submits it to the JetBrains Marketplace, which is third-party software.

# How to use it

- Features: quick launch (Cmd+Esc / Ctrl+Esc), IDE diff viewer, selection and open-tab context sharing (`Read` deny rules block it for matching files), file references (Cmd+Option+K / Alt+Ctrl+K inserts `@src/auth.ts#L1-99`), diagnostics via the `getDiagnostics` tool.
- Run `claude` in the IDE terminal for automatic connection, or `/ide` from an external terminal (start from the IDE project root).
- `/config` **Diff tool**: `auto` (IDE) or `terminal`; shown only when connected (setting `diffTool`).
- Plugin settings (Settings > Tools > Claude Code [Beta]): **Claude command** (e.g. `claude`, `npx @anthropic-ai/claude-code`; WSL: `wsl -d Ubuntu -- bash -lic "claude"`), suppress not-found notification, Option+Enter multi-line (macOS), automatic updates, **Accept connections from all network interfaces** (Networking, Advanced).
- ESC not interrupting: uncheck "Move focus to the editor with Escape" in Settings > Tools > Terminal.
- WSL2 "No available IDEs detected": add a Windows Firewall rule for the WSL2 subnet (from `hostname -I`) or set `networkingMode=mirrored` in `.wslconfig` (Windows 11 22H2+) then `wsl --shutdown`.

# Limits and defaults

- Remote Development: install the plugin on the remote host (Settings > Plugin (Host)).
- Security: in `acceptEdits` mode Claude may edit IDE config files that the IDE auto-executes; prefer Manual mode for edits.

# Notes

The plugin runs a local MCP server named `ide` (hidden from `/mcp`): ephemeral OS-assigned port (not configurable), unencrypted `ws://`, fresh auth token per IDE start written to `~/.claude/ide/<port>.lock` (or `$CLAUDE_CONFIG_DIR/ide/`) and sent as `X-Claude-Code-Ide-Authorization`. Only `mcp__ide__getDiagnostics` (read-only, one file per call) is visible to the model, relevant to `PreToolUse` hook allowlists. Binds to `127.0.0.1` unless all-interfaces is enabled, which exposes the port and token in cleartext on the network.
