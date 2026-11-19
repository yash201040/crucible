---
type: "Reference"
title: "Credential and header helper settings"
description: "Settings that run your own command to supply API keys, AWS or GCP credentials or OpenTelemetry headers."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, authentication, credentials, helpers]
kind: "setting"
maturity: "unlabelled"
since: "2.1.246"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "apiKeyHelper"
  - "awsAuthRefresh"
  - "awsCredentialExport"
  - "gcpAuthRefresh"
  - "otelHeadersHelper"
  - "CLAUDE_CODE_API_KEY_HELPER_TTL_MS"
  - "CLAUDE_CODE_SKIP_VERTEX_AUTH"
  - "CLAUDE_CODE_SKIP_ANTHROPIC_AWS_AUTH"
  - "CLAUDE_CODE_SKIP_MANTLE_AUTH"
  - "CLAUDE_CODE_DISABLE_AUTH_REFRESH_LOCK"
  - "CLAUDE_CODE_OTEL_HEADERS_HELPER_DEBOUNCE_MS"
  - "ANTHROPIC_AUTH_TOKEN"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Five any-file keys that each take a shell command. Useful for unattended runs where credentials rotate. All default to unset.

# How to use it

| Name | What the command does | Notes |
| :- | :- | :- |
| `apiKeyHelper` | Prints the credential sent as both `X-Api-Key` and `Authorization: Bearer` headers (run via `/bin/sh` on macOS and Linux, `cmd` on Windows) | Value cached; rerun after 5 minutes by default (or `CLAUDE_CODE_API_KEY_HELPER_TTL_MS`), on `401` or `403` from the API or a gateway, on a gateway `401` (not `403`) when `CLAUDE_CODE_SKIP_VERTEX_AUTH`, `CLAUDE_CODE_SKIP_ANTHROPIC_AWS_AUTH` or `CLAUDE_CODE_SKIP_MANTLE_AUTH` is set (v2.1.318+), and before a request when the cached output is a JWT that has expired (v2.1.246+). The last three apply only when the helper output is the credential sent and `ANTHROPIC_AUTH_TOKEN` is not set. From project or local settings it does not run in interactive sessions until the workspace trust prompt is accepted |
| `awsAuthRefresh` | Refreshes `.aws` credentials (for example `aws sso login --profile myprofile`) for Bedrock | Run only when an STS check of current credentials fails, then `.aws` is re-read. Concurrent processes with the same command and credentials: one runs it, the rest wait; after 60 seconds a waiting process runs it itself. `CLAUDE_CODE_DISABLE_AUTH_REFRESH_LOCK=1` disables the lock |
| `awsCredentialExport` | Prints AWS credentials as JSON (`aws sts` shape or flat `aws configure export-credentials` shape) | Always runs when set; scoped to Claude Code's Bedrock client so shell commands Claude runs keep ambient credentials |
| `gcpAuthRefresh` | Refreshes Google Cloud Application Default Credentials when expired or unloadable | Same single-runner lock and 60 second wait as `awsAuthRefresh`; without it the error tells you to run `gcloud auth application-default login` |
| `otelHeadersHelper` | Prints a JSON object of string header values for OpenTelemetry exports | Run at startup and periodically; interval via `CLAUDE_CODE_OTEL_HEADERS_HELPER_DEBOUNCE_MS` |

# Notes

Use `awsAuthRefresh` when the flow writes to `.aws`, `awsCredentialExport` when it prints credentials.
