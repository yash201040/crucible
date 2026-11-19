---
type: "Feature"
title: "Computer use in Desktop"
description: "Research-preview screen and app control on macOS and Windows with per-app tiers, off by default."
resource: "https://code.claude.com/docs/en/desktop"
tags: [desktop, computer-use, research-preview, macos, windows]
kind: "ui"
maturity: "research-preview"
since: ""
surfaces: [desktop]
requires: "Pro, Max or Ultra plan (not Team or Enterprise); macOS 14 or later or Windows; Desktop app running"
identifiers:
  - "Enable computer use"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "desktop"
    resource: "https://code.claude.com/docs/en/desktop"
    title: "Desktop application"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude opens apps and controls your screen. It is the broadest and slowest tool: Claude prefers a connector, then Bash, then Claude in Chrome, then the iOS Simulator pane, and uses computer use only when none applies. On macOS it can run in the background in approved apps.

# How to use it

Settings > This computer > System (or Capabilities) > **Enable computer use**. On Windows it takes effect at once; on macOS grant Accessibility and Screen Recording. Per-app prompt: **Allow for this session** or **Deny**; approvals last the session, or 30 minutes in Dispatch-spawned sessions.

| Tier | Allowed | Apps |
| - | - | - |
| View only | screenshots | browsers, trading platforms |
| Click only | click and scroll | terminals, IDEs |
| Full control | click, type, drag, shortcuts | everything else |

Settings also offer **Denied apps** and **Unhide apps when Claude finishes**.

# Limits and defaults

Off by default. Not available in the Linux desktop app. Runs on your real desktop, unlike the sandboxed Bash tool. The iOS Simulator pane works without computer use.
