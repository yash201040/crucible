---
type: "Guide"
title: "Troubleshooting supervisor, auth and gateway errors"
description: "Fixes for unresponsive background service, authentication resolution failures, No LLM gateway and failed starts."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, troubleshooting, daemon, authentication]
kind: "behavior"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude daemon stop --any --keep-workers"
  - "~/.claude/daemon.lock"
  - "Could not resolve authentication method"
  - "No LLM gateway"
  - "possibly low memory"
  - "ANTHROPIC_API_KEY"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

- Background service did not respond (attach, peek or `claude logs` fails): `claude daemon stop --any --keep-workers`, then run `claude agents` within about a minute on macOS/Linux. If the stop prints a message, act per table: `could not be verified as the daemon, so it was not signalled` (all platforms: identify the PID owner, stop only if your supervisor, delete `~/.claude/daemon.lock`); `is still running after SIGKILL` (macOS/Linux: wait or restart computer); `was not sent SIGKILL` (macOS/Linux: rerun; check `ps -ww -o args= -p <pid>`; if it is a `daemon` supervisor `kill -9 <pid>`; delete lock if needed); `supervisor (pid=<pid>) is still running` (Windows: `taskkill /PID <pid>`). Same error on macOS/Linux older than v2.1.300: `claude update`.
- `Could not resolve authentication method` on dispatch while interactive works: the supervisor had no stored credential. Confirm `/login` or API key, `claude daemon stop --any --keep-workers`, then within about a minute start `claude agents` or `claude --bg` from a shell where `ANTHROPIC_API_KEY` is set if you use env-var auth.
- `No LLM gateway`: session lacked your gateway `ANTHROPIC_BASE_URL` because it was dispatched, woken or restarted from another directory. Either `cd` to the named folder in a terminal exporting the gateway and run the message's `claude respawn <id>` (supervisor must have started from a gateway-exporting shell), or put `ANTHROPIC_BASE_URL` and credential in `~/.claude/settings.json` or `.claude/settings.local.json` `env` and run `claude respawn <id>`.
- Session fails before start with `possibly low memory — free some up and retry`: a hypothesis shown only when the process exited silently on a low-memory host. Free memory, press `Enter` on the row (again if asked).
- Empty agent view shows section headers and one-line explanation until first dispatch.
