---
type: "Guide"
title: "Set the gateway base URL and credential"
description: "Point Claude Code at a gateway with ANTHROPIC_BASE_URL plus ANTHROPIC_AUTH_TOKEN, ANTHROPIC_API_KEY or apiKeyHelper, verify with curl and /status."
resource: "https://code.claude.com/docs/en/llm-gateway-connect"
tags: [gateway, credentials, env, verification]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "ANTHROPIC_BASE_URL"
  - "ANTHROPIC_AUTH_TOKEN"
  - "ANTHROPIC_API_KEY"
  - "apiKeyHelper"
  - "/status"
  - "/logout"
  - "~/.claude/settings.json"
  - ".claude/settings.local.json"
  - "env"
  - "x-api-key"
  - "Authorization"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "llm-gateway-connect"
    resource: "https://code.claude.com/docs/en/llm-gateway-connect"
    title: "Connect Claude Code to an LLM gateway"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A developer needs the gateway base URL and a credential (key, token, or a command that fetches one). Admins may already distribute these via managed settings, device management or an `apiKeyHelper`.

# How to use it

| Credential set in | Header sent | Use when |
| - | - | - |
| `ANTHROPIC_AUTH_TOKEN` | `Authorization: Bearer` | Gateway team said "bearer token" or "Authorization header"; also the default guess |
| `ANTHROPIC_API_KEY` | `x-api-key` | Gateway team said "API key" or "x-api-key" |
| `apiKeyHelper` | both headers | Credential rotates or comes from a vault |

A credential in the wrong variable reaches the gateway in a header it does not read and fails with `401`.

- Shell: `export ANTHROPIC_BASE_URL=https://llm-gateway.example.com` and `export ANTHROPIC_AUTH_TOKEN=...` (PowerShell uses `$env:`). Lasts for that terminal only; an editor launched from the dock will not see them.
- Settings file: put both in the `env` block of `~/.claude/settings.json` (all projects) or `.claude/settings.local.json` (one project). Never put the credential in a project's `.claude/settings.json` (committed and shared). When shell and settings `env` both set a variable, the settings value wins.
- Verify first with a one-token `curl` to `$ANTHROPIC_BASE_URL/v1/messages` (headers `Authorization: Bearer`, `anthropic-version: 2023-06-01`, body `max_tokens: 1`). A JSON response starting `{"id":"msg_` means URL and credential work; an unknown-model error still proves them; `401` means switch variable.
- Confirm in Claude Code: `/status` Status tab shows an `Anthropic base URL` line and an `Auth token` or `API key` line. A `Login method` line naming claude.ai means the gateway credential is not active.
- Check for existing admin configuration: running `claude` and landing on the login screen means no credential was distributed.

# Limits and defaults

- With `ANTHROPIC_AUTH_TOKEN` the variable takes precedence at once; with `ANTHROPIC_API_KEY` interactive mode asks once to approve the key. `/logout` clears a saved login so only the gateway credential remains.
- If the gateway is exported only in the shell, it does not reliably reach background agents hosted by the supervisor; use a settings file for gateways that background agents must always use.
