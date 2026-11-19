---
type: "Reference"
title: "Retention sweep event"
description: "claude_code.retention_sweep reports cleanupPeriodDays cleanup of transcripts and data, including skip reasons."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [events, retention, transcripts, cleanup]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.227"
surfaces: [cli]
requires: "Claude Code v2.1.227 or later"
identifiers:
  - "claude_code.retention_sweep"
  - "cleanupPeriodDays"
  - "desktopSessionCleanupPeriodDays"
  - "period_days"
  - "used_default"
  - "skip_reason"
  - "transcripts_deleted"
  - "transcripts_exempted_desktop"
  - "session_files_deleted"
  - "artifacts_deleted"
  - "files_retained_fresh"
  - "files_past_cutoff"
  - "error_count"
  - "--bare"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Logged once per run of the background cleanup sweep that deletes session transcripts and other application data older than `cleanupPeriodDays` (default 30 when unset). The sweep runs at most once per session; if any session on the machine ran it in the last 24 hours, this session's sweep is delayed at least 10 minutes, so a session exiting sooner emits nothing. `claude -p` with `--bare` runs no sweep and emits nothing. A run that deletes nothing still emits the event. Managed `cleanupPeriodDays` pins the period even when a lower-priority settings file is broken.

# How to use it

Attributes: `result` (`complete`, `skipped`), `period_days`, `used_default`, `skip_reason` (only when skipped), `transcripts_deleted` (top-level `~/.claude/projects/*/*.jsonl`), `transcripts_exempted_desktop` (v2.1.248+), `session_files_deleted`, `artifacts_deleted` (a floor), `files_retained_fresh` (a floor), `files_past_cutoff`, `error_count`.

`skip_reason` values: `user_source_disabled` (user settings excluded by `--setting-sources` or SDK `settingSources`, and no enabled source sets `cleanupPeriodDays`), `settings_unknowable` (a settings file unreadable), `settings_invalid_key_set` (validation errors and `cleanupPeriodDays` or `desktopSessionCleanupPeriodDays` explicitly set), `remote_settings_unknowable` (Desktop Code tab on a third-party deployment got no usable server-managed settings).

# Notes

`period_days` and counters are strings; cast before comparing. A machine can legitimately emit no event (nobody launches Claude Code, a session stays open, a session ends before the sweep finishes). See [auditing retention](./audit-security-events.md).
