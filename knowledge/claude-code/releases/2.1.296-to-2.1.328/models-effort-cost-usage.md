---
type: "Release Digest"
title: "Models, effort, cost and usage, 2.1.296 to 2.1.328"
description: "Release-note changes to models, effort levels, fast mode, context windows, pricing, usage limits, retries and OpenTelemetry cost data between 2.1.296 and 2.1.328."
resource: "https://code.claude.com/docs/en/changelog"
tags: [models, effort, cost, usage, otel, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "claude-fable-5-2"
  - "claude-fable-5-1"
  - "CLAUDE_CODE_SUBAGENT_EFFORT"
  - "CLAUDE_CODE_DISABLE_1M_CONTEXT"
  - "CLAUDE_CODE_MAX_CONTEXT_TOKENS"
  - "CLAUDE_CODE_AUTO_COMPACT_WINDOW"
  - "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE"
  - "CLAUDE_CODE_DISABLE_ULTRATHINK"
  - "ultrathink"
  - "maxEffortLevel"
  - "/effort"
  - "/fast"
  - "/model"
  - "/cost"
  - "/usage"
  - "/usage-credits"
  - "/autocompact"
  - "--max-budget-usd"
  - "--advisor"
  - "advisorModel"
  - "/advisor"
  - "CLAUDE_CODE_DISABLE_ADVISOR_TOOL"
  - "CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT"
  - "CLAUDE_CODE_DISABLE_REFUSAL_FALLBACK"
  - "CLAUDE_CODE_MODEL_CATALOG"
  - "ANTHROPIC_DEFAULT_OPUS_MODEL"
  - "availableModels"
  - "deniedModels"
  - "OTEL_RESOURCE_INCLUDE_HOST"
  - "cache_creation_5m_tokens"
  - "cache_creation_1h_tokens"
  - "api_request"
  - "tool_decision"
  - "anthropic.plan"
  - "anthropic.seat_type"
  - "anthropic.provider"
  - "anthropic.custom_base_url"
  - "claude_code.session.count"
  - "mcp_server.name"
  - "gen_ai.provider.name"
  - "gen_ai.conversation.id"
  - "gen_ai.tool.name"
  - "error.type"
  - "num_hooks"
  - "num_success"
  - "DISABLE_TELEMETRY"
  - "CLAUDE_CODE_DISABLE_FEATURE_FLAGS"
  - "/v1/models"
  - "max_input_tokens"
  - "GET /v1/organizations/analytics/cost"
  - "admin.pooled_conflict_rule"
  - "admin.pooled_priority_order"
  - "pooled_budget"
  - "admin.identity_retention_days"
  - "cleanupPeriodDays"
  - "idleCompaction"
  - "CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.296 to 2.1.328"
stale_after: "2027-01-19T00:00:00Z"
---

# What changed

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.328 | 2026-11-19 | Warning in /status and claude doctor when an OpenTelemetry exporter has no endpoint and its data would likely be lost; gateway startup warning for a policy maxEffortLevel that is not a valid effort level. | `/status`, `maxEffortLevel` |
| 2.1.326 | 2026-11-16 | Added OTEL_RESOURCE_INCLUDE_HOST to add host.name and host.id to OpenTelemetry resource attributes (off by default). | `OTEL_RESOURCE_INCLUDE_HOST` |
| 2.1.326 | 2026-11-16 | Automatic compaction in plan mode uses the model answering you (for example Opus with opusplan), so it can cost more. | |
| 2.1.326 | 2026-11-16 | Cowork cloud sessions hold OpenTelemetry export until the first turn, so claude_code.session.count can fall; /usage in fullscreen shows plan limit bars before session cost. | `claude_code.session.count`, `/usage`, `/cost` |
| 2.1.326 | 2026-11-16 | Idle CPU lower; token counts of background agents update every 5 seconds with over 20 subagents. | |
| 2.1.325 | 2026-11-13 | CLAUDE_CODE_MAX_CONTEXT_TOKENS also sets the context window of unrecognized claude- model IDs such as a gateway's claude-sonnet-latest. | `CLAUDE_CODE_MAX_CONTEXT_TOKENS` |
| 2.1.325 | 2026-11-13 | /cost, $.session.usage(), --max-budget-usd and cost and token metrics count a mod's $.model.complete and $.model.classify calls. | `/cost`, `--max-budget-usd` |
| 2.1.325 | 2026-11-13 | Prompt suggestions refresh less often after 8 consecutive turns started by background or scheduled tasks; replies cut at 32,000 output tokens on unrecognized models continue with a 128,000 limit (2.1.327). | |
| 2.1.323 | 2026-11-12 | Context window assumed for an unrecognized model ID changed from 200K to 1M; /autocompact compacts earlier and CLAUDE_CODE_DISABLE_1M_CONTEXT=1 keeps 200K; smaller-window vendor models can fail every turn until /clear once full. | `/autocompact`, `CLAUDE_CODE_DISABLE_1M_CONTEXT` |
| 2.1.323 | 2026-11-12 | Maximum of CLAUDE_CODE_OVERLOADED_RETRY_MAX_DELAY_MS raised from 64000 to 300000. | `CLAUDE_CODE_OVERLOADED_RETRY_MAX_DELAY_MS` |
| 2.1.323 | 2026-11-12 | Added CLAUDE_CODE_DISABLE_AGENT_PROGRESS_SUMMARIES=1 (available since 2.1.318) to turn off subagent progress summaries and the requests that write them; options menu when a model needs usage credits that are off or used up. | `CLAUDE_CODE_DISABLE_AGENT_PROGRESS_SUMMARIES` |
| 2.1.323 | 2026-11-12 | CLAUDE_AUTOCOMPACT_PCT_OVERRIDE in Anthropic-hosted cloud sessions stops applying to auto-memory extraction and some /btw; OTel mcp server names follow the current connector directory. | `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`, `mcp_server.name` |
| 2.1.323 | 2026-11-12 | Gateway /v1/models states max_input_tokens for models with a certain context window. | `/v1/models`, `max_input_tokens` |
| 2.1.322 | 2026-11-10 | Added fast mode on Vertex in the global, us and eu regions, falling back to standard speed if Vertex refuses it. | |
| 2.1.321 | 2026-11-09 | Added Claude Fable 5.2 (claude-fable-5-2) as the default Fable model: 1M context, 8 and 40 dollars per Mtok, 0.20 per Mtok cache reads. | `claude-fable-5-2` |
| 2.1.321 | 2026-11-09 | Saved Fable 5.1 picks move to fable (Pro and Max at once, Team and Enterprise once the organization allows it); /model claude-fable-5-1 switches back; fast mode labels name the current model. | `claude-fable-5-1`, `/model` |
| 2.1.321 | 2026-11-09 | OTel hook events in non-interactive sessions leave two built-in hooks out of num_hooks and num_success after Bash and PowerShell calls. | `num_hooks`, `num_success` |
| 2.1.319 | 2026-11-06 | Added CLAUDE_CODE_DISABLE_FEATURE_FLAGS to stop feature-flag fetching without turning off telemetry; /usage shows spend for today, this week and this month behind a gateway with no spend limit. | `CLAUDE_CODE_DISABLE_FEATURE_FLAGS`, `/usage` |
| 2.1.319 | 2026-11-06 | Gateway: admin.pooled_conflict_rule and admin.pooled_priority_order choose which pooled group budget pays first; /context table kept short. | `admin.pooled_conflict_rule`, `admin.pooled_priority_order` |
| 2.1.318 | 2026-11-04 | Subagents on a different model use that model's effort; mod $.model.fork gains effort; subagent progress summary on cold cache can wait up to 5 minutes. | |
| 2.1.317 | 2026-11-03 | OTel metrics, events and spans gain anthropic.plan, anthropic.seat_type, anthropic.provider and anthropic.custom_base_url. | `anthropic.plan`, `anthropic.seat_type`, `anthropic.provider`, `anthropic.custom_base_url` |
| 2.1.317 | 2026-11-03 | Gateway cost report GET /v1/organizations/analytics/cost for spend over a date range by total, developer, day or IdP group; daily IdP group record kept for admin.identity_retention_days. | `GET /v1/organizations/analytics/cost`, `admin.identity_retention_days` |
| 2.1.316 | 2026-10-31 | Added CLAUDE_CODE_DISABLE_ULTRATHINK; added CLAUDE_CODE_SUBAGENT_EFFORT; gateway pooled group budgets via pooled_budget on the spend limits admin API. | `CLAUDE_CODE_DISABLE_ULTRATHINK`, `CLAUDE_CODE_SUBAGENT_EFFORT`, `pooled_budget` |
| 2.1.316 | 2026-10-31 | Deprecated fast mode for Opus 4.8 as of October 30, 2026; removed on November 30, 2026 with an error and no fallback to standard Opus 4.8; migrate to Opus 5.5. | |
| 2.1.314 | 2026-10-30 | Idle compaction in VS Code and Desktop's Code tab (200K+ token conversation idle); also runs with telemetry off and on Bedrock, Vertex, Foundry and gateways once the one-hour prompt cache is on; flagged requests retry on another model when ANTHROPIC_DEFAULT_OPUS_MODEL, availableModels or deniedModels leaves only an older Opus. | `ANTHROPIC_DEFAULT_OPUS_MODEL`, `availableModels`, `deniedModels` |
| 2.1.312 | 2026-10-27 | Bedrock, Vertex, Foundry and Mantle use the shorter system prompt for unrecognized model names (CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT=0 keeps full); automatic model switch after a flagged message also covers unrecognized names (CLAUDE_CODE_DISABLE_REFUSAL_FALLBACK=1 turns off); usage limit text says 5-hour limit. | `CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT`, `CLAUDE_CODE_DISABLE_REFUSAL_FALLBACK` |
| 2.1.312 | 2026-10-27 | Claude Code stopped sending the claude_code.safety_event OTel event; OTel mcp_server.name reports real names of official plugin remote servers. | `claude_code.safety_event`, `mcp_server.name` |
| 2.1.311 | 2026-10-26 | ultrathink in the interactive terminal runs its turn at xhigh on Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.1 via the Anthropic API; model names drop the [1m] suffix where it has no effect; models load settings from a signed file (CLAUDE_CODE_MODEL_CATALOG=off disables). | `ultrathink`, `CLAUDE_CODE_MODEL_CATALOG` |
| 2.1.304 | 2026-10-19 | Warning on Pro and Max when resuming an inactive conversation would use a noticeable share of the 5-hour usage limit. | |
| 2.1.302 | 2026-10-16 | Idle compaction row in /config; Fast mode label updates. | `idleCompaction` |
| 2.1.301 | 2026-10-15 | Switching to a model with a smaller context window first summarizes a too-long conversation with the previous model. | |
| 2.1.300 | 2026-10-14 | Added cache_creation_5m_tokens and cache_creation_1h_tokens to the OTel api_request event; OTel GenAI attributes on trace spans; /advisor on Claude Platform on AWS with CLAUDE_CODE_DISABLE_ADVISOR_TOOL=1 to turn it off. | `cache_creation_5m_tokens`, `cache_creation_1h_tokens`, `gen_ai.provider.name`, `gen_ai.conversation.id`, `gen_ai.tool.name`, `error.type`, `/advisor`, `--advisor`, `advisorModel`, `CLAUDE_CODE_DISABLE_ADVISOR_TOOL` |
| 2.1.299 | 2026-10-14 | Idle compaction in the terminal: 200K+ token conversation idle about 54 minutes is compacted before its one-hour prompt cache expires; CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS changes the 200K minimum and idleCompaction false turns it off (both need v2.1.290 or later). | `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS`, `idleCompaction` |
| 2.1.299 | 2026-10-14 | /usage warnings for max effort, workflows, always-on context and large tool results; /effort and /fast in agent view set what new sessions start with. | `/usage`, `/effort`, `/fast` |
| 2.1.296 | 2026-10-09 | /cost, status line, --max-budget-usd and SDK cost figures price Sonnet 5.5 cache reads at 0.10 dollars per million tokens (was 0.20). | `/cost`, `--max-budget-usd` |
| 2.1.296 | 2026-10-09 | Added CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL; default limit on MCP tool descriptions sent up front raised from 2,048 to 4,096 characters. | `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL` |
| 2.1.323 | 2026-11-12 | The cleanupPeriodDays cleanup counts unreadable folders as errors. | `cleanupPeriodDays` |

# Not found in the documentation pages

- `CLAUDE_CODE_SUBAGENT_EFFORT`
- `CLAUDE_CODE_MODEL_CATALOG`
- `anthropic.plan`
- `anthropic.seat_type`
- `anthropic.provider`
- `anthropic.custom_base_url`
- `gen_ai.provider.name`
- `gen_ai.conversation.id`
- `gen_ai.tool.name`
- `max_input_tokens`
- `GET /v1/organizations/analytics/cost`
- `admin.pooled_conflict_rule`
- `admin.pooled_priority_order`
