---
type: "Limit"
title: "Mod calls refused in claude -p and SDK runs"
description: "In headless and Agent SDK runs, mod prompts count toward --max-turns and --max-budget-usd and are refused at the limit, so runs can end."
resource: "https://code.claude.com/docs/en/plugins/mods/api"
tags: [mods, headless, max-turns, budget, sdk]
kind: "limit"
maturity: "unlabelled"
since: "2.1.299"
surfaces: [headless, sdk]
requires: "v2.1.299 for refusal at --max-turns; v2.1.304 for subagent turns counted"
identifiers:
  - "--max-turns"
  - "--max-budget-usd"
  - "--input-format stream-json"
  - "the run reached its --max-turns limit"
  - "the run is past its --max-budget-usd limit"
  - "the host has ended its input"
  - "interrupt()"
  - "claude -p"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-api"
    resource: "https://code.claude.com/docs/en/plugins/mods/api"
    title: "Use the mods API"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

In a `claude -p` run or Agent SDK session, a result like `{ drop: 'the run reached its --max-turns limit' }` means the run refused your mod's call. A refused `$.prompt.submit` resolves with `{ drop: '<reason>' }`; other calls (`$.command.run`, `$.agent.spawn`) give the results in the interruption table with the reason substituted.

# How to use it

| Reason | What to do |
| :- | :- |
| `the run reached its --max-turns limit` | Turns from the mod's prompts and spawned subagents count toward `--max-turns` (or the SDK turn limit). Start with a higher limit or stop making the call; a new prompt from user/SDK resets the turn count |
| `the run is past its --max-budget-usd limit` | Raise `--max-budget-usd` or the SDK spend limit; limit applies to total cost so far, which keeps adding across prompts, so a retry gets the same reason |
| `the host has ended its input` | SDK ended streaming input, or stdin closed on `--input-format stream-json`; run is ending, retry gives same reason; keep input open until the mod has no more calls |
| `the session was stopped and nobody has sent input since` | Run was interrupted (e.g. SDK `interrupt()`); retry after the next message as in the interruption concept |

# Limits and defaults

A mod that submits a prompt at the end of every turn makes a `claude -p` run endless unless `--max-turns` or `--max-budget-usd` is set (example: `claude -p "find the TODOs" --max-turns 5`). Prompts are refused at the limit from v2.1.299; subagent turns count toward `--max-turns` from v2.1.304. If others start the run, have the mod stop submitting when done.
