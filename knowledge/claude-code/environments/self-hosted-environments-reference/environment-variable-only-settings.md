---
type: "Reference"
title: "Runner environment-variable-only settings and telemetry"
description: "Env vars with no flag form: background grace, host config dir, fetch depth, git verify skip, plus telemetry controls for session children."
resource: "https://code.claude.com/docs/en/self-hosted-environments-reference"
tags: [self-hosted, env-vars, telemetry, runner, settings]
kind: "env_var"
maturity: "beta"
since: ""
surfaces: [cloud]
requires: ""
identifiers:
  - "SELF_HOSTED_RUNNER_BG_RESULT_GRACE_MS"
  - "SELF_HOSTED_RUNNER_HOST_CONFIG_DIR"
  - "SELF_HOSTED_RUNNER_MAX_LIFETIME_GRACE_MS"
  - "SELF_HOSTED_RUNNER_POST_TURN_SETTLE_MS"
  - "SELF_HOSTED_RUNNER_SIGKILL_GRACE_MS"
  - "CLAUDE_RUNNER_DISABLE_RENEWAL_WARNING"
  - "CLAUDE_RUNNER_FETCH_DEPTH"
  - "CLAUDE_RUNNER_FETCH_SERVER_PROGRESS_CAP_MS"
  - "CLAUDE_RUNNER_SKIP_GIT_VERIFY"
  - "FORCE_AUTOUPDATE_PLUGINS"
  - "CLAUDE_CODE_DISABLE_ARTIFACT"
  - "CLAUDE_CODE_BYOC_ENABLE_DATADOG"
  - "DISABLE_TELEMETRY"
  - "DO_NOT_TRACK"
  - "DISABLE_ERROR_REPORTING"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "CLAUDE_CODE_DISABLE_FEATURE_FLAGS"
  - "CLAUDE_CODE_ENABLE_TELEMETRY"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-reference"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-reference"
    title: "Self-hosted environments reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Settings read only from the runner's environment, plus telemetry behavior. Set telemetry variables on the runner process; it re-asserts them after server-provided variables so the operator's value wins.

# How to use it

| Env var | Default | What it does |
| :- | :- | :- |
| `SELF_HOSTED_RUNNER_BG_RESULT_GRACE_MS` | `30000` | Session counts as busy after a background task finishes until the follow-up turn starts; `0` or unusable falls back to default; v2.1.228+ |
| `SELF_HOSTED_RUNNER_HOST_CONFIG_DIR` | `~/.claude` | Directory snapshotted at startup and seeded into each session's `CLAUDE_CONFIG_DIR`; also moves where `.claude.json` is read for MCP seeding (point at an empty dir to disable) |
| `SELF_HOSTED_RUNNER_MAX_LIFETIME_GRACE_MS` | `900000` | Grace after `--kill-session-after-min` before terminating |
| `SELF_HOSTED_RUNNER_POST_TURN_SETTLE_MS` | `7000` | Cap on busy time after a turn during `--drain-wait-sec`; v2.1.275+ |
| `SELF_HOSTED_RUNNER_SIGKILL_GRACE_MS` | `30000` | Wait for SIGKILL on a child in uninterruptible I/O; floored at post-session timeout + 15 s (+30 s with push-on-release), so 75 s at defaults |
| `CLAUDE_RUNNER_DISABLE_RENEWAL_WARNING` | unset | `1` stops the renewal-refused notice in sessions; v2.1.319+ |
| `CLAUDE_RUNNER_FETCH_DEPTH` | `50` | Fresh-clone fetch depth; positive integer, `full` or `0` for complete |
| `CLAUDE_RUNNER_FETCH_SERVER_PROGRESS_CAP_MS` | `600000` | Per-attempt wait for first data while server progress rises; `0` or `off` cuts off after 2 min; clamped 120000 to 1800000; v2.1.295+ |
| `CLAUDE_RUNNER_SKIP_GIT_VERIFY` | unset | `1` skips `.git` check after a `checkout` hook |
| `FORCE_AUTOUPDATE_PLUGINS` | unset | `1` lets plugin marketplaces auto-update |
| `CLAUDE_CODE_DISABLE_ARTIFACT` | unset | `1` disables the Artifact tool regardless of org setting |

# Limits and defaults

Telemetry: session children send operational telemetry to Anthropic unless disabled; no code or repository content is sent. `CLAUDE_CODE_BYOC_ENABLE_DATADOG=1` opts in to Datadog metrics (off by default). `DISABLE_TELEMETRY`, `DO_NOT_TRACK`, `DISABLE_ERROR_REPORTING`, `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` apply as documented for Claude Code. `CLAUDE_CODE_DISABLE_FEATURE_FLAGS=1` (v2.1.319+) disables feature-flag fetching only. `CLAUDE_CODE_ENABLE_TELEMETRY` is unrelated: it enables OpenTelemetry export to your own collector. Env var overruns of duration caps are clamped.
