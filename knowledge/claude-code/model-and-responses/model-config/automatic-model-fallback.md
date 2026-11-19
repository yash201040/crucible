---
type: "Feature"
title: "Automatic model fallback on flagged requests"
description: "Content-based fallback when safety classifiers flag cybersecurity or biology requests on Fable, Opus 5.5, Sonnet 5.5 and Opus 5."
resource: "https://code.claude.com/docs/en/model-config#automatic-model-fallback"
tags: [fallback, safety, classifiers, subagents, bedrock]
kind: "setting"
maturity: "unlabelled"
since: "2.1.219"
surfaces: [cli, headless, sdk, web, mobile]
requires: "Category-based fallback v2.1.219+; subagent behavior change v2.1.318"
identifiers:
  - "switchModelsOnFlag"
  - "--safe-mode"
  - "ANTHROPIC_DEFAULT_OPUS_MODEL"
  - "ANTHROPIC_DEFAULT_SONNET_MODEL"
  - "ANTHROPIC_DEFAULT_FABLE_MODEL"
  - "modelOverrides"
  - "claude-fable-5"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Fable models, Opus 5.5, Sonnet 5.5 and Opus 5 run with safety classifiers that most often flag cybersecurity and biology content. A flagged request is re-run on a fallback model chosen by category (separate from availability-based [fallback chains](./fallback-model-chains.md)).

# How to use it

| Source model | Cybersecurity flag | Biology flag |
| - | - | - |
| Fable models, Opus 5.5 | Opus 4.8 | Opus 5 |
| Sonnet 5.5 | Sonnet 5 | refusal (no fallback) |
| Opus 5 | Opus 4.8 | refusal (no fallback) |

In the main conversation a transcript notice shows; the session continues on the fallback until `/model`. Before v2.1.219 every flagged Fable 5 request re-ran on the provider's default Opus and Opus 5 was not a source. If the fallback target is blocked by `availableModels`, no fallback occurs and a normal refusal error shows.

Ask first: `/config` then **Switch models when a message is flagged** = **Ask each time**, or `switchModelsOnFlag: false`. Claude Code then pauses and offers switch or edit-and-retry. The first time in an interactive session it may ask whether to switch automatically and saves the choice as `switchModelsOnFlag` (dismiss saves nothing; staying saves `false`).

# Limits and defaults

- Effort after fallback: the flagged request's level is kept (e.g. Opus 5.5 at `medium` falling to Opus 4.8 stays `medium`), unless you chose a level, picked a model, resumed, or a one-turn `ultrathink` or skill `effort` applied. Check with `/effort status`.
- Ask each time exceptions: no prompt when the category has no fallback (refusal), when both models flag (edit/retry or new session), when the target is blocked; mobile cloud sessions cannot edit and retry; non-interactive mode and SDK integrations that cannot show the prompt end the turn with a refusal.
- Subagents started with the Agent tool never pause to ask. With **Switch automatically** (or no choice) the request re-runs on the fallback and the session model is unchanged; with **Ask each time** the subagent fails with `Agent terminated early due to an API error` and the refusal message; with no fallback available it fails either way. Before v2.1.318 a subagent's flagged request re-ran on an available fallback regardless.
- Diagnose triggers: the first request carries workspace context (CLAUDE.md, git status), so security or biology repos can trip it; test with `claude --safe-mode` (disables CLAUDE.md, skills, MCP servers, hooks; git status and directory names remain). Offensive security and biology workloads (pen testing, CTFs) trigger often; for Fable-class access ask the Anthropic account team about trusted access programs. For biology on Fable or Opus 5.5 the first switch moves the session to Opus 5, then later biology flags refuse.
- Bedrock, Agent Platform, Foundry: fallback works only if Claude Code can identify models. Fable recognized when ID contains `claude-fable-5`, equals `ANTHROPIC_DEFAULT_FABLE_MODEL`, or is mapped in `modelOverrides`; Opus 5.5, Sonnet 5.5, Opus 5 by provider ID or `modelOverrides`. An Opus target must resolve (set `ANTHROPIC_DEFAULT_OPUS_MODEL` or keep an Opus 4.8 entry) or fallback stays off for every source including Sonnet 5.5. With the Opus pin set, flagged categories with a fallback re-run on it (Opus 5 biology still refuses); without it, cyber re-runs on the Opus 4.8 entry and Fable/Opus 5.5 biology on an Opus 5 entry. Sonnet 5.5 cyber uses `ANTHROPIC_DEFAULT_SONNET_MODEL` or a Sonnet 5 entry. A pin outside the right family or the refusing model leaves the refusal. The fallback needs a context window at least as large as the session's (source models run 1M there; pin e.g. Opus 4.8 or Sonnet 5).
