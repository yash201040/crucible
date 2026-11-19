---
type: "Reference"
title: "Gateway troubleshooting symptoms and fixes"
description: "Symptom, cause and fix table for gateway sign-in, boot, Postgres, TLS and streaming timeout failures, including long-thinking timeouts."
resource: "https://code.claude.com/docs/en/claude-apps-gateway-deploy"
tags: [gateway, troubleshooting, errors, timeouts, login]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_STREAM_IDLE_TIMEOUT_MS"
  - "CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK"
  - "oidc.scope_on_refresh"
  - "oidc.form_action_origins"
  - "limits.max_request_header_bytes"
  - "NODE_EXTRA_CA_CERTS"
  - "CLAUDE_CODE_CERT_STORE"
  - "NO_PROXY"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-apps-gateway-deploy"
    resource: "https://code.claude.com/docs/en/claude-apps-gateway-deploy"
    title: "Claude apps gateway deployment and operations"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A keyed troubleshooting section. Key messages and their causes:

| Message or symptom | Cause | Fix |
| - | - | - |
| `Not signed in to the Cloud gateway — run /login.` | managed settings force gateway but no gateway sign-in | run `/login` |
| `Administrator policy requires a Cloud gateway sign-in on this machine` | `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `apiKeyHelper` or saved Console key present | unset, remove, or `claude auth logout` |
| `Gateway hosts must be on your organization's private network; <host> resolves to the public...` | gateway name resolves to a public IP (for example dual-stack AAAA) | private-only DNS, or declare the block |
| `Claude Code may not be enabled for your organization` after 403 on managed settings | `access_control` or a WAF/proxy returned 403 | check `access.denied` audit events |
| `The gateway is limiting sign-in attempts right now` | per-IP sign-in limit | list the LB in `trusted_proxies`, then raise `rate_limits` |
| `431` after sign-in | many IdP groups inflate the Authorization header; limit 256 KiB (16 KiB before v2.1.284) | upgrade, raise or remove `limits.max_request_header_bytes`, emit fewer groups |
| `Cloud gateway session expired` every `ttl_hours` | IdP returns no id_token on refresh | `oidc.scope_on_refresh: true` (v2.1.260 or later) |
| `API Error: 400 you aren't in a group that can use this gateway...` | every upstream has `groups`, user in none | add to a group or add an open upstream |
| Every Bedrock request 502, `Could not load credentials from any providers` | IMDSv2 hop limit 1 in container | use task roles/IRSA or hop limit 2 |
| Chrome blocks Approve with form-action CSP | IdP redirects through another host | add `oidc.form_action_origins` |
| Postgres `remaining connection slots are reserved` | replicas times pool exceed DB connections | size the pool, see operations |

Boot failures: missing `store.postgres_url`; unparsable URL (name one host, move password to `store.password`); `requires the native binary` (running under Node); OIDC discovery error; Postgres permission error (grant `CREATE`); the gateway retries Postgres connection 3 times, 2 s apart.

# How to use it

Long thinking timeouts: if an upstream other than `provider: anthropic` shows one request open about 12.5 minutes then `504`s, or on `provider: anthropic` about 20 minutes then `502`/`504`, Claude Code ended a ping-only stream and re-sent without streaming. Raise `CLAUDE_STREAM_IDLE_TIMEOUT_MS` in a policy `env` (for example `"1800000"`); default `300000` allows about 12.5 minutes of pings, `900000` about 22.5, `1800000` about 37.5. Confirm with debug line `Error streaming, falling back to non-streaming mode: Stream idle timeout - no chunks received`; with `CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK=1` the turn ends with `API Error: Stream idle timeout - no chunks received`.

# Notes

When reporting an issue include gateway stderr (redacted), `gateway.yaml`, gateway version; for logins a `claude --debug-file` output. Debug files can contain hook and MCP output.
