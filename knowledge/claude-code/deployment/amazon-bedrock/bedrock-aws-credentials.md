---
type: "Feature"
title: "Bedrock AWS credentials and refresh"
description: "Credential methods, in-memory caching, timeouts and the awsAuthRefresh and awsCredentialExport settings for Claude Code on Bedrock."
resource: "https://code.claude.com/docs/en/amazon-bedrock"
tags: [bedrock, credentials, sso, caching]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Amazon Bedrock"
identifiers:
  - "AWS_BEARER_TOKEN_BEDROCK"
  - "AWS_ACCESS_KEY_ID"
  - "AWS_SECRET_ACCESS_KEY"
  - "AWS_SESSION_TOKEN"
  - "awsAuthRefresh"
  - "awsCredentialExport"
  - "CLAUDE_CODE_SKIP_AWS_CRED_CACHE"
  - "CLAUDE_CODE_AWS_CHAIN_RESOLVE_TIMEOUT_MS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "amazon-bedrock"
    resource: "https://code.claude.com/docs/en/amazon-bedrock"
    title: "Claude Code on Amazon Bedrock"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code uses the default AWS SDK credential chain (EC2 instance profile and ECS task credentials work as-is). Documented sources: `aws configure` profile, access key env vars (`AWS_SESSION_TOKEN` only for temporary credentials), SSO profile (`aws sso login --profile=...` plus `AWS_PROFILE`; the IAM Identity Center region is the profile's `sso_region`), `aws login` (needs AWS CLI 2.32.0+, session up to 12 hours), or a Bedrock API key in `AWS_BEARER_TOKEN_BEDROCK`.

# How to use it

- Bedrock API key: short-term keys last up to 12 hours; long-term keys last until a set expiry. When `AWS_BEARER_TOKEN_BEDROCK` is set, the credential chain is not resolved at all.
- `awsAuthRefresh` (settings key): runs only when credentials look expired (timestamp or API credential error), then retries. Output is shown but no interactive input. Claude Code first calls STS `GetCallerIdentity` (through `HTTPS_PROXY`/`NO_PROXY`; before v2.1.239 it bypassed the proxy and hung) and skips the command if credentials still work. Example: `{"awsAuthRefresh": "aws sso login --profile myprofile", "env": {"AWS_PROFILE": "myprofile"}}`.
- `awsCredentialExport` (settings key): runs at session start and on each credential reload even when the chain is valid; output is captured silently and must be JSON `{"Credentials": {"AccessKeyId", "SecretAccessKey", "SessionToken", "Expiration"}}` (flat `aws configure export-credentials --format process` output also accepted). `Expiration` optional. Alone, it replaces chain resolution at startup.

# Limits and defaults

- Resolved credentials are cached in memory until 5 minutes before expiry, or 1 hour with no expiry; a credential error clears the cache. Not applied to Bedrock API keys. `CLAUDE_CODE_SKIP_AWS_CRED_CACHE=1` resolves per request (no timeout then).
- The cache-filling resolve times out after 60 s (error `AWS default-chain credential resolve timed out`); raise with `CLAUDE_CODE_AWS_CHAIN_RESOLVE_TIMEOUT_MS` (milliseconds). The setup wizard applies the same limit to its AWS calls (`Timed out after 60s waiting for AWS`).

# Notes

If SSO browser tabs keep opening behind VPN or TLS-inspecting proxies, remove `awsAuthRefresh` and run `aws sso login` manually first.
