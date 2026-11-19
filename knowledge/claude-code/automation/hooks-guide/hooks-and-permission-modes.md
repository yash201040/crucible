---
type: "Concept"
title: "Hooks versus permission modes and mods"
description: "A hook deny holds in every mode including bypassPermissions; allow cannot override deny rules or certain prompts; mods can approve in some setups."
resource: "https://code.claude.com/docs/en/hooks-guide"
tags: [hooks, permissions, bypasspermissions, mods]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "permissionDecision"
  - "bypassPermissions"
  - "--dangerously-skip-permissions"
  - "dontAsk"
  - "CLAUDE_CODE_OAUTH_TOKEN"
  - "managed-mcp.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks-guide"
    resource: "https://code.claude.com/docs/en/hooks-guide"
    title: "Automate actions with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A hook in a settings file or a plugin's `hooks/hooks.json` cannot loosen restrictions past what permission rules allow.

# How to use it

- `"deny"` holds in every mode: `permissionDecision: "deny"` blocks the tool even in `bypassPermissions` or with `--dangerously-skip-permissions`. `PreToolUse` hooks fire before any permission-mode check, including `dontAsk`, so they can enforce policy users cannot bypass by switching modes.
- `"allow"` does not bypass settings deny rules and cannot suppress prompts for network-path reads, MCP tools marked `requiresUserInteraction`, Agent SDK `always_ask` tools (unless the mode approves them) and org-`ask` connector tools. In plan mode an `"allow"` for a file edit gets the same prompt, block or approval as with no hook; approve the plan or switch mode to lift that.

# Notes

If the machine lacks managed settings and a `managed-mcp.json`, and the session does not use `/login` credentials for a Team or Enterprise plan (a session on an API key or long-lived `CLAUDE_CODE_OAUTH_TOKEN` does not count), a mod can approve a call your `PreToolUse` hook blocked. In plan mode a mod can approve such a call only when read-only.
