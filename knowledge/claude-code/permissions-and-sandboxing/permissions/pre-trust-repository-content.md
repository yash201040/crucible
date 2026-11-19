---
type: "Reference"
title: "What runs before you trust a folder"
description: "Which repository-supplied content is used when only a parent is trusted or in claude -p and SDK runs, and how to harden an untrusted run."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, workspace-trust, headless, hooks, security]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "--setting-sources"
  - "settingSources"
  - "--bare"
  - "--settings"
  - "disableAllHooks"
  - "disabledMcpjsonServers"
  - "apiKeyHelper"
  - "awsAuthRefresh"
  - "headersHelper"
  - "extraKnownMarketplaces"
  - "mcpServers"
  - "allowed-tools"
  - ".mcp.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

For content a repository can supply, the two columns are: only a parent folder trusted, and `claude -p` or the SDK in a never-trusted folder (no dialog). The parent column does not apply in a nested repository (interactive shows the dialog; `claude -p`/SDK follows the second column).

# How to use it

| Repository supplies | Parent trusted only | `claude -p` / SDK, never trusted |
| :- | :- | :- |
| Hooks in settings files, `env` block, helper commands such as `apiKeyHelper`, a project skill's hooks and `allowed-tools` | Used | Used |
| `permissions.allow` and `additionalDirectories` in `.claude/settings.json` | Not used until trust dialog accepted (shown again, listing them) | Not used; warning `this workspace has not been trusted` on stderr |
| Frontmatter hooks in a project subagent, a project `@skills-dir` plugin, `extraKnownMarketplaces` from repo or `--add-dir` | Not used, no dialog | Not used |
| Inline `mcpServers` in subagent frontmatter from repo or `--add-dir` | Not used, no dialog | Not used |
| Servers in `.mcp.json` (even if approved in repo settings) | Asks before connecting; repo's own approvals do not count | Connected without asking, approved or not; SDK loads them only when `settingSources` includes project settings; `claude mcp list` still reports pending |
| `headersHelper` on a `.mcp.json` server | Not run until trust dialog accepted (shown again); static `headers` only until then | Not run; static `headers` only; prints `headersHelper not run` per server on stderr |

Before running `claude -p` in a repository you did not write:
- `--setting-sources user` (or SDK `settingSources` without project) reads neither project settings nor `.mcp.json`;
- `--bare` reads no hooks, skills, custom commands, subagents, plugins or `.mcp.json` servers from the project. The project `env` block and helpers such as `awsAuthRefresh` still apply; `apiKeyHelper` is read only from `--settings`;
- `--settings '{"disableAllHooks": true}'` turns hooks off for that run (user settings alone are not enough, since project settings take precedence and can set it back to `false`);
- add a `disabledMcpjsonServers` entry to reject a `.mcp.json` server by name in every session type.

# Notes

The repository at https://github.com/anthropics/claude-code/tree/main/examples/settings has starter settings configurations for common deployment scenarios.
