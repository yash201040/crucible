---
type: "Feature"
title: "Gateway model discovery via /v1/models"
description: "Opt-in startup query of GET /v1/models that adds claude- or anthropic-named gateway models to the /model picker, with a 3 second default timeout."
resource: "https://code.claude.com/docs/en/llm-gateway-protocol"
tags: [gateway, model-discovery, picker, cache]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.248"
surfaces: [cli]
requires: "Anthropic Messages format gateway; v2.1.269 for the timeout variable"
identifiers:
  - "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY"
  - "CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS"
  - "/v1/models"
  - "~/.claude/cache/gateway-models.json"
  - "CLAUDE_CONFIG_DIR"
  - "availableModels"
  - "replaceBuiltInOptions"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "llm-gateway-protocol"
    resource: "https://code.claude.com/docs/en/llm-gateway-protocol"
    title: "Claude Code gateway compatibility guide"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Set `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1` (own environment or managed settings). Off by default so a gateway behind a shared API key does not expose every model the key can reach.

# How to use it

- Runs only for the Anthropic Messages format. Skipped when any `CLAUDE_CODE_USE_*` variable is set or `ANTHROPIC_BASE_URL` is unset or `api.anthropic.com`. Runs even with nonessential traffic off (before v2.1.257 it did not).
- Request: `GET /v1/models?limit=1000`, 3 second timeout (raise with `CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS`, v2.1.269 or later). Any redirect, even http to https, fails silently.
- Sends `Authorization` (bearer from `ANTHROPIC_AUTH_TOKEN`, else the `apiKeyHelper` value) and `x-api-key`; both since v2.1.248. `ANTHROPIC_CUSTOM_HEADERS` override same-named built-ins. If no credential header resolves (a credential only in custom headers counts as none) it skips and logs `[gatewayDiscovery] skipped`.
- Response `data` array: `id`, optional `display_name`, optional `description`. Entries kept when `id` contains `claude` or `anthropic` anywhere, case-insensitive (before v2.1.223 only a prefix match).

# Limits and defaults

- Picker entry: `display_name` if it differs from `id`, else the recognized model name, else `id`; description collapsed to one line or "From gateway" (before v2.1.257 always "From gateway").
- Only models allowed by the `availableModels` managed setting are added; `replaceBuiltInOptions` hides discovered models.
- A discovered ID matching an existing row, or the model a built-in alias currently resolves to, collapses into that row.
- Cache at `~/.claude/cache/gateway-models.json` (under `CLAUDE_CONFIG_DIR` if set), refreshed each startup; on failure the cached or built-in list is used.
