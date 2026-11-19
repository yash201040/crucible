---
type: "Feature"
title: "Using a different eval directory"
description: "Move the suite from evals/ with the experimental.evals manifest key or --eval-dir."
resource: "https://code.claude.com/docs/en/plugin-evals"
tags: [evals, manifest, configuration]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "experimental.evals"
  - "--eval-dir"
  - "plugin.json"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugin-evals"
    resource: "https://code.claude.com/docs/en/plugin-evals"
    title: "Test plugins with evals"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

If `evals/` is taken, keep the suite elsewhere: in `plugin.json` add `"experimental": { "evals": "quality/evals" }`, or pass `--eval-dir quality/evals` to both `claude plugin eval` and `claude plugin eval init`. If both are set the flag wins.

# Limits and defaults

Give a relative path of plain directory names such as `qa` or `quality/evals`. An absolute path or one containing `..` is an error as a flag value; an unusable manifest value prints a `Warning:` line and the run uses `evals/`. Cases, results and `init` output all move.
