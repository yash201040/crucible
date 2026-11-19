---
type: "Guide"
title: "Get started with the desktop app"
description: "Install the Claude desktop app, open the Code tab and run a first session, with pointers to the features to try next."
resource: "https://code.claude.com/docs/en/desktop-quickstart"
tags: [desktop, quickstart, install, code-tab]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [desktop]
requires: "Pro, Max, Ultra, Team or Enterprise subscription"
identifiers:
  - "/code-review"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "desktop-quickstart"
    resource: "https://code.claude.com/docs/en/desktop-quickstart"
    title: "Get started with the desktop app"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The desktop app has Claude Code in its **Code** tab; it includes Claude Code, so Node.js and the CLI are not needed. Installers: macOS universal build, Windows x64, Windows ARM64, Linux (beta, apt or .deb).

# How to use it

1. Install, launch, sign in with an Anthropic account; click **Code**. Prompts: upgrade (need a paid plan), sign in online, or a 403 (see authentication troubleshooting).
2. Pick an environment (Local, Cloud, SSH, WSL) and folder, choose a model, type a task, review changes.
3. Permission modes: Auto (background classifier blocks risky actions), Manual, Accept edits, Plan. Auto/Accept edits show a `+12 -1` indicator for the diff view; Manual shows a diff with approve/decline.
4. Next steps listed: interrupt and steer, `@filename`, skills via `/`, `/code-review`, plugins, panes, Browser preview, PR monitoring, scheduled tasks, parallel sessions with optional worktrees, tasks pane for subagents and background commands, side chat, cloud sessions, connectors.

# Limits and defaults

SSH: Desktop installs Claude Code on the remote on first connect; a running task can continue while disconnected but with a Claude account may stop when its sign-in expires. If a new session shows no environment under the prompt box you have the earlier layout.
