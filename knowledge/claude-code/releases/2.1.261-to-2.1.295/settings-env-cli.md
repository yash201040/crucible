---
type: "Release Digest"
title: "Settings, environment variables and CLI, 2.1.261 to 2.1.295"
description: "Release-note entries for settings keys, environment variables, command-line flags and subcommands not covered by other themes, 2.1.261 to 2.1.295."
resource: "https://code.claude.com/docs/en/changelog"
tags: [settings, env-vars, cli, flags, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "forceLoginMethod"
  - "forceLoginGatewayUrl"
  - "attribution"
  - "maxProseWidth"
  - "bashEditDiffEnabled"
  - "CLAUDE_AX_PREPARK_MS"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "otelHeadersHelper"
  - "--bare"
  - "--system-prompt"
  - "--append-system-prompt"
  - "--desktop"
  - "claude purge"
  - "claude attach"
  - "claude logs"
  - "claude auth status --json"
  - "claude doctor"
  - "/status"
  - "--worktree"
  - "claudeCode.environmentVariables"
  - "CLAUDE_CONFIG_DIR"
  - "keybindingFlavor"
  - "keybindings.json"
  - "gateway.yaml"
  - "access_control.allow_cidrs"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.261 to 2.1.295"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Release-note rows (bug fixes removed) for settings, flags and variables that did not fit another theme. Many orchestration-relevant variables are in the other digests of this range (retry, MCP, workflow, gateway, permissions).

# How to use it

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.295 | 2026-10-08 | `forceLoginMethod: "gateway"` and `forceLoginGatewayUrl` now work in your own user settings on machines with no managed settings. | `forceLoginMethod`, `forceLoginGatewayUrl` |
| 2.1.292 | 2026-10-06 | Usage-limit messages write claude.ai settings links with https:// to be clickable. | |
| 2.1.290 | 2026-10-05 | `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` also skips startup connection warm-up; background daemon log writes multi-line messages as one JSON-quoted line. | `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` |
| 2.1.288 | 2026-10-02 | `claude project purge` becomes `claude purge`. | `claude purge` |
| 2.1.287 | 2026-10-01 | `CLAUDE_AX_PREPARK_MS=50` restores the pause before screen-reader output. | `CLAUDE_AX_PREPARK_MS` |
| 2.1.286 | 2026-09-30 | `--bare` limits MCP servers to those named on the command line, no system reminders, no background tasks. | `--bare` |
| 2.1.285 | 2026-09-29 | `claude --desktop`; `allowedProviders` managed setting; `CLAUDE_CODE_DISABLE_WEB_FETCH`; `CLAUDE_CODE_NONSTREAMING_TIMEOUT_RETRIES`. | `--desktop`, `allowedProviders` |
| 2.1.283 | 2026-09-25 | `--system-prompt` and `--append-system-prompt` accept their text and `-file` forms together (file text first). | `--system-prompt`, `--append-system-prompt` |
| 2.1.282 | 2026-09-24 | `maxProseWidth` setting caps prose width in wide terminals; startup notice and `/status`, `claude doctor` entries list ignored telemetry variables from project settings. | `maxProseWidth`, `claude doctor` |
| 2.1.281 | 2026-09-23 | `"attribution": false` in settings.json hides all commit and PR attribution (older CLIs skip a settings file with it, so keep object form in shared files); debug logs name settings `env` variables ignored because launch environment already sets them. | `attribution` |
| 2.1.277 | 2026-09-18 | Gateway env `CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1`. | `CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY` |
| 2.1.275 | 2026-09-17 | Startup warning when a configured `otelHeadersHelper` fails. | `otelHeadersHelper` |
| 2.1.269 | 2026-09-11 | `bashEditDiffEnabled` setting adds a diff of files a Bash command changed to its result. | `bashEditDiffEnabled` |
| 2.1.268 | 2026-09-10 | `claude auth status --json` gains `configDirectory`; gateway startup warning for empty `access_control.allow_cidrs`. | `configDirectory`, `access_control.allow_cidrs` |
| 2.1.265 | 2026-09-08 | `forceLoginGatewayUrl` in managed settings makes gateway sessions from startup. | `forceLoginGatewayUrl` |
| 2.1.261 | 2026-09-04 | `bashOutputMaxChars`/`taskOutputMaxChars`; `--append-subagent-system-prompt-file`; prompt word-editing keys match Bash (`keybindingFlavor` has no effect); `/status` and `claude doctor` "Organization policy" line. | `bashOutputMaxChars`, `taskOutputMaxChars`, `--append-subagent-system-prompt-file`, `keybindingFlavor` |
