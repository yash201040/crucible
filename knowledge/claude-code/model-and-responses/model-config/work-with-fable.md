---
type: "Feature"
title: "Work with Fable models"
description: "How to select Fable 5.2, 5.1 or 5, the one-time settings move, and usage guidance for the most capable models."
resource: "https://code.claude.com/docs/en/model-config#work-with-fable"
tags: [fable, model, selection, long-running]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.321"
surfaces: [cli]
requires: "Fable 5.2 needs Claude Code v2.1.321+, Fable 5.1 needs v2.1.257+"
identifiers:
  - "/model fable"
  - "--model fable"
  - "claude-fable-5-1"
  - "claude-fable-5"
  - "claude-fable-5-2"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Fable models are the most capable in Claude Code, for tasks larger than one sitting: long autonomous sessions, investigation before acting, more self-verification. No Fable model is the account-type default on any plan or provider; select one explicitly.

# How to use it

- Fable 5.2: `/model fable` or `claude --model fable`. In Claude apps gateway sessions use `/model claude-fable-5-2`.
- Fable 5.1 or 5: by ID, `/model claude-fable-5-1`, `/model claude-fable-5`, or `claude --model claude-fable-5-1`. On other providers use the provider model ID or pin with `ANTHROPIC_DEFAULT_FABLE_MODEL`.
- On the Anthropic API a Fable row shows in `/model` unless `availableModels` or organization restrictions exclude it. If the organization cannot use Fable (for example zero data retention) the row is grayed out with a note.
- Tips: describe the outcome not the steps (a [goal](/docs/en/goal) keeps it on target); give ambiguous problems; skip verification reminders; give larger tasks.
- Flagged safety requests trigger [automatic model fallback](./automatic-model-fallback.md).

# Limits and defaults

- On Pro, Max, Ultra, Team and Enterprise, a saved `claude-fable-5-1` in user settings moves to the `fable` alias. Pro/Max/Ultra: first run of v2.1.321 or later (startup line may show `(auto-updated)` once). Team/Enterprise: waits for organization settings, may come at a later startup or never, no `(auto-updated)` line.
- After the move, sessions start at Fable 5.2's default effort unless a level is set. Console accounts, third-party providers, and project, local or managed settings keep `claude-fable-5-1`.
- Fable 5.2 default effort is `medium`.
