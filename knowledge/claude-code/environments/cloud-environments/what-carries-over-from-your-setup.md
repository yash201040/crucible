---
type: "Reference"
title: "What carries over into cloud sessions"
description: "Table of which repo, user and organization configuration reaches a cloud session, and how to add personal preferences."
resource: "https://code.claude.com/docs/en/cloud-environments"
tags: [cloud-sessions, configuration, claude-md, hooks]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [web, cloud]
requires: ""
identifiers:
  - "CLAUDE.md"
  - ".claude/settings.json"
  - ".mcp.json"
  - ".claude/rules/"
  - ".claude/skills/"
  - ".claude/agents/"
  - ".claude/commands/"
  - "enabledPlugins"
  - "extraKnownMarketplaces"
  - "NODE_EXTRA_CA_CERTS"
  - "claude mcp add --scope project"
  - "~/.claude/CLAUDE.md"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cloud-environments"
    resource: "https://code.claude.com/docs/en/cloud-environments"
    title: "Configure cloud environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Cloud sessions start from a fresh clone. Whatever is committed is available; whatever is only on your machine is not. Organization policy arrives via server-managed settings.

# How to use it

| Item | In cloud session? | Note |
| - | - | - |
| Repo `CLAUDE.md`, `.claude/rules/`, `.claude/skills/`, `.claude/agents/`, `.claude/commands/` | Yes | Part of the clone |
| Repo `.claude/settings.json` hooks and permission rules | Yes, in a one-repository session | Multi-repo sessions: see settings in cloud sessions |
| Repo `.mcp.json` servers | Yes, one-repository session | Found from the working directory |
| Plugins/marketplaces declared in repo settings (`enabledPlugins`, `extraKnownMarketplaces`) | No | Not installed in cloud |
| Server-managed settings | Yes, except Claude Tag sessions | Fetched at session start; MDM/managed files on your device do not apply (self-hosted sessions also read the runner image's managed file) |
| User `~/.claude/CLAUDE.md`, skills, agents, commands; user-scoped plugins | No | Commit to repo `.claude/` instead; skills enabled on claude.ai load automatically |
| MCP servers from `claude mcp add` at local/user scope | No | Use `claude mcp add --scope project` and commit `.mcp.json` |
| Transport vars in repo `env` (`NODE_EXTRA_CA_CERTS`, mTLS vars) | No | Ignored and noted in the debug log |
| API keys for services | As network secrets | Otherwise stays an env var |
| Interactive auth such as AWS SSO | No | Browser login cannot run in a cloud session |

A cloud thread in a project loads only the repo root `CLAUDE.md`, `.claude/CLAUDE.md` and non-path-specific `.claude/rules/` files.

Personal preferences without committing: a setup script on one of your own (not shared) environments can write `~/.claude/CLAUDE.md` (loaded as user instructions). Verify with `/context`: `/root/.claude/CLAUDE.md` under Memory files.
