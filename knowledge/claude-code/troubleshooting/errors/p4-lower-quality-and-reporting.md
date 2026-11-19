---
type: "Guide"
title: "Responses seem lower quality, and reporting an error"
description: "Checks when answers degrade with no error (model fallback, effort, context, stale memory, injection warnings) and where to report errors."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, quality, model-fallback, effort, context]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.205"
surfaces: [cli]
requires: ""
identifiers:
  - "--fallback-model"
  - "/model"
  - "/effort"
  - "/context"
  - "/compact"
  - "/clear"
  - "/rewind"
  - "/doctor"
  - "/feedback"
  - "ANTHROPIC_MODEL"
  - "claude doctor"
  - "ultrathink"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Guidance for quality drops with no error shown, which the docs say usually come from conversation state rather than the model. Claude Code does not silently change model versions.

# How to use it

Model fallbacks that can happen:
- A configured `--fallback-model` takes over after an availability error for that turn only, with a transcript notice.
- An Amazon Bedrock or Google Cloud Agent Platform startup check finds the default model unavailable, or the account loses access mid-session.
- Automatic model fallback on Fable models, Opus 5.5, Sonnet 5.5 and Opus 5 moves the session to the flagged category's fallback model when one exists, with a transcript notice.

Checks, in order:
- `/model`: confirm the model; a previous choice or `ANTHROPIC_MODEL` may select a smaller one.
- `/effort`: check reasoning level; defaults vary by model; `ultrathink` shortcut.
- `/context`: see window use; `/compact` at a breakpoint or `/clear`.
- Stale instructions: oversized `CLAUDE.md` and MCP tool definitions use context; `/doctor` flags oversized memory files and unused extensions (before v2.1.205 it opened a diagnostics screen).
- Prefer rewinding (Esc twice or `/rewind`) over correcting in-thread, since a wrong attempt left in context can anchor later answers.
- `/feedback` sends the transcript with a description.
- A suspected prompt-injection warning about context Claude Code itself adds: run `claude update` and retry; report if it repeats. Before v2.1.201 Sonnet 5 refused some requests this way.

Reporting: `/feedback` (also offers a prefilled GitHub issue; needs authentication, and on Bedrock, Google Cloud Agent Platform, Microsoft Foundry or other third-party providers, or with no Anthropic credentials, saves a local archive to send to an account representative). Also `claude doctor` (read-only diagnostic), `/doctor`, status.claude.com, and GitHub issues. Component guides: MCP failures in the MCP docs, hooks in Debug hooks, install problems in Troubleshoot installation and login.

# Notes

If `/feedback` is disabled by policy see [command-specific refusals](./p3-command-specific-errors.md).
