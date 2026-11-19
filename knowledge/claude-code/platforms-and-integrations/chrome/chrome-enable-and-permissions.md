---
type: "Feature"
title: "Enabling Chrome by default and permissions"
description: "Install prompt, enabled-by-default setting, site permission prompts, VS Code and plan mode behavior for Chrome tools."
resource: "https://code.claude.com/docs/en/chrome"
tags: [chrome, permissions, context, defaults]
kind: "setting"
maturity: "unlabelled"
since: "2.1.287"
surfaces: [cli, ide]
requires: "Claude in Chrome extension"
identifiers:
  - "--chrome"
  - "/chrome"
  - "@browser"
  - "CLAUDE_CODE_ENABLE_CFC"
  - "deniedMcpServers"
  - "managed-mcp.json"
  - "tabs_context_mcp"
  - "browser_batch"
  - "createIfEmpty"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "chrome"
    resource: "https://code.claude.com/docs/en/chrome"
    title: "Use Claude Code with Chrome"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

How Chrome gets turned on and how browser actions are authorized.

# How to use it

- Enable by default: run `/chrome` in the CLI and pick the default option; in VS Code, `/chrome` then the **Enabled by default** switch. CLI and VS Code share one setting. With it on and Claude Code v2.1.287 or later, each VS Code session connects at start; earlier versions (or setting off) connect when you type `@browser`.
- Install prompt "Claude wants to use your browser": shown at most once per session when the extension is not detected. Choices: Install extension, Not now, Don't ask again. Suppressed if the org blocks the `claude-in-chrome` server via `deniedMcpServers`, or deploys `managed-mcp.json` without allowing Claude in Chrome alongside the managed set.
- Startup dialog "Claude in Chrome extension detected": Yes turns the default on; No or Esc turns it off.
- Site permissions: approve per site when asked (the dialog starts with "Claude in Chrome wants to"). In auto mode, when the classifier approves a browser call the extension can skip its per-site check, unless permission rules deny any site to Claude in Chrome.
- VS Code: prompts appear as chat cards. With Enabled by default, Claude asks before actions on unallowed sites in Manual, Edit automatically, Auto and Bypass permissions modes (in Auto and Bypass until you type `@browser`).
- Plan mode: a prompt appears before recording a GIF or opening a new tab; `tabs_context_mcp` prompts when it sets `createIfEmpty`, and so does a `browser_batch` call including those actions. In an interactive CLI session where bypass permissions mode is available and feature-flag fetching is off, these run without a prompt.

# Limits and defaults

- Enabling by default increases context usage because browser tools and instructions are always loaded.
- A project cannot turn Chrome on: `CLAUDE_CODE_ENABLE_CFC` set to `1` in a project's `.claude/settings.json` or `.claude/settings.local.json` `env` block is ignored with a warning. Use `claude --chrome` or `/chrome`.
- Claude Code starts normally when Chrome is not running.
