---
type: "Reference"
title: "Network requirements and egress proxy authentication"
description: "Hosts a runner and its sessions must reach, hosts that need no allowlisting, and how to authenticate to a corporate egress proxy."
resource: "https://code.claude.com/docs/en/self-hosted-environments-deploy"
tags: [self-hosted, network, egress, proxy, allowlist]
kind: "mixed"
maturity: "beta"
since: "2.1.238"
surfaces: [cloud]
requires: "Claude Code v2.1.238 or later for proxy-authorization flags"
identifiers:
  - "--proxy-authorization-command"
  - "--proxy-authorization-file"
  - "HTTPS_PROXY"
  - "HTTP_PROXY"
  - "ALL_PROXY"
  - "NO_PROXY"
  - "CLAUDE_CODE_DISABLE_ARTIFACT"
  - "CLAUDE_CODE_BYOC_ENABLE_DATADOG"
  - "DISABLE_ERROR_REPORTING"
  - "DISABLE_TELEMETRY"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-deploy"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-deploy"
    title: "Deploy self-hosted environments to production"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Outbound host list for runner and session containers, plus the mechanism for proxies that need a `Proxy-Authorization` header.

# How to use it

Always required:

| Host | Port | Used for |
| :- | :- | :- |
| `api.anthropic.com` | 443 (HTTPS; WSS for Anthropic-managed git) | Control plane, session streaming, inference, feature flags, JWKS, commit signing, managed git |
| Your git host | 443 or 22 | Clone and push. Not needed for github.com on a runner using `--use-anthropic-git-proxy`, unless `--push-outcome-on-release` or a post-session hook pushes. |

Conditional: `api.github.com` (GitHub CLI with a github.com credential); `downloads.claude.ai` (install, official-marketplace plugins; `install.sh` itself is on `claude.ai`); `storage.googleapis.com` (plugin metadata); `code.claude.com` and `claude.com` (docs lookups, pre-approved WebFetch); `*.frame.claudeusercontent.com` (Artifact tool; disable with `CLAUDE_CODE_DISABLE_ARTIFACT=1`); `registry.npmjs.org` (plugins, npx MCP servers); package mirrors; `http-intake.logs.us5.datadoghq.com` (only with `CLAUDE_CODE_BYOC_ENABLE_DATADOG=1`); `browser-intake-us5-datadoghq.com` (error reports, suppressed by `DISABLE_ERROR_REPORTING=1` or `DISABLE_TELEMETRY=1`); cloud provider endpoints when using Bedrock or Agent Platform.

Not needed: `statsig.anthropic.com`, `*.sentry.io`, `claude.ai`, `platform.claude.com`, `mcp-proxy.anthropic.com`. Host-side `claude auth login` and the installer do reach `claude.ai` (and login also `claude.com`, `platform.claude.com`, hcaptcha, Cloudflare challenges, `sso.claude.com`).

Proxy authentication: set `HTTPS_PROXY`/`HTTP_PROXY`, then one of:

| Flag | Source of header value |
| :- | :- |
| `--proxy-authorization-command <command>` | trimmed stdout of a shell command, run per connection |
| `--proxy-authorization-file <path>` | trimmed contents of a file rotated in place |

# Limits and defaults

- Runner refuses to start if both flags are set (a flag plus the other's env var counts), if no `http://`/`https://` proxy URL is in `HTTPS_PROXY`/`HTTP_PROXY` (either case; `ALL_PROXY` ignored), or if passed to `self-hosted-runner orchestrator`.
- The runner starts a loopback (127.0.0.1) forward-proxy listener, rewrites the proxy variables to point at it, removes `ALL_PROXY` and unset spellings in sessions, and pins `NO_PROXY`. New connections pick up rotated tokens without restart; it never logs the header. Failures return `502 Bad Gateway` to the session.
