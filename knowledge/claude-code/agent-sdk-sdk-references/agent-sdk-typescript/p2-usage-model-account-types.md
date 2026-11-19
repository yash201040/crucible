---
type: "Reference"
title: "Usage, model, account and thinking types"
description: "ModelUsage, Usage, ModelInfo, AgentInfo, AccountInfo, ThinkingConfig, SdkBeta, ApiKeySource, SlashCommand and related shared types."
resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
tags: [usage, cost, model, thinking, types]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "ModelUsage"
  - "NonNullableUsage"
  - "Usage"
  - "costUSD"
  - "thinkingTokens"
  - "canonicalModel"
  - "provider"
  - "costBasis"
  - "output_tokens_details"
  - "fallback_credit"
  - "ModelInfo"
  - "supportsEffort"
  - "supportedEffortLevels"
  - "supportsAdaptiveThinking"
  - "supportsFastMode"
  - "supportsAutoMode"
  - "AgentInfo"
  - "AccountInfo"
  - "ApiKeySource"
  - "SdkBeta"
  - "context-1m-2025-08-07"
  - "ThinkingConfig"
  - "ThinkingDisplay"
  - "SlashCommand"
  - "ConfigScope"
  - "CallToolResult"
  - "SDKMcpResourceLink"
  - "RewindFilesResult"
  - "BUILTIN_TOOL_NAMES"
  - "LEGACY_TOOL_NAME_ALIASES"
  - "AbortError"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-typescript"
    resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
    title: "Agent SDK reference - TypeScript"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Shared types used by results, listings and control methods, with the notes that matter for cost tracking and model choice.

# How to use it

| Type | Key fields and notes |
| :- | :- |
| `ModelUsage` | `inputTokens`, `outputTokens` (already includes `thinkingTokens`; do not add), `cacheReadInputTokens`, `cacheCreationInputTokens`, `webSearchRequests`, `costUSD` (client-side estimate), `contextWindow`, `maxOutputTokens`, `canonicalModel` and `provider` (v2.1.218+; providers `firstParty`, `bedrock`, `vertex`, `foundry`, `anthropicAws`, `mantle`, `gateway`), `costBasis` (`list|managed|unknown`; v2.1.246+; `managed` means a `modelPricing` table). `thinkingTokens` v0.3.257+, partial for resumed sessions begun on earlier versions |
| `Usage` | Anthropic `BetaUsage`: `input_tokens`, `output_tokens`, cache fields, `server_tool_use`, `service_tier`, `speed` (`standard|fast`), `inference_geo`, `iterations`, `output_tokens_details.thinking_tokens`, `fallback_credit` (needs `@anthropic-ai/sdk` 0.115.0+). `output_tokens` is authoritative for billing; the breakdown is for observability. On streamed assistant messages it is a `message_start` placeholder: read the result message's `usage`; `thinking_tokens` reads 0 when no breakdown is reported |
| `ModelInfo` | `value`, `resolvedModel` (v2.1.197+), `displayName`, `description`, `supportsEffort`, `supportedEffortLevels`, `supportsAdaptiveThinking`, `supportsFastMode`, `supportsAutoMode` |
| `AgentInfo` | `name`, `description`, `model?` (alias, ID or `'inherit'`) |
| `AccountInfo` | `email`, `organization`, `subscriptionType`, `tokenSource`, `apiKeySource` |
| `ApiKeySource` | Reported values: `ANTHROPIC_API_KEY`, `apiKeyHelper`, `/login managed key`, `none` (v0.3.234+); `user`, `project`, `org`, `temporary`, `oauth` kept for compatibility, not reported |
| `ThinkingConfig` | `{ type: "adaptive", display? }` (Opus 4.6+), `{ type: "enabled", budgetTokens?, display? }`, `{ type: "disabled" }`. `display` is `"summarized"` or `"omitted"`; on Claude Opus 4.7 and later the API default is `"omitted"`. Takes precedence over deprecated `maxThinkingTokens` |
| `SdkBeta` | Only `"context-1m-2025-08-07"`; retired on the Claude API for Sonnet 4.5 and Sonnet 4 (requests over 200K tokens error). Use a model that runs 1M by default (e.g. `claude-sonnet-5-5`, `claude-opus-5-5`) or the `[1m]` suffix (e.g. `claude-opus-4-6[1m]`) |
| `SlashCommand` | `name`, `description`, `argumentHint`, `aliases`, `builtin` (v0.3.277+) |
| `RewindFilesResult` | `canRewind`, `error`, `filesChanged`, `insertions`, `deletions`, `skippedLinks` |
| `SDKMcpResourceLink` | `uri`, `name`, `title`, `description`, `mimeType`, `size`, `annotations` (v0.3.257+) |
| `BUILTIN_TOOL_NAMES`, `LEGACY_TOOL_NAME_ALIASES` | Alpha, v0.3.301+; alphabetical built-in names (no MCP tools, omits some built-ins); legacy map e.g. `Task` to `Agent`, `KillShell` and `KillBash` to `TaskStop`. Do not build a deny list from it; use `disallowedTools: ["*"]` to deny everything. Presence does not mean the session has the tool (read init `tools`) |
| `AbortError` | The only error class in the typed API; other failures (process exit, launch failure) reject iteration with unclassed errors |

# Limits and defaults

`SDKThinkingTokensMessage` estimates are for progress display; the final count is the result `usage.output_tokens_details.thinking_tokens` and excludes subagent tokens.
