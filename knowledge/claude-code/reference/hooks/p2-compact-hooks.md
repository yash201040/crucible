---
type: "Feature"
title: "PreCompact and PostCompact hook events"
description: "Hooks around context compaction: PreCompact can block it or add summary instructions; PostCompact sees the summary."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, compaction, precompact, context]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "PreCompact"
  - "PostCompact"
  - "manual"
  - "auto"
  - "trigger"
  - "custom_instructions"
  - "compact_summary"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`PreCompact` runs before a compaction; `PostCompact` runs after one completes (log the summary, update external state; no decision control, cannot affect the result). Both use the same matchers: `manual` (`/compact`) and `auto` (auto-compact at the auto-compact window, and idle compaction).

# How to use it

PreCompact input adds `trigger` and `custom_instructions` (for `manual`, what the user passed to `/compact`, `null` if nothing; `null` for `auto`). PostCompact input adds `trigger` and `compact_summary` (the generated conversation summary).

Block compaction with exit 2 (for manual `/compact` stderr is shown to the user) or `"decision": "block"`. When PreCompact exits 0 without blocking, its stdout is used as instructions for the compaction summary.

# Limits and defaults

- PreCompact stdout is capped at 10,000 characters per hook; longer output is cut and a marker appended.
- Blocking auto compaction: if triggered proactively before the context limit, it is skipped and the conversation continues uncompacted; if triggered to recover from a context-limit error already returned by the API, the underlying error surfaces and the current request fails.
- `systemMessage` and `continue` are discarded for both.
