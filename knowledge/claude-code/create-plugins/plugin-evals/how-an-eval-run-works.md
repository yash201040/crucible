---
type: "Concept"
title: "How an eval run works and is scored"
description: "Isolated non-interactive sessions per run, three runs per case by default, scoring, threshold and cost shape."
resource: "https://code.claude.com/docs/en/plugin-evals"
tags: [evals, scoring, runs, cost, headless]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [headless]
requires: ""
identifiers:
  - "--threshold"
  - "--runs"
  - "WITH"
  - "W/OUT"
  - "Δ"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugin-evals"
    resource: "https://code.claude.com/docs/en/plugin-evals"
    title: "Test plugins with evals"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

For each run of a case, Claude Code starts a fresh isolated non-interactive session with only the plugin loaded, sends the prompt, and lets Claude work until it finishes or hits the case's turn or time limit. Each grader then checks the final reply, transcript or a created file.

# Limits and defaults

- Each case runs 3 times by default. A run's score is the fraction of graders passed (weighted if weights are set); the case score is the mean over runs. A case passes when its score meets `--threshold` (default `1.0`).
- Model-call volume: roughly cases x runs agent runs with the plugin and the same number again for the no-plugin baseline, plus three short judge calls per `llm` or `baseline` grader per run.
- Baseline: runs repeated without the plugin give `WITH` and `W/OUT` scores; `Δ` is their difference. A case scoring 1.0 both ways shows the plugin is not what made it pass. See [baseline scoring](./baseline-and-ablation-scoring.md).
