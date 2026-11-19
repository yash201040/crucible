---
type: "Reference"
title: "Disable artifacts"
description: "Ways to turn artifacts off: /config, enableArtifact, CLAUDE_CODE_DISABLE_ARTIFACT, a deny rule, and precedence rules."
resource: "https://code.claude.com/docs/en/artifacts"
tags: [artifacts, settings, disable, permissions]
kind: "setting"
maturity: "unlabelled"
since: "2.1.242"
surfaces: [cli]
requires: "Honoring enableArtifact in project/local settings needs v2.1.242+"
identifiers:
  - "enableArtifact"
  - "disableArtifact"
  - "CLAUDE_CODE_DISABLE_ARTIFACT"
  - "permissions.deny"
  - "Artifact"
  - "/config"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "artifacts"
    resource: "https://code.claude.com/docs/en/artifacts"
    title: "Share session output as artifacts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Ways to turn artifacts off for your own sessions regardless of the organization's setting.

# How to use it

| Where | What |
| --- | --- |
| `/config` | Turn the **Artifacts** row off; writes `"enableArtifact": false` to user settings |
| Settings file | `"enableArtifact": false`. Deprecated `"disableArtifact": true` also turns off |
| Env var | `CLAUDE_CODE_DISABLE_ARTIFACT=1` |
| Permission rule | Add `Artifact` to `permissions.deny` |

# Limits and defaults

- Once off in a `--settings` file or via `CLAUDE_CODE_DISABLE_ARTIFACT`, or turned off by an administrator in managed settings, no settings file turns it back on.
- `"enableArtifact": false` in project `.claude/settings.json` or `.claude/settings.local.json` turns it off for that project; `true` there does not turn it back on. Requires v2.1.242+.
- A `WebFetch` deny/ask rule without `domain:` does not disable artifacts or block reads; `WebFetch(domain:claude.ai)` in deny or ask does apply to artifact reads.
