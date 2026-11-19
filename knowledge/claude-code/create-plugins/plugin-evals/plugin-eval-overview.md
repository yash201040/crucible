---
type: "Feature"
title: "claude plugin eval overview and requirements"
description: "A shell command that runs a plugin against test cases with graders, scored with and without the plugin."
resource: "https://code.claude.com/docs/en/plugin-evals"
tags: [plugins, evals, testing, ci]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.269"
surfaces: [cli, headless]
requires: "Claude Code v2.1.269 or later; git 2.31 or later if git is installed"
identifiers:
  - "claude plugin eval"
  - "claude plugin eval init"
  - "claude plugin validate"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugin-evals"
    resource: "https://code.claude.com/docs/en/plugin-evals"
    title: "Test plugins with evals"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude plugin eval` runs a plugin against a suite of cases and scores the results. A case is a realistic prompt plus one or more graders (pass/fail checks on what Claude produced: a regex over the reply, whether a tool was called, or a rubric judged by a second model). `claude plugin eval init` asks about the plugin, proposes cases and graders, trials them and writes the files; you can also ask Claude to run it from an open session. Uses: measure reliability, catch regressions when the plugin or model changes, and see what the plugin contributes versus none.

# How to use it

Requirements:
- Claude Code v2.1.269+ (`claude update`).
- Git 2.31+ if git is installed; with older git the command stops before any case ([error](./plugin-eval-troubleshooting.md)). Without git it runs normally.
- A plugin directory with `plugin.json` or `.claude-plugin/plugin.json`, or a skills-directory plugin.
- The same auth and provider as normal sessions. Eval runs, judge graders and `init` are real model calls on your account (plan usage or API bill); reported cost is a list-price estimate. For Bedrock, Google Cloud Agent Platform or Microsoft Foundry, run from a shell exporting the same provider variables (each run inherits them).

# Notes

For iterating on one skill inside a conversation, the skill-creator plugin has a similar comparison with its own `evals/evals.json` format; neither tool reads the other's case files. To check syntax and schema rather than behavior use `claude plugin validate`.
