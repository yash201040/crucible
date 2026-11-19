---
type: "Concept"
title: "Single-shot versus streaming input"
description: "Single-shot query() takes one prompt string and ends; streaming input keeps a session open for several messages, images, interrupts and mid-session changes."
resource: "https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode"
tags: [agent-sdk, streaming-input, query, sessions]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "query()"
  - "ClaudeSDKClient"
  - "SDKUserMessage"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-streaming-vs-single-mode"
    resource: "https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode"
    title: "Send messages to a running agent"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two ways to feed a prompt to an Agent SDK session. A single-shot call passes one prompt string to `query()` and the call ends after Claude answers. Streaming input keeps the session open so the application can send more than one message while it runs.

# How to use it

- Choose streaming input for a chat-style application, to attach images, to interrupt a response, or to switch the model or permission mode while the session runs (see the SDK configuration page, "change configuration mid-session").
- Choose single-shot for a single task, such as a serverless function.
- To follow up after a single-shot call has ended, start a new call that resumes the session (continue, resume and fork on the sessions page).

# Notes

Streaming input covers the messages you send. Showing Claude's response as it is generated is a separate feature, "Stream responses in real-time".
