---
type: "Experiment"
title: "Helper sessions under a solver: counted, capped, recorded and closed by a launcher"
description: "A launcher starts every helper session of a run and holds it in code. Live: two levels of real sessions, a session stopped mid-command in two seconds, and a solver that used two helpers and re-checked them. Solvers left to choose did not use one on searchable files."
tags: [workflows, nesting, subagents, headless, cost]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "claude -p"
  - "--session-id"
  - "--disallowedTools"
  - "--max-turns"
  - "--output-format json"
  - "total_cost_usd"
orchestration: "high"
status: "stable"
generated: { by: "claude-code/fable-5.2", at: "2026-11-20T00:00:00Z" }
verified:
  - { by: "process:crucible-probe", at: "2026-11-20T00:00:00Z" }
sources:
  - id: "probe"
    resource: "/experiments/"
    title: "Probe runs on Claude Code 2.1.329, 2026-11-20"
stale_after: "2027-01-19T00:00:00Z"
---

# Question

[An agent of a run can nest through a child session](/experiments/nesting-through-a-child-session.md), but such a session is outside the run. Can each thing the run cannot see be held in code, so that nesting is safe to hand to solvers? And will solvers use it well?

# What was built

`scripts/crucible_helper.py`. A solver writes a task file and calls it; it starts a headless session (`claude -p`, prompt on standard input) and stays detached from the caller as that session's supervisor.

| What the run cannot see | How the launcher holds it |
| --- | --- |
| How many sessions work at once | a fixed number of slots per level (4), taken with a file lock; a level never waits on itself, so levels cannot deadlock |
| What they cost | one allowance per run, in the run's own unit (an average agent on Opus = 1). The cost is the session's own `total_cost_usd`, or its transcript's tokens when it was killed. A start past the allowance is refused |
| That they existed | `<run>/helpers/<id>/`: the task, the prompt, the handoff, notes, and a record with owner, parent, level, model, times, tokens, cost, session id and transcript |
| When they end | the supervisor ends the session and its whole process group when its owner closes, its time is up, the session that started it is gone, or the run stops or is saved; a helper that is stopped takes the helpers it started with it |
| How deep they go | the run's figure (`--depth-max`); the last level is told to work alone and is refused if it tries. Helpers get `--disallowedTools Agent,Workflow`, so every level goes through the launcher |
| Who may use one | the owner's label must be a solver or a repair; any other role is refused |

# Results

Without a model (a stand-in for `claude`, 27 tests): handoff and cost recorded; refusals for role, thin task, model, effort, count and allowance; two, and four, levels deep; never more than the slots at once; time limit, close, stop, vanished owner and dead supervisor each end the session and what it started; a usage-limit failure pauses new starts.

Live, on Claude Code 2.1.329:

| Test | Result |
| --- | --- |
| A Haiku helper told to hand one question to a helper of its own | both sessions ran and were recorded at levels 1 and 2; 34 seconds; 0.01 USD by API prices; the first re-checked what the second handed back |
| A helper stopped while it ran `sleep 421` | its owner's `close` returned in 2 seconds; the session and the sleep were gone; its cost was taken from its transcript; its notes file was handed over |
| Two Sonnet solvers given the instruction, one with a quick job and one with a search over 205 pages | neither used a helper, both for a stated reason (a few searches were quicker); both answers held |
| A Sonnet solver given 880 KB to judge "as a whole", twice (the second time with a size above which to hand over) | did not use a helper either time: it searched instead of reading, stayed under 80K tokens, and said what a search could miss |
| A Sonnet solver told to use two helpers side by side on 420 KB | used `start` twice, `wait` and `close` correctly; re-read all 20 cited lines itself; named the helper next to each fact. The helpers took 51 and 38 seconds on Haiku and cost 0.14 USD together (0.01 of an average agent); the solver itself used 42K tokens |

Prices seen in the CLI's own report on that day, per million input-equivalent tokens (cache read 0.1, cache write 1.25, output 5): Haiku 0.16, Sonnet 3.1, Opus 6.1 USD. A headless session's cache writes are of the one-hour kind.

# What it means for crucible

- The mechanism is safe to switch on: nothing a helper does is outside the ceiling, the records or the stop.
- Solvers do not reach for a helper when files can be searched, even above the stated size. On such work they are right: the search was cheaper than a helper's full reading. Expect helpers to be used mostly where material cannot be filtered first (web pages, logs that must be read through, long builds) and where a solver's own context has already grown large.
- Whether helpers make a long run cheaper or more thorough is not known. The numbers to watch after a real run: `helpers.done_share`, handoffs never read, the share of solvers past 300K tokens of context.
- A helper never has Code Mode, runs in the permission mode of the user's settings, and is not covered by the workflow's waiting on a usage limit.

The live tests ran from an app built on the Agent SDK. A result holds for that release only: run them again after an update.
