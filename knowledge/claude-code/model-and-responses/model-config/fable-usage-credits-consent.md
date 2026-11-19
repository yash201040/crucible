---
type: "Feature"
title: "Fable usage credits and consent prompt"
description: "Fable usage can bill to usage credits; interactive sessions show a consent prompt, unattended sessions hold it for dialogExpiry or bill without asking."
resource: "https://code.claude.com/docs/en/model-config#fable-and-usage-credits"
tags: [fable, usage-credits, consent, unattended]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: "Remote Control answer from device needs v2.1.323+"
identifiers:
  - "dialogExpiry"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Depending on plan and seat tier, Fable usage bills to usage credits instead of the plan's included limits; the `/model` picker then shows "Requires usage credits" on the Fable row. Interactive sessions can show a consent prompt: continue on Fable with usage credits, or switch to the default model. After choosing to continue, it is not shown again.

# How to use it

Dismissing the prompt: when selecting Fable with `/model`, you keep the current model; mid-session, the turn continues on the default model.

Sessions where nobody may be at the terminal (Remote Control connected, a background session, an agent team teammate): the mid-session prompt is held for the `dialogExpiry` deadline (five minutes by default). If unanswered, the turn ends without sending the request, a transcript notice is added, the model selection is unchanged, and consent is asked again on the next message.

- Remote Control or teammate session: press any key at the terminal to cancel the deadline and wait.
- Remote Control in an interactive terminal: also answer on the connected device (lasts that session).
- Background session: answer before the deadline.
- A new message from the remote client before anyone typed at the terminal ends the turn the same way; after someone types, the message queues behind the prompt.

# Limits and defaults

- Agent SDK host application: whether the prompt shows is up to the host; if shown and unanswered by `dialogExpiry`, the turn ends without sending.
- Non-interactive `-p` mode, and an SDK app that does not show the prompt: Claude Code never asks and bills Fable requests to usage credits without asking.
