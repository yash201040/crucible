---
type: "Feature"
title: "Cloud sessions, Remote Control and Dispatch in Desktop"
description: "Send work to the cloud, continue sessions elsewhere, expose local sessions to other devices, and receive Dispatch-started sessions."
resource: "https://code.claude.com/docs/en/desktop"
tags: [desktop, cloud, remote-control, dispatch, handoff]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [desktop, cloud, mobile]
requires: "Dispatch needs Pro, Max or Ultra (not Team or Enterprise)"
identifiers:
  - "remoteControlAtStartup"
  - "disableRemoteControl"
  - "/remote-control"
  - "Connect new sessions to Remote Control"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "desktop"
    resource: "https://code.claude.com/docs/en/desktop"
    title: "Desktop application"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

- **Cloud sessions**: pick a Cloud environment; runs on Anthropic-managed infrastructure by default, continues if you close the app or shut down; supports several repositories; usage counts toward plan limits with no separate compute charge. Monitor from claude.ai/code or the mobile app. Projects coordinate many cloud sessions.
- **Continue in another surface**: session menu > **Open in** > Cloud moves the conversation as a summary (not possible for SSH or WSL sessions), or opens the folder in an editor.
- **Remote Control**: a local session shows on other devices (claude.ai/code, Claude apps) once connected, via the session's **Remote Control** switch, `/remote-control`, or automatically when **Connect new sessions to Remote Control** is on.
- **Dispatch**: a persistent conversation in Cowork; it can spawn a Code session (explicit request, or for bug fixes, dependency updates, tests, PRs). Push notification when it finishes or needs approval.

# How to use it

Turn Remote Control off: per session (switch), per computer (Settings toggle; toggle on then off to save), any session incl. CLI (`disableRemoteControl: true` in `~/.claude/settings.json`), or managed (`remoteControlAtStartup: false` in highest-ranked MDM or managed file; needs v4.4212.0+). Admin console has Desktop, Cloud sessions and Remote Control toggles.

# Limits and defaults

Computer-use approvals in Dispatch-spawned sessions expire after 30 minutes. In HIPAA Enterprise orgs Desktop, Cloud sessions and Remote Control are off by default and Owners cannot turn the latter two on once the HIPAA configuration is applied.
