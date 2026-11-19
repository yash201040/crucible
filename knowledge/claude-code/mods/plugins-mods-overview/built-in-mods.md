---
type: "Reference"
title: "Mods built into Claude Code"
description: "Built-in mods listed under Built-in in /plugin, such as cc-plugin-diff and cc-plugin-sec-default, with where they run and how to turn them off."
resource: "https://code.claude.com/docs/en/plugins/mods/overview"
tags: [mods, built-in, agents-md, telemetry]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "cc-plugin-agents-md"
  - "cc-plugin-diff"
  - "cc-plugin-plugin-authoring"
  - "cc-plugin-sec-default"
  - "cc-plugin-telemetry"
  - "cc-plugin-you-should-know"
  - "DISABLE_TELEMETRY"
  - "AGENTS.md"
  - "/diff"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-overview"
    resource: "https://code.claude.com/docs/en/plugins/mods/overview"
    title: "Mods overview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Some Claude Code features are mods. In `/plugin`, **Installed** tab, they appear under **Built-in**; they cannot be updated or uninstalled.

| Name | What it does | Where on | Turn off |
| :- | :- | :- | :- |
| `cc-plugin-agents-md` | loads `AGENTS.md` as project instructions | every session except those that cannot read `AGENTS.md` | disable in `/plugin`, or choose which instruction files load |
| `cc-plugin-diff` | takes over `/diff` and draws its pane | interactive terminal sessions | disable in `/plugin` (built-in `/diff` then answers) |
| `cc-plugin-plugin-authoring` | gives Claude the `plugin-authoring` skill for writing mods (skill only, no mod code) | unless Anthropic turned installed mods off remotely | disable in `/plugin` |
| `cc-plugin-sec-default` | guards what the organization manages from user-installed mods | where the guard loads | cannot; admin sets order in managed settings |
| `cc-plugin-telemetry` | sends analytics records Claude Code and built-in mods log | wherever analytics are on | disable in `/plugin`, or `DISABLE_TELEMETRY` |
| `cc-plugin-you-should-know` | a side agent shows a note above the prompt for things you might have missed | off until turned on | disable in `/plugin` |

# Notes

Other Built-in plugins: open details in `/plugin`. Built-in mods are not stopped by `disableAllHooks`, `--bare` or `--safe-mode`. Public sources in the `mods` directory of the Claude Code repository: `diff`, `agents-md` (with a `userConfig` option), `sec-default` (model for a policy-enforcing mod), `telemetry` (adds methods other mods call and ships their types).
