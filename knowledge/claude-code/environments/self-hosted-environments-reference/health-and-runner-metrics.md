---
type: "Reference"
title: "Health endpoint and runner Prometheus metrics"
description: "GET /healthz body, runner /metrics series, session lifecycle counter semantics, and how to join session cost to idle time."
resource: "https://code.claude.com/docs/en/self-hosted-environments-reference"
tags: [self-hosted, prometheus, metrics, health, observability]
kind: "api"
maturity: "beta"
since: ""
surfaces: [cloud]
requires: ""
identifiers:
  - "/healthz"
  - "/metrics"
  - "claude_code_self_hosted_runner_info"
  - "claude_code_self_hosted_runner_capacity"
  - "claude_code_self_hosted_runner_active_sessions"
  - "claude_code_self_hosted_runner_locked_account"
  - "claude_code_self_hosted_runner_last_poll_age_seconds"
  - "claude_code_self_hosted_runner_poll_errors_total"
  - "claude_code_self_hosted_runner_sessions_started_total"
  - "claude_code_self_hosted_runner_sessions_completed_total"
  - "claude_code_self_hosted_runner_sessions_failed_total"
  - "claude_code_self_hosted_runner_sessions_interrupted_total"
  - "claude_code_self_hosted_runner_initializing_sessions"
  - "claude_code_self_hosted_runner_session_init_duration_seconds"
  - "claude_code_self_hosted_runner_session_init_errors_total"
  - "claude_code_self_hosted_runner_session_start_hook_errors_total"
  - "claude_code_self_hosted_runner_session_idle_seconds"
  - "OTEL_METRICS_EXPORTER"
  - "CLAUDE_CODE_ENABLE_TELEMETRY"
  - "OTEL_METRICS_INCLUDE_SESSION_ID"
  - "claude_code_cost_usage_total"
  - "CLAUDE_RUNNER_EXIT_REASON"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-reference"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-reference"
    title: "Self-hosted environments reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each runner serves `GET /healthz` and `GET /metrics` on `--health-port` (default 8080).

# How to use it

`/healthz` returns 200 whenever the process is alive once registered and startup checks are done, so it detects only a dead process. JSON body: `status`, `runner_id` (`ccrunner_...`), `active_sessions`, `last_poll_at`, `last_poll_age_ms` (both `null` until first successful poll). Alert on `last_poll_age_ms`; keep liveness probes on the status code.

| Series | Notes |
| :- | :- |
| `claude_code_self_hosted_runner_info{runner_id,version,client_label}` | Always 1; inventory and version drift |
| `..._capacity`, `..._active_sessions` | Configured capacity; sessions running |
| `..._locked_account{email}` | Present once locked and a token with `act.email` was issued; absent for Claude Tag agent; consider dropping the email label at scrape |
| `..._last_poll_age_seconds` | Since last success; alert over 60 |
| `..._poll_errors_total{error_kind}` | `transport`, `timeout`, `5xx`, `429`, `4xx`; alert on rate over 5m above 0 |
| `..._sessions_started_total{client_platform}` | Spawned children; origins such as `web_claude_ai`, `ios`, `android`, `desktop_app`, `claude_code_cli`, `unknown`; Slack is `claude_in_slack` or `claude-in-slack` |
| `..._sessions_completed_total`, `_failed_total`, `_interrupted_total` | Terminal counters (one increments at exit) |
| `..._initializing_sessions`, `..._session_init_duration_seconds` | Init phase gauge and histogram |
| `..._session_init_errors_total` | Failures before init (checkout hook, git prep, token, pre-init crash) |
| `..._session_start_hook_errors_total` | `SessionStart` hooks reporting error |
| `..._session_idle_seconds{session_id,client_platform}` | Seconds idle (0 when busy); useful for sessions stuck on an unanswered permission prompt |

Pass-through of session-child metrics: with `OTEL_METRICS_EXPORTER=prometheus` on the host and `CLAUDE_CODE_ENABLE_TELEMETRY=1` in sessions, counters and gauges (not histograms) are re-exposed on the runner `/metrics` tagged `session_id` and `client_platform` at `--capacity` above 1; at capacity 1 the child binds port 9464 itself. Join cost to idle time on `ccr_session_id` (child metrics carry it unless `OTEL_METRICS_INCLUDE_SESSION_ID=false`); the runner metric needs `label_replace(... "ccr_session_id", "cse_$1", "session_id", "session_(.*)")` against `claude_code_cost_usage_total`.

# Limits and defaults

- Counter semantics: `completed` covers clean exit 0, archive/delete, clean release (idle, retire, kill-limit, startup timeout, server deassign); `failed` is non-zero child exit; `interrupted` is runner termination for drain or after the kill-limit grace window. Started minus the other three equals children running. The post-session hook's `CLAUDE_RUNNER_EXIT_REASON` reports clean handoffs as `interrupted`, so reconcile with counters carefully.
- On one-shot environments (`--capacity 1`, `--drain-grace-sec 0`) a runner exits right after its session so terminal counters are rarely scraped. For throughput use `claude_code_self_hosted_orchestrator_spawn_hooks_total{result="ok"}`; utilization `sum(active_sessions)` over `sum(capacity)`; backlog `pool_pending_sessions` and `queue_circuit_broken_sessions`; per-session outcomes via the `post-session` hook.
