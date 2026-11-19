# agents-and-parallel-work/cross-session-messaging

* [Messaging sessions on other machines and in the cloud](cross-machine-and-cloud.md) - Transport per location, offline and cannot-receive conditions, container limits and reply rules for cloud sessions. **[high]**
* [Message delivery, refusal and usage](delivery-and-refusal.md) - How messages arrive between turns or start a turn, when Claude Code refuses them, and that they count as prompts. **[high]**
* [Notice when another session goes idle](idle-notice-subscription.md) - SendMessage notify_when_idle subscribes to one notice when a local session next goes idle or exits. **[high]**
* [Inbound controls: crossSessionInbound](inbound-controls.md) - accept, hold or refuse arriving messages, the default permission-mode rule, the approval dialog and held-message limits. **[high]**
* [How a session treats an incoming message](incoming-message-treatment.md) - Messages from other sessions are not user input: they cannot approve, change config or run commands. **[high]**
* [Cross-session messaging limits](limitations.md) - Plain text only, size cap about a million characters, burst and loop throttling, 50 queued, and exchange pauses. **[high]**
* [Seeing which sessions Claude can reach](listing-reachable-sessions.md) - /list-agents rows, Remote Control detail withholding, session naming and addressing by name or identifier.
* [Non-interactive sessions and the inbox socket](non-interactive-and-inbox-socket.md) - claude -p workers can receive messages; the per-session socket, token env vars, auth line and sandbox settings. **[high]**
* [Cross-session messaging overview](overview-and-requirements.md) - Claude can list and message your other Claude Code sessions via ListAgents and SendMessage; version and provider requirements. **[high]**
* [Restricting and turning off messaging](restrict-and-turn-off.md) - isolatePeerMachines requires approval for cross-machine sends; refuse and deny rules turn receiving and sending off. **[high]**
