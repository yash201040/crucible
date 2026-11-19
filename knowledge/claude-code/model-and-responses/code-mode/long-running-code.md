---
type: "Limit"
title: "Code Mode long-running and background code"
description: "Code waits up to ten minutes by default; in auto or bypassPermissions mode it can run in the background for up to two hours."
resource: "https://code.claude.com/docs/en/code-mode"
tags: [code-mode, background, timeouts, permission-modes]
kind: "limit"
maturity: "experimental"
since: "2.1.328"
surfaces: [cli]
requires: "Code Mode on; auto or bypassPermissions mode for background code"
identifiers:
  - "--permission-mode auto"
  - "bypassPermissions"
  - "acceptEdits"
  - "--tools"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-mode"
    resource: "https://code.claude.com/docs/en/code-mode"
    title: "Run tool calls from code with Code Mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

While code runs a long build or test, Claude either waits or lets it continue in the background.

# Limits and defaults

- **Waiting**: Claude answers after the code finishes; the code stops after ten minutes. In Manual and `acceptEdits` modes, time at a tool permission prompt does not count (before v2.1.328 it did).
- **Background**: you can keep talking to Claude; the code can run up to two hours.

# How to use it

Start the session in auto or `bypassPermissions` mode for background code. If Claude still waits:
- You switched modes: press `Shift+Tab` back to the starting mode.
- You started in another mode: if auto mode is available, exit and run `claude --continue --permission-mode auto` with Code Mode on.
- Version before v2.1.328 and picked from the `claude --resume` list: update, then rerun the same `claude --resume` with Code Mode on (or use `--continue` to stay on your version).
- You passed tool names to `--tools`: restart in auto mode without that flag.

When new code starts in auto mode while earlier code still runs, the earlier code loses classifier review and Claude Code asks about its remaining calls that would need review. With no IDE connected the prompt counts down (`Claude Code will automatically block this request in 1:59, to avoid holding up an unattended session`). If unanswered, that call is refused and later countdown-worthy calls are refused without a prompt until you send Claude a message.
