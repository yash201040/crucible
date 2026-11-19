---
type: "Feature"
title: "Environment variables in cloud environments"
description: "How .env-format variables on an environment reach sessions, when they refresh, and which ones are treated specially."
resource: "https://code.claude.com/docs/en/cloud-environments"
tags: [cloud-sessions, environment-variables, vm, secrets]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [web, cloud, desktop, mobile]
requires: ""
identifiers:
  - "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE"
  - "OTEL_*"
  - "CLAUDE_CODE_REMOTE"
  - "CLAUDE_CODE_REMOTE_SESSION_ID"
  - "BASH_DEFAULT_TIMEOUT_MS"
  - "BASH_MAX_TIMEOUT_MS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cloud-environments"
    resource: "https://code.claude.com/docs/en/cloud-environments"
    title: "Configure cloud environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Environment variables are set in the environment's dialog in `.env` format, one `KEY=value` per line. Matching quotes around a value are not part of the value. Quote a value that spans lines or contains `#` (unquoted, `#` starts a comment and the rest of the line is dropped).

# How to use it

```text
NODE_ENV=development
LOG_LEVEL=debug
DATABASE_URL=postgres://localhost:5432/myapp
```

- Values become ordinary variables readable by any command Claude runs, except `OTEL_*`: Claude Code keeps those for its own telemetry export and does not pass them to commands.
- Anthropic-hosted: values are read when the session is created and each time Claude Code starts in the VM again (VM restored after idle, or VM reclaimed and rebuilt). After an edit, an existing session keeps old values until then. You cannot pause the VM yourself. To use a value at once, set it on the command (for example `LOG_LEVEL=trace npm test`) or start a new session.
- The session sets some variables itself. `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` set by the session overrides one you add, so adding it has no effect.
- The setup script runs before these variables are set.
- Sessions can read their own ID in `CLAUDE_CODE_REMOTE_SESSION_ID`; the VM carries `CLAUDE_CODE_REMOTE=true` (never true locally).
- To raise command timeouts, add `BASH_DEFAULT_TIMEOUT_MS` and `BASH_MAX_TIMEOUT_MS` (milliseconds).

# Limits and defaults

Anyone who uses the environment can read its variables and setup script. Do not put secrets there; use a [network secret](./network-secrets.md) in an Anthropic-hosted environment. Do not put secrets in a shared environment's variables, since every member's sessions read them.
