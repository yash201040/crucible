---
type: "Guide"
title: "Claude Code on mobile"
description: "The Claude iOS and Android app as a client for cloud sessions, projects, Remote Control and Dispatch, with notifications and limitations."
resource: "https://code.claude.com/docs/en/mobile"
tags: [mobile, remote-control, dispatch, cloud, notifications]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [mobile, cloud]
requires: "claude.ai account; not Console API key or third-party providers; Dispatch needs Pro, Max or Ultra"
identifiers:
  - "/mobile"
  - "/ios"
  - "/android"
  - "claude remote-control"
  - "/remote-control"
  - "~/.claude/uploads/"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mobile"
    resource: "https://code.claude.com/docs/en/mobile"
    title: "Claude Code on mobile"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

There is no separate mobile Claude Code app. The Claude app for iOS and Android (iPad uses the iOS app) is a client: code runs elsewhere. Cloud sessions and Remote Control live in the **Code** tab; Dispatch is a task you message.

| Feature | Connects to | Use when |
| - | - | - |
| Cloud sessions | cloud infrastructure | repo on GitHub, keep running after you leave |
| Projects | conversation coordinating parallel cloud threads | stream of related work |
| Remote Control | session on your computer | needs local files, tools, MCP servers |
| Dispatch | Desktop app | message a task and let Dispatch route it |

# How to use it

- `/mobile` (aliases `/ios`, `/android`) shows a QR code for claude.ai/mobile. Sign in with the same account and organization; open **Code**, or claude.ai/code/new.
- Cloud: select repository and branch, describe the task; sessions persist across devices; can watch a PR and fix CI.
- Remote Control: start with `claude remote-control` or `/remote-control`, scan the QR code or pick the session in the app. Photos are saved under `~/.claude/uploads/` and the path is given to Claude; other files are downloaded and passed as `@` references.
- Push notifications while Remote Control is active when a long task finishes or a decision is needed (two `/config` toggles; you can also ask "notify me when the tests finish"). Dispatch sends its own.

# Limits and defaults

- Terminal-only commands such as `/plugin` and `/resume` do not work from the app.
- Permission modes: cloud sessions Accept edits, Plan, Auto; Remote Control sessions Manual, Accept edits, Plan, Auto; Bypass permissions cannot be selected.
- Dispatch not available on Team or Enterprise. If the machine sleeps during Remote Control, Claude Code reconnects when it is back online; Remote Control and Dispatch need the machine on.
