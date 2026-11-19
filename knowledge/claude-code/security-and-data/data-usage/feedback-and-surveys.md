---
type: "Reference"
title: "Feedback commands and session quality surveys"
description: "What /feedback and the session survey send, how to disable them, and the related environment variables and settings."
resource: "https://code.claude.com/docs/en/data-usage"
tags: [feedback, survey, privacy, env-vars]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/feedback"
  - "/bug"
  - "/share"
  - "DISABLE_FEEDBACK_COMMAND"
  - "CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY"
  - "CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL"
  - "feedbackSurveyRate"
  - "DISABLE_TELEMETRY"
  - "DO_NOT_TRACK"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "~/.claude/feedback-bundles/"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "data-usage"
    resource: "https://code.claude.com/docs/en/data-usage"
    title: "Data usage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/feedback` (and `/bug`, `/share`, same path) sends a copy of the conversation including code to Anthropic, stored in Google Cloud Storage; optionally a GitHub issue is created in the public repository. The dialog lets you pick the current session (default) or also other sessions from the same project over the last 24 hours or 7 days. Claude-drafted feedback is queued locally and sent only when the user chooses.

# How to use it

| Name | Effect |
| - | - |
| `DISABLE_FEEDBACK_COMMAND=1` | Opt out of `/feedback` |
| `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY=1` | Disable session quality surveys; also disabled by `DISABLE_TELEMETRY`, `DO_NOT_TRACK` or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` |
| `CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL=1` | With nonessential traffic blocked, logs ratings to the configured OpenTelemetry collector only; transcript-share follow-up stays off |
| `feedbackSurveyRate` | Setting: probability between `0` and `1` for survey frequency |

# Limits and defaults

- The rating survey records only the rating. The optional follow-up ("Can Anthropic look at your session transcript...") on Yes uploads the transcript, subagent transcripts and raw session log (known key and token patterns redacted); shared transcripts are retained up to 6 months. Survey responses cannot be used for training.
- On Bedrock, Agent Platform, Foundry, signed-in Claude apps gateway sessions, or with no Anthropic credentials, Yes (and `/feedback`) writes the payload to `~/.claude/feedback-bundles/` instead; nothing leaves the machine until the file is forwarded.
- Organizations with zero data retention, product feedback disabled by policy, or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` never see the follow-up.
