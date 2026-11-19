---
type: "Reference"
title: "Usage policy and safeguard refusals"
description: "Refusals for Usage Policy, cybersecurity safeguards, reasoning extraction and output filtering, and how to recover in a session or -p run."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, refusals, safeguards, usage-policy, recovery]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "/rewind"
  - "/feedback"
  - "--safe-mode"
  - "--continue"
  - "--resume"
  - "reasoning_extraction"
  - "showThinkingSummaries"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Refusals returned by the API rather than failures of Claude Code.

# How to use it

- **Usage Policy refusal:** `API Error: <model> can't help with this. Start a new session to continue.` plus a Request ID and Message ID. The check evaluates the whole conversation, so a new message, `--continue` or `--resume` usually re-triggers it. Recover with Esc twice or `/rewind`, or `/clear` (old conversation stays in `/resume`). In `-p` mode rewind is unavailable: retry with a rephrased prompt in a new session without `--continue`; switching `--model` may help. On Bedrock, Agent Platform and Foundry this message also covers cybersecurity flags. Wording changed at v2.1.219.
- **Safety measures flagged a cybersecurity topic:** `<model>'s safeguards flagged this message`. Apply to the Cyber Verification Program for legitimate work, `/feedback` for false positives. Models with automatic model fallback print a different message (on Opus 5.5 and Sonnet 5.5 it opens `<model>'s safeguards flagged this session`). Earlier wordings: v2.1.219 to v2.1.296, v2.1.203 to v2.1.218, and before v2.1.203.
- **Safeguards flagged a request for Claude's reasoning:** category `reasoning_extraction`, shown as a `Details` line (v2.1.234+). Remove instructions asking Claude to write out its reasoning verbatim or in a fixed format, whether in a prompt, CLAUDE.md, skill, subagent prompt, output style or MCP tool description. Test with `claude --safe-mode`, which starts with customizations disabled. Explanations and action summaries are still fine.
- **Output blocked by content filtering policy:** API output filter stopped generation; rephrase or `/rewind`.

# Notes

Relevant to prompts shared across many unattended agents: one flagged customization can cause repeated refusals in every run that loads it.
