---
type: "Reference"
title: "Gateway upstreams, failover and per-team routing"
description: "How the gateway forwards inference to Anthropic, Bedrock, Mantle, AWS, Google Cloud or Foundry upstreams, fails over, and routes by group."
resource: "https://code.claude.com/docs/en/claude-apps-gateway-config"
tags: [gateway, upstreams, failover, bedrock, routing]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "cloud provider credentials per upstream"
identifiers:
  - "upstreams"
  - "provider: anthropic"
  - "provider: bedrock"
  - "provider: mantle"
  - "provider: anthropicAws"
  - "provider: anthropicGoogleCloud"
  - "provider: vertex"
  - "provider: foundry"
  - "name"
  - "auth"
  - "base_url"
  - "headers"
  - "groups"
  - "forward_user_identity"
  - "guardrail"
  - "guardrail.input_tagging"
  - "guardrail_trace"
  - "assume_role"
  - "assume_role.role_arn"
  - "assume_role.external_id"
  - "assume_role.session_name"
  - "timeouts.upstream_ttfb_ms"
  - "models"
  - "auto_include_builtin_models"
  - "upstream_model"
  - "capability_rejected:"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-apps-gateway-config"
    resource: "https://code.claude.com/docs/en/claude-apps-gateway-config"
    title: "Claude apps gateway configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`upstreams` is an ordered list. The gateway forwards inference to the first upstream that resolves the requested model and does not exclude the developer through its `groups` list. Providers: `anthropic`, `bedrock`, `mantle` (Amazon Bedrock Mantle endpoint, v2.1.283 or later), `anthropicAws` (Claude Platform on AWS, v2.1.198 or later), `anthropicGoogleCloud` (Claude Models on Google Cloud, Anthropic managed, v2.1.307 or later), `vertex` (Google Cloud Agent Platform), `foundry` (Microsoft Foundry).

# How to use it

Failover: on `5xx`, `429`, `401`, `403`, `404`, `501` or timeout the gateway tries the next upstream; other `4xx` do not fail over. 404 failover needs v2.1.198 or later. The gateway keeps no record of failed upstreams. Multiple upstreams of one provider need distinct `name:`. If every upstream failed, the client gets the last `429`, else last `401`/`403`, `404`, `501`, else its own `502 all upstreams failed (N attempted)`.

| Provider | Key fields | Auth |
| - | - | - |
| `anthropic` | `auth.api_key` (x-api-key), `auth.oauth_token` (Bearer), or Workload Identity Federation (`federation_rule_id`, `organization_id`, `identity_token_file`, optional `workspace_id`, `service_account_id`) | static keys read at startup; federation token file re-read each exchange |
| `bedrock` | `region`, `auth: {}` (AWS default chain), or `aws_access_key_id`/`aws_secret_access_key`/`aws_session_token`, or `aws_bearer_token` | grant `bedrock:InvokeModel`, `InvokeModelWithResponseStream`, `CountTokens` |
| `mantle` | `region`, required `models` list, optional `assume_role` (v2.1.318 or later), `base_url` | same auth as bedrock |
| `anthropicAws` | `region`, `workspace_id` (required), `auth.api_key` or SigV4 | separate IAM service name `aws-external-anthropic` |
| `anthropicGoogleCloud` | `project_id`, `workspace_id`, `auth: {}` or `service_account_json` | needs `roles/claude.user` |
| `vertex` | `region` (or `global`), `project_id`, `auth` | `roles/aiplatform.user` |
| `foundry` | `resource`, `auth.use_azure_ad: true` or `api_key` | needs `models:` mapping deployment names |

Other upstream features:

- `forward_user_identity: true` (anthropic provider with a non-Anthropic `base_url`; v2.1.233 or later) adds headers `x-litellm-end-user-id`, `x-claude-gateway-user-id`, `x-claude-gateway-user-email`; a `429` for a request carrying email then does not fail over (v2.1.267 or later).
- `headers:` static request headers per upstream (v2.1.277 or later); reserved names include `authorization`, `x-api-key`, `host`, `content-type`, `user-agent`, and prefixes `anthropic-`, `x-goog-`, `x-amz-`, `x-amzn-`.
- `guardrail: {id, version}` on every bedrock upstream or none (v2.1.281 or later); `guardrail.input_tagging` values `last_message`, `user_messages`, `all_messages`, `all_messages_and_system` (v2.1.316 or later); `guardrail_trace: true` writes `guardrail.trace` audit events (v2.1.314 or later).
- `assume_role` (v2.1.281 or later): `role_arn`, `external_id`, `session_name` (`email` or `sub`) for cross-account use and per-developer AWS attribution; one STS call per developer per hour per replica; cannot combine with `aws_bearer_token`.
- `groups: [..]` on an upstream limits it to those IdP groups (v2.1.314 or later). A developer in no listed group when every upstream has `groups` gets `API Error: 400 you aren't in a group that can use this gateway...`. Put open upstreams last.
- `models:` list with `upstream_model` maps (keys are upstream `name`) is required for non-US Bedrock regions, provisioned-throughput ARNs and Foundry deployments. `auto_include_builtin_models: false` exposes only the listed models. A custom id skips upstreams absent from its map.

# Limits and defaults

First-byte wait: `provider: anthropic` uses `timeouts.upstream_ttfb_ms` (120000 default); other providers wait up to one hour unless that key is set (streaming, v2.1.295 or later). Cloud upstream clients refresh credentials internally, no restart needed. Cross-provider failover changes the governing agreement and geography. A one-hour cache TTL set in a policy goes to every upstream.

# Notes

Cloud 400/413 rejections surface either as Anthropic-envelope text or a `capability_rejected:` token (for example `capability_rejected: prompt_too_long`, which Claude Code compacts on); needs v2.1.233 or later.
