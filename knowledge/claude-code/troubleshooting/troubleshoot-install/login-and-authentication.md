---
type: "Guide"
title: "Login and authentication troubleshooting"
description: "Fixes for OAuth errors, 403s, disabled organization, missing role, token expiry, Keychain fallback and cloud-provider credentials."
resource: "https://code.claude.com/docs/en/troubleshoot-install"
tags: [login, oauth, authentication, credentials, keychain]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.211"
surfaces: [cli, ide]
requires: ""
identifiers:
  - "/login"
  - "/logout"
  - "/status"
  - "claude auth login"
  - "ANTHROPIC_API_KEY"
  - "BROWSER"
  - "CLAUDE_CONFIG_DIR"
  - "~/.claude/.credentials.json"
  - "ANTHROPIC_VERTEX_PROJECT_ID"
  - "CLOUD_ML_REGION"
  - "ANTHROPIC_FOUNDRY_API_KEY"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "troubleshoot-install"
    resource: "https://code.claude.com/docs/en/troubleshoot-install"
    title: "Troubleshoot installation and login"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Fixes for sign-in and credential problems.

# How to use it

- Clean reset: `/logout`, close, restart with `claude`, log in again. Press `c` at the login prompt to copy the OAuth URL.
- `OAuth error: Invalid code`: code expired or truncated; retry quickly, or open the URL in a local browser when remote/SSH.
- `API Error: 403 Request not allowed`: check an active Pro/Max/Ultra subscription, or for Console users the "Claude Code" or "Developer" role; proxies can interfere.
- `Claude Code access has not been granted for this account`: Enterprise role is Custom and no custom role grants Claude Code; an Owner must assign a role or change it, then log in again.
- `API Error: 400 ... "This organization has been disabled"` with an active subscription: a stale `ANTHROPIC_API_KEY` overrides subscription OAuth. In `-p` non-interactive mode the key is always used when present. Unset it and check shell profiles; `/status` shows the active method.
- WSL2, SSH, containers: use the separate login URL, paste the code at `Paste code here`, or run `claude auth login` (reads the code from stdin). On WSL2 set `BROWSER` to the Windows browser path.
- Bedrock/Agent Platform/Foundry: errors `Could not load credentials from any providers`, `Could not load the default credentials`, `ChainedTokenCredential authentication failed`. Verify with `aws sts get-caller-identity`, `gcloud auth application-default login` (with `ANTHROPIC_VERTEX_PROJECT_ID` and `CLOUD_ML_REGION` set), or `az login` (or `ANTHROPIC_FOUNDRY_API_KEY`). IDE extensions may not inherit the shell environment.

# Limits and defaults

- Parallel sessions on one machine share a saved login and coordinate renewal so one process refreshes at a time. Before v2.1.211, waking from sleep could make two sessions renew with the same token, revoking the login for all open sessions.
- On macOS, credentials go to the login Keychain; if it rejects writes, login falls back to plaintext `~/.claude/.credentials.json`. `claude doctor` reports `macOS Keychain is not writable`. Fix by `security unlock-keychain ~/Library/Keychains/login.keychain-db`, resync the keychain password, then `/logout` and `/login`. Logging out removes all stored credentials including saved MCP server logins and plugin sensitive values.
- On a full network home directory, login save can fail while `claude auth login` still prints `Login successful.`; free space and sign in again. Before v2.1.318 a valid stored login could be replaced with an empty file.

# Notes

Token validation depends on an accurate system clock.
