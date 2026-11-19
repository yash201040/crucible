---
type: "Reference"
title: "Network access requirements and allowlists"
description: "Hosts Claude Code reaches, what each is for and how to disable optional ones, plus provider routing, IP allowlist and GitHub firewall notes."
resource: "https://code.claude.com/docs/en/network-config"
tags: [allowlist, firewall, domains, telemetry]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, web]
requires: ""
identifiers:
  - "api.anthropic.com"
  - "claude.ai"
  - "claude.com"
  - "platform.claude.com"
  - "sso.claude.com"
  - "mcp-proxy.anthropic.com"
  - "downloads.claude.ai"
  - "storage.googleapis.com"
  - "registry.npmjs.org"
  - "bridge.claudeusercontent.com"
  - "*.frame.claudeusercontent.com"
  - "github.com"
  - "raw.githubusercontent.com"
  - "http-intake.logs.us5.datadoghq.com"
  - "browser-intake-us5-datadoghq.com"
  - "formulae.brew.sh"
  - "code.claude.com"
  - "*.claudemcpcontent.com"
  - "ENABLE_CLAUDEAI_MCP_SERVERS"
  - "disableClaudeAiConnectors"
  - "enableArtifact"
  - "CLAUDE_CODE_DISABLE_ARTIFACT"
  - "CLAUDE_CODE_PLUGIN_PREFER_HTTPS"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "DISABLE_TELEMETRY"
  - "DO_NOT_TRACK"
  - "DISABLE_ERROR_REPORTING"
  - "skipWebFetchPreflight"
  - "CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "network-config"
    resource: "https://code.claude.com/docs/en/network-config"
    title: "Enterprise network configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The URLs to allowlist in proxies and firewalls, especially in containers.

# How to use it

| Host | Used for |
|---|---|
| `api.anthropic.com` | Claude API, WebFetch domain safety check, feature flags, telemetry events |
| `claude.ai`, `claude.com`, `platform.claude.com`, `sso.claude.com` | account authentication (Console and claude.ai OAuth token exchange use platform.claude.com; SSO uses sso.claude.com) |
| `mcp-proxy.anthropic.com` | claude.ai MCP connectors; stop with `ENABLE_CLAUDEAI_MCP_SERVERS=false` or `disableClaudeAiConnectors` |
| `downloads.claude.ai` | plugin executables, native installer/updater, version checks |
| `storage.googleapis.com` | plugin install counts; native installer before 2.1.116 |
| `registry.npmjs.org` | plugin installs, npx MCP servers, npm/bun installs |
| `bridge.claudeusercontent.com` | Claude in Chrome WebSocket bridge |
| `*.frame.claudeusercontent.com` | Artifact reads; drop with `"enableArtifact": false` or `CLAUDE_CODE_DISABLE_ARTIFACT=1` |
| `github.com` | cloning plugin marketplaces; `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` for HTTPS only |
| `raw.githubusercontent.com` | `/release-notes` changelog (not fetched in non-interactive or cloud sessions) |
| `*-review.googlesource.com` | Gerrit lookup in Desktop Code tab on googlesource checkouts; optional |
| `http-intake.logs.us5.datadoghq.com`, `browser-intake-us5-datadoghq.com` | optional telemetry and error reports, direct Anthropic API only; disable with `DISABLE_TELEMETRY`, `DO_NOT_TRACK`, `DISABLE_ERROR_REPORTING`, or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` |
| `formulae.brew.sh` | Homebrew update checks |
| `code.claude.com` | documentation lookups only |

- Third-party providers or a Claude apps gateway: model traffic goes to the provider or gateway; WebFetch still calls `api.anthropic.com` for its safety check unless `skipWebFetchPreflight: true`. Sessions on third-party providers never send to the Datadog hosts, even when a platform sets `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST`.
- Fast mode behind an `ANTHROPIC_BASE_URL` gateway: keep `api.anthropic.com` reachable via the proxy; the availability check goes there, never to the gateway.
- IP allowlists: route `bridge.claudeusercontent.com` through the same egress as `claude.ai` and `api.anthropic.com`, or add a dedicated egress address; otherwise Claude in Chrome cannot connect.
- GitHub: cloud sessions and Code Review connect from Anthropic infrastructure; GitHub Enterprise Cloud with IP allow lists needs allow list inheritance for GitHub Apps plus Anthropic outbound IPs; GHES behind a firewall needs Anthropic outbound IPs allowlisted. Self-hosted environment sessions connect from inside your network unless the runner uses the Anthropic git proxy.
- Desktop and claude.ai need extra hosts (`assets-proxy.anthropic.com`, other `*.claudeusercontent.com`; allowing only `claude.ai` yields a blank page) and `*.claudemcpcontent.com` for MCP App widgets. Artifacts optionally use `fonts.googleapis.com`, `fonts.gstatic.com` (fallback fonts if blocked) and libraries from `cdnjs.cloudflare.com`, `cdn.jsdelivr.net`, `cdn.tailwindcss.com`, `code.jquery.com`, `unpkg.com` (no fallback); block with fast rejection, not silent drop.
