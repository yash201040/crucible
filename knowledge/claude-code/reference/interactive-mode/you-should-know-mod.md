---
type: "Feature"
title: "You should know suggestions (built-in mod)"
description: "An off-by-default built-in mod where a side agent flags one thing you may have missed, with its cost and controls."
resource: "https://code.claude.com/docs/en/interactive-mode#you-should-know-suggestions"
tags: [mod, plugin, side-agent, cost]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.287"
surfaces: [cli]
requires: "Direct Claude API connection (claude.ai account or Console API key); not LLM gateway, Claude apps gateway or apiKeyHelper"
identifiers:
  - "/plugin enable cc-plugin-you-should-know@builtin"
  - "/plugin disable cc-plugin-you-should-know@builtin"
  - "CLAUDE_CODE_YOU_SHOULD_KNOW_DEBUG"
  - "cleanupPeriodDays"
  - "~/.claude/plugins/store/"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "interactive-mode"
    resource: "https://code.claude.com/docs/en/interactive-mode"
    title: "Interactive mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A built-in mod (a plugin built into Claude Code) that is off by default. While on, a side agent rereads the conversation periodically and may show a short note above the prompt. The side agent is a separate request to the same model with no tools; the main agent only sees a note if you send it with **Chat in main session**.

# How to use it

Enable with `/plugin enable cc-plugin-you-should-know@builtin`; disable with `/plugin disable cc-plugin-you-should-know@builtin`, from the **Installed** tab of `/plugin`, or **Turn off suggestions** on the `Dismissed.` line (clears after 20 seconds). Answer by typing the digit on an empty prompt: Learn more (Understood, Chat in main session, Dismiss), Knew this already, Dismiss. Set `CLAUDE_CODE_YOU_SHOULD_KNOW_DEBUG=1` to watch checks.

# Limits and defaults

Not listed in sessions that skip feature flags (e.g. `DISABLE_TELEMETRY` set) or in a first session after install or upgrade. Each check is billed as a background request: conversation read from prompt cache, but the several thousand tokens of instructions and the reply are billed in full each time. Recent notes and known topics are kept in a file starting `cc-plugin-you-should-know` under `~/.claude/plugins/store/`, deleted after `cleanupPeriodDays` without use.
