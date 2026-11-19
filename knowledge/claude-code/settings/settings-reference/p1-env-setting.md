---
type: "Feature"
title: "env setting and ignored variables"
description: "The env key sets environment variables for every session and subprocess; lists which variables project and local settings may not set."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [env, environment-variables, settings, telemetry]
kind: "setting"
maturity: "unlabelled"
since: "2.1.282"
surfaces: [cli, headless, sdk]
requires: "OTEL group ignored in project/local needs v2.1.282"
identifiers:
  - "env"
  - "CLAUDE_CONFIG_DIR"
  - "CLAUDE_CODE_TMPDIR"
  - "OTEL_LOG_RAW_API_BODIES"
  - "ENABLE_BETA_TRACING_DETAILED"
  - "BETA_TRACING_ENDPOINT"
  - "CLAUDE_CODE_ENABLE_TELEMETRY"
  - "CLAUDE_CODE_ENHANCED_TELEMETRY_BETA"
  - "ENABLE_ENHANCED_TELEMETRY_BETA"
  - "OTEL_LOGS_EXPORTER"
  - "OTEL_METRICS_EXPORTER"
  - "OTEL_TRACES_EXPORTER"
  - "OTEL_LOG_USER_PROMPTS"
  - "OTEL_LOG_ASSISTANT_RESPONSES"
  - "OTEL_LOG_TOOL_CONTENT"
  - "OTEL_LOG_TOOL_DETAILS"
  - "OTEL_EXPORTER_OTLP_*"
  - "OTEL_EXPORTER_PROMETHEUS_HOST"
  - "OTEL_EXPORTER_PROMETHEUS_PORT"
  - "OTEL_RESOURCE_INCLUDE_HOST"
  - "CLAUDE_CODE_PROCESS_WRAPPER"
  - "CLAUDE_CODE_SYNC_SKILLS"
  - "CLAUDE_CODE_SYNC_PLUGINS"
  - "CLAUDE_CODE_PLUGIN_CACHE_DIR"
  - "CLAUDE_CODE_PLUGIN_SEED_DIR"
  - "CLAUDE_CODE_OAUTH_TOKEN"
  - "CLAUDE_CODE_OAUTH_REFRESH_TOKEN"
  - "CLAUDE_CODE_OAUTH_SCOPES"
  - "CLAUDE_AX_SCREEN_READER"
  - "CLAUDE_AX_STARTUP_QUIET_MS"
  - "CLAUDE_CODE_USER_DIALOG_TIMEOUT_MS"
  - "CLAUDE_CODE_DISABLE_ATTACHMENTS"
  - "CLAUDE_CODE_DISABLE_FILE_MENTIONS"
  - "CLAUDE_CODE_EXPERIMENTAL_CODE_MODE"
  - "CLAUDE_CODE_REMOTE"
  - "CLAUDE_CODE_ACCOUNT_UUID"
  - "CLAUDE_CODE_MESSAGING_SOCKET"
  - "CLAUDE_CODE_MESSAGING_TOKEN"
  - "CLAUDE_CODE_PROJECT_DIR_NAME"
  - "CLAUDE_CODE_RESTRICTED"
  - "CLAUDE_CODE_DISABLE_POWERSHELL_CMD_RM_DENY"
  - "CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT"
  - "CLAUDE_CODE_DISABLE_SUBSTITUTION_RM_PROMPT"
  - "CLAUDE_CODE_DISABLE_INLINE_SHELL_RM_PROMPT"
  - "CLAUDE_CODE_STRICT_INLINE_SHELL_RM_PROMPT"
  - "CLAUDE_CODE_DISABLE_MOUNTED_DRIVE_RM_PROMPT"
  - "CLAUDE_CODE_DISABLE_ULTRAREVIEW_TRUST_CHECK"
  - "CLAUDE_CODE_EVEN_MORE_DANGEROUSLY_SKIP_PERMISSIONS"
  - "CLAUDE_CODE_WARN_DISK_FREE_GIB"
  - "CLAUDE_CODE_WARN_MEMORY_FREE_GIB"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`env` (scope `Any file`, object of variable name to string value, default unset) sets environment variables for every session and for the subprocesses Claude Code starts. Most variables in the environment variables reference can go here, which is how to apply one to every session or roll it out to a team.

```json
{ "env": { "DISABLE_AUTO_COMPACT": "1", "ANTHROPIC_BASE_URL": "https://proxy.example.com" } }
```

# How to use it

How values interact with the shell:
- A value here overwrites the same variable exported in the shell; among files the highest-precedence wins.
- When the Claude Desktop app or a self-hosted environment runner starts the session, its launch environment wins and a settings `env` value for a variable it already sets is ignored (the debug log can name it).
- Set a variable to `""` to cancel a shell export; it counts as unset for provider selection and subprocesses inherit the empty value.
- `NO_COLOR` and `FORCE_COLOR` set here reach only subprocesses, not Claude Code's own colors.
- Values are plain text and reach every subprocess; use `otelHeadersHelper` for rotating OTLP tokens and `apiKeyHelper` for API credentials.

When applied: user settings, `--settings`, managed settings at startup and again on a saved change to the merged `env`; project and local settings after workspace trust, or at startup in `-p` mode (which never shows the trust dialog); variables classified safe (model selection, timeouts and limits, feature toggles) at startup from every file except the ignored ones; after `/cd` (v2.1.246+) the new directory's project and local `env` is layered on the previous.

