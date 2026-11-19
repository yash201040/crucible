---
type: "Feature"
title: "Organization effort limits"
description: "Caps on effort level per model and role (Enterprise) or via the maxEffortLevel managed setting on any plan or provider."
resource: "https://code.claude.com/docs/en/model-config#organization-effort-limits"
tags: [effort, limits, enterprise, managed-settings]
kind: "setting"
maturity: "unlabelled"
since: "2.1.195"
surfaces: [cli, headless]
requires: "Per-role limits need Claude Enterprise and Claude Code v2.1.195+; maxEffortLevel works on any plan and provider"
identifiers:
  - "maxEffortLevel"
  - "--effort"
  - "/effort"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An organization can cap effort level two ways: per-role maximum per model set by Enterprise admins (delivered with model restrictions and reaching the same sessions), and the `maxEffortLevel` managed setting that caps on the client for any plan or provider (Bedrock, Agent Platform, Foundry). When both apply to a model the lower cap wins.

# How to use it

- Levels above the cap are not offered in the `/effort` picker; naming a higher level with `--effort` or `/effort` runs at the cap.
- A plain-text `--print` run with `--effort` above the cap prints a warning on stderr naming requested and applied levels. In interactive sessions, with `json` or `stream-json` output, or in background agents, the warning goes to the debug log.
- Caps are per model, so switching models can change available levels.
- When several roles grant the same model, the least restrictive cap applies.

# Notes

To keep users at or below a level in managed settings, use `maxEffortLevel`; a managed `effortLevel` is just a default that `/effort` or `--effort` can change.
