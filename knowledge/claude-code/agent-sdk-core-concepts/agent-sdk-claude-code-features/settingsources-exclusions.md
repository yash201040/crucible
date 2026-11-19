---
type: "Limit"
title: "Inputs settingSources does not control"
description: "Managed policy, global config, auto memory, claude.ai connectors and sandbox credentials load regardless; multi-tenant guidance."
resource: "https://code.claude.com/docs/en/agent-sdk/claude-code-features"
tags: [isolation, multi-tenant, managed-settings, auto-memory]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "CLAUDE_CONFIG_DIR"
  - "autoMemoryEnabled"
  - "CLAUDE_CODE_DISABLE_AUTO_MEMORY"
  - "strictMcpConfig"
  - "disableClaudeAiConnectors"
  - "ENABLE_CLAUDEAI_MCP_SERVERS"
  - "CLAUDE_CODE_OAUTH_TOKEN"
  - "sandbox.credentials"
  - "~/.claude.json"
  - "mcpServers"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-claude-code-features"
    resource: "https://code.claude.com/docs/en/agent-sdk/claude-code-features"
    title: "Use Claude Code features in the SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Input | Behavior | To disable |
| :- | :- | :- |
| Managed policy settings (MDM plist, registry, managed file; server-managed settings fetched when authenticating with a qualifying credential) | Always loaded | Remove from host; server-managed settings are controlled by an Owner in your Claude organization, not disableable from the SDK |
| `~/.claude.json` | Always read | Relocate with `CLAUDE_CONFIG_DIR` in `env` |
| Auto memory at `~/.claude/projects/<project>/memory/` | Loaded into system prompt; agent writes memories with `Write`/`Edit` (so those tools must be enabled) | `autoMemoryEnabled: false` or `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` |
| claude.ai MCP connectors | Loaded with claude.ai login; not loaded when `CLAUDE_CODE_OAUTH_TOKEN` holds a `claude setup-token` token; `mcpServers: {}` does not suppress them | `strictMcpConfig: true`, `disableClaudeAiConnectors: true`, or `ENABLE_CLAUDEAI_MCP_SERVERS=false` |
| `sandbox.credentials` `deny` and file `mask` entries in `~/.claude/settings.json` | Kept as restrictions even when user settings are excluded (only narrow sandbox access) | Remove the entries |

# Limits and defaults

Do not rely on default `query()` options for multi-tenant isolation. For multi-tenant deployments run each tenant in its own filesystem and set `settingSources: []` plus `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` in `env`. Server-managed settings are still fetched with an organization credential; filesystem isolation does not remove them.
