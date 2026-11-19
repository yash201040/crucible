---
type: "Feature"
title: "Claude in Chrome browser integration"
description: "Connects Claude Code to the Claude in Chrome extension for browser automation from the CLI or VS Code, with prerequisites and restrictions."
resource: "https://code.claude.com/docs/en/chrome"
tags: [chrome, browser, automation, extension]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide]
requires: "Chrome or Edge (or other Chromium browser), Claude in Chrome extension 1.0.36+, direct Anthropic plan (Pro, Max, Ultra, Team, Enterprise), /login sign-in; not WSL"
identifiers:
  - "--chrome"
  - "/chrome"
  - "claude-in-chrome"
  - "claude setup-token"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "chrome"
    resource: "https://code.claude.com/docs/en/chrome"
    title: "Use Claude Code with Chrome"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code works with the Claude in Chrome extension to drive a visible browser window: live debugging (console and DOM), design verification, web app testing, authenticated apps (it shares the browser login state), data extraction, task automation, file uploads and GIF session recording. Claude opens new tabs, collected into a Chrome tab group tied to the session; on a login page or CAPTCHA it pauses for the user.

# How to use it

`claude --chrome` starts a session with Chrome; a one-time intro dialog appears on first launch. `/chrome` shows status ("Status: Enabled", "Extension: Installed"), manages permissions, reconnects the extension, and picks which connected browser to use. Browser tools are listed via `/mcp` then `claude-in-chrome` then View tools.

Tab group closing in local sessions: `/clear` closes the group (unless surviving work is running); `/resume`, exit, or `/clear` with surviving work close it only if it holds only empty new tabs.

# Limits and defaults

- Works with Chrome and Edge; extension detection/setup also for Brave, Arc, Vivaldi, Opera. Not supported in WSL.
- Chrome stays off if signed in with an API key or a `claude setup-token` token, even with `--chrome`. Not available via Amazon Bedrock, Google Cloud Agent Platform or Microsoft Foundry.
- HIPAA-enabled Enterprise orgs: off by default, an Owner can enable it in Organization settings > Claude in Chrome (BAA does not cover third-party site data). Zero Data Retention orgs: unavailable in Claude Code even with `--chrome`; `/chrome` reports it is disabled by policy.
