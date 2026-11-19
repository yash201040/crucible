---
type: "Concept"
title: "Cloud setup script failures and timeouts"
description: "Why a cloud environment setup script fails or hangs, including the roughly five-minute environment cache build budget."
resource: "https://code.claude.com/docs/en/web-quickstart"
tags: [setup-script, cloud-environment, timeouts, troubleshooting]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cloud]
requires: ""
identifiers:
  - "SessionStart"
  - "set -x"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "web-quickstart"
    resource: "https://code.claude.com/docs/en/web-quickstart"
    title: "Get started with Claude Code in the cloud"
stale_after: "2027-01-19T00:00:00Z"
---

# Limits and defaults

- A setup script exiting non-zero makes the session fail to start, or start without what the script failed to install (the session remains usable if it started).
- Causes: registry not allowed by the network access level (Limited with Allow package managers covers most; None blocks all), missing paths in a fresh clone, commands that differ on Ubuntu.
- Debug with `set -x` at the top; append `|| true` to non-critical commands. After fixing, start a new session so the script reruns; for a failed cloud scheduled task run, use Run now on the task.
- Roughly five-minute time budget for building the environment cache; exceeding it makes new sessions hang or fail with a generic container error. Fixes: run independent installs in parallel with `&` and a final `wait`; move big downloads to a SessionStart hook that launches them in the background; remove long retry sleeps.
