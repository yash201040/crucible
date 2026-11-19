---
type: "Guide"
title: "Letting Claude run unattended and from scripts"
description: "Five-question readiness checklist, claude -p flags for scripts (--bare, dontAsk, max-turns), and auto mode behavior with -p."
resource: "https://code.claude.com/docs/en/best-practices"
tags: [headless, unattended, bare, permissions, automation]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: "--bare auth from ANTHROPIC_API_KEY, apiKeyHelper in --settings file, or cloud provider credentials"
identifiers:
  - "claude -p"
  - "--bare"
  - "--append-system-prompt"
  - "--mcp-config"
  - "--settings"
  - "--allowedTools"
  - "--permission-mode dontAsk"
  - "--permission-mode auto"
  - "--max-turns"
  - "--max-budget-usd"
  - "--output-format json"
  - "stream-json"
  - "--verbose"
  - "ANTHROPIC_API_KEY"
  - "apiKeyHelper"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "best-practices"
    resource: "https://code.claude.com/docs/en/best-practices"
    title: "Best practices for Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude -p "prompt"` runs once and exits (CI jobs, git hooks, shell loops). Before leaving a run unattended, answer: 1) Does it know what done looks like (goal, spec, failing test)? 2) Can it check its own work (tests, Stop hook, review)? 3) What may it touch (permission rules, `dontAsk`, sandbox, worktree, one pushable branch)? 4) What stops it (`--max-turns`, `--max-budget-usd`, spend limit)? 5) Where does the result go and who signs off (PR, comment, summary, then a person approving)?

# How to use it

| Flag | What it does |
| - | - |
| `--bare` | Skips hooks, skills, plugins, MCP servers and CLAUDE.md files (repo and machine) so the run is the same everywhere; never uses the claude.ai login |
| `--append-system-prompt`, `--mcp-config`, `--settings` | Pass in explicitly what the run needs; hooks passed via `--settings` do not run under `--bare` |
| `--allowedTools` | Pre-approves tools |
| `--permission-mode dontAsk` | Refuses anything that would have prompted |
| `--max-turns` | Caps turns; hitting it exits with an error |
| `--output-format json` | One result object to parse |
| `stream-json` with `--verbose` | Streams events as they happen |

```bash
claude --bare -p "Migrate $file to the new logger API and commit. Reply OK or FAIL." \
  --allowedTools "Read,Edit,Bash(git add *),Bash(git commit *)" --permission-mode dontAsk --max-turns 20
```

# Limits and defaults

`--permission-mode auto` works with `-p`: a classifier block denies that action and Claude carries on; repeated blocks do not pause the run as in a terminal (see the repeated block thresholds section of permission modes). Try a script on three files first.
