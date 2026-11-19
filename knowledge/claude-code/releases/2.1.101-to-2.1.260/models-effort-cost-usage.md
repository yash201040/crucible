---
type: "Release Digest"
title: "Models, effort, cost and usage (2.1.101 to 2.1.260)"
description: "Release notes 2.1.101 to 2.1.260 on model launches, defaults, effort, fast mode, caching TTL, cost, usage and telemetry."
resource: "https://code.claude.com/docs/en/changelog"
tags: [models, effort, cost, usage, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "prompt_cache"
  - "bedrock:CountTokens"
  - "claude-fable-5-1"
  - "--effort"
  - "/effort"
  - "rate_limits.spend_limit"
  - "/usage-credits"
  - "modelPicker"
  - "promptCacheTtl"
  - "subagentPromptCacheTtl"
  - "modelPricing"
  - "/model"
  - "/fast"
  - "--max-budget-usd"
  - "CLAUDE_CODE_RETRY_WATCHDOG"
  - "ANTHROPIC_DEFAULT_MODEL"
  - "CLAUDE_CODE_DISABLE_1M_CONTEXT"
  - "claude-opus-5"
  - "CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH"
  - "subagentStatusLine"
  - "workflow.run_id"
  - "workflow.name"
  - "OTEL_LOG_ASSISTANT_RESPONSES"
  - "OTEL_LOG_USER_PROMPTS"
  - "--model"
  - "ANTHROPIC_MODEL"
  - "enforceAvailableModels"
  - "availableModels"
  - "/usage"
  - "claude_code.lines_of_code.count"
  - "fallbackModel"
  - "--fallback-model"
  - "MAX_THINKING_TOKENS"
  - "--thinking"
  - "OTEL_RESOURCE_ATTRIBUTES"
  - "CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE"
  - "OTEL_METRICS_INCLUDE_ENTRYPOINT"
  - "ANTHROPIC_WORKSPACE_ID"
  - "claude_code.skill_activated"
  - "invocation_trigger"
  - "ANTHROPIC_BEDROCK_SERVICE_TIER"
  - "claude_code.at_mention"
  - "stop_reason"
  - "tool_use_id"
  - "effort.level"
  - "/cost"
  - "/stats"
  - "effort"
  - "xhigh"
  - "OTEL_LOG_RAW_API_BODIES"
  - "ENABLE_PROMPT_CACHING_1H"
  - "ENABLE_PROMPT_CACHING_1H_BEDROCK"
  - "FORCE_PROMPT_CACHING_5M"
  - "DISABLE_PROMPT_CACHING"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.101 to 2.1.260"
stale_after: "2027-01-19T00:00:00Z"
---

# Changes by version

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.260 | 2026-09-03 | /cost and status line prompt_cache field give a likely cause for cache misses; /effort on Fable 5.1 no longer invalidates the cache; Bedrock gateway counts aborted-request input tokens via CountTokens | `prompt_cache`, `bedrock:CountTokens` |
| 2.1.257 | 2026-09-01 | Claude Fable 5.1 (claude-fable-5-1), default Fable, 1M context, $10/$50 per Mtok, cache reads $0.25; --effort lifts default-effort hold for that session only; /effort s sets session-only | `claude-fable-5-1`, `--effort`, `/effort` |
| 2.1.251 | 2026-08-28 | Spend limit bar in /usage and rate_limits.spend_limit status field; per-session prompt-cache line in /cost; Enterprise seat default Opus 5; /effort saves default per model; default commit trailer Co-Authored-By: Claude Code for non-Claude models | `rate_limits.spend_limit`, `prompt_cache` |
| 2.1.248 | 2026-08-27 | /usage-credits lets members request a higher limit from admins | `/usage-credits` |
| 2.1.243 | 2026-08-25 | Loops breakdown in /usage; modelPicker setting; promptCacheTtl and subagentPromptCacheTtl settings; modelPricing managed setting; /model, /fast, /effort run immediately on Bedrock, Vertex, Foundry | `modelPicker`, `promptCacheTtl`, `subagentPromptCacheTtl`, `modelPricing`, `/model`, `/fast` |
| 2.1.243 | 2026-08-25 | Sonnet 5 shown at $2/$10 per Mtok as standard price; clearer error for effort xhigh or max with thinking off |  |
| 2.1.239 | 2026-08-21 | Cost estimates (/cost, status line, --max-budget-usd) include the 1.1x US-only-inference premium; CLAUDE_CODE_RETRY_WATCHDOG fails fast on spend-limit and out-of-credits errors | `--max-budget-usd`, `CLAUDE_CODE_RETRY_WATCHDOG` |
| 2.1.236 | 2026-08-19 | ANTHROPIC_DEFAULT_MODEL sets the starting model (a /model pick overrides it and persists); /usage shows usage-credits spend for Team and Enterprise | `ANTHROPIC_DEFAULT_MODEL` |
| 2.1.225 | 2026-08-08 | Gateway spend-limit support in usage warnings (gateway on 2.1.225) |  |
| 2.1.223 | 2026-08-06 | CLAUDE_CODE_DISABLE_1M_CONTEXT holds every native-1M model to 200K via auto-compaction | `CLAUDE_CODE_DISABLE_1M_CONTEXT` |
| 2.1.219 | 2026-07-24 | Claude Opus 5 (claude-opus-5) default Opus, 1M context, fast mode $10/$50 per Mtok; Opus 4.7 removed from fast mode | `claude-opus-5`, `/fast` |
| 2.1.214 | 2026-07-18 | OTel events gain message.uuid, client_request_id, tool_source; CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH sets the 60 KB truncation; reasoning effort in subagentStatusLine payload | `CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH`, `subagentStatusLine` |
| 2.1.212 | 2026-07-17 | Transcripts record effort on each assistant message |  |
| 2.1.210 | 2026-07-14 | Auto mode classifier defaults to Sonnet 5 for external sessions |  |
| 2.1.207 | 2026-07-11 | Bedrock, Vertex and Claude Platform on AWS default to Claude Opus 4.8 |  |
| 2.1.202 | 2026-07-06 | Telemetry attributes workflow.run_id and workflow.name | `workflow.run_id`, `workflow.name` |
| 2.1.197 | 2026-06-30 | Claude Sonnet 5 default model, native 1M context, $2/$10 per Mtok promotional through August 31 |  |
| 2.1.196 | 2026-06-29 | Organization default models show as Org default or Role default in /model |  |
| 2.1.193 | 2026-06-25 | claude_code.assistant_response OTel event; OTEL_LOG_ASSISTANT_RESPONSES controls redaction | `OTEL_LOG_ASSISTANT_RESPONSES`, `OTEL_LOG_USER_PROMPTS` |
| 2.1.187 | 2026-06-23 | Org-configured model restrictions apply to picker, --model, /model, ANTHROPIC_MODEL | `--model`, `ANTHROPIC_MODEL` |
| 2.1.175 | 2026-06-12 | enforceAvailableModels managed setting makes availableModels constrain the Default model too | `enforceAvailableModels`, `availableModels` |
| 2.1.174 | 2026-06-12 | /usage attribution shows cache misses, long context, subagents and per-skill/agent/plugin/MCP breakdowns (VSCode) | `/usage` |
| 2.1.172 | 2026-06-10 | model attribute on claude_code.lines_of_code.count OTel metric | `claude_code.lines_of_code.count` |
| 2.1.170 | 2026-06-09 | Claude Fable 5 launched |  |
| 2.1.166 | 2026-06-06 | fallbackModel setting (up to three fallbacks); --fallback-model applies to interactive; one retry on fallback after unexpected non-retryable error; MAX_THINKING_TOKENS=0 and --thinking disabled disable thinking on default-thinking models | `fallbackModel`, `--fallback-model`, `MAX_THINKING_TOKENS`, `--thinking` |
| 2.1.161 | 2026-06-02 | OTEL_RESOURCE_ATTRIBUTES values become metric labels | `OTEL_RESOURCE_ATTRIBUTES` |
| 2.1.154 | 2026-05-28 | Opus 4.8 defaults to high effort; fast mode on Opus 4.8 2x price for 2.5x speed; lean system prompt default except Haiku, Sonnet, Opus 4.7 and earlier; CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE deprecated | `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE` |
| 2.1.152 | 2026-05-27 | Switches to --fallback-model for the rest of session when primary not found; app.entrypoint metric attribute via OTEL_METRICS_INCLUDE_ENTRYPOINT=true | `OTEL_METRICS_INCLUDE_ENTRYPOINT` |
| 2.1.149 | 2026-05-22 | /usage per-category breakdown of skills, subagents, plugins and MCP servers | `/usage` |
| 2.1.144 | 2026-05-19 | Renamed extra usage to usage credits (/extra-usage now /usage-credits); /model changes current session only | `/usage-credits` |
| 2.1.142 | 2026-05-14 | Fast mode uses Opus 4.7 by default; CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE=1 pins Opus 4.6 | `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE` |
| 2.1.141 | 2026-05-13 | ANTHROPIC_WORKSPACE_ID scopes workload identity federation token to a workspace | `ANTHROPIC_WORKSPACE_ID` |
| 2.1.126 | 2026-05-01 | /model picker lists gateway /v1/models; claude_code.skill_activated gains invocation_trigger | `claude_code.skill_activated`, `invocation_trigger` |
| 2.1.122 | 2026-04-28 | ANTHROPIC_BEDROCK_SERVICE_TIER (default, flex, priority); claude_code.at_mention log event | `ANTHROPIC_BEDROCK_SERVICE_TIER`, `claude_code.at_mention` |
| 2.1.121 | 2026-04-28 | OTel LLM spans gain stop_reason, gen_ai.response.finish_reasons, user_system_prompt | `stop_reason` |
| 2.1.119 | 2026-04-23 | OTel tool_result and tool_decision include tool_use_id; status line JSON includes effort.level and thinking.enabled | `tool_use_id`, `effort.level` |
| 2.1.118 | 2026-04-23 | /cost and /stats merged into /usage | `/usage`, `/cost`, `/stats` |
| 2.1.117 | 2026-04-22 | Pro/Max default effort on Opus 4.6 and Sonnet 4.6 is high (was medium); OTel cost, token, api_request metrics gain effort attribute | `effort` |
| 2.1.111 | 2026-04-16 | xhigh effort level for Opus 4.7 (--effort xhigh); /effort slider; OTEL_LOG_RAW_API_BODIES emits full API bodies | `xhigh`, `OTEL_LOG_RAW_API_BODIES` |
| 2.1.108 | 2026-04-14 | ENABLE_PROMPT_CACHING_1H opts into 1-hour cache TTL (API key, Bedrock, Vertex, Foundry) and FORCE_PROMPT_CACHING_5M forces 5 minutes; startup warning when DISABLE_PROMPT_CACHING* set; /model warns that switching re-reads history uncached | `ENABLE_PROMPT_CACHING_1H`, `ENABLE_PROMPT_CACHING_1H_BEDROCK`, `FORCE_PROMPT_CACHING_5M`, `DISABLE_PROMPT_CACHING` |

# Not found in the documentation pages

These identifiers occur only in the release notes, not in the saved documentation pages:

- `subagentStatusLine`
- `--thinking`
