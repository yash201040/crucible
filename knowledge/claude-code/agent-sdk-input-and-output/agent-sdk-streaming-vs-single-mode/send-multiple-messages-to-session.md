---
type: "Guide"
title: "Send more than one message to a session"
description: "How to send several messages, including images, to one SDK session in TypeScript (async generator) and Python (ClaudeSDKClient), and how queued messages are read."
resource: "https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode"
tags: [agent-sdk, streaming-input, images, async-generator]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "SDKUserMessage"
  - "ClaudeSDKClient"
  - "client.query()"
  - "receive_response()"
  - "parent_tool_use_id"
  - "priority"
  - "pushMessage()"
  - "closeInput()"
  - "userMessages()"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-streaming-vs-single-mode"
    resource: "https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode"
    title: "Send messages to a running agent"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A session can receive many user messages. TypeScript passes an async generator of `SDKUserMessage` objects as the `prompt` of `query()`. Python opens a `ClaudeSDKClient` and calls `client.query()` per message.

# How to use it

| Language | Text message | Image message |
| - | - | - |
| TypeScript | generator yields `{ type: "user", message: { role: "user", content }, parent_tool_use_id: null }`; the generator waits between yields for the next user message | `content` is an array of `{type:"text"}` and `{type:"image", source:{type:"base64", media_type:"image/png", data}}` blocks |
| Python | `client.query("text")` | pass an async generator that yields user message dicts with the same content blocks |

To get one separate response per message, wait for the previous response's result message before sending the next. TypeScript: the generator awaits a promise that the `for await` loop resolves on the result message. Python: call `client.query()` again after the `receive_response()` loop ends.

A chat-interface pattern for TypeScript keeps a `pending` array: `pushMessage()` (called per user message), `closeInput()` (called when the user closes the chat) and a `userMessages()` generator that waits when the array is empty and returns when closed.

# Limits and defaults

- A message sent during tool calls reaches Claude after those tool calls finish. Claude answers it and the earlier message in one response; if the turn ends first, Claude starts a new turn for it (see agent-loop "Turns and budget").
- Messages pushed during a response can share one response. The `priority` field of `SDKUserMessage` chooses when Claude reads a message pushed during a response.

# Notes

If Claude did not see an image, the docs point to the troubleshooting entry "Image could not be processed".
