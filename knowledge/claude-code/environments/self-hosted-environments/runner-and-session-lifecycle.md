---
type: "Concept"
title: "Runner ownership, lease and shutdown lifecycle"
description: "How a runner locks to one owner, claims sessions under a lease, polls, drains and retires."
resource: "https://code.claude.com/docs/en/self-hosted-environments"
tags: [runner, lifecycle, lease, capacity, retire]
kind: "behavior"
maturity: "beta"
since: "2.1.280"
surfaces: [cloud]
requires: "Self-hosted environments (Team or Enterprise)"
identifiers:
  - "--capacity"
  - "--drain-grace-sec"
  - "--retire-at"
  - "--defer-shutdown-max-min"
  - "--release-idle-session-min"
  - "SELF_HOSTED_RUNNER_POST_TURN_SETTLE_MS"
  - "SELF_HOSTED_RUNNER_BG_RESULT_GRACE_MS"
  - "pool_id"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments"
    resource: "https://code.claude.com/docs/en/self-hosted-environments"
    title: "Self-hosted environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Mechanics of how runners claim and run sessions in a self-hosted environment.

# How to use it

- Key terms: environment, environment secret (single shared credential, shown once at creation, labeled environment key in the admin UI), runner (registers, receives a runner token, polls), session (child Claude Code process spawned by the runner). In API fields and metrics the environment is `pool` and its ID is `pool_id`.
- Owner locking: the first session a runner picks up locks it to that session's owner; it then serves only that owner, up to `--capacity` concurrent sessions. The owner is the user account, or for Claude Tag channel sessions the Claude Tag agent. Minimum fleet size is the number of owners expected active at once.
- Session lifecycle: runner with free capacity claims and holds a lease; clones the repository; spawns the child; child streams events over HTTPS while the runner polls (each poll refreshes the lease and is the heartbeat).
- Exit behaviour after sessions finish depends on `--drain-grace-sec`: default `0` exits as soon as active sessions finish (so Kubernetes can restart it with a fresh disk); a positive value keeps polling the locked owner's queue that many seconds.
- `--retire-at <epoch-seconds>`: for hosts destroyed without a signal or with a short grace (sandbox lifetime cap, spot reclaim), set a few minutes before destruction. At that time the runner stops taking work, releases each session via the same path as `--release-idle-session-min`, and exits 0. A signal-less kill without it looks like a crash and the session requeues. `SIGTERM` needs no flag; `--defer-shutdown-max-min` keeps serving held sessions.

# Limits and defaults

- Lease lapses about 60 seconds after polling stops; requeue then takes a few minutes or more.
- Each poll request gets 10 seconds; on timeout or unparseable response the runner keeps serving live sessions and retries after a second or two, doubling the gap per repeated failure up to 20 seconds.
- At retire, a mid-turn session is released after the turn ends, waiting for the child to report turn end up to `SELF_HOSTED_RUNNER_POST_TURN_SETTLE_MS` (before v2.1.280 released immediately). Background tasks are waited on up to 60 seconds, then released; a pending follow-up turn is awaited up to `SELF_HOSTED_RUNNER_BG_RESULT_GRACE_MS`.
- A turn that outlives the kill is still lost.

# Notes

Runner-to-owner locking isolates checked-out code between owners without wiping disk between them.
