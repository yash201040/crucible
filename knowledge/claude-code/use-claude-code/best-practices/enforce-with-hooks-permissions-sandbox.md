---
type: "Feature"
title: "Enforce rules: hooks, permission rules, sandbox"
description: "Hook handler types, onFailure block, deny rules that hold in every mode, sandbox limits, and where a rule's scope lives."
resource: "https://code.claude.com/docs/en/best-practices"
tags: [hooks, permissions, sandbox, deny-rules, managed-settings]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide]
requires: "Sandbox on macOS, Linux, WSL2"
identifiers:
  - "PostToolUse"
  - "PreToolUse"
  - "onFailure"
  - "permissions.allow"
  - "permissions.ask"
  - "permissions.deny"
  - "/sandbox"
  - "/hooks"
  - ".claude/settings.json"
  - ".claude/settings.local.json"
  - "~/.claude/settings.json"
  - "managed-settings.json"
  - "bypassPermissions"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "best-practices"
    resource: "https://code.claude.com/docs/en/best-practices"
    title: "Best practices for Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

If something must happen every time, use a hook, a deny rule or a managed setting; CLAUDE.md is for guidelines.

# How to use it

- Hooks run at fixed points (before or after a tool call, when Claude tries to stop, at session start). Handler can be a shell command, an HTTP POST, an MCP tool call, or a `prompt`/`agent` hook (a model decides, so not deterministic). For real enforcement use `command` or `http`, and add `onFailure: "block"` to also stop the action when the hook crashes or times out.
- Formatter example: `PostToolUse` with matcher `Edit|Write` running `jq -r '.tool_input.file_path'` then `npx prettier --write --ignore-unknown`.
- Migrations rule: a `PreToolUse` hook that exits 2 for paths under `migrations/`; `/hooks` shows the result.
- Permissions example: `allow` `Bash(pnpm tsc --noEmit)`, `ask` `Bash(git push *)`, `deny` `Read(./.env)`, `Read(./.env.local)`, `Read(./secrets/**)`. `deny` rules hold in every mode, including auto and `bypassPermissions`.
- Sandbox: `/sandbox` confines Claude's shell commands (macOS, Linux, WSL2) and picks up `Read` deny and `WebFetch(domain:...)` rules. By default Claude can ask to retry a blocked command outside the sandbox through the normal permission flow; strict sandbox mode (the `/sandbox` Overrides tab) turns that off.

# Limits and defaults

- A `Read` deny rule catches `cat .env` but not a script that opens the file. A `WebFetch` domain deny does nothing about `curl` unless the sandbox is on.
- Rule scope: `.claude/settings.local.json` and `~/.claude/settings.json` are yours alone ("Yes, and don't ask again" saves to the local file). `.claude/settings.json` is the repo's: deny rules apply at once, `allow` rules wait for the folder trust dialog, and workspace trust decides when its hooks start. Managed settings (admin console, MDM, `managed-settings.json`) cannot be overridden by personal files.
- Keep the enforced set small; at about forty hooks and deny rules most are probably preferences.
