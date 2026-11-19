---
type: "Guide"
title: "Skill troubleshooting and listing budget"
description: "Fix skills that do not trigger, trigger too often, stop being followed, have truncated descriptions or vanished; listing budget settings."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, troubleshooting, listing-budget, context]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.196"
surfaces: [cli]
requires: ""
identifiers:
  - "skillListingBudgetFraction"
  - "SLASH_COMMAND_TOOL_CHAR_BUDGET"
  - "skillListingMaxDescChars"
  - "/context"
  - "--debug"
  - "~/.claude/skills/.trash/"
  - "manifest.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Common skill problems and the settings that tune how skills are listed to Claude.

# How to use it

- Not triggering: put natural keywords in `description`; check it appears in "What skills are available?"; rephrase; invoke with `/skill-name`; check [refused names](./skill-name-rules.md); if `paths` is set, files must be inside the current working directory (not a sibling worktree, even if added with `/add-dir`; use `/cd` or start in that worktree). Malformed YAML loads the body with empty metadata so `/skill-name` works but Claude cannot match; `--debug` shows the parse error.
- Triggers too often: make the description more specific or add `disable-model-invocation: true`.
- Stops following: move must-hold rules to hooks; word guidance for the whole task; after compaction invoke again (see [lifecycle](./skill-content-lifecycle.md)).
- Descriptions cut short: the listing always has every name but drops descriptions to fit a budget of 1% of the model's context window, dropping least-invoked skills first. `/doctor` estimates the cost; a debug-log warning appears on overflow. The `/context` Skills row shows the post-budget size (before v2.1.196 it counted full text).
- Raise the budget with `skillListingBudgetFraction` (e.g. `0.02` = 2%) or `SLASH_COMMAND_TOOL_CHAR_BUDGET` (fixed character count); free budget with `"name-only"` in `skillOverrides`; per-entry cap 1,536 characters of `description` plus `when_to_use`, configurable with `skillListingMaxDescChars`.
- Angle brackets in `description` or `when_to_use` display as `&lt;` and `&gt;`; use square brackets or `argument-hint`.
- Personal skills disappeared: check `~/.claude/skills/.trash/`. Before v2.1.280 a `manifest.json` in `~/.claude/skills/` moved the folders it listed into a timestamped trash folder. Restore by moving back before the retention sweep (default 30 days).
