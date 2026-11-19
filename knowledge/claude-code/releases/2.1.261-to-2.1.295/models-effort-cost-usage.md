---
type: "Release Digest"
title: "Models, effort, cost and usage, 2.1.261 to 2.1.295"
description: "Release-note entries for new models, effort and Ultracode, pricing, retries, usage figures, telemetry and the Claude apps gateway from 2.1.261 to 2.1.295."
resource: "https://code.claude.com/docs/en/changelog"
tags: [models, effort, cost, usage, telemetry, gateway]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "claude-haiku-5-5"
  - "claude-sonnet-5-5"
  - "claude-opus-5-5"
  - "effortLevel"
  - "maxEffortLevel"
  - "modelSettings"
  - "/effort"
  - "/effort ultracode"
  - "/autocompact"
  - "/fast"
  - "/model"
  - "/cost"
  - "/usage"
  - "/context"
  - "/usage-credits"
  - "/rate-limit-options"
  - "CLAUDE_CODE_DISABLE_1M_CONTEXT"
  - "ANTHROPIC_BASE_URL"
  - "ANTHROPIC_DEFAULT_OPUS_MODEL"
  - "modelOverrides"
  - "CLAUDE_CODE_SUBAGENT_MODEL_FORCE"
  - "availableModels"
  - "enforceAvailableModels"
  - "modelPricing"
  - "multiplier"
  - "pricing"
  - "rate_limits.spend_limit"
  - "used_usd"
  - "limit_usd"
  - "period"
  - "CLAUDE_CODE_OVERLOADED_RETRY_BASE_DELAY_MS"
  - "CLAUDE_CODE_RETRY_WATCHDOG_MAX_WAIT_MS"
  - "CLAUDE_CODE_NONSTREAMING_TIMEOUT_RETRIES"
  - "API_TIMEOUT_MS"
  - "CLAUDE_CODE_GATEWAY_HINT_HEADERS"
  - "x-claude-code-prompt-id"
  - "x-claude-code-request-class"
  - "x-claude-code-agent-type"
  - "x-claude-code-prev-tool-durations"
  - "x-claude-code-compaction"
  - "x-claude-code-context-compacted"
  - "CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS"
  - "OTEL_LOG_TOOL_DETAILS"
  - "OTEL_LOG_RAW_API_BODIES"
  - "OTEL_METRICS_INCLUDE_REPOSITORY"
  - "OTEL_LOG_MANAGED_SETTINGS"
  - "claude_code.llm_request"
  - "claude_code.managed_settings_resolved"
  - "claude_code.at_mention"
  - "user_prompt"
  - "prompt_text"
  - "hook_execution_complete"
  - "tool.output"
  - "upstream_ttfb_ms"
  - "load_test_mode"
  - "assume_role"
  - "guardrail"
  - "telemetry.forward_to"
  - "telemetry.resource_attributes"
  - "store.connect_timeout_seconds"
  - "store.readiness_grace_seconds"
  - "CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY"
  - "CLAUDE_GATEWAY_ALLOW_LOOPBACK"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.261 to 2.1.295"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Release-note rows (bug fixes removed) about new models and their prices, effort levels, retry budgets, spend and usage figures, OpenTelemetry events and the Claude apps gateway. Newest first.

