---
type: "Reference"
title: "MCP installation scopes and precedence"
description: "Local, project and user scopes, where each is stored, approval prompts, and how duplicate servers resolve."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, scopes, precedence, security]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk, cloud]
requires: ""
identifiers:
  - "--scope local"
  - "--scope project"
  - "--scope user"
  - "~/.claude.json"
  - ".mcp.json"
  - "managedMcpServers"
  - "--strict-mcp-config"
  - "--setting-sources"
  - "settingSources"
  - "disabledMcpjsonServers"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

| Scope | Loads in | Shared | Stored in |
|---|---|---|---|
| local (default) | current project only | no | `~/.claude.json` under the project path |
| project | current project only | yes, via version control | `.mcp.json` in project root |
| user | all your projects | no | `~/.claude.json` |

MCP "local scope" differs from general local settings (`.claude/settings.local.json`).

Project-scoped servers prompt for approval in interactive sessions (reset with `claude mcp reset-project-choices`). `claude -p`, Agent SDK and cloud sessions outside a project's threads load them without asking; so does a `bypassPermissions` session with `skipDangerousModePermissionPrompt` set. To keep a server out anyway: add it to `disabledMcpjsonServers` (blocks in every permission mode); exclude project settings with `--setting-sources` or SDK `settingSources`; or start with `--strict-mcp-config`, which loads only `--mcp-config` servers (skipping the prompt for project servers not loaded needs v2.1.246 or later).

# Limits and defaults

Precedence (highest first): local, project, user, plugin-provided, claude.ai connectors. The whole entry of the winning source is used, with no field merging. Scopes match duplicates by name; plugins and connectors match by endpoint (URLs equal ignoring case of scheme/host, default port, trailing slash; a different path, query, userinfo or non-default port is a different server). A server from the `managedMcpServers` managed setting outranks all (v2.1.259 or later).
