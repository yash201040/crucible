---
type: "Feature"
title: "Monitor tool"
description: "Runs a background command and streams each output line to Claude as an event, with deadlines and permission rules shared with Bash."
resource: "https://code.claude.com/docs/en/tools-reference#monitor-tool"
tags: [monitor, background, events, deadline, plugins]
kind: "tool"
maturity: "unlabelled"
since: "2.1.310"
surfaces: [cli, headless]
requires: "Windows needs Git Bash; v2.1.310+ on cloud providers or with telemetry/nonessential traffic disabled"
identifiers:
  - "Monitor"
  - "timeout_ms"
  - "TaskStop"
  - "DISABLE_TELEMETRY"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude watches something in the background (tail a log, poll a PR or CI job, watch a directory, track script output, a WebSocket feed) and reacts when events arrive, without pausing the conversation. Usually Claude writes a small script and each output line is an event.

# How to use it

- Every watch has a deadline: 5 minutes by default, at most 30 minutes, and at most 10 minutes in a non-interactive `-p` run given a single prompt. At the deadline the watch ends and Claude gets one notice, so it can restart it.
- Stop by asking Claude to cancel, ending the session, or `TaskStop`. Stopping a subagent that started monitors (for example from `/tasks`) stops those monitors.
- Permissions follow Bash rules (`allow`/`deny` patterns for Bash apply). In auto mode, allow rules naming `Monitor` itself are set aside so the classifier reviews Monitor commands as it does Bash.
- Plugins can declare monitors that start automatically when active.
- Minimum version: on Amazon Bedrock, Claude Platform on AWS, Google Cloud Agent Platform or Microsoft Foundry, or with `DISABLE_TELEMETRY` or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` set (feature-flag fetching off), Monitor needs v2.1.310+. Windows needs Git Bash.

# Notes

WebSocket watches are covered in [Monitor WebSocket source](./monitor-websocket-source.md). Monitor commands count toward the [tool memory cap](./tool-memory-limit-linux.md).
