---
type: "Reference"
title: "Options mapped to features"
description: "Table mapping each Agent SDK option in TypeScript and Python to the feature it controls."
resource: "https://code.claude.com/docs/en/agent-sdk/configuration"
tags: [options, reference, mapping, agent-sdk]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "permissionMode"
  - "permission_mode"
  - "canUseTool"
  - "can_use_tool"
  - "systemPrompt"
  - "system_prompt"
  - "mcpServers"
  - "mcp_servers"
  - "agents"
  - "hooks"
  - "skills"
  - "plugins"
  - "outputFormat"
  - "output_format"
  - "resume"
  - "forkSession"
  - "fork_session"
  - "sessionStore"
  - "session_store"
  - "enableFileCheckpointing"
  - "enable_file_checkpointing"
  - "effort"
  - "sandbox"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-configuration"
    resource: "https://code.claude.com/docs/en/agent-sdk/configuration"
    title: "Configure your agent"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Which option serves which feature. (`allowedTools`, `settingSources`, `model`, `env`, `cwd`, turn and budget caps are covered in sibling concepts.)

# How to use it

| TypeScript | Python | Controls |
| - | - | - |
| `permissionMode` | `permission_mode` | what the agent does without approval |
| `allowedTools` | `allowed_tools` | pre-approved tool calls |
| `canUseTool` | `can_use_tool` | your approval callback |
| `systemPrompt` | `system_prompt` | the agent's instructions |
| `settingSources` | `setting_sources` | which filesystem settings load |
| `mcpServers` | `mcp_servers` | external tool servers |
| `agents` | `agents` | subagent definitions |
| `hooks` | `hooks` | callbacks at lifecycle points |
| `skills` | `skills` | which skills load |
| `plugins` | `plugins` | which plugins load |
| `outputFormat` | `output_format` | structured output schemas |
| `resume` | `resume` | continuing a stored session |
| `forkSession` | `fork_session` | branching a session |
| `sessionStore` | `session_store` | external session persistence |
| `enableFileCheckpointing` | `enable_file_checkpointing` | rewindable file edits |
| `effort` | `effort` | how much work Claude puts into responses |
| `sandbox` | `sandbox` | sandbox behavior for tool execution |

# Notes

For multi-tenant isolation, the hosting page uses `settingSources` / `setting_sources`, `env` and `cwd` to isolate each tenant's settings and memory.
