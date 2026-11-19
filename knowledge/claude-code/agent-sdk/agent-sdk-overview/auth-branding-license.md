---
type: "Limit"
title: "Agent SDK authentication, branding and license rules"
description: "Third parties may not offer claude.ai login or rate limits; allowed and forbidden branding; Commercial Terms apply."
resource: "https://code.claude.com/docs/en/agent-sdk/overview"
tags: [sdk, authentication, branding, license]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers: []
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-overview"
    resource: "https://code.claude.com/docs/en/agent-sdk/overview"
    title: "Agent SDK overview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Rules for products built on the Agent SDK.

# Limits and defaults

- Authentication: unless previously approved, Anthropic does not allow third-party developers to offer claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK. Use the API key authentication methods in the Quickstart.
- Branding (optional for partners). Allowed: "Claude Agent" (preferred for dropdown menus); "Claude" inside a menu already labeled "Agents"; "{YourAgentName} Powered by Claude" if you have an existing agent name. Not permitted: "Claude Code" or "Claude Code Agent"; Claude Code-branded ASCII art or visual elements that mimic Claude Code. The product must keep its own branding and not appear to be Claude Code or an Anthropic product.
- License: use is governed by Anthropic's Commercial Terms of Service, including for products offered to your own customers, except where a component or dependency has a different license in its LICENSE file.
