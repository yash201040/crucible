# agent-sdk-input-and-output/agent-sdk-streaming-output

* [Enable partial message streaming](enable-partial-message-streaming.md) - Set includePartialMessages / include_partial_messages to receive StreamEvent messages with raw API deltas as text and tool calls are generated.
* [Message flow and cut-off streams](message-flow-and-cut-off-streams.md) - Order of StreamEvent and AssistantMessage messages, and what to expect when a stream is interrupted, dropped or falls back to non-streaming.
* [Stream tool calls and build a streaming UI](stream-tool-calls-and-ui.md) - Track tool_use blocks and accumulate input_json_delta chunks, using an in_tool flag to show progress in a chat UI.
* [StreamEvent reference](streamevent-reference.md) - Type names per SDK, the raw event types, and caveats such as no subagent deltas and parent_tool_use_id always empty.
