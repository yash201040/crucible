---
type: "Guide"
title: "VS Code extension install and CLI comparison"
description: "Install the Claude Code VS Code extension, sign in, and understand how it differs from the CLI and connects to it."
resource: "https://code.claude.com/docs/en/vs-code"
tags: [vscode, extension, install, ide, cli]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.318"
surfaces: [ide, cli]
requires: "VS Code 1.94.0 or later; any paid Claude plan or Console account"
identifiers:
  - "anthropic.claude-code"
  - "/ide"
  - "autoInstallIdeExtension"
  - "CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL"
  - "claude --resume"
  - "Developer: Reload Window"
  - "Claude Code: Open Walkthrough"
  - "ANTHROPIC_API_KEY"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "vs-code"
    resource: "https://code.claude.com/docs/en/vs-code"
    title: "Use Claude Code in VS Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A graphical Claude Code panel in VS Code (recommended way to use Claude Code there), also installable in Cursor and other VS Code forks (Open VSX). The extension's version number equals the bundled Claude Code version, so a feature needing v2.1.286 needs extension 2.1.286+. The extension bundles a private CLI copy for the chat panel but does not add `claude` to PATH; typing `claude` in the integrated terminal needs the standalone CLI install. Open the panel via the Spark icon in the editor toolbar (needs an open file), Activity Bar sessions list, Command Palette, or the status bar "Claude Code" item.

# How to use it

- Sign in on first open (browser). If `ANTHROPIC_API_KEY` is set in the shell but the sign-in prompt still shows, launch VS Code with `code .` to inherit the environment.
- Extension and CLI share conversation history: continue an extension conversation with `claude --resume`.
- CLI features absent from the extension: `!` Bash shortcut, tab completion; commands and skills are a subset (type `/`).
- CLI connection: integrated terminal auto-connects once the extension is installed; Claude Code v2.1.318 or later does not install the extension for you (`/ide` then reports "No available IDEs detected"). From an external terminal run `/ide`, which installs the extension unless `autoInstallIdeExtension` is false.
- Uninstall: the extension returns after `/ide` from an external terminal or (before v2.1.318) starting `claude` in the integrated terminal. Prevent with `autoInstallIdeExtension` false in `~/.claude.json`, `CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL=1` in a settings `env`, or the "Auto-install IDE extension" `/config` toggle.

# Limits and defaults

- Third-party providers (Bedrock, Agent Platform, Foundry): check `disableLoginPrompt` and configure the provider in `~/.claude/settings.json`; features needing a claude.ai account (plan usage bars, voice dictation, Web tab) are unavailable.
- Claude apps gateway sign-in from the panel requires v2.1.316+.
- Screen reader announcements require v2.1.236+.
- Does not work in Restricted Mode (workspace trust).
