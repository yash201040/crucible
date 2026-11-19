# agent-sdk/agent-sdk-troubleshooting

* [CLINotFoundError and missing native binary](cli-not-found-errors.md) - Errors when the SDK cannot find the Claude Code executable in Python or TypeScript, with fixes.
* [ProcessError, ResultError and process-exit errors](cli-process-exit-errors.md) - What Python and TypeScript raise when the Claude Code process exits nonzero or reports an error result. **[high]**
* [Failed to start Claude Code and Not connected](launch-failure-and-not-connected.md) - Launch-failure messages in Python and TypeScript, and the ClaudeSDKClient Not connected error.
* [Python max_buffer_size JSON decode error](max-buffer-size-json-error.md) - CLIJSONDecodeError when one CLI message exceeds max_buffer_size (default 1,048,576), and how to recover the work. **[high]**
* [Streaming input errors and image blocks](streaming-input-errors.md) - Abort errors, the silent Python prompt-stream failure, and the note Claude gets for an image block with no source.
* [structured_output missing despite success](structured-output-none.md) - A result with subtype success can carry no structured_output; treat as failure and check for refusal or an unsatisfiable schema. **[high]**
* [SDK symptom to page routing](symptom-routing-table.md) - Maps Agent SDK symptoms and error strings to the troubleshooting section that covers them.
* [Refusal to run .bat or .cmd CLI on Windows](windows-batch-script-refusal.md) - The Python SDK refuses a batch-script CLI path on Windows for security; use a native claude.exe.
