---
type: "Reference"
title: "Gateway error troubleshooting table"
description: "Common errors behind a gateway (401, 400 beta fields, adaptive thinking, context limits, fast mode, WAF 403, TLS) with cause and fix."
resource: "https://code.claude.com/docs/en/llm-gateway-connect"
tags: [gateway, errors, troubleshooting, betas, compaction]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS"
  - "CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING"
  - "CLAUDE_CODE_AUTO_COMPACT_WINDOW"
  - "CLAUDE_CODE_MAX_OUTPUT_TOKENS"
  - "CLAUDE_CODE_DISABLE_ADVISOR_TOOL"
  - "CLAUDE_CODE_SKIP_FAST_MODE_NETWORK_ERRORS"
  - "CLAUDE_CODE_SKIP_FAST_MODE_ORG_CHECK"
  - "NODE_EXTRA_CA_CERTS"
  - "forceLoginMethod"
  - "forceLoginOrgUUID"
  - "forceLoginGatewayUrl"
  - "~/.claude/feedback-bundles/"
  - "/compact"
  - "/fast"
  - "/feedback"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "llm-gateway-connect"
    resource: "https://code.claude.com/docs/en/llm-gateway-connect"
    title: "Connect Claude Code to an LLM gateway"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The page's table of gateway-side causes and fixes.

# How to use it

| Symptom | Cause | Fix |
| - | - | - |
| Warning naming two credential sources (`auth may not work as expected`) | Gateway credential and saved login both active | Unset the variable, or `/logout` |
| `401` invalid or unrecognized token | Credential not issued by gateway or in the wrong header | Match variable to credential kind; regenerate key |
| `Your apiKeyHelper script is failing` / `apiKeyHelper failed:` on stderr in non-interactive mode | Helper produced no usable key (requests carry a placeholder) | Run the command directly; re-authenticate |
| `Connection refused` or `ENOTFOUND`, often after a silent retry pause | Nothing answers at base URL | curl test; check VPN/firewall |
| `API returned an empty or malformed response (HTTP 200)` | HTML or login page from gateway or proxy | curl test; fix route |
| `400` naming `context_management`, `Extra inputs are not permitted` | Upstream rejects fields sent to Anthropic-format endpoints | `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1`; else set the matching `CLAUDE_CODE_USE_*` variable |
| `400` naming `thinking` or `adaptive` | Upstream does not accept adaptive reasoning (requested for Claude Opus 4.6, Sonnet 4.6, Haiku 5.5, Fable 5 and later) | Upgrade upstream; on Opus 4.6 and Sonnet 4.6 `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1`. Capability variables apply only to provider configurations, not behind an `ANTHROPIC_BASE_URL` gateway |
| `400` with the gateway's own context-limit wording (`ContextWindowExceededError`) | Gateway enforces a smaller window and rewrites the error, so no auto compact and retry | `/compact`; set `CLAUDE_CODE_AUTO_COMPACT_WINDOW` (clamped to at least 100,000 and at most the model window) and `CLAUDE_CODE_MAX_OUTPUT_TOKENS` below the model output limit |
| `400` rejecting a tool schema `pattern`, v2.1.265 through v2.1.267 | Artifact tool schema regex with `\p{...}` in a gradual rollout | Update to v2.1.268 or later, or turn artifacts off |
| `400` rejecting tool type such as `Input tag 'advisor_20260301'`, v2.1.275 | Advisor tool entry sent in a gradual rollout | v2.1.276 or later, or `CLAUDE_CODE_DISABLE_ADVISOR_TOOL=1` on v2.1.275 |
| Models missing from `/model` | Names not built in, or a replacing `modelPicker` lineup | Enable model discovery or add names via model configuration |
| `/fast` unavailable (network issues) | Availability check goes direct to `api.anthropic.com` | Allowlist it, or `CLAUDE_CODE_SKIP_FAST_MODE_NETWORK_ERRORS=1` |
| `/fast` unavailable with gateway-issued key in `ANTHROPIC_API_KEY` | Check not sent for non-Anthropic-format keys | `CLAUDE_CODE_SKIP_FAST_MODE_NETWORK_ERRORS=1` |
| `/fast` disabled by organization with `ANTHROPIC_AUTH_TOKEN` only | Check needs claude.ai login or API key | `CLAUDE_CODE_SKIP_FAST_MODE_ORG_CHECK=1` |
| `/feedback` saves a local file | Gateway credentials are not Anthropic credentials | Archive in `~/.claude/feedback-bundles/`; send to account rep |
| Login prompt though curl works | No credential of its own; project settings `env` applies only after first-run wizard and trust prompt | Set token in shell, `~/.claude/settings.json` or managed settings |
| `ANTHROPIC_API_KEY` ignored with no prompt | A previously declined key stays ignored | Enable under `/config` `Use custom API key` |
| `This machine's managed settings require a first-party login` / `Administrator policy requires a Cloud gateway sign-in` | `forceLoginMethod`, `forceLoginOrgUUID`, `forceLoginGatewayUrl` cannot coexist with gateway credentials | Admin removes those keys or the credential |
| `403` HTML body, nothing in gateway logs | WAF blocked body (XSS rules match tags and code) | Exempt `/v1/messages` from body inspection (AWS WAF `CrossSiteScripting_Body`) |
| TLS errors when curl works | Runtime trusts different CAs | `NODE_EXTRA_CA_CERTS` to the CA bundle |
