---
type: "Feature"
title: "sandbox.credentials: deny files and env vars"
description: "Declare credential files and environment variables to hide from sandboxed commands using deny mode, with merge rules across settings scopes."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, credentials, secrets, deny]
kind: "setting"
maturity: "unlabelled"
since: "2.1.246"
surfaces: [cli]
requires: ""
identifiers:
  - "sandbox.credentials"
  - "sandbox.credentials.files"
  - "sandbox.credentials.envVars"
  - "CLAUDE_CODE_SUBPROCESS_ENV_SCRUB"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`sandbox.credentials` names credential files and environment variables to protect from sandboxed commands. Each entry has a file `path` or env var `name` and a `mode` (`deny` or `mask`; see [mask credentials](./mask-credentials.md)). There is no built-in deny list: only what you list is restricted.

# How to use it

```
{ "sandbox": { "enabled": true, "credentials": {
  "files": [ {"path": "~/.aws/credentials", "mode": "deny"}, {"path": "~/.ssh", "mode": "deny"} ],
  "envVars": [ {"name": "GITHUB_TOKEN", "mode": "deny"}, {"name": "NPM_TOKEN", "mode": "deny"} ] } } }
```

- `deny` on a file denies reads in the sandbox (same as `filesystem.denyRead`); `deny` on an env var unsets it before each sandboxed command.
- File protection belongs to the filesystem layer, so it does not apply if filesystem isolation is disabled; env var protection still does.
- File paths follow the sandbox path-prefix rules.

# Limits and defaults

- `deny` entries merge from every scope; any scope can add one, none can remove another scope's.
- Excluding project or local settings sources applies none of their `credentials` entries (v2.1.246+). Excluding user settings keeps its `deny` entries and file `mask` entries as restrictions but drops env var `mask` entries.
- Affects sandboxed Bash only. To strip credentials from all subprocesses, set `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB`.
