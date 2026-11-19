---
type: "Reference"
title: "Application data and automatic cleanup"
description: "Files Claude Code writes under ~/.claude (transcripts, file history, debug logs), cleanupPeriodDays retention and when the sweep is skipped."
resource: "https://code.claude.com/docs/en/claude-directory"
tags: [retention, transcripts, cleanup, sessions]
kind: "setting"
maturity: "unlabelled"
since: "2.1.288"
surfaces: [cli, desktop]
requires: ""
identifiers:
  - "cleanupPeriodDays"
  - "desktopSessionCleanupPeriodDays"
  - "~/.claude/projects/<project>/<session>.jsonl"
  - "~/.claude/projects/<project>/<session>/subagents/"
  - "~/.claude/projects/<project>/<session>/tool-results/"
  - "~/.claude/projects/<project>/<session>/mcp-tasks/"
  - "~/.claude/file-history/"
  - "~/.claude/plans/"
  - "~/.claude/debug/"
  - "~/.claude/paste-cache/"
  - "~/.claude/image-cache/"
  - "~/.claude/uploads/"
  - "~/.claude/dev-mods/"
  - "~/.claude/session-env/"
  - "~/.claude/tasks/"
  - "~/.claude/shell-snapshots/"
  - "~/.claude/backups/"
  - "~/.claude/feedback-bundles/"
  - "~/.claude/feedback/drafts/"
  - "~/.claude/usage-data/"
  - "~/.claude/sessions/"
  - "~/.claude/seed-admin/"
  - "--bare"
  - "retention_sweep"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-directory"
    resource: "https://code.claude.com/docs/en/claude-directory"
    title: "Explore the .claude directory"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`~/.claude` holds data Claude Code writes during sessions, in plaintext. Anything passing through a tool (file contents, command output, pasted text) is written to a transcript. Transcripts can also hold the system prompt, tool definitions, request parameters and loaded instruction files such as CLAUDE.md.

# How to use it

Files older than `cleanupPeriodDays` (default 30, minimum 1; `0` fails validation) are deleted when Claude Code can safely determine the retention period. The same cutoff applies to automatic removal of orphaned worktrees.

| Path under `~/.claude/` | Contents |
| - | - |
| `projects/<project>/<session>.jsonl` | Conversation transcript with tool calls and results, plus system prompt, tool definitions, request parameters |
| `projects/<project>/<session>.orphaned-<timestamp>-<suffix>.jsonl`, `...jsonl.superseded-<timestamp>` | Previous transcript set aside; not in the session picker |
| `projects/<project>/<session>/subagents/` | Subagent transcripts, removed with the parent transcript |
| `projects/<project>/<session>/tool-results/` | Large tool outputs and full-size MCP images |
| `projects/<project>/<session>/mcp-tasks/` | State a resumed session needs to follow running MCP tasks, and unread finished results |
| `file-history/<session>/` | Pre-edit snapshots for checkpoint restore; the 100 most recent checkpoints kept; unreferenced snapshots deleted except each file's first |
| `plans/` | Plan-mode plan files |
| `debug/` | Per-session debug logs while debug logging is on (`--debug` or `/debug`) |
| `paste-cache/` | Large pastes |
| `image-cache/<session>/` | Images attached by v2.1.274 and earlier; later versions save images in an `images/` directory per session under the `CLAUDE_CODE_TMPDIR` temp directory |
| `uploads/<session>/` | Files and mobile photos attached to a Remote Control session; cloud-session attachments stay in the cloud environment |
| `dev-mods/<session>/` | Mods Claude wrote during the session |
| `session-env/` | Per-session environment metadata |
| `tasks/` | Task lists from the task tools, one directory per list |
| `shell-snapshots/` | Aliases, functions, shell options applied by the Bash tool; removed on clean exit |
| `backups/` | Earlier `~/.claude.json` copies; the five newest kept plus any unparsable version |
| `feedback-bundles/` | Redacted transcript archives from `/feedback` on third-party providers or without Anthropic credentials |
| `feedback/drafts/` | Queued Claude-drafted feedback; swept after `cleanupPeriodDays` or 30 days, whichever is shorter; max 10 drafts (oldest deleted) |
| `usage-data/` | `/insights` reports and cached analysis |
| `skills/.trash/`, `plugins/.trash/` | Skills and plugins removed by claude.ai sync, recoverable until swept |
| `plugins/installed_plugins.set-aside.<date>.<hash>.json`, `plugins/installed_plugins.unreadable.<date>.<hash>.kept` | Dated copies before rewriting `installed_plugins.json` |
| `plugins/mcpb/` | Extracted MCP bundles; age counts from last session using it |
| `todos/`, `statsig/`, `logs/` | Legacy, no longer written |

Separate retention:
- `sessions/`: one small file per running session (detects concurrent sessions and crashes); removed on exit, crash leftovers cleared next launch.
- `seed-admin/`: scratch git directories for an ultrareview or cloud session upload; removed when the upload ends or later.
- Auto memory (`projects/<project>/memory/`): not swept; removed only if empty for the whole retention period. Before v2.1.228 the sweep could delete old files under it.
- Claude Desktop and Cowork transcripts: kept at any age unless `desktopSessionCleanupPeriodDays` is set (v2.1.248 or later; earlier versions delete after `cleanupPeriodDays`). They are deleted after `cleanupPeriodDays` if managed settings set it or the HIPAA configuration applies.

# Limits and defaults

The sweep is skipped when:
- `claude -p` runs with `--bare` (no sweep in that session).
- Claude Code cannot safely determine retention; the `retention_sweep` event lists the causes, and `/status` warns when a settings file is unreadable or `cleanupPeriodDays` / `desktopSessionCleanupPeriodDays` have settings errors.

With managed `cleanupPeriodDays`, the sweep runs at the managed value even if a lower-priority file has errors.

# Notes

The page's table of a session scratchpad is covered in [scratchpad](./session-scratchpad-directory.md).
