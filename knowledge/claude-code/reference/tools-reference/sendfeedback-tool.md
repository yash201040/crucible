---
type: "Feature"
title: "SendFeedback tool and Claude-drafted feedback"
description: "Claude drafts feedback reports queued locally for review; controls, retention of drafts and where the tool is absent."
resource: "https://code.claude.com/docs/en/tools-reference#sendfeedback-tool-behavior"
tags: [feedback, drafts, privacy, zdr]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.238"
surfaces: [cli]
requires: "Interactive terminal session on the Claude API; not Zero Data Retention or HIPAA organizations"
identifiers:
  - "SendFeedback"
  - "feedbackDrafts"
  - "CLAUDE_CODE_SEND_FEEDBACK"
  - "DISABLE_FEEDBACK_COMMAND"
  - "/feedback"
  - "/bug"
  - "~/.claude/feedback/drafts/"
  - "cleanupPeriodDays"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude drafts a report when a tool keeps failing, it cannot help, a mistake occurs or you ask it to file feedback. Drafts are saved under `~/.claude/feedback/drafts/` and nothing is sent until you choose.

# How to use it

- A card shows the title: `1` review, `2` twice to send, `0` dismiss (dismissed drafts stay queued). At most three cards per session by default (server-adjustable); after that, or with `feedbackDrafts` set to `quiet`, only a footer count shows.
- `/feedback` with no argument opens the queue of all sessions' drafts; edit title, area, details; **Send transcript** `yes` or `no` (starts `yes` if the transcript is available; sending from the card never includes it); `w` writes a report yourself; `/feedback <text>` and `/bug` open the standard dialog.
- Report carries title, area, details, environment info (version, OS, model), recent API request IDs, and optionally the transcript. The working directory stays local.
- Turn off: `/config` **Claude-drafted feedback** `off` (writes `feedbackDrafts`), `CLAUDE_CODE_SEND_FEEDBACK=0` for one session, or `quiet` for no cards. Managed settings `feedbackDrafts` take precedence.

# Limits and defaults

Queue holds 10 drafts across sessions (the oldest is deleted on the eleventh); drafts expire after 30 days or `cleanupPeriodDays` if shorter; `/exit` with queued drafts asks to review or discard. Tool absent in `-p` runs and Agent SDK sessions, cloud sessions, Bedrock, Claude Platform on AWS, Google Cloud Agent Platform, Foundry, LLM gateway with its own key, with `CLAUDE_CODE_SEND_FEEDBACK=0`, `DISABLE_FEEDBACK_COMMAND=1`, any non-empty `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, feature-flag fetching off, orgs with product feedback off, Zero Data Retention (sending fails with `Feedback collection is not available for organizations with custom data retention policies.` if the tool still appears), or HIPAA configuration.
