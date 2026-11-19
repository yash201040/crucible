---
type: "Feature"
title: "Auto mode classifier charge notice"
description: "Notice shown when server-side no-charge classifier checks do not reach the session, so Claude Code's own billed classifier requests are used."
resource: "https://code.claude.com/docs/en/auto-mode-classifier-billing"
tags: [auto-mode, classifier, billing, gateway, unattended]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: "Notice never appears on Pro, Max, Ultra or Team plans"
identifiers:
  - "We're changing auto mode to no longer charge for classifier requests in Claude Code. However, this session isn't eligible."
  - "/status"
  - "stream-json"
  - "-p"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "auto-mode-classifier-billing"
    resource: "https://code.claude.com/docs/en/auto-mode-classifier-billing"
    title: "Auto mode classifier request charges"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

In auto mode a classifier checks actions (shell commands, network requests) before they run. Where server-side checks are on, the server does this inside the session's own model requests at no charge. The notice means the server's checks are not reaching the session, so Claude Code makes its own classifier requests, which count toward token usage on your account. Auto mode keeps working and is billed as before.

# How to use it

Interactive: Claude Code holds the first action it would check until you answer.
- **Enter**: continue; the held action and rest of the session use Claude Code's own classifier requests; the notice does not repeat in that session. If the notice named a gateway, acknowledging it suppresses it on this machine for 24 hours; otherwise it returns the next time a session falls back.
- **Esc** or **Ctrl+C**: cancels; the held action does not run and the turn stops, session still in auto mode; nothing remembered, so it reappears before the next checked action.
- To stop using auto mode, switch permission modes with `Shift+Tab` afterwards.

Unattended: where the notice cannot wait for an answer, Claude Code reports the same text and the session continues in auto mode, unless a gateway acknowledgment within the last 24 hours dismissed it. With `-p` the text goes to stderr; in `stream-json` output it is a `system` warning message that Agent SDK applications can read from the message stream.

# Limits and defaults

Check a session with `/status`: the **Auto mode server** row reads `Enabled` while server checks decide the session's actions and `Disabled` once it has fallen back. When a gateway cuts responses short or rewrites results unreadably you get denials with no verdict instead of this notice (see the server-side classifier review and "The server returned no safety verdict" docs).
