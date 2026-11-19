---
type: "Release Digest"
title: "Headless, SDK and automation, 2.1.261 to 2.1.295"
description: "Release-note entries for claude -p, Agent SDK sessions, routines, self-hosted runners, cloud sessions and unattended behavior from 2.1.261 to 2.1.295."
resource: "https://code.claude.com/docs/en/changelog"
tags: [headless, sdk, unattended, routines, release-notes, runner]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [headless, sdk, cloud]
requires: ""
identifiers:
  - "claude -p"
  - "CLAUDE_CODE_RETRY_WATCHDOG"
  - "CLAUDE_CODE_RETRY_WATCHDOG_MAX_WAIT_MS"
  - "rate_limit_event"
  - "--input-format stream-json"
  - "CLAUDE_CODE_MCP_STARTUP_WAIT_MS"
  - "plugin_errors"
  - "system/init"
  - "--bare"
  - "--permission-mode"
  - "claude self-hosted-runner"
  - "--drain-marker-file"
  - "--remove-session-state"
  - "--use-anthropic-git-proxy"
  - "--retire-at"
  - "--configure-git"
  - "--system-prompt-file"
  - "--append-system-prompt-file"
  - "claude --environment"
  - "CLAUDE_RUNNER_FETCH_SERVER_PROGRESS_CAP_MS"
  - "CCR_AUTO_MODE_ALLOW"
  - "CCR_AUTO_MODE_ENVIRONMENT"
  - "CCR_AUTO_MODE_SOFT_DENY"
  - "GIT_ALLOW_PROTOCOL"
  - "claude mcp serve"
  - "/fast"
  - "ping"
  - "/btw"
  - "/recap"
  - "/output-style"
  - "/ultrareview"
  - "CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.261 to 2.1.295"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Release-note rows (bug fixes removed) for non-interactive runs (`-p`, Agent SDK, stream-json), scheduled routines, cloud sessions and self-hosted runners. Newest first.

