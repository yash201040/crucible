---
type: "Reference"
title: "Orchestrator metrics, autoscaling and alert rules"
description: "Orchestrator /healthz and /metrics series, autoscaling guidance for HPA and KEDA, PodMonitor, and sample Prometheus alert rules."
resource: "https://code.claude.com/docs/en/self-hosted-environments-reference"
tags: [self-hosted, orchestrator, prometheus, autoscaling, alerts]
kind: "api"
maturity: "beta"
since: ""
surfaces: [cloud]
requires: ""
identifiers:
  - "claude_code_self_hosted_orchestrator_info"
  - "claude_code_self_hosted_orchestrator_connected"
  - "claude_code_self_hosted_orchestrator_last_poll_age_seconds"
  - "claude_code_self_hosted_orchestrator_poll_errors_total"
  - "claude_code_self_hosted_orchestrator_queue_pending_sessions"
  - "claude_code_self_hosted_orchestrator_queue_backing_off_sessions"
  - "claude_code_self_hosted_orchestrator_queue_circuit_broken_sessions"
  - "claude_code_self_hosted_orchestrator_sessions_given_up_total"
  - "claude_code_self_hosted_orchestrator_pool_pending_sessions"
  - "claude_code_self_hosted_orchestrator_pool_active_sessions"
  - "claude_code_self_hosted_orchestrator_spawn_hooks_total"
  - "claude_code_self_hosted_orchestrator_spawn_hook_duration_seconds"
  - "claude_code_self_hosted_orchestrator_warm_hints_dispatched_total"
  - "claude_code_self_hosted_orchestrator_session_queue_wait_seconds"
  - "claude_code_self_hosted_orchestrator_clock_skew_seconds"
  - "claude_code_self_hosted_orchestrator_scm_connector_connected"
  - "claude_code_self_hosted_orchestrator_scm_connector_requests_forwarded_total"
  - "ClaudeRunnerPollStale"
  - "ClaudeRunnerVersionDrift"
  - "ClaudeRunnerInitErrorsHigh"
  - "ClaudeRunnerPollErrors"
  - "ClaudeRunnerSessionStartHookErrors"
  - "ClaudeOrchestratorDisconnected"
  - "ClaudeOrchestratorPollStale"
  - "ClaudeOrchestratorCircuitBroken"
  - "ClaudeOrchestratorPollErrors"
  - "ClaudeOrchestratorSpawnHookFailing"
  - "ClaudeRunnersBelowFloor"
  - "ClaudeOrchestratorSessionsWaiting"
  - "ClaudeOrchestratorQueueWaitHigh"
  - "ClaudeOrchestratorAbsent"
  - "ignoreNullValues"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-reference"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-reference"
    title: "Self-hosted environments reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The orchestrator serves its own `/healthz` and `/metrics` on its health port. Its `/healthz` always returns 200; the body has `connected` (most recent poll succeeded), `queue_counts`, `last_error` (reset on success), and, with the SCM connector, `scm_connector_connected` and a `scm_connector` object.

# How to use it

| Series (prefix `claude_code_self_hosted_orchestrator_`) | Notes |
| :- | :- |
| `info{version,pool_id,orchestrator_uuid,hostname}` | Always 1 |
| `connected` | 1 if last poll succeeded |
| `last_poll_age_seconds` | Since last attempt (not last success); alert above 90 at defaults |
| `poll_errors_total{error_kind}` | Same five kinds as runner |
| `queue_pending_sessions`, `queue_backing_off_sessions` | Claimable now; in retry backoff |
| `queue_circuit_broken_sessions` | Blocked until a user messages or an Owner retries from Activity; alert above 0 |
| `sessions_given_up_total{cause}` | `lease_expiry`, `retries_exhausted`, `hook_declined`; v2.1.328+; use SUM |
| `pool_pending_sessions`, `pool_active_sessions` | Environment-wide, identical per instance; use MAX |
| `spawn_hooks_total{result}` | `ok`, `retryable`, `non_retryable` |
| `spawn_hook_duration_seconds`, `session_queue_wait_seconds` | Histograms (queue wait excludes pre-warming) |
| `warm_hints_dispatched_total`, `clock_skew_seconds` | Standby dispatches; local minus server skew |
| `scm_connector_connected`, `scm_connector_requests_forwarded_total` | Absent without `--scm-connector-host` |

Autoscaling: queue-depth scaling uses `pool_pending_sessions` (not `queue_pending_sessions`); capacity scaling uses runner `active_sessions` over `capacity`; gate on `connected == 1`. During a full poll outage HPA holds replicas, but KEDA's Prometheus scaler with default `ignoreNullValues: "true"` reads empty as zero and scales in; set `ignoreNullValues: "false"` with an optional `fallback` floor.

PodMonitor example selects label `app.kubernetes.io/part-of: claude-code-self-hosted-runner` and the named port `health`, path `/metrics`, interval 30s.

# Notes

Sample alert rules given: ClaudeRunnerPollStale (last poll over 60 s for 2m), ClaudeRunnerVersionDrift (mixed versions 30m), ClaudeRunnerInitErrorsHigh (over 3 init errors in 10m), ClaudeRunnerPollErrors, ClaudeRunnerSessionStartHookErrors, ClaudeOrchestratorDisconnected, ClaudeOrchestratorPollStale, ClaudeOrchestratorCircuitBroken, ClaudeOrchestratorPollErrors, ClaudeOrchestratorSpawnHookFailing (over 3 non-ok in 5m). Extra rules: fixed fleet `ClaudeRunnersBelowFloor` (fewer than floor, about half of replicas, for 10m; not for on-demand fleets); on-demand `ClaudeOrchestratorSessionsWaiting` (above 0 for 10m), `ClaudeOrchestratorQueueWaitHigh` (p99 queue wait over 160 s for 5m), `ClaudeOrchestratorAbsent` (no orchestrator scraped for 5m). Orchestrator-side alerts all go quiet within about 10 minutes of the orchestrator dying, so keep Absent and Disconnected loaded.
