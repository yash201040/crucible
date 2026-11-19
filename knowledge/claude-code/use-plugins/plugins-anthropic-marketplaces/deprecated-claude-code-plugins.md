---
type: "Limit"
title: "Deprecated claude-code-plugins marketplace"
description: "The claude-code-plugins marketplace in anthropics/claude-code is deprecated; ralph-wiggum became ralph-loop and claude-opus-4-5-migration is retired."
resource: "https://code.claude.com/docs/en/plugins/anthropic-marketplaces"
tags: [marketplace, deprecated, migration, plugins]
kind: "behavior"
maturity: "deprecated"
since: ""
surfaces: []
requires: ""
identifiers:
  - "claude-code-plugins"
  - "ralph-wiggum"
  - "ralph-loop"
  - "claude-opus-4-5-migration"
  - "claude plugin install"
  - "claude plugin uninstall"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-anthropic-marketplaces"
    resource: "https://code.claude.com/docs/en/plugins/anthropic-marketplaces"
    title: "Anthropic's marketplaces"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The `claude-code-plugins` marketplace in `anthropics/claude-code` is deprecated. Skip any tutorial step that runs `/plugin marketplace add anthropics/claude-code` and use `claude plugin install <plugin>@claude-plugins-official` in the shell.

# How to use it

- Unless you use one of the two plugins below, leave existing `claude-code-plugins` plugins as they are; they update from the `claude-plugins-official` repository.
- `ralph-wiggum` is now `ralph-loop`; its commands start with `/ralph-loop:`. If missing, run `claude plugin install ralph-loop@claude-plugins-official`.
- `claude-opus-4-5-migration` is retired: `claude plugin uninstall claude-opus-4-5-migration@claude-code-plugins`.
