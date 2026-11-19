---
type: "Release Digest"
title: "Settings, environment variables and CLI, 2.1.296 to 2.1.328"
description: "Release-note changes to settings keys, environment variables, command-line flags and subcommands, and gateway and login settings between 2.1.296 and 2.1.328."
resource: "https://code.claude.com/docs/en/changelog"
tags: [settings, env-vars, cli-flags, gateway, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "CLAUDE_CODE_DISABLE_SHELL_HEAD_START"
  - "CLAUDE_CODE_GATEWAY_HINT_HEADERS"
  - "x-claude-code-managed-settings-checksum"
  - "attributionProject"
  - "admin.billing_group_tag"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "DISABLE_TELEMETRY"
  - "DO_NOT_TRACK"
  - "CLAUDE_CODE_AUTOMOUNT_ROOTS"
  - "CLAUDE_CODE_PERFORCE_MODE"
  - "CLAUDE_CODE_CERT_STORE"
  - "CLAUDE_CODE_DISABLE_LOOPED_CROSS_CERT_DROP"
  - "NODE_EXTRA_CA_CERTS"
  - "ALL_PROXY"
  - "HTTPS_PROXY"
  - "CLAUDE_CODE_ATTRIBUTION_HEADER"
  - "forceLoginGatewayUrl"
  - "forceLoginMethod"
  - "managed.policy_mode"
  - "policy_mode"
  - "oidc.user_id_claim"
  - "login_notice"
  - "CLAUDE_GATEWAY_LOG_FORMAT"
  - "assume_role"
  - "guardrail.input_tagging"
  - "guardrail_trace"
  - "listen.trusted_proxies"
  - "groups"
  - "managed.policies"
  - "desktopHome"
  - "coworkTabEnabled"
  - "chatSessionRetentionDays"
  - "axScreenReader"
  - "CLAUDE_AX_SCREEN_READER"
  - "FORCE_HYPERLINK"
  - "/tui"
  - "/config"
  - "--settings"
  - "claude doctor"
  - "/doctor"
  - "claude install"
  - "claude gateway"
  - "claude auth login"
  - "claude auth logout"
  - "claude setup-token"
  - "claude purge"
  - "--help"
  - "promptSuggestionEnabled"
  - "claudeCode.promptSuggestions"
  - "claudeCode.attachSelection"
  - "claudeCode.spinnerVerbs"
  - "spinnerVerbs"
  - "prefersReducedMotion"
  - "claudeCode.claudeProcessWrapper"
  - "CLAUDE_CODE_PROXY_RESOLVES_HOSTS"
  - "CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST"
  - "CLAUDE_CODE_DISABLE_FEATURE_FLAGS"
  - "CLAUDE_CODE_DISABLE_ULTRATHINK"
  - "CLAUDE_CODE_RESUME_HINT_COMMAND"
  - "policyHelper"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.296 to 2.1.328"
stale_after: "2027-01-19T00:00:00Z"
---

# What changed

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.328 | 2026-11-19 | Gateway startup warning for invalid policy maxEffortLevel; /status and claude doctor warn about OTel exporter with no endpoint. | `claude doctor` |
| 2.1.327 | 2026-11-17 | Added x-claude-code-managed-settings-checksum to gateway hint headers (sent where managed settings set CLAUDE_CODE_GATEWAY_HINT_HEADERS=1). | `x-claude-code-managed-settings-checksum`, `CLAUDE_CODE_GATEWAY_HINT_HEADERS` |
| 2.1.327 | 2026-11-17 | Added attributionProject setting to name a session's billing group for gateways that set admin.billing_group_tag. | `attributionProject`, `admin.billing_group_tag` |
| 2.1.327 | 2026-11-17 | Added /tui classic as the name for the non-fullscreen renderer; /tui default still works. | `/tui` |
| 2.1.327 | 2026-11-17 | Added CLAUDE_CODE_DISABLE_SHELL_HEAD_START=1 to stop shell start-up files running before the first Bash command is approved. | `CLAUDE_CODE_DISABLE_SHELL_HEAD_START` |
| 2.1.327 | 2026-11-17 | Anthropic-hosted cloud sessions ignore more repository flag and plugin delivery settings; CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC acts at most as DISABLE_TELEMETRY there. | `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, `DISABLE_TELEMETRY` |
| 2.1.327 | 2026-11-17 | /status lists broken config files and ignored permission settings; /config notes when other settings override a row. | `/config`, `/status` |
| 2.1.326 | 2026-11-16 | /status row says when a provider or DISABLE_TELEMETRY turns features off; commands that are off say why instead of Unknown command. | `/status` |
| 2.1.326 | 2026-11-16 | Added --await-initialize refusal with --bg; subcommand wording changes with JSON output unchanged; /claude-api skill builds on Managed Agents by default. | |
| 2.1.326 | 2026-11-16 | First-run theme preselects Auto (match terminal); /doctor shares findings as it works; settings and .mcp.json JSON errors give line and column. | `/doctor` |
| 2.1.325 | 2026-11-13 | Marketplace ref accepts any commit on a branch or tag; plugin downloads use CONNECT with ALL_PROXY. | `ALL_PROXY` |
| 2.1.323 | 2026-11-12 | Organization settings and policy requests no longer use a proxy set only by ALL_PROXY; set HTTPS_PROXY. | `ALL_PROXY`, `HTTPS_PROXY` |
| 2.1.323 | 2026-11-12 | Added CLAUDE_CODE_PERFORCE_MODE startup notice when Perforce settings are found and mode is off; CLAUDE_CODE_AUTOMOUNT_ROOTS for autofs map roots deeper than one folder below /. | `CLAUDE_CODE_PERFORCE_MODE`, `CLAUDE_CODE_AUTOMOUNT_ROOTS` |
| 2.1.323 | 2026-11-12 | CLAUDE_CODE_AUTO_MODE_MODEL supported in managed settings for Desktop sessions on third-party providers; managed policyHelper no longer reads env from user or --settings files. | `CLAUDE_CODE_AUTO_MODE_MODEL`, `policyHelper` |
| 2.1.323 | 2026-11-12 | Remote Control and others: DISABLE_TELEMETRY or DO_NOT_TRACK no longer hides permission details from other devices (fix). | `DO_NOT_TRACK` |
| 2.1.321 | 2026-11-09 | Gateway: Bedrock, Vertex and Foundry upstreams ignore ANTHROPIC_*_BASE_URL variables in the gateway environment; set base_url on the upstream. managed policy_mode layered now adds managed MCP servers over every matching policy. | `policy_mode`, `base_url` |
| 2.1.319 | 2026-11-06 | Gateway: admin.pooled_conflict_rule, admin.pooled_priority_order, login_notice, CLAUDE_GATEWAY_LOG_FORMAT=json and several boot warnings (desktopHome, GovCloud mixing, Bedrock guardrail header). | `login_notice`, `CLAUDE_GATEWAY_LOG_FORMAT`, `desktopHome`, `coworkTabEnabled`, `chatSessionRetentionDays` |
| 2.1.318 | 2026-11-04 | Gateway: assume_role on mantle upstreams; IDE extension no longer installed or updated when Claude Code starts in an IDE terminal; a log warning when a federation Google token is about to expire. | `assume_role` |
| 2.1.316 | 2026-10-31 | Gateway: managed.policy_mode layered; guardrail.input_tagging on Bedrock upstreams; CLAUDE_CODE_DISABLE_LOOPED_CROSS_CERT_DROP; CLAUDE_CODE_DISABLE_ULTRATHINK. | `managed.policy_mode`, `guardrail.input_tagging`, `CLAUDE_CODE_DISABLE_LOOPED_CROSS_CERT_DROP`, `CLAUDE_CODE_DISABLE_ULTRATHINK` |
| 2.1.314 | 2026-10-30 | Gateway upstreams gain an optional groups list; Bedrock upstreams gain guardrail_trace; FORCE_HYPERLINK=false (also no, off) now turns hyperlinks off. | `groups`, `guardrail_trace`, `FORCE_HYPERLINK` |
| 2.1.312 | 2026-10-27 | Gateway: oidc.user_id_claim identifies people by an id_token claim other than sub. | `oidc.user_id_claim` |
| 2.1.311 | 2026-10-26 | DISABLE_COMPACT in settings files can only turn compaction off; VS Code extension starts sessions with DISABLE_TELEMETRY set when VS Code's telemetry setting is off. | `DISABLE_COMPACT` |
| 2.1.307 | 2026-10-21 | axScreenReader and CLAUDE_AX_SCREEN_READER in a settings env block apply only from user, managed or --settings settings (since 2.1.305). | `axScreenReader`, `CLAUDE_AX_SCREEN_READER` |
| 2.1.307 | 2026-10-21 | Added /claude-api api-version to move API code to version 2026-10-21. | `/claude-api` |
| 2.1.305 | 2026-10-20 | VS Code spinnerVerbs and similar display fixes (see apps table). | |
| 2.1.300 | 2026-10-14 | Gateway: claude gateway stops at start on a desktop policy key Claude Desktop cannot use; forceLoginGatewayUrl naming an Anthropic-operated gateway applies managed settings in Desktop's Code tab. | `claude gateway`, `forceLoginGatewayUrl` |
| 2.1.299 | 2026-10-14 | CLAUDE_CODE_ATTRIBUTION_HEADER=0 in a gateway code policy's env turns off the attribution block in Desktop's Code tab and in sessions behind a gateway. | `CLAUDE_CODE_ATTRIBUTION_HEADER` |
| 2.1.296 | 2026-10-09 | Added a code key to the gateway's managed.policies[] (same settings as cli, also in Desktop's Code tab). | `managed.policies`, `code` |
| 2.1.296 | 2026-10-09 | --debug names unrecognized frontmatter fields in custom agent files. | `--debug` |
