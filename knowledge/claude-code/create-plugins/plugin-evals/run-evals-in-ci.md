---
type: "Guide"
title: "Run evals in CI and exit codes"
description: "A recommended CI invocation with pinned models and a cost ceiling, and the meaning of exit codes 0, 1, 2, 130 and 143."
resource: "https://code.claude.com/docs/en/plugin-evals"
tags: [evals, ci, exit-codes, headless]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [headless]
requires: ""
identifiers:
  - "--trust-plugin"
  - "--json results.json"
  - "--threshold 0.8"
  - "--max-cost-usd 20"
  - "ANTHROPIC_API_KEY"
  - "partial: true"
  - "skippedPaidGraders"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugin-evals"
    resource: "https://code.claude.com/docs/en/plugin-evals"
    title: "Test plugins with evals"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Run with `--json` to write the result and fail the build on the exit code. Example:

```
claude plugin eval . --trust-plugin --json results.json --threshold 0.8 --model claude-sonnet-5 --judge-model claude-haiku-4-5 --no-publish --max-cost-usd 20
```

# How to use it

| Exit | Meaning |
| :- | :- |
| 0 | Every case scored at or above `--threshold` and nothing else failed |
| 1 | A case below threshold, a case file failed to load, no cases found, a run could not start, or a run ended on an API error; also untrusted directory without `--trust-plugin`, invalid option, or `--json` result unwritable |
| 2 | Partial run: `--max-cost-usd` hit or credential rejected before or at the first run; `results.json` written with `partial: true` and the reason |
| 130 | Interrupted; partial results written |
| 143 | Terminated (e.g. CI timeout) |

The with-minus-without delta is reported but never changes the exit code; neither do HTML report write or publish problems.

# Limits and defaults

- The runner needs a Claude Code install and credentials in the environment (e.g. `ANTHROPIC_API_KEY` or cloud provider variables).
- Without `--trust-plugin`, a checkout Claude Code does not trust is refused with exit 1 when it cannot ask.
- Cheap every-change suites: use graders that do not call a judge, `--ablation none` where `Δ` is not needed, and exclude `partial: true` documents and runs with `skippedPaidGraders` from trend charts.
- Without `--json`, run locally to see per-run progress and grader lines. If exit is 1 though all cases passed, a stderr line names the cause. Default threshold 1.0 fails on any case below perfect.
