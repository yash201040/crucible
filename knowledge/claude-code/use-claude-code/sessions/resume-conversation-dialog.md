---
type: "Feature"
title: "The Resume this conversation dialog"
description: "A usage estimate shown when resuming a long conversation on Pro, Max and Ultra plans."
resource: "https://code.claude.com/docs/en/sessions"
tags: [sessions, usage-limits, prompt-caching, resume]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Pro, Max or Ultra plan"
identifiers:
  - "Resume this conversation?"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sessions"
    resource: "https://code.claude.com/docs/en/sessions"
    title: "Manage sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The dialog's estimate is the share of your 5-hour usage limit that the saved conversation alone would use; it does not count usage already spent. It can appear when resuming a long conversation after a long break (prompt caching) or on a different model. The estimated use is incurred when you send your first message after **Resume**, not when you select it.

# How to use it

- **Resume**: keep working in the saved conversation.
- **Start a new conversation**: for work that does not need it; reopen later with `/resume`. The estimate does not apply to the first message in the new conversation. If the option says Claude can look up the conversation, you can still refer to earlier work.
