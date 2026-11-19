---
type: "Feature"
title: "Wait for a usage limit to reset (auto-continue)"
description: "Claude Code waits in the open session when a claude.ai usage limit hits and continues the task after reset."
resource: "https://code.claude.com/docs/en/interactive-mode#wait-for-a-usage-limit-to-reset"
tags: [usage-limit, auto-continue, unattended, subscription]
kind: "setting"
maturity: "unlabelled"
since: "2.1.234"
surfaces: [cli]
requires: "Interactive session signed in with a claude.ai subscription"
identifiers:
  - "autoContinueAtUsageLimit"
  - "/rate-limit-options"
  - "/usage-credits"
  - "/config autoContinueAtUsageLimit=false"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "interactive-mode"
    resource: "https://code.claude.com/docs/en/interactive-mode"
    title: "Interactive mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

On by default in interactive sessions with a claude.ai subscription. Footer lines show the reset time and when Claude will continue. At reset, Claude Code prompts Claude to pick the task up where it stopped (the last message is not resent). Permissions are still asked, so an unattended task can stop on a prompt.

# How to use it

- After a computer sleep over about 30 minutes that spans the reset, you must press `Enter` to continue.
- Early continue: adding credits with `/usage-credits`, signing back in after `/upgrade`, or switching model with `/model` triggers a check. Under `opusplan` and similar settings that run plan mode on another model, it waits for reset.
- Cancel: `Esc` at an empty prompt, `Ctrl+C`, or `/rate-limit-options` then **Don't continue automatically**. Sending a prompt ends the wait.
- Start one manually: pick **Wait here, then continue automatically** in `/rate-limit-options` (the menu opens once per reset window).
- Turn off: `/config` **Continue automatically at usage limit**, or `autoContinueAtUsageLimit` to `false` in user settings. `/config autoContinueAtUsageLimit=false` works also with `-p` but the `key=value` form cannot turn it back on, because the setting grants unattended execution.

# Limits and defaults

- Stops after three automatic continuations (notification `Automatic continue stopped after repeated usage-limit hits`); the count resets on a new prompt or menu pick. Also stops after three continuations for a `/goal` or session-scoped scheduled task spanning reset windows.
- The wait ends without continuing if you exit (it does not restart on resume), change accounts, clear, rewind, `/resume`, `/teleport`, relaunch via `/tui` or `/restart`, move to Desktop, background or cloud, if the reset is over 24 hours away, or if a `UserPromptSubmit` hook blocks the continuation prompt.
- Not started on its own for Remote Control and agent team teammate sessions, resets over 24 hours away, or an Opus/Sonnet limit while on another family. Not offered at all in background sessions and `-p` runs, with API keys, cloud providers or usage-based billing, or an LLM gateway without a saved claude.ai login.
