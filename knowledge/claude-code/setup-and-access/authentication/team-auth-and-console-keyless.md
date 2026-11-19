---
type: "Guide"
title: "Team authentication and keyless Console sign-in"
description: "Setting up Teams, Enterprise, Console and cloud auth, Console roles, and signing in to Console without an API key."
resource: "https://code.claude.com/docs/en/authentication#set-up-team-authentication"
tags: [teams, console, keyless, oauth-profile]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.242"
surfaces: [cli]
requires: "Claude Code v2.1.242 or later for keyless Console sign-in"
identifiers:
  - "ANTHROPIC_PROFILE"
  - "ant auth login"
  - "ant auth logout"
  - "forceLoginOrgUUID"
  - "forceLoginMethod"
  - "apiKeyHelper"
  - "ANTHROPIC_AUTH_TOKEN"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "authentication"
    resource: "https://code.claude.com/docs/en/authentication"
    title: "Authentication"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Options for teams: Claude for Teams or Enterprise (recommended; Teams has SSO and server-managed settings, Enterprise adds domain capture, role-based permissions and the compliance API), Claude Console, Claude apps gateway, Bedrock, Vertex, Foundry. Console roles: **Claude Code** (can only create Claude Code API keys) and **Developer** (any key).

# How to use it

At `/login` choose the Console account, then either "Sign in with your Console account" (labeled `(recommended)`; stores an OAuth token as an Anthropic profile, creates no API key) or "Create an API key" (labeled `(legacy)`). Unset `ANTHROPIC_API_KEY` first. A key is created without asking on cloud providers, when any settings file sets `forceLoginOrgUUID` or `forceLoginMethod: "claudeai"`, when `forceLoginMethod` is `"console"` without `forceLoginOrgUUID` (until retry), or when a managed source exists but cannot be read.

The profile written is `ANTHROPIC_PROFILE`, the active profile, or `default`; a federation profile is refused rather than overwritten. It signs you out of any stored claude.ai login; `/logout` removes and revokes it. Expired profile logins fail until you sign in again.

To stop offering keyless sign-in on managed machines, deploy `forceLoginOrgUUID` (the Console org ID) in managed settings; developers need an API-key-capable role first. Afterwards `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN` and `apiKeyHelper` sessions are refused, and a profile plus a saved API key together is refused.

# Limits and defaults

- Cloud-provider auth: follow provider docs, distribute env vars, install.
- Existing Console logins stay logged in after deployment; a saved key is blocked on machines requiring gateway sign-in or a cloud provider.
