---
type: "Reference"
title: "Cloud provider credential errors"
description: "Errors for expired or denied AWS, Google Cloud and Microsoft Foundry credentials, including the 60-second AWS chain resolve timeout."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, bedrock, vertex, foundry, credentials]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: "Amazon Bedrock, Claude Platform on AWS, Google Cloud Agent Platform or Microsoft Foundry"
identifiers:
  - "awsAuthRefresh"
  - "gcpAuthRefresh"
  - "CLAUDE_CODE_AWS_CHAIN_RESOLVE_TIMEOUT_MS"
  - "CLAUDE_CODE_USE_ANTHROPIC_GOOGLE_CLOUD"
  - "CLAUDE_CODE_SKIP_VERTEX_AUTH"
  - "GOOGLE_APPLICATION_CREDENTIALS"
  - "ANTHROPIC_FOUNDRY_AUTH_TOKEN"
  - "ANTHROPIC_FOUNDRY_API_KEY"
  - "cloud_credential_error"
  - "AWS_PROFILE"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Authentication failures with third-party model providers. Each message starts with a stable phrase and a varying hint in the middle.

# How to use it

| Leading phrase | Trigger | Fix |
|---|---|---|
| `AWS credentials expired or invalid` | 401 from Claude Platform on AWS or the Mantle endpoint | Run `awsAuthRefresh` command (e.g. `aws sso login --profile myprofile`), or `/login` then "Claude Platform on AWS · refresh credentials". Before v2.1.273 shown only when `awsAuthRefresh` was set. |
| `AWS authentication failed` | 403 from AWS provider, or 401 from Bedrock | Bedrock reports expired tokens as 403 but also authorization denial (`AccessDeniedException`); check IAM and model access. |
| `Google Cloud credentials expired or invalid` | 401 from Agent Platform | `gcpAuthRefresh` or `gcloud auth application-default login`; with `CLAUDE_CODE_SKIP_VERTEX_AUTH` refresh the gateway token. |
| `Google Cloud authentication failed` | 403 | Check IAM roles and model enablement. |
| `Microsoft Foundry authentication failed` | 401 or 403 | Rotate `ANTHROPIC_FOUNDRY_API_KEY`, mint a new `ANTHROPIC_FOUNDRY_AUTH_TOKEN`, or `az login`. |
| `API Error: Could not load AWS credentials` / `Could not load Google Cloud credentials` | No usable credentials from the AWS chain or Google ADC | In `-p` and the SDK the code is `cloud_credential_error` (before v2.1.267: `server_error` or `unknown`). |
| `AWS default-chain credential resolve timed out` | Chain gave nothing within 60 seconds (hung `credential_process`, unreachable IMDS) | Complete sign-in beforehand; raise `CLAUDE_CODE_AWS_CHAIN_RESOLVE_TIMEOUT_MS` (milliseconds). Before v2.1.207 a stalled chain waited forever. |
| `Timed out after 60s waiting for AWS` | Bedrock setup wizard verification step | Same variable; a single stalled request shows `A request to AWS timed out.` |

# Notes

If the hint says credentials are managed by this environment, the launching app owns them; retry or contact the administrator.