# How to use it

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.295 | 2026-10-08 | Background requests behind a gateway use Haiku 4.5 instead of the session model (fallback to session model). | |
| 2.1.295 | 2026-10-08 | Token counts behind a gateway on Bedrock use AWS CountTokens (grant `bedrock:CountTokens`); gateway upstream `models` list and `timeouts.upstream_ttfb_ms`; `upstream_request_id` in the `inference` audit event; `request-id` response header. | `upstream_ttfb_ms`, `bedrock:CountTokens` |
| 2.1.293 | 2026-10-07 | Claude Haiku 5.5 (`claude-haiku-5-5`) default Haiku on the Anthropic API: 1M context, $0.10/$0.50 per Mtok ($0.50/$2.50 for prompts over 100K). | `claude-haiku-5-5` |
| 2.1.293 | 2026-10-07 | `claude_code.at_mention` logging emits at most 100 agent and 100 MCP-resource events per prompt read. | `claude_code.at_mention` |
| 2.1.292 | 2026-10-06 | `CLAUDE_CODE_OVERLOADED_RETRY_BASE_DELAY_MS` sets a longer base delay for 529 retries; Agent tool `effort` parameter. | `CLAUDE_CODE_OVERLOADED_RETRY_BASE_DELAY_MS` |
| 2.1.290 | 2026-10-05 | Interactive WebSearch budget refills over time (100 calls/hour; `CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR`, 0 turns off) instead of ending after 200. | `CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR` |
| 2.1.290 | 2026-10-05 | `/code-review` at medium effort reports cleanup and CLAUDE.md findings on models without tuned review settings (incl. Opus 5.5, Sonnet 5.5). | `/code-review` |
| 2.1.288 | 2026-10-02 | `/autocompact` saves the auto-compact window per model. | `/autocompact` |
| 2.1.287 | 2026-10-01 | Opus 4.7+ and Fable use a 1M window by default on Bedrock, Vertex, Foundry and gateways, no `[1m]` suffix (`CLAUDE_CODE_DISABLE_1M_CONTEXT=1` keeps 200K); model switches after a flagged message keep your effort; `prompt_text` added to `user_prompt` event. | `CLAUDE_CODE_DISABLE_1M_CONTEXT`, `prompt_text` |
| 2.1.286 | 2026-09-30 | One retry limit covers a whole model call: at most 14 requests with default retry settings; fallback notices say when 1M dropped to 200K. | |
| 2.1.285 | 2026-09-29 | Sessions behind a custom `ANTHROPIC_BASE_URL` use the 1M window of models that have one (Opus 4.7+, Sonnet 5+, Fable); `/autocompact 200k` if the gateway stops at 200K. | `ANTHROPIC_BASE_URL`, `/autocompact` |
| 2.1.285 | 2026-09-29 | Bedrock/Vertex fall back to an older model of the same tier when the default is removed; unusable models remembered up to a day. | |
| 2.1.284 | 2026-09-28 | Claude Sonnet 5.5 (`claude-sonnet-5-5`) default Sonnet on the Anthropic API: 1M context, $2/$10 per Mtok, $0.20/Mtok cache reads. | `claude-sonnet-5-5` |
| 2.1.284 | 2026-09-28 | Ultracode is its own toggle in `/effort` (Tab or `/effort ultracode [on\|off]`), no longer forces xhigh; keybinding actions `effortSlider:decreaseEffort`, `increaseEffort`, `toggleUltracode`. | `/effort ultracode`, `effortSlider:toggleUltracode` |
| 2.1.284 | 2026-09-28 | Retries after a mid-response disconnect share one budget with the request's other retries; safety-flag model switches with pinned Opus (`ANTHROPIC_DEFAULT_OPUS_MODEL`, `modelOverrides`) let the API pick the model. | `ANTHROPIC_DEFAULT_OPUS_MODEL`, `modelOverrides` |
| 2.1.284 | 2026-09-28 | Gateway spend limit in `/usage` and status line shows dollars; `rate_limits.spend_limit` gains `used_usd`, `limit_usd`, `period`; gateway `auth: { google: {} }` for `telemetry.forward_to`; `/rate-limit-options` in `/help`. | `rate_limits.spend_limit`, `used_usd`, `limit_usd`, `period`, `telemetry.forward_to` |
| 2.1.283 | 2026-09-25 | `x-claude-code-prompt-id` gateway hint header (opt in `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1`); `availableModelsMatch` and `deniedModels` managed settings; gateway `load_test_mode` and `mantle` upstream. | `x-claude-code-prompt-id`, `CLAUDE_CODE_GATEWAY_HINT_HEADERS`, `load_test_mode` |
| 2.1.283 | 2026-09-25 | `tool.output` span event includes MCP, WebFetch, WebSearch outputs when `OTEL_LOG_TOOL_CONTENT=1`; compaction spinner counts summary tokens. | `tool.output` |
| 2.1.281 | 2026-09-23 | Gateway: `assume_role`, `guardrail: {id, version}`, `telemetry.resource_attributes`; resume of long sessions faster; "Prompt is too long" recovery summarizes a huge first prompt on its own. | `assume_role`, `guardrail`, `telemetry.resource_attributes` |
| 2.1.280 | 2026-09-22 | Claude Opus 5.5 (`claude-opus-5-5`) default Opus: 1M context, $4/$20 per Mtok, $0.20/Mtok cache reads; default model on Pro and Team Standard changed from Sonnet to Opus. | `claude-opus-5-5` |
| 2.1.280 | 2026-09-22 | Saved effort from before per-model `/effort` no longer applies to new models such as Opus 5.5; Opus 4.7, 4.8, Fable 5 stop holding launch-default effort over `/effort`, `effortLevel` or per-model level in `-p`/SDK; hook output sizes in `hook_execution_complete`. | `effortLevel`, `/effort` |
| 2.1.280 | 2026-09-22 | `/cost` cache-miss causes name thinking mode and display changes. | `/cost` |
| 2.1.277 | 2026-09-18 | Gateway `headers:` map per upstream; `CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1` for proxy-only egress; Fable always in `/model` on the Anthropic API. | `CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY`, `CLAUDE_GATEWAY_ALLOW_LOOPBACK` |
| 2.1.275 | 2026-09-17 | Prompt caching for a `--system-prompt` with a `__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__` line: text above it cached globally; plan-usage reads shared across windows within a minute. | `__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__` |
| 2.1.274 | 2026-09-17 | `effort` attribute on the `claude_code.llm_request` span; `claude_code.managed_settings_resolved` event (`OTEL_LOG_MANAGED_SETTINGS=1` for redacted settings); `OTEL_LOG_RAW_API_BODIES=file:<dir>` writes `index.jsonl` linking requests and responses; gateway `store.connect_timeout_seconds` (default 5 s). | `claude_code.llm_request`, `claude_code.managed_settings_resolved`, `OTEL_LOG_MANAGED_SETTINGS`, `OTEL_LOG_RAW_API_BODIES`, `store.connect_timeout_seconds` |
| 2.1.273 | 2026-09-15 | Gateway hint headers `x-claude-code-request-class`, `-agent-type`, `-prev-tool-durations`, `-compaction`, `-context-compacted`; `OTEL_LOG_TOOL_DETAILS=1` adds real agent, skill, plugin, MCP server names to cost and token metrics. | `x-claude-code-request-class`, `x-claude-code-agent-type`, `x-claude-code-prev-tool-durations`, `x-claude-code-compaction`, `x-claude-code-context-compacted`, `OTEL_LOG_TOOL_DETAILS` |
| 2.1.271 | 2026-09-14 | `modelPricing` managed setting and gateway `pricing` block accept `multiplier` above 1 up to 10. | `modelPricing`, `multiplier` |
| 2.1.269 | 2026-09-11 | `OTEL_METRICS_INCLUDE_REPOSITORY` tags metrics with `vcs.*` attributes; `CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS` extends `/v1/models` discovery timeout (default 3 s). | `OTEL_METRICS_INCLUDE_REPOSITORY`, `CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS` |
| 2.1.268 | 2026-09-10 | Gateway `pricing:` in `gateway.yaml` delivers the same rates to clients via managed settings so `/cost` and telemetry match the spend meter. | `pricing` |
| 2.1.267 | 2026-09-09 | `maxEffortLevel` setting (top-level or per model under `modelSettings`) caps effort on every provider. | `maxEffortLevel`, `modelSettings` |
| 2.1.261 | 2026-09-04 | `/context` token counting uses a local estimate when the token-counting API is unavailable; API no-header retry waits up to `API_TIMEOUT_MS`. | `/context`, `API_TIMEOUT_MS` |
