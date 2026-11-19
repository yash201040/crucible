---
type: "Concept"
title: "What connected devices can do and see"
description: "How a device connected over Remote Control sees compaction, model and effort changes, forks, diffs, background tasks and push notifications."
resource: "https://code.claude.com/docs/en/remote-control"
tags: [remote-control, mobile, fork, push-notifications, models]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.238"
surfaces: [cli, web, mobile]
requires: ""
identifiers:
  - "/model"
  - "/effort"
  - "/autocompact"
  - "/advisor"
  - "/output-style"
  - "/focus"
  - "CLAUDE_CODE_EFFORT_LEVEL"
  - "CLAUDE_CLIENT_PRESENCE_FILE"
  - "dialogExpiry"
  - "claude mcp login"
  - "--no-browser"
  - "/mcp reconnect"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "remote-control"
    resource: "https://code.claude.com/docs/en/remote-control"
    title: "Continue local sessions from any device with Remote Control"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A connected device mirrors the terminal conversation and can steer it. Behaviors the page lists:

- Subagents and workflows already running in the background appear on connect; stopping one from the device stops it on the machine.
- Compaction progress and `/clear` are shown on devices. `/resume` or `/teleport` disconnects Remote Control if the session has a share link (check needs v2.1.324+); otherwise new messages go to whichever conversation is open in the terminal but earlier history is not sent.
- Cross-session messaging uses the same connection.
- Diff pane in a git repo: changes since the branch split from the default branch (incl. uncommitted), or only uncommitted on the default branch.
- Model picked from a device runs the session on it (v2.1.238+); `/model <name>` sent to an interactive session also sets the default for new sessions. Effort from a device applies locally (control needs v2.1.234+); `CLAUDE_CODE_EFFORT_LEVEL` pins the level.
- Fork: in claude.ai/code choose Fork in the session menu or from an earlier message (needs v2.1.277+ locally). Declined if the session is busy or hosted by VS Code or another Agent SDK app.
- Session title order: `--name`/argument, `/rename`, last meaningful message, auto-generated name.

# How to use it

Commands that work from mobile/web: text-output commands `/compact`, `/clear`, `/context`, `/usage`, `/exit`, `/usage-credits`, `/recap`, `/reload-plugins` (interactive terminal sessions only); `/model`, `/effort`, `/fast`, `/color`, `/rename` (value as argument); `/mcp` (text summary on mobile; directory of connectors on web; `reconnect`, `enable`, `disable` need an interactive terminal session); `/config key=value` on mobile; `/autocompact 500k` (from v2.1.221); `/advisor opus|off` (v2.1.260); `/output-style <name>` (built-in styles only, v2.1.269); `/focus on|off` (v2.1.281). Commands like `/plugin` and `/resume` are local-only; `/claude-api` is unavailable from mobile/web.

Re-authorize a claude.ai connector from a shell: `claude mcp login "claude.ai Slack" --no-browser`, open the printed link, then `/mcp reconnect claude.ai Slack` in the running session (or start a new session). A `!` line sent from mobile/web is a message, not shell mode.

Push notifications: install the Claude app, sign in with the same account, allow notifications, then `/config` and enable "Push when Claude decides" and/or "Push when actions required". No other per-event configuration. Set `CLAUDE_CLIENT_PRESENCE_FILE` to a marker file path to suppress pushes while the file exists.

# Limits and defaults

- Forwarded dialogs other than permission prompts and `AskUserQuestion` expire after five minutes by default (then the no-action default applies); adjust or disable with `dialogExpiry` (v2.1.224+). An unanswered Fable usage-credits prompt ends the turn (v2.1.323+).
- Attachments that fail to download add a note like `[1 of 3 attachments did not arrive]`.
- Team/Enterprise members without billing access cannot send a usage-credits request from mobile/web.
