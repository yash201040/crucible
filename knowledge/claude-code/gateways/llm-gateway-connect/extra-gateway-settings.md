---
type: "Reference"
title: "Additional gateway variables: headers, discovery, helper, quiet mode"
description: "Custom headers, gateway model discovery, apiKeyHelper caching and the switch that turns off traffic outside the gateway path."
resource: "https://code.claude.com/docs/en/llm-gateway-connect"
tags: [gateway, headers, model-discovery, apikeyhelper, egress]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.227"
surfaces: [cli]
requires: ""
identifiers:
  - "ANTHROPIC_CUSTOM_HEADERS"
  - "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY"
  - "replaceBuiltInOptions"
  - "modelPicker"
  - "claude --debug"
  - "~/.claude/debug/<session-id>.txt"
  - "apiKeyHelper"
  - "CLAUDE_CODE_API_KEY_HELPER_TTL_MS"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "skipWebFetchPreflight"
  - "CLAUDE_CODE_SKIP_FAST_MODE_NETWORK_ERRORS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "llm-gateway-connect"
    resource: "https://code.claude.com/docs/en/llm-gateway-connect"
    title: "Connect Claude Code to an LLM gateway"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Settings beyond the base URL and credential. Set only if the admin names them or the network restricts egress.

# How to use it

| Name | What it does |
| - | - |
| `ANTHROPIC_CUSTOM_HEADERS` | One `Name: Value` pair per line (`\n` between pairs inside a JSON `env` string). Routing/tenant headers count as headers that need approval; from project settings they follow the env-application rules. |
| `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1` | At startup queries the gateway for its model list and adds it to the `/model` picker; each entry shows the gateway description or `From gateway`. `replaceBuiltInOptions` in a `modelPicker` lineup hides discovered names too, except the model in use. Check `[gatewayDiscovery]` lines under `claude --debug` in `~/.claude/debug/<session-id>.txt`. |
| `apiKeyHelper` | Shell command printing only the credential to stdout (script path or PowerShell invocation). Output cached 5 minutes by default; the value is sent in both `Authorization` and `x-api-key`. On v2.1.227 or later extra banner or log text makes the helper fail. |
| `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` | Helper cache lifetime in ms, for example `900000` for 15 minutes. |
| `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` | Stops background traffic to Anthropic and third parties (version checks, telemetry, release notes). |

# Limits and defaults

`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` disables auto-updates; suppresses the fast mode availability check (`CLAUDE_CODE_SKIP_FAST_MODE_NETWORK_ERRORS` restores it); does not affect gateway model discovery (before v2.1.257 it stopped discovery refreshing); does not affect the WebFetch domain safety check, which still calls `api.anthropic.com` (turn off with `skipWebFetchPreflight: true`).
