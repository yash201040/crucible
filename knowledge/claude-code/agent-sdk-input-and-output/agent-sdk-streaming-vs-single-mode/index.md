# agent-sdk-input-and-output/agent-sdk-streaming-vs-single-mode

* [Interrupt a running response](interrupt-a-response.md) - interrupt() stops a response partway and keeps the session open; the response ends with an error_during_execution result and unread queued messages still arrive. **[high]**
* [Read each response and its result message](read-each-response-result-message.md) - Each response ends with a result message whose subtype reports how it ended; loop behavior on error results differs between TypeScript and Python. **[high]**
* [Send more than one message to a session](send-multiple-messages-to-session.md) - How to send several messages, including images, to one SDK session in TypeScript (async generator) and Python (ClaudeSDKClient), and how queued messages are read. **[high]**
* [Single-shot versus streaming input](single-shot-vs-streaming-input.md) - Single-shot query() takes one prompt string and ends; streaming input keeps a session open for several messages, images, interrupts and mid-session changes. **[high]**
