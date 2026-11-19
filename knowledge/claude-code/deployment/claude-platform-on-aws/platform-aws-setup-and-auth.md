---
type: "Guide"
title: "Claude Platform on AWS setup and auth"
description: "Point Claude Code at the Anthropic-operated Claude API with AWS SigV4 or a workspace API key, plus model pinning and verification."
resource: "https://code.claude.com/docs/en/claude-platform-on-aws"
tags: [aws, claude-platform, auth, sigv4]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk, headless]
requires: "Claude Platform on AWS subscription via AWS Marketplace and a workspace in the AWS-linked Anthropic organization"
identifiers:
  - "CLAUDE_CODE_USE_ANTHROPIC_AWS"
  - "ANTHROPIC_AWS_WORKSPACE_ID"
  - "ANTHROPIC_AWS_API_KEY"
  - "ANTHROPIC_AWS_BASE_URL"
  - "AWS_REGION"
  - "awsAuthRefresh"
  - "ANTHROPIC_DEFAULT_FABLE_MODEL"
  - "ANTHROPIC_DEFAULT_OPUS_MODEL"
  - "ANTHROPIC_DEFAULT_SONNET_MODEL"
  - "ANTHROPIC_DEFAULT_HAIKU_MODEL"
  - "ENABLE_PROMPT_CACHING_1H"
  - "anthropic-workspace-id"
  - "/login"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-platform-on-aws"
    resource: "https://code.claude.com/docs/en/claude-platform-on-aws"
    title: "Claude Code on Claude Platform on AWS"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Platform on AWS is the Anthropic-operated Claude API with AWS authentication, IAM and AWS Marketplace billing; same models and API features on the same release schedule as the Claude API. Subscribing through Marketplace creates a new Anthropic organization separate from any existing one; credentials do not transfer.

# How to use it

- Auth option 1, SigV4: standard AWS credential chain (env vars, `~/.aws/credentials`, IAM roles, SSO). CI: give the runner an IAM role and set `AWS_REGION`. Configure `awsAuthRefresh` to re-run a login command on expiry (also runs at startup when credentials can't be validated, output shown in an `Authentication` panel); then `/login` > **3rd-party platform** > **Claude Platform on AWS · refresh credentials** reloads without restart.
- Auth option 2, workspace API key from the AWS Console (**Claude Platform on AWS > API keys**) in `ANTHROPIC_AWS_API_KEY`; sent as `x-api-key`, takes precedence over SigV4. Keys from a separate Claude Console organization do not work.
- Configure: `CLAUDE_CODE_USE_ANTHROPIC_AWS=1`, `ANTHROPIC_AWS_WORKSPACE_ID=wrkspc_...` (required; sent as the `anthropic-workspace-id` header on every request), `AWS_REGION`. Base URL is `https://aws-external-anthropic.{region}.api.aws`, region resolved like Bedrock; override with `ANTHROPIC_AWS_BASE_URL`.
- Provider is opt-in; Bedrock and Foundry take precedence in routing, so unset `CLAUDE_CODE_USE_BEDROCK` and `CLAUDE_CODE_USE_FOUNDRY`.
- Pin models (same IDs as the Claude API): `ANTHROPIC_DEFAULT_FABLE_MODEL`, `_OPUS_`, `_SONNET_`, `_HAIKU_`. Unpinned `opus` resolves to Opus 5.5 (before v2.1.280: Opus 5, from v2.1.219).
- Prompt caching automatic; `ENABLE_PROMPT_CACHING_1H=1` for 1-hour TTL (billed higher).
- Verify: startup banner shows `Claude Platform on AWS`; `/status` shows `API provider`, `Workspace ID`, `AWS region`, and the base URL if overridden.

# Limits and defaults

`/login` and `/logout` do not sign into a claude.ai subscription here. Some features are unavailable or differ; see the feature availability matrix.

# Notes

Troubleshooting: `403`/`AccessDenied` (IAM lacks `aws-external-anthropic` actions, or stale `ANTHROPIC_AWS_API_KEY` overriding SigV4); missing-workspace error (workspace ID unset, not implied by AWS credentials); requests still going to `api.anthropic.com` (`CLAUDE_CODE_USE_ANTHROPIC_AWS` not truthy, or Bedrock/Foundry set).
