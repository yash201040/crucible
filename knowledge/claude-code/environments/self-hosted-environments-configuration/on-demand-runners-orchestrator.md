---
type: "Feature"
title: "On-demand runners and the orchestrator"
description: "A stateless orchestrator runs a spawn-runner hook per queued session to boot one single-use runner each, with an exit-code contract."
resource: "https://code.claude.com/docs/en/self-hosted-environments-configuration"
tags: [self-hosted, orchestrator, autoscaling, spawn-runner, kubernetes]
kind: "mixed"
maturity: "beta"
since: "2.1.299"
surfaces: [cloud]
requires: "Self-hosted environments (Team or Enterprise)"
identifiers:
  - "claude self-hosted-runner orchestrator"
  - "spawn-runner"
  - "--hook-timeout"
  - "--expected-spawn-seconds"
  - "--min-idle"
  - "--shutdown-drain-sec"
  - "--release-idle-session-min"
  - "--kill-session-after-min"
  - "--exit-if-unused-min"
  - "--environment-secret-file"
  - "SELF_HOSTED_RUNNER_ENVIRONMENT_SECRET"
  - "CLAUDE_RUNNER_WORK_ORDER_FILE"
  - "CLAUDE_RUNNER_ORDER_ID"
  - "CLAUDE_RUNNER_ATTEMPT"
  - "CLAUDE_RUNNER_ORDER_SERVER_TIME"
  - "CLAUDE_RUNNER_POOL_ID"
  - "CLAUDE_RUNNER_ACCOUNT_ID"
  - "CLAUDE_RUNNER_ACCOUNT_EMAIL"
  - "CLAUDE_RUNNER_PRIMARY_REPO_URL"
  - "CLAUDE_RUNNER_PRIMARY_REPO_REVISION"
  - "CLAUDE_RUNNER_REPO_SOURCES"
  - "CLAUDE_RUNNER_CORRELATION_ID"
  - "CLAUDE_RUNNER_SPAWN_REASON"
  - "/healthz"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-configuration"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-configuration"
    title: "Customize sessions in self-hosted environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Instead of a fixed fleet, run `claude self-hosted-runner orchestrator --environment-secret-file /etc/claude/environment-secret --hooks-dir /etc/claude/hooks`. It polls Anthropic for spawn requests (one per queued session with no runner) and runs `${hooks-dir}/spawn-runner` for each, which submits a workload (Kubernetes Job, EC2 instance, Nomad dispatch). The environment secret stays only on the orchestrator host, which never runs user code; each spawned runner gets a single-use work order. The orchestrator is stateless: two or more replicas may run, each request claimed by exactly one; all must share the same `--expected-spawn-seconds`.

# How to use it

Hook inputs: `CLAUDE_RUNNER_WORK_ORDER_FILE` (signed JWT, deleted after the hook exits, copy it), `CLAUDE_RUNNER_ORDER_ID` (dedup key), `CLAUDE_RUNNER_SESSION_ID`/`_UUID` and `CLAUDE_RUNNER_ATTEMPT` (empty/0 for pre-warming), `CLAUDE_RUNNER_ORDER_SERVER_TIME`, `CLAUDE_RUNNER_POOL_ID` (`ccpool_...`), `CLAUDE_RUNNER_ACCOUNT_ID`, `CLAUDE_RUNNER_ACCOUNT_EMAIL` (PII), `CLAUDE_RUNNER_PRIMARY_REPO_URL`, `CLAUDE_RUNNER_PRIMARY_REPO_REVISION`, `CLAUDE_RUNNER_REPO_SOURCES` (JSON array of `{url, revision}`), `CLAUDE_RUNNER_CORRELATION_ID`, `CLAUDE_RUNNER_CLIENT_PLATFORM`, `CLAUDE_RUNNER_SPAWN_REASON` (v2.1.318+ on orchestrator).

Spawned runner registers with the JWT via `--environment-secret-file` or `SELF_HOSTED_RUNNER_ENVIRONMENT_SECRET`; use `--capacity 1`. Pre-warming (`--min-idle`) work orders register unbound.

Contract: (1) be idempotent on `CLAUDE_RUNNER_ORDER_ID`, never the session ID; (2) do not retry the workload; (3) exit 0 = submitted, exit 1 or timeout = retryable (blocked after 10 in a row), exit 2+ = non-retryable, session blocked until a new user message or an Owner selects Retry in the Activity tab; (4) set `--expected-spawn-seconds` at least your p99 spawn-to-registration time. Hook stdout/stderr go to the orchestrator log with credentials redacted; the last 512 characters of stderr become the spawn error.

Make runners exit: `--release-idle-session-min 30`, `--kill-session-after-min 480`, `--exit-if-unused-min 60` (standby), then remove the workload (for example `ttlSecondsAfterFinished`). A shell hook with `set -e` should use an EXIT trap turning failures into exit 1 and a `permanent` helper for exit 2.

`CLAUDE_RUNNER_SPAWN_REASON` values: `session_created`, `no_runner_registered`, `hook_failed`, `runner_lost`, `runner_reported_failure`, `resumed`, `requeued`, `server_retry`, `prewarm`; keep a default branch because values can be added.

# Limits and defaults

- `--hook-timeout` default 60 seconds; `--expected-spawn-seconds` default 120 seconds.
- Runners the hook starts do not exit by default.
- Before v2.1.305 a background process holding the hook's stdout/stderr made the hook hit the timeout; now the orchestrator logs `exited, but a process it started still has the hook's stdout or stderr open` and keeps up to 64 KB of later output. A hook that waits for its runner is killed at the timeout with its process tree (`timed out after 60000ms, sending SIGTERM to process tree`).
- `--shutdown-drain-sec` (needs v2.1.299+; older exits `error: unknown flag --shutdown-drain-sec`): give running hooks time on SIGTERM. Defaults guidance: `--shutdown-drain-sec 70` with stop timeout 85 seconds (`terminationGracePeriodSeconds: 85` or `TimeoutStopSec=85`); drain at least hook timeout plus 10, stop timeout at least drain plus 15. Without it the orchestrator stops immediately; the session is re-requested after the lease. Under systemd `KillMode=control-group` also signals hooks; `KillMode=mixed` kills in-unit runners without draining.

# Notes

A hook that names workloads by session ID leaves re-opened sessions stuck Queued or Failed (activity-tab errors such as `runner did not register within ETA after max attempts`, `spawn-runner hook timed out after 60000ms`).
