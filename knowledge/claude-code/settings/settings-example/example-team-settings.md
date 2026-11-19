---
type: "Guide"
title: "Example: team shared settings.json"
description: "A committed .claude/settings.json with permissions, a PreToolUse hook, marketplace and plugin, sandbox rules, plansDirectory, and caveats."
resource: "https://code.claude.com/docs/en/settings-example"
tags: [settings, example, team, sandbox, hooks]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, cloud]
requires: ""
identifiers:
  - "permissions.allow"
  - "permissions.ask"
  - "permissions.deny"
  - "hooks.PreToolUse"
  - "matcher"
  - "${CLAUDE_PROJECT_DIR}"
  - "extraKnownMarketplaces"
  - "enabledPlugins"
  - "sandbox.enabled"
  - "sandbox.filesystem.allowWrite"
  - "sandbox.network.allowedDomains"
  - "plansDirectory"
  - ".claude/hooks/block-rm.sh"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-example"
    resource: "https://code.claude.com/docs/en/settings-example"
    title: "Example settings files"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A team's `.claude/settings.json` committed at the repo top so everyone gets the same permissions, hooks and plugin marketplace.

# How to use it

| Key | Example | Effect |
| :- | :- | :- |
| `permissions.allow` | `Bash(npm run *)` | run npm scripts without asking |
| `permissions.ask` | `Bash(git push *)` | confirm pushes |
| `permissions.deny` | `Read(./.env)`, `Read(./.env.*)`, `Read(./secrets/**)` | block reads of env files and secrets |
| `hooks.PreToolUse` | matcher `Bash`, hook `type: command`, command `${CLAUDE_PROJECT_DIR}/.claude/hooks/block-rm.sh` | script that can block each Bash command |
| `extraKnownMarketplaces` | `acme-tools` from github repo `acme-corp/claude-plugins` | register marketplace on every clone |
| `enabledPlugins` | `"code-formatter@acme-tools": true` | enable a plugin; an external-source plugin still needs each person to install once |
| `sandbox` | `enabled: true`, `filesystem.allowWrite: ["/tmp/build"]`, `network.allowedDomains: ["registry.npmjs.org", "*.example.com"]` | sandbox commands |
| `plansDirectory` | `"./plans"` | keep plan files in the repo |

# Limits and defaults

- Cloud sessions with one repository outside a project's threads read the committed file too.
- OpenTelemetry exporter variables in repository settings are ignored apart from some values that turn telemetry off; set them in managed settings or each person's user file.
- Allow rules and `extraKnownMarketplaces` take effect after each person trusts this folder itself (not only a parent); deny and ask rules apply in every session.
- Rules match the command as written: `Bash(git push *)` does not match `git -C . push`. `Read(./.env)` stops file tools and commands naming the file (such as `cat .env`) but not `grep -r` over the directory; the `sandbox` block closes that gap because sandbox adds `Read` deny paths to what every sandboxed command cannot read (`sandbox.filesystem.denyRead`).
