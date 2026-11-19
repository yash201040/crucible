---
type: "Reference"
title: "Feature pass-through, automatic retries and disabling betas"
description: "Beta header and body field pairs that break behind a gateway, Claude Code's own retry recovery per capability, and CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS scope."
resource: "https://code.claude.com/docs/en/llm-gateway-protocol"
tags: [gateway, betas, retries, tool-search, structured-outputs]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.304"
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS"
  - "CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING"
  - "CLAUDE_CODE_DISABLE_STRUCTURED_OUTPUTS"
  - "CLAUDE_CODE_ENABLE_FINE_GRAINED_TOOL_STREAMING"
  - "CLAUDE_CODE_AUTO_MODE_SERVER"
  - "CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST"
  - "ANTHROPIC_BETAS"
  - "CLAUDE_CODE_EXTRA_BODY"
  - "context_management"
  - "output_config"
  - "output_config.effort"
  - "output_config.format"
  - "output_config.task_budget"
  - "defer_loading"
  - "tool_reference"
  - "strict"
  - "cache_control"
  - "safeguards"
  - "CLAUDE_CODE_USE_MANTLE"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "llm-gateway-protocol"
    resource: "https://code.claude.com/docs/en/llm-gateway-protocol"
    title: "Claude Code gateway compatibility guide"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code treats an `ANTHROPIC_BASE_URL` gateway as an Anthropic-format endpoint and sends the beta headers and body fields it sends to `api.anthropic.com`, except a small set of direct-connection defaults (fine-grained tool streaming is off on a custom base URL; set `CLAUDE_CODE_ENABLE_FINE_GRAINED_TOOL_STREAMING=1` to receive it). A gateway that strips a header while passing its body field, or rewrites or redacts request bodies, produces `400` errors.

# How to use it

| Feature | Pair and symptom |
| - | - |
| Adaptive reasoning | No beta; `thinking: {"type":"adaptive"}` for Opus 4.6, Sonnet 4.6, Haiku 5.5, Fable 5 and later, and unrecognized names. `400` on `thinking`/`adaptive`; upgrade upstream or `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` on Opus 4.6 and Sonnet 4.6 |
| Context management | Beta header with `context_management`; `400 Extra inputs are not permitted` (common with Bedrock upstream) |
| Extended context, interleaved thinking | Beta headers only; silently unavailable if stripped |
| Beta tool fields | `strict`, `defer_loading` with tool betas |
| Effort, structured outputs | `output_config` (effort, format, task budget), each with its own beta; `CLAUDE_CODE_DISABLE_STRUCTURED_OUTPUTS=1` removes only the format (v2.1.288 or later) |
| Mid-conversation system messages | `role: "system"` entries for Opus 4.8, later and unrecognized models; `400 Unexpected role "system"` |
| Effort per turn | On Opus 5.5, Sonnet 5.5, Haiku 5.5, Fable 5.2, Fable 5.1 a beta pairs with `output_config.effort` on `role: "system"` entries |
| Prompt caching | `cache_control` on `system` blocks and messages; stripping gives uncached input every turn, no error |
| Token counting | `count_tokens` endpoint; else estimated counts in `/context` |

Automatic retries (the gateway sees one extra request): thinking type enabled or adaptive switched once (before v2.1.121 no retry); mid-conversation system messages moved into user messages (until `/clear` or compaction); `cache_control` marker moved to the last non-system message; thinking blocks dropped after a signature rejection or `bound to a different conversation`; advisor tool entry dropped (since v2.1.280); `output_config.effort` dropped (the `effort-2025-11-24` beta rejection form needs v2.1.310); `context_management` dropped (v2.1.304); other named `anthropic-beta` values (most need v2.1.314) when the `400` carries the API's `Unexpected value(s)` sentence or `capability_rejected: beta_header:<value>`; tool search fields `defer_loading` and `tool_reference` dropped after `400` or `422` (v2.1.305). A value from `ANTHROPIC_BETAS` is never dropped. Rejected effort/advisor values stay out until Claude Code exits (effort per model, advisor per base URL; advisor then makes `/advisor` unavailable); `context_management` and other covered values stay out for the conversation or until the prompt is rebuilt (compaction), and for the model across new conversations until exit when the error uses the API sentence or `beta_header:` token.

# Limits and defaults

`CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` stops: context management, beta tool fields (`strict`, `defer_loading`), `output_config.format` (v2.1.287 or later), `output_config.task_budget`, MCP tool search. It leaves: extended context, interleaved thinking and effort betas, `output_config.effort`, adaptive `thinking`, `role: "system"` entries, the auto mode server-side classifier review beta and `safeguards` field (turn off with `CLAUDE_CODE_AUTO_MODE_SERVER=0`; also needed when a host sets `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST`), the OAuth beta, and fields from `ANTHROPIC_BETAS` or `CLAUDE_CODE_EXTRA_BODY`. On v2.1.227 or later managed settings can keep MCP tool search on under this variable: kept on direct connections without HIPAA and through `ANTHROPIC_BASE_URL` gateways; no effect on cloud providers or Claude apps gateway; tool search stays off in HIPAA sessions. `ANTHROPIC_DEFAULT_*_MODEL_SUPPORTED_CAPABILITIES` applies only to `CLAUDE_CODE_USE_BEDROCK`, `CLAUDE_CODE_USE_VERTEX`, `CLAUDE_CODE_USE_FOUNDRY` and `CLAUDE_CODE_USE_MANTLE`.
