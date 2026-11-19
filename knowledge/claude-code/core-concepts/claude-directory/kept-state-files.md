---
type: "Reference"
title: "Files kept until deleted and state files to keep"
description: "Paths the retention sweep does not remove (history, stats, remote settings cache, policy limits) and state directories that must not be deleted."
resource: "https://code.claude.com/docs/en/claude-directory"
tags: [state, history, cache, retention]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "~/.claude/history.jsonl"
  - "~/.claude/stats-cache.json"
  - "~/.claude/remote-settings.json"
  - "~/.claude/cache/changelog.md"
  - "~/.claude/policy-limits.json"
  - "policy-limits.json.stamp.json"
  - ".credentials.json"
  - "agent-memory/"
  - "jobs/"
  - "daemon/"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-directory"
    resource: "https://code.claude.com/docs/en/claude-directory"
    title: "Explore the .claude directory"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Paths the cleanup sweep does not remove (unless a row says otherwise).

# How to use it

| Path under `~/.claude/` | Contents |
| - | - |
| `history.jsonl` | Typed prompts with timestamp and project path; used for up-arrow recall, `Ctrl+R` search, `!` completion. Entries older than `cleanupPeriodDays` are removed each sweep when the HIPAA configuration applies |
| `stats-cache.json` | Aggregated token and cost counts shown by `/usage` |
| `remote-settings.json` | Cached server-managed settings (or `{}`); only present when the session fetches them; checked at startup and hourly; deleted on logout |
| `cache/changelog.md` | Cached changelog shown by `/release-notes`; refreshed in the background |
| `policy-limits.json` | Cached feature policy for some account types; a `policy-limits.json.stamp.json` sidecar records which account or key it belongs to; both deleted on logout |

State files to keep (caches and lock files are safe to delete): `.credentials.json` (login credentials), `agent-memory/` (subagent memory), `jobs/` and `daemon/` (background session state).

# Notes

Do not delete `~/.claude.json`, `~/.claude/settings.json` or `~/.claude/plugins/`.