# Limits and defaults

Project and local settings drop (warning visible with `claude --debug`) variables a checked-out repository should not control; set them in the shell, user settings or managed settings:

| Group | Variables |
| :- | :- |
| Where files are stored | `CLAUDE_CONFIG_DIR`, `CLAUDE_CODE_TMPDIR`, OS dir variables (`HOME`, `TMPDIR`, `TMP`, `TEMP`, `XDG_*`) |
| Windows program and config paths | `SystemRoot`, `ComSpec`, `ProgramData`, `LOCALAPPDATA`, `PATHEXT`, `PSModulePath`, `ProgramFiles` family |
| Session-content export | `OTEL_LOG_RAW_API_BODIES`, `ENABLE_BETA_TRACING_DETAILED`, `BETA_TRACING_ENDPOINT` |
| OpenTelemetry on/where/what (needs v2.1.282) | `CLAUDE_CODE_ENABLE_TELEMETRY`, `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA`, `ENABLE_ENHANCED_TELEMETRY_BETA`, `OTEL_LOGS_EXPORTER`, `OTEL_METRICS_EXPORTER`, `OTEL_TRACES_EXPORTER`, `OTEL_LOG_USER_PROMPTS`, `OTEL_LOG_ASSISTANT_RESPONSES`, `OTEL_LOG_TOOL_CONTENT`, `OTEL_LOG_TOOL_DETAILS`, `OTEL_EXPORTER_OTLP_*` ending `_ENDPOINT`, `_HEADERS`, `_PROTOCOL`, `_CERTIFICATE`, `_CLIENT_KEY`, `_INSECURE`, `OTEL_EXPORTER_PROMETHEUS_HOST`, `OTEL_EXPORTER_PROMETHEUS_PORT`, `OTEL_RESOURCE_INCLUDE_HOST` |
| Startup and sync | `CLAUDE_CODE_PROCESS_WRAPPER`, `CLAUDE_CODE_SYNC_SKILLS`, `CLAUDE_CODE_SYNC_PLUGINS`, `CLAUDE_CODE_PLUGIN_CACHE_DIR`, `CLAUDE_CODE_PLUGIN_SEED_DIR` |
| claude.ai sign-in | `CLAUDE_CODE_OAUTH_TOKEN`, `CLAUDE_CODE_OAUTH_REFRESH_TOKEN`, `CLAUDE_CODE_OAUTH_SCOPES` |
| Accessibility | `CLAUDE_AX_SCREEN_READER` and other `CLAUDE_AX_*` (e.g. `CLAUDE_AX_STARTUP_QUIET_MS`) |
| Dialog and attachments (ignored from v2.1.290) | `CLAUDE_CODE_USER_DIALOG_TIMEOUT_MS`, `CLAUDE_CODE_DISABLE_ATTACHMENTS` |
| Mentions | `CLAUDE_CODE_DISABLE_FILE_MENTIONS` |

- From the OTel group, only values that turn something off still apply from project/local settings: `none` for the three exporter selectors and an off value such as `0` for `OTEL_LOG_USER_PROMPTS`, `OTEL_LOG_TOOL_CONTENT`, `OTEL_LOG_TOOL_DETAILS`. Such a value overrides user settings but not the launch environment, a `--settings` file or managed settings. Interactive sessions show a startup notice; `/status` and `claude doctor` list ignored names (never values). `-p` and Agent SDK sessions show no notice, so check the collector still receives data after upgrading.
- Before v2.1.251 project/local could also set the file-location and session-content variables (except `HOME` and `XDG_CONFIG_HOME`); before v2.1.290 also the dialog timer and `CLAUDE_CODE_DISABLE_ATTACHMENTS`.
- `CLAUDE_CODE_EXPERIMENTAL_CODE_MODE` turns Code Mode on from the shell, user settings or a `--settings` file only, not managed, project or local; a `0` in any of the first three or in managed settings keeps it off. When managed settings contain `1`, set your own `1` in user settings; a shell `1` is ignored.
- Ignored from every file: identity variables owned by hosting environments (`CLAUDE_CODE_REMOTE`, `CLAUDE_CODE_ACCOUNT_UUID`); `CLAUDE_CODE_MESSAGING_SOCKET` (v2.1.224+) and `CLAUDE_CODE_MESSAGING_TOKEN` (v2.1.228+), exported by Claude Code itself; launch-environment-only variables `CLAUDE_CODE_PROJECT_DIR_NAME` (v2.1.234+), `CLAUDE_CODE_RESTRICTED`, `CLAUDE_CODE_DISABLE_POWERSHELL_CMD_RM_DENY` (v2.1.283+), `CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT`, `CLAUDE_CODE_DISABLE_SUBSTITUTION_RM_PROMPT`, `CLAUDE_CODE_DISABLE_INLINE_SHELL_RM_PROMPT`, `CLAUDE_CODE_STRICT_INLINE_SHELL_RM_PROMPT`, `CLAUDE_CODE_DISABLE_MOUNTED_DRIVE_RM_PROMPT`, `CLAUDE_CODE_DISABLE_ULTRAREVIEW_TRUST_CHECK`, `CLAUDE_CODE_EVEN_MORE_DANGEROUSLY_SKIP_PERMISSIONS`, `CLAUDE_CODE_WARN_DISK_FREE_GIB` and `CLAUDE_CODE_WARN_MEMORY_FREE_GIB` (both v2.1.304+).
