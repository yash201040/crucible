---
type: "Guide"
title: "What subagents cost and keeping context cost down"
description: "Subagents cost tokens and sometimes time; use haiku, tool limits and /usage; /clear, /compact and the one-hour idle compaction note."
resource: "https://code.claude.com/docs/en/best-practices"
tags: [subagents, cost, usage, compact, haiku]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "/usage breakdown on Pro, Max, Ultra, Team and Enterprise"
identifiers:
  - "model: haiku"
  - "tools: Read, Grep, Glob"
  - ".claude/agents/"
  - "/usage"
  - "/clear"
  - "/compact"
  - "/loop"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "best-practices"
    resource: "https://code.claude.com/docs/en/best-practices"
    title: "Best practices for Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude delegates on its own: broad searches go to the built-in Explore agent, side tasks are forked while fork mode is on (the default), and started subagents run in the background by default.

# How to use it

- Subagents pay off for: parallel independent work, keeping long output out of the main conversation, a reviewer that has not seen how the code was written, and giving a task fewer tools.
- Costs are mostly tokens (each subagent sends its own requests against the same usage); a fresh subagent must gather context first and can be slower. By default it is the same model or smaller, so you get parallelism or fresh eyes, not a smarter answer.
- Cut cost: `model: haiku` in the definition for simple jobs; ask for short summaries; check `/usage` for each subagent type's share; limit a custom agent in `.claude/agents/` with `tools: Read, Grep, Glob` (enforced by Claude Code), e.g. `.claude/agents/reviewer.md` with name, description and those tools.
- Context cost: every request sends the whole conversation. `/usage` breaks usage down by skill, subagent, plugin and MCP server and flags patterns (long context, frequent cache misses) once one passes 10% of usage. `/clear` between unrelated tasks (`/clear oauth-migration` names the session left); `/compact keep the API changes and the test commands` focuses a summary and is itself a big request, more so after cache expiry.
- Background work keeps sending requests while you are away: a `/loop`, a goal's check after every turn, subagents.

# Limits and defaults

Most current models have a 1M-token window. The prompt cache lasts about an hour on a subscription and five minutes on an API key, cloud provider or usage credits; subagents get five minutes unless changed. On the one-hour cache, a session past about 200K tokens left idle is compacted shortly before expiry.
