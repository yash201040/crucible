---
type: "Reference"
title: "ENABLE_TOOL_SEARCH values and exceptions"
description: "The ENABLE_TOOL_SEARCH variable (unset, true, auto, auto:N, false) and when tool search is forced off or on."
resource: "https://code.claude.com/docs/en/agent-sdk/tool-search"
tags: [tool-search, env-var, configuration, gateway]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.304"
surfaces: [sdk]
requires: ""
identifiers:
  - "ENABLE_TOOL_SEARCH"
  - "auto"
  - "auto:N"
  - "auto:5"
  - "CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS"
  - "ANTHROPIC_BASE_URL"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-tool-search"
    resource: "https://code.claude.com/docs/en/agent-sdk/tool-search"
    title: "Scale to many tools with tool search"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`ENABLE_TOOL_SEARCH` controls whether and when tool definitions are deferred. Set it in the `env` option of `query()` (TypeScript replaces the subprocess environment, so spread `...process.env`; Python merges into the inherited environment).

# How to use it

| Value | Behavior |
| --- | --- |
| (unset) | On; definitions deferred and discovered on demand. Falls back to upfront loading on models earlier than Opus 4 and Sonnet 4, earlier Agent Platform models, and Azure-hosted Microsoft Foundry |
| `true` | On, same fallbacks |
| `auto` | Off (upfront) until deferrable definitions reach 10% of the model's context window, then on; can stay on in the same conversation even if they later drop below 10% |
| `auto:N` | `auto` with custom percentage; `auto:5` activates at 5%; lower activates sooner |
| `false` | Off; all definitions loaded every turn |

# Limits and defaults

- Models on the SDK's unsupported list load upfront whatever the value. On Google Cloud's Agent Platform: Claude Opus 4.5, Sonnet 4.5, Haiku 4.5 and later default on; earlier models load upfront (their stacks reject the beta header) and cannot be overridden. Before Claude Code v2.1.221 the SDK disabled tool search for all Agent Platform models unless `ENABLE_TOOL_SEARCH` was set.
- Behind an `ANTHROPIC_BASE_URL` gateway it is on by default with nothing to set. Before v2.1.304 it was disabled behind a gateway unless `ENABLE_TOOL_SEARCH` was `true`, `auto` or `auto:N`.
- `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` keeps it off and `ENABLE_TOOL_SEARCH` cannot override. From Claude Code v2.1.227 an organization can keep it on under this variable via managed settings. In a session with the HIPAA configuration it is off and neither the variable nor managed settings turns it back on.
- With `auto`, the threshold counts every deferrable definition: each MCP tool not marked `alwaysLoad`, from any server, plus built-ins that load on demand. Core built-ins (Bash, Read, Edit) load upfront and are not counted. A mod in a plugin can defer a tool or load it upfront, changing the count.
