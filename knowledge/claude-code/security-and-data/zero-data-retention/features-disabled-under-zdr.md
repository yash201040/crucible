---
type: "Limit"
title: "Features disabled under zero data retention"
description: "Backend-blocked features under ZDR, including cloud sessions, artifacts, feedback and Remote Control, and Fable model availability."
resource: "https://code.claude.com/docs/en/zero-data-retention"
tags: [zdr, disabled-features, cloud-sessions, models]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, cloud]
requires: "ZDR-enabled organization"
identifiers:
  - "/feedback"
  - "/bug"
  - "/share"
  - "/model"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "zero-data-retention"
    resource: "https://code.claude.com/docs/en/zero-data-retention"
    title: "Zero data retention"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Features that need stored prompts or completions are blocked at the backend regardless of client display; using one returns an error that the organization's policies do not allow it. Future features may be disabled too.

# How to use it

| Disabled feature | Reason |
| - | - |
| Cloud sessions (including from Desktop) | Server-side storage of conversation history |
| Chat and Cowork unified | Requires cloud sessions |
| Claude Tag | Retains channel memory and session transcripts |
| Artifacts in Claude Code | Stores published page content |
| Claude Docs | Stores document content |
| `/feedback`, `/bug`, `/share` | Sends conversation data to Anthropic |
| Remote Control | Stores transcript on Anthropic servers |

# Limits and defaults

Claude Fable 5.2, Fable 5.1 and Fable 5 are Covered Models that require data retention by default; availability for a ZDR org follows Covered Models policy. Where unavailable they are absent from or disabled in the `/model` picker and the server rejects requests. Other models stay available; Fable is not the default and the `best` alias resolves to Opus.
