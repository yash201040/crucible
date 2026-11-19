---
type: "Feature"
title: "Claude Security plugin install and prerequisites"
description: "The claude-security plugin runs a multi-agent vulnerability scan inside a Claude Code session on your session's model; needs python3 3.9+ and a paid plan or API access."
resource: "https://code.claude.com/docs/en/claude-security"
tags: [security, plugin, scan, multi-agent]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide, desktop]
requires: "Paid plan, Anthropic API access or third-party provider (dynamic workflows); Python 3.9+ as python3; Git for change scans and patches"
identifiers:
  - "/plugin install claude-security@claude-plugins-official"
  - "/plugin marketplace add anthropics/claude-plugins-official"
  - "/plugin marketplace update claude-plugins-official"
  - "claude plugin uninstall claude-security"
  - "/claude-security"
  - "/workflows"
  - "/model"
  - "ANTHROPIC_DEFAULT_SONNET_MODEL"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-security"
    resource: "https://code.claude.com/docs/en/claude-security"
    title: "Scan your codebase for vulnerabilities"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A plugin that runs a multi-agent scan locally in your session. For a whole repository at the default effort, agents map architecture, build a threat model, hunt for vulnerabilities, and independently review every finding before the report. Scope can be the whole repository or only changes (branch diff, PR diff, single commit). Each scan counts toward your usage. The managed Claude Security product (Enterprise plan; also lets you run scans on Claude Mythos) is separate.

# How to use it

Install from the official marketplace: `/plugin install claude-security@claude-plugins-official`, choose a scope. Update through the normal plugin update flow (auto-updates unless turned off). Uninstall from `/plugin` or `claude plugin uninstall claude-security`. If it reports `Run /reload-plugins to apply.`, reload plugins. Errors: `Marketplace "claude-plugins-official" not found` (add the marketplace); `Plugin "claude-security" not found in marketplace "claude-plugins-official"` (update the marketplace catalog).

# Limits and defaults

- Needs the dynamic workflows feature for agent orchestration; on Pro, turn it on via the Dynamic workflows row in `/config`. Progress is visible under `/workflows`.
- The plugin makes no model calls of its own and has no separate key. Hunting, verification and patch agents use your session model (`/model`); a few supporting steps such as repository mapping use the `sonnet` alias. On third-party providers (Bedrock, Google Cloud's Agent Platform, Foundry) the alias may resolve to another version, so pin `ANTHROPIC_DEFAULT_SONNET_MODEL` if needed.
- Runs on Linux, macOS, Windows. A full scan works without version control; change scans and patching need git. `python3` older than 3.9 or missing makes the menu warn.
- On a Fable model, "safeguards flagged this message" notices are expected: the request is re-run on an Opus model via automatic model fallback.

# Notes

The plugin works best in auto mode so agents proceed without a prompt at each step. Scans may take a while, use many tokens, and need Claude Code left open.
