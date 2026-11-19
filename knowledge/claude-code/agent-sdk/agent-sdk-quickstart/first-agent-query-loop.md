---
type: "Guide"
title: "First agent with query()"
description: "The minimal agentic loop: query() streams messages while Claude reads, edits and runs tools, driven by prompt and options."
resource: "https://code.claude.com/docs/en/agent-sdk/quickstart"
tags: [query, agent-loop, streaming, options]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "query"
  - "ClaudeAgentOptions"
  - "allowedTools"
  - "allowed_tools"
  - "permissionMode"
  - "permission_mode"
  - "systemPrompt"
  - "system_prompt"
  - "mcpServers"
  - "AssistantMessage"
  - "ResultMessage"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-quickstart"
    resource: "https://code.claude.com/docs/en/agent-sdk/quickstart"
    title: "Quickstart"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`query()` is the main entry point. It returns an async iterator, so you loop with `async for` (Python) or `for await` (TypeScript) and receive one message per step: Claude's reasoning, a tool call, a tool result, or the final result. The SDK handles orchestration, tool execution, context management and retries. The loop ends when Claude finishes or errors.

# How to use it

```
query(prompt="...", options=ClaudeAgentOptions(allowed_tools=["Read","Edit","Glob"], permission_mode="acceptEdits"))
```

TypeScript uses `query({ prompt, options: { allowedTools, permissionMode } })`. Python imports `query, ClaudeAgentOptions, AssistantMessage, ResultMessage` from `claude_agent_sdk`; TypeScript imports `query` from `@anthropic-ai/claude-agent-sdk`.

Filter messages for readable output: assistant messages hold text blocks and tool-call blocks (`name`); the result message (`ResultMessage` / `type === "result"`) has a `subtype` such as `success`. Unfiltered streams include system initialization and internal state. Other option examples: add `WebSearch` or `Bash` to `allowedTools`, pass `systemPrompt`, `mcpServers`. If you do not need live output, collect messages and read them after the loop.

# Notes

Single-shot `query()` versus streaming input is explained in the streaming-vs-single-mode page. An example prompt with Bash enabled: write unit tests, run them, fix failures.
