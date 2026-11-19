---
type: "Feature"
title: "Python query() and ClaudeSDKClient"
description: "The two Python entry points: one-shot query() and the session-keeping ClaudeSDKClient with interrupt, model and MCP controls."
resource: "https://code.claude.com/docs/en/agent-sdk/python"
tags: [python, sdk, query, client, sessions]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: "pip install claude-agent-sdk (Python)"
identifiers:
  - "claude-agent-sdk"
  - "query()"
  - "ClaudeSDKClient"
  - "connect"
  - "receive_messages"
  - "receive_response"
  - "interrupt"
  - "set_permission_mode"
  - "set_model"
  - "rewind_files"
  - "get_mcp_status"
  - "get_context_usage"
  - "reconnect_mcp_server"
  - "toggle_mcp_server"
  - "stop_task"
  - "get_server_info"
  - "disconnect"
  - "Transport"
  - "continue_conversation"
  - "resume"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-python"
    resource: "https://code.claude.com/docs/en/agent-sdk/python"
    title: "Agent SDK reference - Python"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The Python Agent SDK drives Claude Code from Python. `query()` is an async function that starts a new session per call by default and yields messages. `ClaudeSDKClient` keeps one session across several exchanges. Install into a virtual environment (`pip install claude-agent-sdk`); on recent Debian, Ubuntu and Homebrew system Python, plain `pip install` fails with `externally-managed-environment`.

# How to use it

| Feature | `query()` | `ClaudeSDKClient` |
| :- | :- | :- |
| Session | new by default | same session reused |
| Conversation | single exchange | multiple exchanges in one context |
| Connection | automatic | manual |
| Interrupts | not supported | supported |
| Hooks, custom tools, streaming input | supported | supported |
| Continue chat | manual via `continue_conversation` or `resume` | automatic |

`query(*, prompt: str | AsyncIterable[dict], options: ClaudeAgentOptions | None, transport: Transport | None) -> AsyncIterator[Message]`.

`ClaudeSDKClient(options, transport)` methods:

| Method | What it does |
| :- | :- |
| `connect(prompt=None)` | connect, optional initial prompt or stream |
| `query(prompt, session_id="default")` | send a request in streaming mode |
| `receive_messages()` | all messages |
| `receive_response()` | messages up to and including a `ResultMessage` |
| `interrupt()` | stop signal, streaming mode only |
| `set_permission_mode(mode)` | change mode mid-session |
| `set_model(model=None)` | change model; `None` resets to default; an `auto` mode session drops to `default` if the new model does not support auto |
| `rewind_files(user_message_id)` | restore files; needs `enable_file_checkpointing=True` |
| `get_mcp_status()` | status of all MCP servers |
| `get_context_usage()` | context breakdown (same data as `/context`) |
| `reconnect_mcp_server(name)` | retry a failed server |
| `toggle_mcp_server(name, enabled)` | enable or disable mid-session; disabling a stdio, SSE or HTTP server removes its tools |
| `stop_task(task_id)` | stop a background task; a `TaskNotificationMessage` with status `"stopped"` follows |
| `get_server_info()` | init info incl. commands and output styles |
| `disconnect()` | close |

Usable as `async with ClaudeSDKClient() as client:`. A streamed prompt (async iterable of user message dicts) starts being answered on the first yielded message; pair each `query()` with its own `receive_response()` loop.

# Limits and defaults

- Avoid `break` when iterating messages: it can cause asyncio cleanup issues.
- `interrupt()` does not clear the buffer. Drain the interrupted turn (its `ResultMessage` has `terminal_reason` `"aborted_streaming"` or `"aborted_tools"`) with `receive_response()` before reading the next query's response.
- `get_context_usage()` triggers several token-counting API requests that do not appear in the message stream (not billed on the Anthropic API).
- `Transport` (abstract class: `connect`, `write`, `read_messages`, `close`, `is_ready`, `end_input`) is a low-level internal API that may change between releases.
