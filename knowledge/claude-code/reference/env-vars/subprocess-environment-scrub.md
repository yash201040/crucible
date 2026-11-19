---
type: "Feature"
title: "Subprocess environment scrub and script caps"
description: "CLAUDE_CODE_SUBPROCESS_ENV_SCRUB strips credentials from Bash, hook and stdio MCP subprocess environments, with companion call caps and MCP allowlist."
resource: "https://code.claude.com/docs/en/env-vars#what-the-subprocess-environment-scrub-removes"
tags: [security, credentials, subprocess, prompt-injection]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.251"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_SUBPROCESS_ENV_SCRUB"
  - "CLAUDE_CODE_SCRIPT_CAPS"
  - "CLAUDE_CODE_MCP_ALLOWLIST_ENV"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

With `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1`, Claude Code removes credentials from the environments of subprocesses it starts (Bash commands, hooks, stdio MCP servers), reducing what a prompt injection can read. Claude Code itself keeps its credentials for API calls. `claude-code-action` sets it automatically when `allowed_non_write_users` is configured.

# How to use it

- `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB`: `1` to enable. Credentials are recognized by variable name or by value shape; treat it as one layer next to narrow permission rules. Leave unset if a subprocess needs a removed variable.
- `CLAUDE_CODE_SCRIPT_CAPS`: JSON object, used when the scrub is set, limiting how many times scripts may run per session. Keys are substrings matched against command text, values are integer limits, for example `{"deploy.sh": 2}`. Substring matching also counts `./scripts/deploy.sh $(evil)`. Fan-out via `xargs` or `find -exec` is not detected; defense in depth only.
- `CLAUDE_CODE_MCP_ALLOWLIST_ENV`: `1` spawns stdio MCP servers with only a safe baseline environment plus the server's configured `env`, instead of inheriting the shell environment.

| Example variable | What the scrub does |
| :- | :- |
| `ANTHROPIC_API_KEY`, `AWS_SECRET_ACCESS_KEY` | Removes it |
| `NPM_TOKEN`, `DB_PASSWORD` | Removes it (name looks like a credential) |
| `DATABASE_URL` containing a password | Removes it (value looks like a credential) |
| `PIP_INDEX_URL` or `NPM_CONFIG_REGISTRY` containing a password | Keeps the URL, cuts username and password |
| `CLAUDE_CONFIG_DIR` | Removes it |
| `GITHUB_TOKEN`, `GH_TOKEN`, `GH_ENTERPRISE_TOKEN`, `GITHUB_ENTERPRISE_TOKEN` | Leaves in place so `gh` and GitHub API scripts work |
| `HTTP_PROXY`, `HTTPS_PROXY` | Leaves in place, including URL credentials; the sandbox may set them itself |
| `GIT_CONFIG_COUNT`, `GIT_CONFIG_KEY_<n>`, `GIT_CONFIG_VALUE_<n>` | Leaves in place |
| A secret whose name and value look benign | Leaves in place |

# Limits and defaults

- Because `GITHUB_TOKEN` stays, give GitHub Actions jobs the narrowest `permissions`; to remove a GitHub token from sandboxed Bash add a `deny` entry under `sandbox.credentials`.
- On Linux the scrub also runs Bash subprocesses in an isolated PID namespace so they cannot read host process environments through `/proc`; side effect: `ps`, `pgrep` and `kill` cannot see or signal host processes.
- Before v2.1.251 the scrub removed only `ANTHROPIC_API_KEY` and `AWS_SECRET_ACCESS_KEY`.
