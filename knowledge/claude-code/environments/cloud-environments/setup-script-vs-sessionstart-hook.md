---
type: "Guide"
title: "Setup scripts vs SessionStart hooks in the cloud"
description: "When to use each, the order they run, an example dependency-install hook keyed on CLAUDE_CODE_REMOTE, and cloud limitations of hooks."
resource: "https://code.claude.com/docs/en/cloud-environments"
tags: [cloud-sessions, hooks, sessionstart, dependencies]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, web, cloud]
requires: ""
identifiers:
  - "SessionStart"
  - "CLAUDE_CODE_REMOTE"
  - "CLAUDE_PROJECT_DIR"
  - "matcher"
  - "startup|resume"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cloud-environments"
    resource: "https://code.claude.com/docs/en/cloud-environments"
    title: "Configure cloud environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A setup script provisions the VM (toolchains and CLIs not pre-installed). A SessionStart hook does project setup that should run everywhere, local and cloud (such as `npm install`).

# How to use it

| | Setup scripts | SessionStart hooks |
| - | - | - |
| Configured in | Environment dialog (and admin page for shared environments) | A settings file such as repo `.claude/settings.json` |
| Runs | Before Claude Code launches; skipped when a cached environment exists | After Claude Code launches, every session including resumed |
| Where | Cloud sessions only | Local and cloud |

Dependency-install hook in repo `.claude/settings.json`:

```json
{ "hooks": { "SessionStart": [ { "matcher": "startup|resume",
  "hooks": [ { "type": "command",
    "command": "bash \"$CLAUDE_PROJECT_DIR\"/scripts/install_pkgs.sh" } ] } ] } }
```

The script exits at once unless `CLAUDE_CODE_REMOTE` is `true`, `cd`s to `$CLAUDE_PROJECT_DIR`, skips `npm install` while a sha256 file (`node_modules/.install_pkgs.sha256` covering the script, `package.json`, `package-lock.json`) still matches, and runs `pip install -r requirements.txt`. Add any other inputs (workspace `package.json`, `.npmrc`, postinstall inputs) to the hashed list.

Which other hooks run: Anthropic-hosted runs hooks from server-managed settings and, outside a project thread, from the repo (Claude Tag sessions get no server-managed settings). Self-hosted also runs hooks seeded from the runner host's `~/.claude/` and runner-image managed settings. User-level `~/.claude/settings.json` hooks do not reach the cloud.

# Limits and defaults

- One repository per session: with several repositories in an Anthropic-hosted session no repo's `.claude/settings.json` hooks load; use a setup script.
- Not in a project's cloud threads: repo hooks do not run there, whatever the repo count (use a setup script, or runner host settings when self-hosted).
- No cloud-only scoping: exit early unless `CLAUDE_CODE_REMOTE` is `true`.
- Needs network access (fails at None); Bun is a known proxy problem.
- Adds startup latency each start or resume, with no caching.
