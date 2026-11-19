---
type: "Feature"
title: "Handle custom tool errors"
description: "A handler error does not stop the agent loop; return isError true to control the message Claude reads."
resource: "https://code.claude.com/docs/en/agent-sdk/custom-tools"
tags: [errors, custom-tools, iserror, agent-loop]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "isError"
  - "is_error"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-custom-tools"
    resource: "https://code.claude.com/docs/en/agent-sdk/custom-tools"
    title: "Give Claude custom tools"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The in-process MCP server catches uncaught exceptions and returns them as error results, so the query does not fail.

# How to use it

| What happens | Result |
| --- | --- |
| Handler throws | Converted to an error result with the raw exception message; Claude sees it and the loop continues |
| Handler returns `isError: true` (TS) / `"is_error": True` (Python) | Claude sees the message you compose, with added context |

In both cases Claude can retry, try another tool, or explain. Catch non-200 HTTP statuses and network or JSON errors yourself when the raw message is not enough. The converter example also returns `isError` for an unsupported conversion.
