---
type: "Reference"
title: "HIPAA configuration: confirmation and what developers see"
description: "How to confirm the configuration is active and which features turn off, including WebFetch, cloud sessions, feedback, artifacts and credential stripping."
resource: "https://code.claude.com/docs/en/hipaa-setup"
tags: [hipaa, restrictions, mcp-tool-search, credentials, confirmation]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.286"
surfaces: [cli, desktop]
requires: ""
identifiers:
  - "/status"
  - "claude doctor"
  - "--cloud"
  - "/teleport"
  - "/feedback"
  - "/bug"
  - "ENABLE_TOOL_SEARCH"
  - "ANTHROPIC_API_KEY"
  - "ANTHROPIC_AUTH_TOKEN"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hipaa-setup"
    resource: "https://code.claude.com/docs/en/hipaa-setup"
    title: "Set up Claude Code (local mode) for a HIPAA-ready organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Confirm after the Primary Owner applies the configuration: restart `claude` (a running session picks it up within about an hour), see the startup notice `Per your organization's policy, some features are limited · /status for details`, a `HIPAA configured` footer tag (before v2.1.286 `HIPAA`), and `HIPAA` on the `Organization configuration` line of `/status`. Applying it turns the Code tab off in Desktop until an Owner turns the **Desktop** toggle back on. If missing, check account and connection, an `Organization policy` line in `/status` (or `claude doctor` outside a session) for a blocked policy fetch, or that it is not applied yet.

# How to use it

| What a developer notices | Why |
| - | - |
| WebFetch unavailable | Off; web search still works |
| `--cloud`, `/teleport`, Remote Control refused | Cloud sessions and Remote Control off |
| `/feedback`, `/bug` unavailable | Feedback off |
| Cannot publish an artifact | Artifact publishing off |
| MCP tools load upfront | MCP tool search off; `ENABLE_TOOL_SEARCH` and managed settings cannot turn it on |
| MCP server or hook reading `ANTHROPIC_API_KEY` stops authenticating | Anthropic credentials (`ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`) are removed from shell commands, hooks and MCP servers Claude Code starts |
| Restrictions remain after `/login` to another organization | HIPAA status lasts until restart |

# Limits and defaults

Cloud provider and GitHub credentials are not removed, and the BAA does not cover data sent to those services. Use permission rules and the sandbox to limit commands and hosts.
