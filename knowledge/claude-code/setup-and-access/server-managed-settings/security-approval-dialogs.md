---
type: "Reference"
title: "Security approval dialogs for delivered settings"
description: "Which server-delivered settings need user approval, approval memory, and non-interactive behavior."
resource: "https://code.claude.com/docs/en/server-managed-settings#security-approval-dialogs"
tags: [server-managed, approval, hooks, headless]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.251"
surfaces: [cli, headless, sdk, ide, desktop]
requires: ""
identifiers:
  - "apiKeyHelper"
  - "statusLine"
  - "otelHeadersHelper"
  - "sandbox.bwrapPath"
  - "sandbox.socatPath"
  - "sandbox.ripgrep"
  - "sandbox.network.tlsTerminate"
  - "sandbox.credentials"
  - "sandbox.filesystem.disabled"
  - "claudeMd"
  - "ANTHROPIC_CUSTOM_HEADERS"
  - "API_FORCE_IDLE_TIMEOUT"
  - "DISABLE_TELEMETRY"
  - "DO_NOT_TRACK"
  - "DISABLE_ERROR_REPORTING"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "CLAUDE_CODE_DISABLE_1M_CONTEXT"
  - "OTEL_EXPORTER_OTLP_ENDPOINT"
  - "OTEL_LOG_RAW_API_BODIES"
  - "ENABLE_BETA_TRACING_DETAILED"
  - "ConfigChange"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "server-managed-settings"
    resource: "https://code.claude.com/docs/en/server-managed-settings"
    title: "Configure server-managed settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Settings that could pose security risk require explicit approval in an interactive session before they apply. Rejecting makes Claude Code exit.

# How to use it

Needs approval: shell-command settings (`apiKeyHelper`, `statusLine`, `otelHeadersHelper`); sandbox binary settings (`sandbox.bwrapPath`, `sandbox.socatPath`, `sandbox.ripgrep`); sandbox network/isolation settings (`sandbox.network.tlsTerminate`, `httpProxyPort`, `socksProxyPort`, `sandbox.credentials`, `allowAppleEvents`, `allowNestedUserNamespaces`, `enableWeakerNestedSandbox`, `enableWeakerNetworkIsolation`, `sandbox.filesystem.disabled`, `network.allowAllUnixSockets`, `allowUnixSockets`, `allowMachLookup`; before v2.1.251 no approval; a deny-only `sandbox.credentials` needs none); some `env` variables; any hook. A managed CLAUDE.md via `claudeMd` needs none (v2.1.260+; earlier it did).

Env without approval: feature toggles, model selection (`ANTHROPIC_MODEL`, `DISABLE_PROMPT_CACHING`, `CLAUDE_CODE_EFFORT_LEVEL`), context/compaction (`DISABLE_AUTO_COMPACT`, but not `CLAUDE_CODE_DISABLE_1M_CONTEXT`), UI options, numeric limits. Always approval (non-empty): proxy or base-URL variables, `OTEL_EXPORTER_OTLP_ENDPOINT`, `CLAUDE_CODE_DISABLE_1M_CONTEXT`. By value: `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, `DISABLE_ERROR_REPORTING`, `DISABLE_TELEMETRY`, `DO_NOT_TRACK` with truthy values need none; `API_FORCE_IDLE_TIMEOUT` truthy none (before v2.1.248 any value triggered it); `ANTHROPIC_CUSTOM_HEADERS` lines naming credentials, org/tenant selectors, routing/host overrides or API-behavior headers (`Authorization`, `X-Api-Key`, `Host`, `anthropic-beta`, `X-Amzn-Bedrock-*`) need approval (before v2.1.251 none); falsy `ENABLE_BETA_TRACING_DETAILED` or `OTEL_LOG_RAW_API_BODIES` need none.

# Limits and defaults

- Approval memory in the config directory: claude.ai login or keyless Console sign-in - one per organization (latest account); gateway - one per gateway (re-shown on change, different gateway, new certificate; none saved for a loopback http dev gateway); other credentials (API key, `CLAUDE_CODE_OAUTH_TOKEN`) - one per delivered settings, kept with the cache and cleared by `/logout` or `claude auth logout`.
- Non-interactive runs (`claude -p`, Agent SDK, VS Code chat panel, desktop Code tab): settings needing approval apply for that run only, are not recorded as approved or cached, so each such run refetches at startup. `claude install` / `claude update` run on last-approved settings (v2.1.246+). A `claude plugin` command without keyboard input uses last-approved settings or errors without a cache.
- `ConfigChange` hooks do not fire for server-managed or MDM changes and cannot block a `policy_settings` change.
