---
type: "Release Digest"
title: "Settings, environment variables and CLI (2.1.101 to 2.1.260)"
description: "Release notes 2.1.101 to 2.1.260 on settings keys, environment variables, flags and subcommands."
resource: "https://code.claude.com/docs/en/changelog"
tags: [settings, env-vars, cli, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "timeFormat"
  - "timeZone"
  - "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "policyHelper"
  - "CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST"
  - "keybindingFlavor"
  - "spellcheck"
  - "selection:clear"
  - "CLAUDE_CODE_TOOL_MEMORY_LIMIT"
  - "ANTHROPIC_BEDROCK_REGION_PREFIX"
  - "crossSessionInbound"
  - "dialogExpiry"
  - "remoteControlAtStartup"
  - "emojiCompletionEnabled"
  - "FORCE_HYPERLINK"
  - "vimInsertModeRemaps"
  - "--ax-screen-reader"
  - "CLAUDE_AX_SCREEN_READER"
  - "axScreenReader"
  - "CLAUDE_CODE_RETRY_WATCHDOG"
  - "CLAUDE_CODE_MAX_RETRIES"
  - "CLAUDE_ENABLE_STREAM_WATCHDOG"
  - "CLAUDE_CODE_DISABLE_MOUSE_CLICKS"
  - "CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP"
  - "respondToBashCommands"
  - "teammateMode"
  - "attribution.sessionUrl"
  - "CLAUDE_CLIENT_PRESENCE_FILE"
  - "footerLinksRegexes"
  - "wheelScrollAccelerationEnabled"
  - "API_FORCE_IDLE_TIMEOUT"
  - "requiredMinimumVersion"
  - "requiredMaximumVersion"
  - "CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL"
  - "CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN"
  - "CLAUDE_CODE_FORCE_SYNC_OUTPUT"
  - "CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE"
  - "claude project purge"
  - "--dry-run"
  - "--all"
  - "prUrlTemplate"
  - "CLAUDE_CODE_HIDE_CWD"
  - "DISABLE_UPDATES"
  - "tui"
  - "autoScrollEnabled"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.101 to 2.1.260"
stale_after: "2027-01-19T00:00:00Z"
---

# Changes by version

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.257 | 2026-09-01 | timeFormat and timeZone settings; CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY runs even with CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC; policyHelper in MDM or managed-settings.json refreshes when fetch reports removal | `timeFormat`, `timeZone`, `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY`, `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, `policyHelper` |
| 2.1.251 | 2026-08-28 | Environment CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST sessions skip Bedrock inference-profile discovery | `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` |
| 2.1.238 | 2026-08-20 | keybindingFlavor setting (readline or classic) | `keybindingFlavor` |
| 2.1.235 | 2026-08-18 | spellcheck setting underlines misspellings using aspell, hunspell or ispell | `spellcheck` |
| 2.1.234 | 2026-08-17 | selection:clear keybinding action | `selection:clear` |
| 2.1.233 | 2026-08-14 | CLAUDE_CODE_TOOL_MEMORY_LIMIT opt-in memory cgroup for Bash commands on Linux | `CLAUDE_CODE_TOOL_MEMORY_LIMIT` |
| 2.1.232 | 2026-08-13 | /config rows Dialog expiry and Messages from your other sessions |  |
| 2.1.224 | 2026-08-07 | ANTHROPIC_BEDROCK_REGION_PREFIX prefers a cross-region inference profile; crossSessionInbound, dialogExpiry settings | `ANTHROPIC_BEDROCK_REGION_PREFIX`, `crossSessionInbound`, `dialogExpiry` |
| 2.1.222 | 2026-08-04 | Repo-local settings can no longer turn on Remote Control auto-start (only off); enable at user scope | `remoteControlAtStartup` |
| 2.1.217 | 2026-07-21 | emojiCompletionEnabled setting; FORCE_HYPERLINK=0 opts out of footer link hyperlinks | `emojiCompletionEnabled`, `FORCE_HYPERLINK` |
| 2.1.211 | 2026-07-15 | Integer environment variables accept scientific notation and underscores such as 1e6 and 64_000 |  |
| 2.1.208 | 2026-07-14 | vimInsertModeRemaps setting; screen reader mode via --ax-screen-reader, CLAUDE_AX_SCREEN_READER=1 or axScreenReader | `vimInsertModeRemaps`, `--ax-screen-reader`, `CLAUDE_AX_SCREEN_READER`, `axScreenReader` |
| 2.1.199 | 2026-07-02 | CLAUDE_CODE_RETRY_WATCHDOG raises default retries for non-capacity transient errors to 300 and lifts the 15 cap on CLAUDE_CODE_MAX_RETRIES | `CLAUDE_CODE_RETRY_WATCHDOG`, `CLAUDE_CODE_MAX_RETRIES` |
| 2.1.196 | 2026-06-29 | Streaming idle watchdog on by default for all providers (abort and retry after 5 minutes without events); CLAUDE_ENABLE_STREAM_WATCHDOG=0 disables | `CLAUDE_ENABLE_STREAM_WATCHDOG` |
| 2.1.195 | 2026-06-26 | CLAUDE_CODE_DISABLE_MOUSE_CLICKS disables mouse click, drag and hover in fullscreen | `CLAUDE_CODE_DISABLE_MOUSE_CLICKS` |
| 2.1.193 | 2026-06-25 | CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP=1 disables memory-pressure reaping of idle background shells | `CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP` |
| 2.1.186 | 2026-06-22 | CLAUDE_CODE_MAX_RETRIES capped at 15; respondToBashCommands setting; teammateMode iterm2 | `respondToBashCommands`, `teammateMode` |
| 2.1.183 | 2026-06-19 | attribution.sessionUrl omits the claude.ai session link; /config --help lists shorthand keys | `attribution.sessionUrl` |
| 2.1.181 | 2026-06-17 | CLAUDE_CLIENT_PRESENCE_FILE suppresses mobile push while you are at the machine | `CLAUDE_CLIENT_PRESENCE_FILE` |
| 2.1.176 | 2026-06-12 | footerLinksRegexes setting for footer link badges | `footerLinksRegexes` |
| 2.1.174 | 2026-06-12 | wheelScrollAccelerationEnabled setting | `wheelScrollAccelerationEnabled` |
| 2.1.169 | 2026-06-08 | API_FORCE_IDLE_TIMEOUT=0 opts out of default 5-minute idle timeout on Vertex/Foundry | `API_FORCE_IDLE_TIMEOUT` |
| 2.1.163 | 2026-06-04 | requiredMinimumVersion and requiredMaximumVersion managed settings refuse to start outside the range | `requiredMinimumVersion`, `requiredMaximumVersion` |
| 2.1.136 | 2026-05-08 | CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL re-enables survey for OTel-capturing enterprises | `CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL` |
| 2.1.132 | 2026-05-06 | CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1 keeps native scrollback | `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN` |
| 2.1.129 | 2026-05-06 | CLAUDE_CODE_FORCE_SYNC_OUTPUT=1; CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE for Homebrew and WinGet; skillOverrides | `CLAUDE_CODE_FORCE_SYNC_OUTPUT`, `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE` |
| 2.1.126 | 2026-05-01 | claude project purge [path] deletes all Claude Code state for a project (--dry-run, -y, -i, --all) | `claude project purge`, `--dry-run`, `--all` |
| 2.1.119 | 2026-04-23 | prUrlTemplate setting; CLAUDE_CODE_HIDE_CWD; /config settings persist to ~/.claude/settings.json | `prUrlTemplate`, `CLAUDE_CODE_HIDE_CWD` |
| 2.1.118 | 2026-04-23 | DISABLE_UPDATES blocks all update paths including claude update | `DISABLE_UPDATES` |
| 2.1.110 | 2026-04-15 | /tui command and tui setting; autoScrollEnabled | `tui`, `autoScrollEnabled` |
