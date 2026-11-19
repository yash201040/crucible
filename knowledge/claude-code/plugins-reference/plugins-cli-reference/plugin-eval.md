---
type: "Feature"
title: "claude plugin eval"
description: "Runs a plugin's eval cases several times in isolated sessions, with and without the plugin, and reports scored results with CI exit codes."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, evals, ci, cost-limit]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.269"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "claude plugin eval"
  - "--runs <n>"
  - "-j, --concurrency <n>"
  - "--model <model>"
  - "--judge-model <model>"
  - "--ablation <mode>"
  - "--threshold <0..1>"
  - "--max-cost-usd <usd>"
  - "--allow-tools <tools...>"
  - "--scaffold"
  - "--trust-plugin"
  - "--mocks <mode>"
  - "--eval-dir <dir>"
  - "--json [path]"
  - "--no-publish"
  - "--case"
  - "--tag"
  - "--output-dir"
  - "--report"
  - "--allow-real-servers"
  - "--keep-temp"
  - "--verbose"
  - "experimental.evals"
  - "ANTHROPIC_MODEL"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude plugin eval [target] [options]` runs a plugin's eval cases and reports scored results. Requires v2.1.269 or later. Each case is a prompt plus graders; Claude Code runs it several times in an isolated session with only the target plugin loaded, and by default also without the plugin so the report shows the difference.

`target` defaults to the current directory; it can be a plugin directory, a single `prompt.md` or `case.yaml`, an installed plugin as `name` or `name@marketplace`, or `name@skills-dir`. Put the target before `--tag`, `--allow-tools` and `--json`, because each takes the following words as its value.

# How to use it

| Option | Description | Default |
| :- | :- | :- |
| `--runs <n>` | Runs per case in each arm | Case's `runs`, else 3 |
| `-j, --concurrency <n>` | Agent sessions at once, 1 to 8; they share your rate limit | `1` |
| `--model <model>` | Model for the agent under test | Case's `model`, else `ANTHROPIC_MODEL`, else Claude Code default |
| `--judge-model <model>` | Model for `llm` and `baseline` graders | Model for background tasks |
| `--ablation <mode>` | `none` or `with-without` | Decided per case |
| `--threshold <0..1>` | Exit 1 if any case scores below | `1.0` |
| `--max-cost-usd <usd>` | Stop before the next run once spend reaches this, exit 2, report partial results | No limit |
| `--allow-tools <tools...>` | Grant tools beyond the read-only set, e.g. `Bash`, `Write`, `Edit`, `"mcp__plugin_<plugin>_<server>__*"` | |
| `--scaffold` | Run each case's `scaffold_script` | Off |
| `--trust-plugin` | Skip the first-run trust prompt, for CI | Off |
| `--mocks <mode>` | `record` or `off` | `record` |
| `--eval-dir <dir>` | Directory below the plugin holding cases | Manifest `experimental.evals`, else `evals` |
| `--json [path]` | Print the result document to stdout or write to a `.json` path | |
| `--no-publish` | Keep the HTML report local | |

Further options not tabled: `--case`, `--tag`, `--output-dir`, `--report`, `--allow-real-servers`, `--keep-temp`, `--verbose`.

# Limits and defaults

| Exit code | Meaning |
| :- | :- |
| `0` | Suite passed |
| `1` | Failing case, load error, untrusted plugin directory, run ended on an API error, or other cause listed under Run evals in CI |
| `2` | Partial run |
| `130` | Interrupted |
| `143` | Terminated |
