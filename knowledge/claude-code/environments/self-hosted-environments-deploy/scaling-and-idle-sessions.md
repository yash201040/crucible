---
type: "Feature"
title: "Scale the fleet and release idle sessions"
description: "Fixed fleet versus on-demand runners, owner-locking, releasing idle sessions, holding idle sessions, and kill-after limits."
resource: "https://code.claude.com/docs/en/self-hosted-environments-deploy"
tags: [self-hosted, scaling, idle-sessions, resume, runner]
kind: "cli_flag"
maturity: "beta"
since: "2.1.311"
surfaces: [cloud]
requires: ""
identifiers:
  - "--release-idle-session-min"
  - "--kill-session-after-min"
  - "--hold-idle-file"
  - "--max-hold-min"
  - "--push-outcome-on-release"
  - "SELF_HOSTED_RUNNER_MAX_LIFETIME_GRACE_MS"
  - "claude_code_self_hosted_runner_session_idle_seconds"
  - "claude self-hosted-runner orchestrator"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-deploy"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-deploy"
    title: "Deploy self-hosted environments to production"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The orchestrator decides how many runners exist. A runner is locked to one owner (user or Claude Tag agent), so the minimum replica count is the number of concurrently active owners; `--capacity` only adds parallelism within one owner.

# How to use it

- Fixed fleet: static replicas, scale on Prometheus metrics. On-demand: `claude self-hosted-runner orchestrator` polls for queued sessions and runs the `spawn-runner` hook.
- Sessions stay queued while runners are online when idle sessions hold slots (a session keeps its slot after its turn). Check `claude_code_self_hosted_runner_session_idle_seconds` per session, then start every runner with `--release-idle-session-min 30` (example). Releasing makes the runner exit if it was its last session; resume happens at the user's next message.
- Hold: `--hold-idle-file <path>` (v2.1.311+) in a directory sessions cannot write; touch the file more often than every 3 minutes from the host; `--max-hold-min` caps the hold (default one day; set above `--release-idle-session-min`, example 240). Log lines `idle release held`, `idle release no longer held`; `leftover-hold=` in the `watchdog config` line. Forced releases (`--retire-at`, `--defer-shutdown-max-min`, `--kill-session-after-min`) end a hold.
- `--kill-session-after-min` (example 480): from v2.1.260 the runner releases the session and terminates only after a grace window (15 min default, `SELF_HOSTED_RUNNER_MAX_LIFETIME_GRACE_MS`). Before v2.1.260 it terminated outright.

# Limits and defaults

- Not counted as idle: turn ended with a background task running; turn waiting on an approval from a non-MCP tool while it runs; turn waiting on an MCP `elicitation/create`. Pair with `--kill-session-after-min`.
- Resumed sessions lose unpushed work (fresh clone). `--push-outcome-on-release` pushes outcome branches best-effort using host git credentials; restrict who can push `claude/*` refs, since the runner fetches the previously pushed branch on resume without verifying the pusher. Uncommitted changes and `checkout`-hook repositories are still lost; snapshot from the `post-session` hook. A command cut off by a lost runner can run again; Claude sees its outcome as unknown.
- A repository added mid-session is cloned over HTTPS and can fail without credentials; some connectors not connected in claude.ai do not appear; connectors added mid-session do not appear.
