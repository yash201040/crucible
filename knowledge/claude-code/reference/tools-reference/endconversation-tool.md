---
type: "Feature"
title: "EndConversation tool"
description: "A tool that ends an interactive session in rare abuse cases; exempt from permission rules and hooks, and absent in headless and SDK runs."
resource: "https://code.claude.com/docs/en/tools-reference#endconversation-tool-behavior"
tags: [endconversation, session, safeguard, surfaces]
kind: "tool"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Claude Opus 4.8, Claude Sonnet 5, Claude Fable 5 or later of those families; Claude API (not cloud providers)"
identifiers:
  - "EndConversation"
  - "--bare"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude uses it only after repeated abusive messages following a clear warning, or when you ask to end the session and confirm. Frustration, profanity or a failing task do not qualify.

# How to use it

After it fires, the session locks: new prompts return `Claude ended this conversation. Start a new session (or /clear) to continue.` and only `/clear`, `/resume`, `/help`, `/exit`, `/feedback` run. The end is recorded in the transcript, so resume restores the lock. Resuming an ended session with `-p` errors and exits with code 1.

# Limits and defaults

- Never prompts for permission and PreToolUse hooks do not run. Deny and ask rules naming it have no effect, and `--disallowedTools` or a `--tools` list cannot remove it while another tool remains. If deny rules remove every other tool and match it (as `"*"` does), it is removed too, unless an allow rule names it.
- Subagents never get it; background tasks sharing the main tool list see it but calling it ends nothing.
- Appears only in interactive terminal sessions (including IDE integrated terminal and JetBrains plugin). Absent in `-p` runs, Agent SDK sessions, the VS Code extension panel, GitHub Actions, cloud sessions, `--bare` sessions, Amazon Bedrock, Claude Platform on AWS, Google Cloud Agent Platform, Microsoft Foundry and cloud gateway sessions.
