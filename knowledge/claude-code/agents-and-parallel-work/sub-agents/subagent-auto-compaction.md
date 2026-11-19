---
type: "Feature"
title: "Subagent auto-compaction"
description: "Subagents compact as their own context fills; autoCompactWindow lowers the window per subagent."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, compaction, context, tokens]
kind: "frontmatter"
maturity: "unlabelled"
since: "2.1.296"
surfaces: [cli]
requires: ""
identifiers:
  - "autoCompactWindow"
  - "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE"
  - "CLAUDE_CODE_AUTO_COMPACT_WINDOW"
  - "compact_boundary"
  - "preTokens"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Compaction triggers as a subagent's own window fills; `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` applies too. Compaction is logged in the subagent transcript as `{"type":"system","subtype":"compact_boundary","compactMetadata":{"trigger":"auto","preTokens":167189}}`, where `preTokens` is tokens used before compaction.

# How to use it

Set `autoCompactWindow` in frontmatter to a plain integer of `100000` or more (v2.1.296 or later), e.g. `autoCompactWindow: 200000`. `200k` is read as 200, below the minimum, so the field is ignored (search `claude --debug` log for `invalid autoCompactWindow`).

# Limits and defaults

- No visible effect if the value is not below the auto-compact window the subagent would otherwise inherit, or when running the whole session as the subagent via `--agent` / `agent` setting.
- With `CLAUDE_CODE_AUTO_COMPACT_WINDOW` also set, the lowest of the field value, the model's context window and the variable's window is used. Before v2.1.312 the field had no effect while the variable set the window.
