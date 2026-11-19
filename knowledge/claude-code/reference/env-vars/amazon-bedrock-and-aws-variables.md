---
type: "Reference"
title: "Amazon Bedrock and Claude Platform on AWS variables"
description: "Endpoint, region prefix, service tier, API key, credential-chain timeout and content-type variables for Bedrock, Mantle and Claude Platform on AWS."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [bedrock, aws, mantle, credentials]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: "Amazon Bedrock or Claude Platform on AWS"
identifiers:
  - "ANTHROPIC_AWS_API_KEY"
  - "ANTHROPIC_AWS_BASE_URL"
  - "ANTHROPIC_AWS_WORKSPACE_ID"
  - "ANTHROPIC_BEDROCK_BASE_URL"
  - "ANTHROPIC_BEDROCK_MANTLE_BASE_URL"
  - "ANTHROPIC_BEDROCK_REGION_PREFIX"
  - "ANTHROPIC_BEDROCK_SERVICE_TIER"
  - "AWS_BEARER_TOKEN_BEDROCK"
  - "CLAUDE_CODE_AWS_CHAIN_RESOLVE_TIMEOUT_MS"
  - "CLAUDE_CODE_SKIP_AWS_CRED_CACHE"
  - "CLAUDE_CODE_DISABLE_AUTH_REFRESH_LOCK"
  - "CLAUDE_CODE_DISABLE_BEDROCK_CONTENT_TYPE_DEFAULT"
  - "CLAUDE_CODE_DISABLE_BEDROCK_CONTENT_TYPE_GUARD"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

AWS-side configuration. Provider switches are in [provider selection](./provider-selection-and-auth-skips.md).

# How to use it

| Variable | What it does |
| :- | :- |
| `ANTHROPIC_AWS_API_KEY` | Workspace API key for Claude Platform on AWS; sent as `x-api-key`, beats AWS SigV4. |
| `ANTHROPIC_AWS_BASE_URL` | Endpoint override; default `https://aws-external-anthropic.{region}.api.aws`. Region resolves as on Bedrock. |
| `ANTHROPIC_AWS_WORKSPACE_ID` | Required for Claude Platform on AWS; sent as `anthropic-workspace-id` on every request. |
| `ANTHROPIC_BEDROCK_BASE_URL` | Override the Bedrock endpoint (custom endpoint or LLM gateway). |
| `ANTHROPIC_BEDROCK_MANTLE_BASE_URL` | Override the Bedrock Mantle endpoint. |
| `ANTHROPIC_BEDROCK_REGION_PREFIX` | Cross-region inference profile prefix tried first: `us`, `eu`, `apac`, `jp`, `au`, `global`. Ignored in GovCloud. Requires v2.1.224+. |
| `ANTHROPIC_BEDROCK_SERVICE_TIER` | Bedrock service tier: `default`, `flex`, `priority`. |
| `AWS_BEARER_TOKEN_BEDROCK` | Bedrock API key. |
| `CLAUDE_CODE_AWS_CHAIN_RESOLVE_TIMEOUT_MS` | Wait for the AWS default credential chain before failing with `AWS default-chain credential resolve timed out` (default 60000). Applies to Bedrock, Claude Platform on AWS, Mantle. Requires v2.1.207+. |
| `CLAUDE_CODE_SKIP_AWS_CRED_CACHE` | `1` resolves the credential chain on every request (SSO profiles then ask IAM Identity Center each time). Requires v2.1.207+. |
| `CLAUDE_CODE_DISABLE_AUTH_REFRESH_LOCK` | `1` makes each process run its own `gcpAuthRefresh` or `awsAuthRefresh` instead of waiting for another process. Requires v2.1.286+. |
| `CLAUDE_CODE_DISABLE_BEDROCK_CONTENT_TYPE_DEFAULT` | `1` stops treating a Bedrock stream with missing/empty `Content-Type` as the binary event stream; use only for a gateway re-emitting SSE. Requires v2.1.239+. |
| `CLAUDE_CODE_DISABLE_BEDROCK_CONTENT_TYPE_GUARD` | `1` skips the check that the stream is `application/vnd.amazon.eventstream`; prefer fixing the gateway. Requires v2.1.208+. |
