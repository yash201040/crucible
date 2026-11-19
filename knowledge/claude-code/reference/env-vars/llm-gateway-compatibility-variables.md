---
type: "Reference"
title: "LLM gateway compatibility and host-managed variables"
description: "Variables that adjust system prompt attribution, strip pre-release API features, send hint headers, discover gateway models and let a host own provider routing."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [gateway, compatibility, headers, hosts]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_ATTRIBUTION_HEADER"
  - "CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS"
  - "CLAUDE_CODE_DISABLE_STRUCTURED_OUTPUTS"
  - "CLAUDE_CODE_GATEWAY_HINT_HEADERS"
  - "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY"
  - "CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS"
  - "CLAUDE_CODE_EXTRA_BODY"
  - "CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Compatibility knobs for LLM gateways and third-party hosts that embed Claude Code.

# How to use it

| Variable | What it does |
| :- | :- |
| `CLAUDE_CODE_ATTRIBUTION_HEADER` | `0` omits the attribution block (client version and prompt fingerprint) from the system prompt start. Direct-API caching is unaffected. Some direct-connection setups keep the block on auto mode classifier requests anyway. Before v2.1.181 the block held a per-request token on custom base URLs and Foundry, so set `0` on those versions if a gateway caches on the body or forwards to a third party. |
| `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` | `1` strips pre-release `anthropic-beta` headers, paired body fields and beta tool-schema fields such as `defer_loading` and `eager_input_streaming`. Use when a gateway rejects with `Unexpected value(s)` for the beta header or `Extra inputs are not permitted`; also removes MCP tool search. |
| `CLAUDE_CODE_DISABLE_STRUCTURED_OUTPUTS` | `1` stops sending `output_config.format` and its beta value; other pre-release capabilities stay on. Requires v2.1.288+. |
| `CLAUDE_CODE_GATEWAY_HINT_HEADERS` | `1` sends gateway hint headers (such as `x-claude-code-request-class`, `x-claude-code-compaction`) on a custom proxy or third-party provider; `0` stops them everywhere, including direct API where they are sent by default. Requires v2.1.273+. |
| `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY` | `1` fills the `/model` picker from the gateway's `/v1/models` when `ANTHROPIC_BASE_URL` points at an Anthropic-compatible gateway (LiteLLM, Kong, internal proxy). Off by default; an `availableModels` allowlist still filters (deliver via MDM or managed file, not server-managed settings). |
| `CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS` | Timeout for that discovery request (default `3000`); plain digits only, others keep the default. Requires v2.1.269+. |
| `CLAUDE_CODE_EXTRA_BODY` | JSON object merged into the top level of model request bodies (not some non-conversation requests such as `/model` checks). A shell-exported value also applies to background sessions dispatched with `claude agents` or `--bg`; before v2.1.206 they ignored it. |
| `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` | Set by host platforms embedding Claude Code. Claude Code then ignores provider, endpoint and auth variables in settings files (`CLAUDE_CODE_USE_BEDROCK`, `ANTHROPIC_BASE_URL`, `ANTHROPIC_API_KEY`), ignores managed-settings model keys (`model`, `fallbackModel`, `modelOverrides`) and model variables in a managed `env` block (`availableModels` still applies unless the host supplies its own), and skips the automatic third-party telemetry opt-out. |
