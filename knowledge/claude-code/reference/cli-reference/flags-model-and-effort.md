---
type: "Reference"
title: "Model, effort and context flags"
description: "Flags for choosing the model, effort level, fallback chain, advisor model, auto-compact window and API beta headers."
resource: "https://code.claude.com/docs/en/cli-reference"
tags: [model, effort, fallback, advisor, compaction]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.203"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "--model"
  - "--effort"
  - "--fallback-model"
  - "--advisor"
  - "--autocompact"
  - "--betas"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cli-reference"
    resource: "https://code.claude.com/docs/en/cli-reference"
    title: "CLI reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Per-session overrides for model choice, reasoning effort and context handling.

# How to use it

| Flag | Version | What it does |
| :- | :- | :- |
| `--model` | | Alias (`sonnet`, `opus`, `haiku`, `fable`) or full model name. Overrides the `model` setting and `ANTHROPIC_MODEL`. Example `claude --model claude-sonnet-5` |
| `--effort` | `ultracode` v2.1.203+ | `low`, `medium`, `high`, `xhigh`, `max`, or `ultracode`; available levels depend on the model. `ultracode` requests `xhigh` with ultracode on. Overrides `modelSettings` and `effortLevel` for the session without persisting |
| `--fallback-model` | | Comma-separated list tried in order when the primary model is overloaded or unavailable (for example retired), such as `sonnet,haiku`. Overrides the `fallbackModel` setting |
| `--advisor <model>` | | Enable the server-side advisor tool with `fable`, `opus`, `sonnet` or a full model ID; beats the `advisorModel` setting. `fable` requires Fable access |
| `--autocompact <auto\|tokens>` | v2.1.221+ | Auto-compact window for this session without saving, same values as `/autocompact` (example `500k`) |
| `--betas` | | Beta headers for API requests; API key users only (example `interleaved-thinking`) |
