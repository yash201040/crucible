---
type: "Guide"
title: "Logging in and account types"
description: "First-launch login, supported account types, multiple accounts via CLAUDE_CONFIG_DIR, and why the login prompt may reappear."
resource: "https://code.claude.com/docs/en/authentication"
tags: [login, accounts, config-dir, auth]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.290"
surfaces: [cli]
requires: ""
identifiers:
  - "claude auth login"
  - "claude auth logout"
  - "/login"
  - "/logout"
  - "CLAUDE_CONFIG_DIR"
  - "ANTHROPIC_API_KEY"
  - "forceLoginOrgUUID"
  - "forceLoginMethod"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "authentication"
    resource: "https://code.claude.com/docs/en/authentication"
    title: "Authentication"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

On first launch `claude` opens a browser login unless an approved `ANTHROPIC_API_KEY` is set or an earlier `claude auth login` (or a dev-container credentials volume) exists. Accounts: Claude Pro/Max/Ultra, Teams/Enterprise, Console, cloud providers (Bedrock, Vertex, Foundry; set env vars or pick "3rd-party platform" in the wizard for Bedrock and Vertex), or a self-hosted Claude apps gateway (corporate SSO; the gateway token is the only credential).

# How to use it

- Press `c` to copy the login URL; paste a displayed code at `Paste code here if prompted`.
- `/logout` logs out and resets first-launch setup state.
- Several accounts at once: set `CLAUDE_CONFIG_DIR` per account, e.g. `alias claude-work='CLAUDE_CONFIG_DIR=~/.claude-work claude'`. Each directory has its own settings, history and login. Keyless Console sign-ins are stored outside the config directory so they are not kept apart.

# Limits and defaults

The login prompt can reappear after an earlier sign-in when: the sign-in expired, `forceLoginOrgUUID` restricts organizations, `forceLoginMethod` requires a different kind (with `"claudeai"` a Console API key does not count; with `"console"` a claude.ai account does not), or the version is older than v2.1.290 (prompt appeared regardless of sign-in).
