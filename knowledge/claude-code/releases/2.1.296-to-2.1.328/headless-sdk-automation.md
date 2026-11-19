---
type: "Release Digest"
title: "Headless, SDK and automation, 2.1.296 to 2.1.328"
description: "Release-note changes to claude -p, the Agent SDK, self-hosted runner, remote-control, scheduled tasks and unattended retries between 2.1.296 and 2.1.328."
resource: "https://code.claude.com/docs/en/changelog"
tags: [headless, sdk, self-hosted-runner, remote-control, unattended, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [headless, sdk, cli, cloud]
requires: ""
identifiers:
  - "claude -p"
  - "--resume"
  - "--continue"
  - "CLAUDE_CODE_DISABLE_DEFERRED_TOOL_RESUME"
  - "claude self-hosted-runner"
  - "--repository-folder"
  - "--capacity"
  - "--hook-label"
  - "--metadata"
  - "--environment"
  - "spawn-runner"
  - "--correlation-id"
  - "--use-anthropic-gh"
  - "--trust-workspace"
  - "CLAUDE_RUNNER_SESSION_UUID"
  - "CLAUDE_CODE_REMOTE_SESSION_UUID"
  - "CLAUDE_RUNNER_SPAWN_REASON"
  - "CLAUDE_RUNNER_CHECKOUT_PATH"
  - "CLAUDE_CODE_DISABLE_NESTED_SESSION_ID"
  - "CLAUDE_CODE_RESUME_INTERRUPTED_TURN_MAX_AGE_MS"
  - "--hold-idle-file"
  - "--max-hold-min"
  - "--checkout-hook-timeout-min"
  - "--startup-timeout-min"
  - "--shutdown-drain-sec"
  - "--release-idle-session-min"
  - "--retire-at"
  - "--remove-session-state"
  - "--use-anthropic-git-proxy"
  - "--configure-git"
  - "claude remote-control"
  - "--settings"
  - "--sandbox"
  - "--no-sandbox"
  - "CLAUDE_CODE_RETRY_WATCHDOG"
  - "CLAUDE_CODE_RETRY_WATCHDOG_MAX_USAGE_LIMIT_WAIT_MS"
  - "CLAUDE_CODE_RETRY_WATCHDOG_USAGE_LIMIT_RECHECK_MS"
  - "CLAUDE_CODE_OVERLOADED_RETRY_MAX_DELAY_MS"
  - "--await-initialize"
  - "--output-format"
  - "stream-json"
  - "credential_expires_at"
  - "loginExpiresAt"
  - "claude auth status"
  - "--bare"
  - "AskUserQuestion"
  - "afkTimeoutMs"
  - "CLAUDE_CODE_GZIP_REQUEST_BODIES"
  - "claude ultrareview"
  - "CLAUDE_CODE_DISABLE_ULTRAREVIEW_TRUST_CHECK"
  - "CLAUDE_CODE_RESUME_HINT_COMMAND"
  - "claude purge"
  - "/loop"
  - "CLAUDE_CODE_LOOP_KEEPALIVE"
  - "claude rm"
orchestration: "high"
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
| 2.1.328 | 2026-11-19 | A host can stop claude -p --resume and --continue from running a tool call that a hook deferred. | `CLAUDE_CODE_DISABLE_DEFERRED_TOOL_RESUME`, `--resume`, `--continue` |
| 2.1.328 | 2026-11-19 | Warning when a message from a session that skips permission prompts may be held and dropped by a cloud session; claude -p text output says on stderr when a message from another session is held or dropped. | |
| 2.1.328 | 2026-11-19 | claude -p and SDK sessions fetch managed-settings plugins with their own git repository in the background for a later session; a short run may exit up to 30 seconds later. | |
| 2.1.328 | 2026-11-19 | Self-hosted runner: --repository-folder names the session folder for a repository at --capacity 1; sessions refused earlier when the repository path is a symlink. | `--repository-folder`, `--capacity` |
| 2.1.328 | 2026-11-19 | Self-hosted runner: --hook-label on the orchestrator and --metadata key=value on claude --environment label sessions for the spawn-runner hook. | `--hook-label`, `--metadata`, `--environment`, `spawn-runner` |
| 2.1.328 | 2026-11-19 | Self-hosted runner: new orchestrator /metrics claude_code_self_hosted_orchestrator_session_queue_wait_by_reason_seconds and claude_code_self_hosted_orchestrator_sessions_given_up_total. | `claude_code_self_hosted_orchestrator_session_queue_wait_by_reason_seconds`, `claude_code_self_hosted_orchestrator_sessions_given_up_total` |
| 2.1.328 | 2026-11-19 | Self-hosted runner: built-in gh api is off by default where settings guard GitHub tools by name; --use-anthropic-gh true turns it on. | `--use-anthropic-gh` |
| 2.1.328 | 2026-11-19 | Self-hosted runner: CLAUDE_RUNNER_SESSION_UUID and CLAUDE_CODE_REMOTE_SESSION_UUID are both set for the session and its checkout, post-session and spawn-runner hooks. | `CLAUDE_RUNNER_SESSION_UUID`, `CLAUDE_CODE_REMOTE_SESSION_UUID` |
| 2.1.328 | 2026-11-19 | Self-hosted runner: resumed sessions check whether earlier work is still there and say what is missing; warning when host settings.json sets a default permission mode sessions ignore. | |
| 2.1.328 | 2026-11-19 | Non-interactive sessions in Desktop and Agent SDK on third-party providers or with telemetry or feature flags off end the turn when closed with a question open. | |
| 2.1.328 | 2026-11-19 | Improved time to resume large sessions and memory in long SDK sessions. | |
| 2.1.327 | 2026-11-17 | -p mode runs fewer git commands before the first request. | `-p` |
| 2.1.326 | 2026-11-16 | --await-initialize is refused with --bg or --worktree --tmux. | `--await-initialize` |
| 2.1.326 | 2026-11-16 | Self-hosted runners under --trust-workspace false ignore more repository settings; set such values in user or managed settings. | `--trust-workspace` |
| 2.1.326 | 2026-11-16 | Remote Control connects through a proxy with a CONNECT tunnel; --verbose session debug logs go to ~/.claude/child-logs/. | `claude remote-control`, `--verbose` |
| 2.1.326 | 2026-11-16 | Self-hosted runner: Linux and macOS sessions with no gh get a built-in gh api by default; --use-anthropic-gh false turns it off. | `--use-anthropic-gh` |
| 2.1.326 | 2026-11-16 | --bare sessions on an unapproved API key: moving to the background is refused in most setups and claude --bare --bg exits with an error if the background service lacks the key. | `--bare`, `--bg` |
| 2.1.326 | 2026-11-16 | "Continue automatically at usage limit" stops with a notice when the login changes or ends during the wait. | |
| 2.1.325 | 2026-11-13 | claude remote-control exits with status 4 when it stops by itself (single-session runs still exit 0) and 69 when it cannot register, so a service manager can restart it. | `claude remote-control` |
| 2.1.325 | 2026-11-13 | claude -p with no cached account data waits for it before its first request, so a first run in a clean environment can start a few seconds later. | |
| 2.1.325 | 2026-11-13 | -p and SDK runs in a worktree or submodule mounted into a container apply .claude/settings.local.json allow rules only once the folder is trusted. | |
| 2.1.325 | 2026-11-13 | Scheduled tasks and /loop ask before running a skill that declares allowed-tools or hooks; add Skill(name) to permissions.allow to run it unattended. | `/loop`, `permissions.allow` |
| 2.1.325 | 2026-11-13 | Web, cloud scheduled tasks and Cowork cloud sessions start despite sandbox.failIfUnavailable because the hosted container has no command sandbox. | `sandbox.failIfUnavailable` |
| 2.1.325 | 2026-11-13 | Self-hosted runners refuse a session whose session folder or repository path is a symbolic link. | |
| 2.1.323 | 2026-11-12 | Progress heartbeat every 30 seconds while hooks run long in claude -p and SDK sessions, so a host does not end the turn as hung. | |
| 2.1.323 | 2026-11-12 | Added CLAUDE_CODE_RESUME_HINT_COMMAND so a launching program can name its own resume command in the exit hint. | `CLAUDE_CODE_RESUME_HINT_COMMAND` |
| 2.1.323 | 2026-11-12 | Self-hosted runner: exit code of an on-demand runner whose work order was superseded reverted to 1 (2.1.321 and 2.1.322 had made it 0). | |
| 2.1.323 | 2026-11-12 | claude rm and the agents view say a session is removed from the list, not deleted. | `claude rm` |
| 2.1.323 | 2026-11-12 | Memory use improved for non-interactive sessions during compaction with very large transcript files (2.1.310). | |
| 2.1.321 | 2026-11-09 | Added --settings <file> to claude remote-control, applied to every session it starts; changes need a restart. | `--settings`, `claude remote-control` |
| 2.1.321 | 2026-11-09 | AskUserQuestion in claude -p and SDK sessions denies a host's permission answer that sets the undocumented afkTimeoutMs field. | `AskUserQuestion`, `afkTimeoutMs` |
| 2.1.321 | 2026-11-09 | Self-hosted runner: an on-demand runner the server refuses as not needed exits 0 instead of 1. | |
| 2.1.321 | 2026-11-09 | Remote Control sessions keep the folder they started in; a client can no longer move them. | |
| 2.1.319 | 2026-11-06 | Self-paced /loop ends when a turn finishes without rescheduling; CLAUDE_CODE_LOOP_KEEPALIVE=1 keeps the old fallback wakeup. | `/loop`, `CLAUDE_CODE_LOOP_KEEPALIVE` |
| 2.1.319 | 2026-11-06 | /loop confirmations in cloud sessions note that a timer stops with its container. | `/loop` |
| 2.1.319 | 2026-11-06 | Self-hosted runner: CLAUDE_RUNNER_CHECKOUT_PATH gives each repository in a session its own folder (-2, -3 suffixes); end-of-session debug log upload removed unless --remove-session-state keeps nothing. | `CLAUDE_RUNNER_CHECKOUT_PATH`, `--remove-session-state` |
| 2.1.319 | 2026-11-06 | claude purge and old-session clean-up retry a folder that could not be fully deleted. | `claude purge` |
| 2.1.318 | 2026-11-04 | claude auth status gains loginExpiresAt and claude -p JSON results gain credential_expires_at; claude -p text output warns on stderr from 10 days before a stored claude.ai sign-in ends. | `loginExpiresAt`, `credential_expires_at`, `claude auth status` |
| 2.1.318 | 2026-11-04 | Unattended runs (claude -p, SDK) stop rewriting ~/.claude.json on every run when nothing changed. | |
| 2.1.318 | 2026-11-04 | Self-hosted runner: CLAUDE_RUNNER_SPAWN_REASON added to the spawn-runner hook environment (for example runner_lost, resumed); orchestrator log lines ok/nack now include reason=. | `CLAUDE_RUNNER_SPAWN_REASON` |
| 2.1.317 | 2026-11-03 | CLAUDE_CODE_DISABLE_NESTED_SESSION_ID=1 on a self-hosted runner makes claude -p inside a session use that session's ID and transcript. | `CLAUDE_CODE_DISABLE_NESTED_SESSION_ID` |
| 2.1.317 | 2026-11-03 | Self-hosted runner: after a 5xx other than 501 or 529, polls and sessions open new connections; a session moved to a new runner now sees the interrupted tool call when older than the max age. | `CLAUDE_CODE_RESUME_INTERRUPTED_TURN_MAX_AGE_MS` |
| 2.1.311 | 2026-10-26 | Added --hold-idle-file and --max-hold-min to self-hosted-runner to keep an idle session while the host reports leftover processes. | `--hold-idle-file`, `--max-hold-min` |
| 2.1.311 | 2026-10-26 | --output-format json and stream-json write DEL, C1 control and Unicode format characters in strings as \uXXXX escapes. | `--output-format`, `stream-json` |
| 2.1.309 | 2026-10-22 | claude ultrareview requires workspace trust: it asks on a terminal, else refuses; scripts pass --trust-workspace or set CLAUDE_CODE_DISABLE_ULTRAREVIEW_TRUST_CHECK=1. | `claude ultrareview`, `--trust-workspace`, `CLAUDE_CODE_DISABLE_ULTRAREVIEW_TRUST_CHECK` |
| 2.1.309 | 2026-10-22 | The dangerous rm and rmdir prompt in bypass mode in Desktop and VS Code denies the command at once with a rewrite hint so unattended sessions keep going. | |
| 2.1.307 | 2026-10-21 | Self-hosted runner: checkout hooks are stopped after 30 minutes by default; raise --checkout-hook-timeout-min or set 0. | `--checkout-hook-timeout-min` |
| 2.1.307 | 2026-10-21 | Unparseable tool calls are retried up to twice before the turn ends with an error. | |
| 2.1.305 | 2026-10-20 | Added CLAUDE_CODE_RETRY_WATCHDOG_USAGE_LIMIT_RECHECK_MS so unattended retry mode notices a usage limit lifted before its reset. | `CLAUDE_CODE_RETRY_WATCHDOG`, `CLAUDE_CODE_RETRY_WATCHDOG_USAGE_LIMIT_RECHECK_MS` |
| 2.1.302 | 2026-10-16 | claude -p and Agent SDK sessions with no permission mode start in default mode on third-party providers, telemetry off or fresh install; --permission-mode auto keeps auto. | `--permission-mode` |
| 2.1.301 | 2026-10-15 | Added CLAUDE_CODE_RETRY_WATCHDOG_MAX_USAGE_LIMIT_WAIT_MS so unattended retry mode ends a request at a usage limit that resets too far away. | `CLAUDE_CODE_RETRY_WATCHDOG_MAX_USAGE_LIMIT_WAIT_MS` |
| 2.1.300 | 2026-10-14 | Removed --sandbox and --no-sandbox from claude remote-control (passing either exits with an error); set sandbox.enabled in settings. | `--sandbox`, `--no-sandbox`, `sandbox.enabled` |
| 2.1.300 | 2026-10-14 | Large requests to api.anthropic.com use gzip even with telemetry off; CLAUDE_CODE_GZIP_REQUEST_BODIES=0 turns it off. | `CLAUDE_CODE_GZIP_REQUEST_BODIES` |
| 2.1.300 | 2026-10-14 | Local session transcripts also record each API request's system prompt, tools and parameters. | |
| 2.1.299 | 2026-10-14 | Added --shutdown-drain-sec to the orchestrator: on SIGTERM it stops polling and gives in-flight work that many seconds. | `--shutdown-drain-sec` |
| 2.1.299 | 2026-10-14 | /btw side questions in non-interactive sessions return a timeout error after 11 minutes; the exit resume command names the session by ID, not name. | `/btw` |
| 2.1.296 | 2026-10-09 | Added CLAUDE_CODE_OVERLOADED_RETRY_MAX_DELAY_MS to set the maximum backoff for overloaded (529) retries (maximum later raised from 64000 to 300000 in 2.1.323). | `CLAUDE_CODE_OVERLOADED_RETRY_MAX_DELAY_MS` |

# Not found in the documentation pages

- `CLAUDE_CODE_DISABLE_DEFERRED_TOOL_RESUME`
- `--repository-folder`
- `--hook-label`
- `--metadata`
- `--correlation-id`
- `--use-anthropic-gh`
- `CLAUDE_CODE_DISABLE_NESTED_SESSION_ID`
- `--checkout-hook-timeout-min`
- `--await-initialize`
- `credential_expires_at`
- `loginExpiresAt`
- `CLAUDE_CODE_LOOP_KEEPALIVE`
