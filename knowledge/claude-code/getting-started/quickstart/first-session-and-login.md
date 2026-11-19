---
type: "Guide"
title: "First session, login and account types"
description: "Starting claude in a project, the accepted account types, login behavior, and where Claude Console cost tracking workspace comes from."
resource: "https://code.claude.com/docs/en/quickstart"
tags: [login, authentication, quickstart, accounts]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Claude Pro/Max/Ultra/Team/Enterprise, Claude Console account, or a supported cloud provider"
identifiers:
  - "claude"
  - "claude --version"
  - "/login"
  - "/help"
  - "/resume"
  - "ANTHROPIC_API_KEY"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "quickstart"
    resource: "https://code.claude.com/docs/en/quickstart"
    title: "Quickstart"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Install (same commands as the [overview](../overview/install-and-surfaces.md)), confirm with `claude --version` (prints a version number followed by `(Claude Code)`), then run `claude` in a project directory.

# How to use it

On first use Claude Code prompts for login. Accepted accounts:
- Claude Pro, Max, Ultra, Team or Enterprise (recommended).
- Claude Console (API access, pre-paid credits). First login automatically creates a "Claude Code" workspace in the Console for centralized cost tracking.
- Amazon Bedrock, Google Cloud's Agent Platform or Microsoft Foundry.
- A self-hosted Claude apps gateway: the admin pre-configures the gateway URL and `/login` opens on the **Cloud gateway** screen for corporate SSO.

If `ANTHROPIC_API_KEY` is set and you approve the key when asked, the login prompt is skipped. Credentials are stored, so login is one-time. `/login` inside a session switches accounts or re-authenticates. The prompt shows version, model and working directory; `/help` lists commands, `/resume` continues a previous conversation.

# Notes

The first approval of a code change uses the session's permission mode; `Shift+Tab` switches it at any time.
