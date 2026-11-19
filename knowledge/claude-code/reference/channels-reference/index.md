# reference/channels-reference

* [Channel contract overview and requirements](channel-overview-and-requirements.md) - A channel is a local MCP server that pushes events into a session over stdio; what it must declare and emit. **[high]**
* [Expose a reply tool (two-way channels)](expose-a-reply-tool.md) - A two-way channel declares tools, registers a standard MCP reply tool and tells Claude via instructions how to route replies.
* [Gate inbound messages by sender](gate-inbound-messages.md) - An ungated channel is a prompt-injection vector; gate on sender identity, not room, before emitting a notification. **[high]**
* [Channel notification format and delivery](notification-format.md) - notifications/claude/channel params (content, meta), the resulting channel tag, and how events are queued without acknowledgement. **[high]**
* [Package a channel as a plugin](package-as-plugin.md) - Distribute a channel as a plugin enabled per session with --channels; allowlist rules for the official marketplace and org lists.
* [Permission relay for channels](permission-relay.md) - A two-way channel can receive tool-approval prompts, sanitized and credential-masked, and return allow or deny verdicts by request ID. **[high]**
* [Channel Server constructor options](server-options.md) - MCP Server constructor fields that make a server a channel: claude/channel, claude/channel/permission, tools and instructions.
* [Testing channels with --dangerously-load-development-channels](test-with-development-flag.md) - During the research preview custom channels bypass the allowlist only through a per-entry development flag that needs an interactive session. **[high]**
* [Example: build a webhook receiver channel](webhook-receiver-example.md) - Walkthrough of a one-file Bun channel that forwards HTTP POSTs on port 8788 into a session, with registration and troubleshooting.
