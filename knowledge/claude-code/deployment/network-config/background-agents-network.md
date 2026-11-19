---
type: "Feature"
title: "Network settings for background agents"
description: "Background sessions are hosted by a shared supervisor, so network variables must live in settings, not the shell; processWrapper applies there too."
resource: "https://code.claude.com/docs/en/network-config"
tags: [background-agents, supervisor, settings, launcher]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude agents"
  - "--bg"
  - "/background"
  - "claude daemon stop --any"
  - "processWrapper"
  - "CLAUDE_CODE_PROCESS_WRAPPER"
  - "env"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "network-config"
    resource: "https://code.claude.com/docs/en/network-config"
    title: "Enterprise network configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Background agents (`claude agents`, `--bg`, `/background`) run under a per-user supervisor process that starts on demand and outlives the shell. It is shared by all terminals and inherits the environment of whichever shell starts it first.

# How to use it

- Put proxy, CA and mTLS variables in the `env` block of `~/.claude/settings.json` or managed settings; a shell-only export reaches background agents only if that shell cold-started the supervisor.
- Corporate launcher: set `processWrapper` (or `CLAUDE_CODE_PROCESS_WRAPPER`, which wins if both set; deliver through managed settings or user settings, not a shell export) so the supervisor and workers start through it; a wrapper earlier on `PATH` is bypassed because they start from a fixed path.
- An already-running supervisor keeps its launch configuration; run `claude daemon stop --any` so the next `claude agents` or `--bg` starts one that honors the change.