# How to use it

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.295 | 2026-10-08 | A `claude -p` run that stays open after its last turn prints a stderr line (when a terminal) saying what it is waiting for. | `claude -p` |
| 2.1.295 | 2026-10-08 | New `CLAUDE_CODE_RETRY_WATCHDOG_MAX_WAIT_MS` caps how long unattended retry mode waits out 429 and 529 errors. | `CLAUDE_CODE_RETRY_WATCHDOG_MAX_WAIT_MS`, `CLAUDE_CODE_RETRY_WATCHDOG` |
| 2.1.295 | 2026-10-08 | Headless `rate_limit_event` usage-limit warnings say whether the account has extra usage turned on. | `rate_limit_event` |
| 2.1.295 | 2026-10-08 | Scheduled and Run-now routine runs with telemetry disabled publish new private artifacts and update your own without asking. | |
| 2.1.295 | 2026-10-08 | Self-hosted runner no longer passes `CCR_AUTO_MODE_ALLOW`, `CCR_AUTO_MODE_ENVIRONMENT`, `CCR_AUTO_MODE_SOFT_DENY` into a session's environment. | `CCR_AUTO_MODE_ALLOW`, `CCR_AUTO_MODE_ENVIRONMENT`, `CCR_AUTO_MODE_SOFT_DENY` |
| 2.1.293 | 2026-10-07 | Self-hosted runner orchestrator sleeps 4-6 s between polls (was constant 5 s) so replicas desynchronize. | |
| 2.1.292 | 2026-10-06 | `claude -p` and SDK first turn no longer waits for HTTP and SSE MCP servers to answer `resources/list`. | `claude -p` |
| 2.1.292 | 2026-10-06 | Scheduled and Run-now routine runs publish a new private artifact without approval (connector/other-access requests still ask). | |
| 2.1.290 | 2026-10-05 | Self-hosted runners: `claude --environment <id>` creates its session through the current Sessions API; session ids keep `session_...` form. | `claude --environment` |
| 2.1.288 | 2026-10-02 | Background command time limit applies only in unattended sessions (`-p`, Agent SDK, CI, cloud); terminal, desktop and VS Code have no limit. | `-p` |
| 2.1.288 | 2026-10-02 | Cloud session first turn no longer waits for a stdio MCP server configured with `alwaysLoad: false`. | `alwaysLoad` |
| 2.1.287 | 2026-10-01 | SDK: a message with priority "now" no longer cancels a running web fetch or web search. | |
| 2.1.287 | 2026-10-01 | Headless MCP startup retries a remote server whose first connect failed transiently without waiting for the slowest server. | |
| 2.1.286 | 2026-09-30 | `--bare` connects only MCP servers named on the command line, sends no system reminders, starts no background tasks; a shell command reaching its timeout stops instead of backgrounding. | `--bare` |
| 2.1.286 | 2026-09-30 | One retry limit covers a whole model call: with default retry settings a failing call sends at most 14 requests. | |
| 2.1.286 | 2026-09-30 | SDK and `-p` sessions are more responsive when a host re-sends an MCP server enable for an already-connected server. | |
| 2.1.285 | 2026-09-29 | `claude -p` and Python Agent SDK on third-party providers or with telemetry off start in auto mode when no permission mode is configured; `--permission-mode` overrides. | `claude -p`, `--permission-mode` |
| 2.1.285 | 2026-09-29 | With partial messages on, a `ping` stream event is sent every 30 s during a non-streaming fallback request (Anthropic API, Claude Platform on AWS, gateways). | `ping` |
| 2.1.285 | 2026-09-29 | New `CLAUDE_CODE_NONSTREAMING_TIMEOUT_RETRIES` caps re-sends of a timed-out non-streaming fallback request. | `CLAUDE_CODE_NONSTREAMING_TIMEOUT_RETRIES` |
| 2.1.284 | 2026-09-28 | Non-interactive first turn still waits up to 2 s for MCP servers named by `--allowedTools` or an `mcp_tool` hook, even when `CLAUDE_CODE_MCP_STARTUP_WAIT_MS` is 0. | `--allowedTools`, `CLAUDE_CODE_MCP_STARTUP_WAIT_MS` |
| 2.1.284 | 2026-09-28 | `/recap` declines when relayed from a chat thread, routine or webhook; works from terminal, apps, Remote Control, `-p` or SDK host. | `/recap` |
| 2.1.283 | 2026-09-25 | `plugin_errors` entries for `--plugin-dir` failures in stream-json `system/init` gain `path`. | `plugin_errors`, `system/init`, `--plugin-dir` |
| 2.1.283 | 2026-09-25 | `claude -p` and Claude Code Remote no longer load the interactive UI at startup. | `claude -p` |
| 2.1.283 | 2026-09-25 | New routine schedules default to a few minutes past the hour (exact-hour routines can start minutes late). | |
| 2.1.281 | 2026-09-23 | Dangerous `rm` prompt in `--dangerously-skip-permissions` and auto mode waits 2 minutes, then denies with a rewrite hint so unattended sessions continue. | `CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT`, `--dangerously-skip-permissions` |
| 2.1.281 | 2026-09-23 | Self-hosted runners pass system prompts as private files; wrappers must use `--system-prompt-file` / `--append-system-prompt-file`. | `--system-prompt-file`, `--append-system-prompt-file` |
| 2.1.280 | 2026-09-22 | Self-hosted runner git in lifecycle hooks ignores hook folders named in shared git files; local-path and `git://` remotes need `GIT_ALLOW_PROTOCOL`. | `GIT_ALLOW_PROTOCOL` |
| 2.1.278 | 2026-09-19 | `/ultrareview` in non-interactive sessions refuses when the repository has no base branch or shared history (2.1.277). | `/ultrareview` |
| 2.1.277 | 2026-09-18 | SDK/headless first turn no longer waits on the per-directory CLAUDE.md lookup; background Haiku auto-title request removed from `claude -p` outside SDK/IDE. | `claude -p` |
| 2.1.277 | 2026-09-18 | Dangerous-rm prompt names the flagged command and suggests a `${VAR:?}` guard so headless runs can recover. | |
| 2.1.275 | 2026-09-17 | Hosted sessions keep an unanswered permission prompt up after a container restart. | |
| 2.1.274 | 2026-09-17 | `CLAUDE_CODE_MCP_STARTUP_WAIT_MS` bounds how long the first non-interactive turn waits for connecting MCP servers (0 = don't wait). | `CLAUDE_CODE_MCP_STARTUP_WAIT_MS` |
| 2.1.274 | 2026-09-17 | `--input-format stream-json` first turn no longer waits up to 2 s for still-connecting MCP servers with deferred tools. | `--input-format stream-json` |
| 2.1.274 | 2026-09-17 | Self-hosted runners skip a read-only repository the git host refuses at the access check instead of failing session start. | |
| 2.1.274 | 2026-09-17 | Routines skip a run and retry for up to 72 hours when the owner's GitHub connection is missing, instead of switching off. | |
| 2.1.273 | 2026-09-15 | Fork of a `--remote-control` session runs as a background session on your computer. | |
| 2.1.271 | 2026-09-14 | Fast mode in Claude Code Remote sessions (cloud and self-hosted): host setting or `/fast` applies where the organization allows. | `/fast` |
| 2.1.271 | 2026-09-14 | `claude self-hosted-runner --drain-marker-file <path>`: if the file exists at a SIGTERM drain, the runner reports a host drain (telemetry only). | `--drain-marker-file`, `claude self-hosted-runner` |
| 2.1.271 | 2026-09-14 | `claude mcp serve` sends a progress update every 30 s from a running tool call. | `claude mcp serve` |
| 2.1.271 | 2026-09-14 | Monitor watches always have a deadline (max 30 min; 10 in single-prompt `-p` runs), replacing the no-timeout `persistent` option. | `persistent` |
| 2.1.269 | 2026-09-11 | `/output-style [name]` works over Remote Control and in cloud and other headless sessions. | `/output-style` |
| 2.1.269 | 2026-09-11 | New `claude plugin eval` runs a plugin eval suite with scored JSON + HTML results. | `claude plugin eval` |
| 2.1.268 | 2026-09-10 | `claude self-hosted-runner --remove-session-state` (default off) deletes per-session directories under `<base-dir>/_sessions/` at session end. | `--remove-session-state` |
| 2.1.267 | 2026-09-09 | Self-hosted runner reports `--use-anthropic-git-proxy` at registration and warns per session on the legacy git proxy. | `--use-anthropic-git-proxy` |
| 2.1.261 | 2026-09-04 | Handling when the API sends no response headers: retry waits up to `API_TIMEOUT_MS` (10 min default). | `API_TIMEOUT_MS` |

# Not found in the documentation pages

- `claude --environment`
- `CCR_AUTO_MODE_ALLOW`
- `CCR_AUTO_MODE_ENVIRONMENT`
- `CCR_AUTO_MODE_SOFT_DENY`
