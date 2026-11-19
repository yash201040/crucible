---
type: "Feature"
title: "Computer use in the CLI"
description: "Built-in computer-use MCP server lets Claude see and control macOS apps from an interactive CLI session."
resource: "https://code.claude.com/docs/en/computer-use"
tags: [computer-use, macos, mcp, gui]
kind: "mixed"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: "macOS; Pro, Max or Ultra plan (not Team or Enterprise); claude.ai auth; interactive session (not -p)"
identifiers:
  - "computer-use"
  - "/mcp"
  - "/status"
  - "-p"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "computer-use"
    resource: "https://code.claude.com/docs/en/computer-use"
    title: "Let Claude use your computer from the CLI"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A research preview. Claude can open apps, click, type and read the screen to build and validate native apps, test UIs, debug layout issues and drive GUI-only tools (including the iOS Simulator). It is the broadest and slowest option; Claude prefers an MCP server for the service, then Bash, then Claude in Chrome for browser work, and uses computer use only if none apply.

# How to use it

1. In an interactive session run `/mcp`, select `computer-use` (built-in MCP server, off by default, shown disabled) and choose Enable. The setting persists per project.
2. On first use grant macOS Accessibility (click, type, scroll) and Screen Recording (see screen); then pick Try again. A restart of Claude Code may be needed after Screen Recording.
3. Approve apps per session: a prompt lists apps, extra permissions (such as clipboard) and how many apps get hidden; choose Allow for this session or Deny. Warnings: terminals and IDEs "Can run commands on your computer"; Finder "Can open, change, or delete any file, and run apps and scripts"; System Settings "Can change system settings". Control tiers: browsers and trading platforms view-only, terminals and IDEs click-only, others full control.

# Limits and defaults

- Not available with `-p` (non-interactive), on Linux or Windows (use Desktop), or with Bedrock, Google Cloud Agent Platform or Foundry.
- One session at a time holds a lock taken at first computer-use action and released when the session exits; a second session errors ("Computer use is in use by another Claude session"). A crashed session's lock is released automatically.
- Other visible apps are hidden while Claude works (always on in the CLI) and restored at the end of the turn. The terminal stays visible but is excluded from screenshots.
- Screenshots are downscaled automatically (e.g. 3456x2234 to about 1372x887); no setting for target size.
- Esc anywhere (key consumed) or Ctrl+C aborts; a notification says "press Esc to stop".
- Runs on the real desktop, not the sandboxed Bash tool; trust boundary differs.
- CLI vs Desktop: Desktop supports macOS and Windows, a Settings toggle, a configurable denied-apps list and optional auto-unhide; the CLI has macOS only, enable via `/mcp`, no denied-apps list yet, and no Dispatch integration.
- `computer-use` missing from `/mcp`: check macOS, plan (`/status`), claude.ai auth, interactive session.
