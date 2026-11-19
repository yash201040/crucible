---
type: "Reference"
title: "claude plugin eval options and targets"
description: "Targets and flags for run count, concurrency, models, threshold, cost ceiling, grants, mocks and output."
resource: "https://code.claude.com/docs/en/plugin-evals"
tags: [evals, cli, flags, cost, concurrency]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.269"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "--runs <n>"
  - "-j"
  - "--concurrency <n>"
  - "--model <model>"
  - "--judge-model <model>"
  - "--ablation <mode>"
  - "--threshold <0..1>"
  - "--max-cost-usd <usd>"
  - "--allow-tools <tools...>"
  - "--scaffold"
  - "--trust-plugin"
  - "--mocks <mode>"
  - "--allow-real-servers"
  - "--json [path]"
  - "--output-dir <dir>"
  - "--no-publish"
  - "--publish-report"
  - "--keep-temp"
  - "--case <glob>"
  - "--tag <tag>"
  - "--eval-dir"
  - "--no-scaffold"
  - "--report"
  - "--verbose"
  - "name@marketplace"
  - "name@skills-dir"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugin-evals"
    resource: "https://code.claude.com/docs/en/plugin-evals"
    title: "Test plugins with evals"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Targets (first argument):

| Target | What runs |
| :- | :- |
| plugin root such as `.` | Every case under its eval directory with that plugin loaded |
| a `prompt.md` or `case.yaml` file | That case with its enclosing plugin |
| installed plugin `name` or `name@marketplace` | The plugin and its cases, read in place or from the installed copy; results under `./evals/results/` (or `./<dir>/results/` with `--eval-dir`) in the current directory |
| `name@skills-dir` | Same, for a skills-directory plugin |
| omitted | Current directory as a path |

Put the target before `--tag`, `--allow-tools` and `--json` (the first two take lists and `--json` takes an optional path, so each would read a following target as its value). `claude plugin eval --help` lists all options.

# How to use it

| Option | Default | Effect |
| :- | :- | :- |
| `--runs <n>` | case `runs`, else 3 | Runs per case per arm |
| `-j`, `--concurrency <n>` | `1` | Up to this many agent runs at once, 1 to 8; shares your rate limit; results keep case order |
| `--model <model>` | case `model`, else `ANTHROPIC_MODEL`, else default | Model under test; pin in CI |
| `--judge-model <model>` | background-task model | Model for `llm` and `baseline` graders |
| `--ablation <mode>` | per case | `none` one arm; `with-without` adds the baseline |
| `--threshold <0..1>` | `1.0` | Pass level for with-arm score; any case below makes exit code 1 |
| `--max-cost-usd <usd>` | no ceiling | Ceiling on list-price cost estimate (not plan usage), checked before each run starts; started runs finish so spend can pass it; unstarted runs mean exit 2 with partial results |
| `--allow-tools <tools...>` | none | Grants beyond read-only set |
| `--scaffold` | off | Run each case's `scaffold_script` |
| `--trust-plugin` | off | Skip the first-run trust prompt; use in CI |
| `--mocks <mode>` | `record` | `record` answers from mocks, no real servers, saves agent-mock answers; `off` ignores mocks and starts real servers |
| `--allow-real-servers` | off | With `--mocks record`, start real servers for unmocked servers |
| `--json [path]` | off | Print result document to stdout or write to a path ending `.json`; quiet run |
| `--output-dir <dir>` | `<eval dir>/results/<timestamp>/` | Where `aggregate-result.json` and `report.html` go |
| `--no-publish` | | Keep HTML report local |
| `--publish-report` | | Publish even where it would stay local |
| `--keep-temp` | off | Keep each run's sandbox directory and print its path |
| `--case <glob>`, `--tag <tag>` | | Filter by case name or any tag |
| `--eval-dir`, `--no-scaffold`, `--report`, `--verbose` | | Also exist (listed in `--help`) |
