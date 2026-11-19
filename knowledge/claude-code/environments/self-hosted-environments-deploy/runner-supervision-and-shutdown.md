---
type: "Guide"
title: "Kubernetes, Compose, shutdown timing and runner exits"
description: "Deployment recipes, health probes, how SIGTERM drains a runner, defer-shutdown, stop-timeout sizing, and restart-with-backoff rules."
resource: "https://code.claude.com/docs/en/self-hosted-environments-deploy"
tags: [self-hosted, kubernetes, shutdown, drain, supervisor]
kind: "mixed"
maturity: "beta"
since: ""
surfaces: [cloud]
requires: ""
identifiers:
  - "--health-port"
  - "/healthz"
  - "terminationGracePeriodSeconds"
  - "stop_grace_period"
  - "--drain-wait-sec"
  - "--session-stop-grace-sec"
  - "--post-session-hook-timeout-sec"
  - "--defer-shutdown-max-min"
  - "--retire-at"
  - "--base-dir"
  - "--capacity"
  - "--remove-session-state"
  - "--startup-timeout-min"
  - "CLAUDE_RUNNER_FETCH_DEPTH"
  - "claude self-hosted-runner doctor"
  - "--log-file"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-deploy"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-deploy"
    title: "Deploy self-hosted environments to production"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

How to run a runner fleet under Kubernetes or Docker Compose and shut it down without losing work.

# How to use it

- Kubernetes Deployment args: `self-hosted-runner --environment-secret-file /etc/claude/environment-secret --capacity 4 --base-dir /workspace`, secret mounted read-only, liveness/readiness on `GET /healthz` port 8080 (`--health-port`), `terminationGracePeriodSeconds: 90`, label `app.kubernetes.io/part-of: claude-code-self-hosted-runner`. `/healthz` returns 200 whenever the process is alive; alert on `last_poll_age_seconds` to catch a stuck runner. Nothing answers until the runner registers, so raise `initialDelaySeconds` or add a `startupProbe` if probes fail during startup.
- Compose: `restart: always`, `stop_grace_period: 90s`; restarts reuse the container's writable layer, so use for evaluation only.
- Drain on SIGTERM: stop taking sessions, wait up to `--drain-wait-sec` (default 0), terminate session process trees (`--session-stop-grace-sec`, default 5), run `post-session` hook (`--post-session-hook-timeout-sec`, default 60). Runner logs `This runner needs up to 80s` at defaults (0+5+60+15 headroom, +30 with `--push-outcome-on-release`). Set the supervisor stop timeout at least that; with `--drain-wait-sec 120` use about 200.
- `--defer-shutdown-max-min <n>` (v2.1.238+): first signal keeps serving sessions up to n minutes, then releases all, then drains after a post-release grace (75 s default, or `--drain-wait-sec` + 15 if above 60 s). Stop timeout >= n minutes + 155 s at defaults. A second signal drains immediately; a signal during drain force-exits.
- Owners can post a status message on the environment (Cloud environments page) before a restart.
- Same `--base-dir` and `--capacity` on every runner in an environment: `--capacity 1` checks out directly under base dir, higher uses per-session worktrees; mismatches break paths of resumed sessions.
- Pre-warmed checkout: canonical clone at `<base-dir>/<repo-owner>/<repo>` with `origin` remote; runner fetches (never `--depth` into existing clone), resets hard at capacity 1 (never `git clean`). Per-session dirs under `<base-dir>/_sessions/` persist unless `--remove-session-state`. Confirm with `--log-level debug` (`Prefetched repo found at`). Git ops have a 120 s no-progress watchdog and 30 min hard cap. `CLAUDE_RUNNER_FETCH_DEPTH` default 50.
- Restart rules: do not restart on-demand runners (single-use work order). Failed starts print `[runner:fatal]` or `error:`; Kubernetes and Docker back off automatically; systemd does not (5 starts in 10 s trips its limit); for your own supervisor start at 5 s, double after runs under a minute, cap at 5 min. `claude self-hosted-runner doctor` starts an interactive diagnosis session (needs `claude auth login` for full access; reads logs only if `--log-file` set).

# Limits and defaults

If the stop timeout expires during drain, no `post-session` hook runs, the runner does not deregister, and requeue can take minutes.
