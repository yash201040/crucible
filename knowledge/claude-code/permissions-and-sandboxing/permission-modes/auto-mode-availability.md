---
type: "Concept"
title: "Auto mode and its requirements"
description: "What auto mode is, supported plans, providers and models, how to disable it, and why it may be unavailable."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [auto-mode, classifier, availability, models, managed-settings]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.283"
surfaces: [cli, ide, desktop, headless, sdk]
requires: "Supported model and provider; not disabled by settings or Anthropic"
identifiers:
  - "auto"
  - "permissions.disableAutoMode"
  - "disableAutoMode"
  - "claude auto-mode defaults"
  - "defaultMode"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Auto mode lets Claude run without routine prompts. A separate classifier model reviews actions before they run, blocking anything that escalates beyond the request, targets unrecognized infrastructure, or seems driven by hostile content Claude read. Explicit ask rules still force a prompt. It also nudges Claude to keep working without clarifying questions (Claude still asks when the prompt or a skill relies on it). The Proactive output style is the alternative for stronger autonomy in a prompting mode. The docs warn it reduces prompts but does not guarantee safety.

# How to use it

`claude --permission-mode auto`; or cycle with `Shift+Tab`. Administrators remove it with `permissions.disableAutoMode` = `"disable"` in managed settings: `auto` leaves the `Shift+Tab` cycle, a `--permission-mode auto` session starts Manual, and a running auto session leaves auto (message `auto mode disabled by settings`) when the setting arrives from an admin-deployed source (before v2.1.251 a running session kept auto).

# Limits and defaults

- Plans: all plans. Team and Enterprise: available by default.
- Anthropic API, Claude Platform on AWS, Claude Models on Google Cloud (Anthropic managed): Claude Opus 4.6 or later, Sonnet 4.6 or later, Haiku 5.5, or a Fable model.
- Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, signed-in Claude apps gateway: only Sonnet 5 or later, Opus 4.7 or later, Haiku 5.5, Fable models. Haiku 5.5 there needs v2.1.293+. Other models start the session Manual.
- Not supported on any provider: Sonnet 4.5, Opus 4.5, Haiku 4.5, claude-3 models.
- From v2.1.283 auto is the built-in start mode for interactive terminal/VS Code on every plan and provider; earlier only Pro, Max, Ultra, Team.
- If unavailable, check requirements and `disableAutoMode`; Anthropic may have turned it off server-side or rejected it for the account. Such an answer keeps auto off until the session ends.
- On Bedrock, Agent Platform, Foundry and gateway: interactive sessions start in auto; `-p`/SDK start `default`. Use `--permission-mode auto`, `permissionMode: "auto"` or `permission_mode="auto"`.
- A message naming a model and saying auto mode "cannot determine the safety" of an action means a classifier request failed (usually transient; on Bedrock it can repeat until the account can invoke the model). See the errors reference.
- `claude auto-mode defaults` prints the built-in rule lists as JSON.
