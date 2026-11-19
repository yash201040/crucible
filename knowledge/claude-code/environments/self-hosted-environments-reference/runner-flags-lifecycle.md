---
type: "Reference"
title: "Runner CLI flags: capacity, lifecycle and drain"
description: "Runner flags for base dir, capacity, idle release, kill limits, drain, retire, hold and health, with env var pairs and defaults."
resource: "https://code.claude.com/docs/en/self-hosted-environments-reference"
tags: [self-hosted, runner, cli-flags, lifecycle, drain]
kind: "cli_flag"
maturity: "beta"
since: ""
surfaces: [cloud, cli]
requires: "Linux or macOS host"
identifiers:
  - "--api-url"
  - "--base-dir"
  - "SELF_HOSTED_RUNNER_BASE_DIR"
  - "--capacity"
  - "--client-label"
  - "SELF_HOSTED_RUNNER_CLIENT_LABEL"
  - "--defer-shutdown-max-min"
  - "SELF_HOSTED_RUNNER_DEFER_SHUTDOWN_MAX_MS"
  - "--drain-grace-sec"
  - "SELF_HOSTED_RUNNER_DRAIN_GRACE_MS"
  - "--drain-marker-file"
  - "SELF_HOSTED_RUNNER_DRAIN_MARKER_FILE"
  - "--drain-wait-sec"
  - "SELF_HOSTED_RUNNER_DRAIN_WAIT_MS"
  - "--exit-if-unused-min"
  - "SELF_HOSTED_RUNNER_IDLE_SHUTDOWN_MS"
  - "--health-port"
  - "SELF_HOSTED_RUNNER_HEALTH_PORT"
  - "--hold-idle-file"
  - "SELF_HOSTED_RUNNER_HOLD_IDLE_FILE"
  - "--kill-session-after-min"
  - "SELF_HOSTED_RUNNER_MAX_LIFETIME_MS"
  - "--max-hold-min"
  - "SELF_HOSTED_RUNNER_MAX_HOLD_MS"
  - "--post-session-hook-timeout-sec"
  - "SELF_HOSTED_RUNNER_POST_SESSION_HOOK_TIMEOUT_MS"
  - "--release-idle-session-min"
  - "SELF_HOSTED_RUNNER_SESSION_IDLE_MS"
  - "--retire-at"
  - "SELF_HOSTED_RUNNER_RETIRE_AT"
  - "--session-stop-grace-sec"
  - "SELF_HOSTED_RUNNER_SESSION_STOP_GRACE_MS"
  - "--startup-timeout-min"
  - "SELF_HOSTED_RUNNER_STARTUP_TIMEOUT_MS"
  - "--log-level"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-reference"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-reference"
    title: "Self-hosted environments reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Flags of `claude self-hosted-runner` (run `--help` for the authoritative list on your version). Most flags have an env var; the flag wins when both are set. Duration flags take minutes or seconds on the CLI but the env var is always milliseconds (`--exit-if-unused-min 10` equals `SELF_HOSTED_RUNNER_IDLE_SHUTDOWN_MS=600000`).

# How to use it

| Flag | Env var | Default | What it does |
| :- | :- | :- | :- |
| `--api-url <url>` | none | `https://api.anthropic.com` | API base; testing only |
| `--base-dir <path>` | `SELF_HOSTED_RUNNER_BASE_DIR` | `/workspace` (none on Windows) | Checkouts and per-session dirs; created at startup, exit `cannot create or write to base directory` on failure (before v2.1.225 failed at first session). Same value on all runners in an environment |
| `--capacity <n>` | none | `1` | Max concurrent sessions, all for one locked owner |
| `--client-label <label>` | `SELF_HOSTED_RUNNER_CLIENT_LABEL` | hostname | Registration label, `client_label` metric label; v2.1.248+ |
| `--defer-shutdown-max-min <n>` | `SELF_HOSTED_RUNNER_DEFER_SHUTDOWN_MAX_MS` | `0` (off) | Keep serving after first SIGTERM/SIGINT for n minutes; v2.1.238+ |
| `--drain-grace-sec <n>` | `SELF_HOSTED_RUNNER_DRAIN_GRACE_MS` | `0` | After sessions finish, exit immediately (0) or keep re-polling the owner's queue n seconds (weakens per-session isolation) |
| `--drain-marker-file <path>` | `SELF_HOSTED_RUNNER_DRAIN_MARKER_FILE` | unset | Host-written marker so exit is reported as a host drain; v2.1.271+ |
| `--drain-wait-sec <n>` | `SELF_HOSTED_RUNNER_DRAIN_WAIT_MS` | `0` | Wait up to n s for in-flight turns/background tasks at drain |
| `--exit-if-unused-min <n>` | `SELF_HOSTED_RUNNER_IDLE_SHUTDOWN_MS` | `0` (off) | Exit after n minutes with no work ever assigned |
| `--health-port <port>` | `SELF_HOSTED_RUNNER_HEALTH_PORT` | `8080` | `/healthz` and `/metrics`; `0` disables |
| `--hold-idle-file <path>` | `SELF_HOSTED_RUNNER_HOLD_IDLE_FILE` | unset | Host-touched file holds an idle session; v2.1.311+ |
| `--kill-session-after-min <n>` | `SELF_HOSTED_RUNNER_MAX_LIFETIME_MS` | `0` (off) | Wall-clock limit; v2.1.260+ releases then terminates after grace |
| `--max-hold-min <n>` | `SELF_HOSTED_RUNNER_MAX_HOLD_MS` | `1440` | Cap on a hold; at or below release-idle holds nothing; `0` off; v2.1.311+ |
| `--post-session-hook-timeout-sec <n>` | `SELF_HOSTED_RUNNER_POST_SESSION_HOOK_TIMEOUT_MS` | `60` | Budget for the post-session hook |
| `--release-idle-session-min <n>` | `SELF_HOSTED_RUNNER_SESSION_IDLE_MS` | `0` (off) | Release slot after n idle minutes |
| `--retire-at <epoch-seconds>` | `SELF_HOSTED_RUNNER_RETIRE_AT` | unset | Retire at a Unix time; values before 2001 or after year 5138 rejected |
| `--session-stop-grace-sec <n>` | `SELF_HOSTED_RUNNER_SESSION_STOP_GRACE_MS` | `5` | Wait for clean Claude exit before force-kill |
| `--startup-timeout-min <n>` | `SELF_HOSTED_RUNNER_STARTUP_TIMEOUT_MS` | `15` | Release slot if child not initialized; `0` off |
| `--log-level <level>` | none | `info` | `info` or `debug` |

# Limits and defaults

- Caps: `--*-min` flags max 10080 min (7 days); `--drain-grace-sec` max 604800 s; `--drain-wait-sec` max 86400 s; `--session-stop-grace-sec` and `--post-session-hook-timeout-sec` uncapped. Over a cap, a flag fails startup; the env var is clamped.
- Helm warning: `SELF_HOSTED_RUNNER_STARTUP_TIMEOUT_MS: "15"` is 15 ms, not 15 minutes.
- Startup timeout: v2.1.299 through v2.1.308 released a session mid-turn after the timeout without a `user` or `assistant` message; update to v2.1.309+. During a turn that starts before init, the slot is kept until n minutes pass with no line on the child's activity channel; after init `--release-idle-session-min` governs.
- "Pool" is the old name of an environment in metrics and API fields (`pool_id`, `ccpool_...`).
