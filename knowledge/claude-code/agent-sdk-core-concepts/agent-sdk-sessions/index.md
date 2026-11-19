# agent-sdk-core-concepts/agent-sdk-sessions

* [Automatic session management](automatic-session-management.md) - Python ClaudeSDKClient and TypeScript continue:true track sessions without handling IDs; V2 session API removed.
* [Capture the session ID](capture-session-id.md) - Where to read the session ID: result message in both SDKs, init message earlier in TypeScript. **[high]**
* [Choosing a session approach](choose-an-approach.md) - Which session mechanism fits one-shot, multi-turn, restart, specific-session, fork and stateless use cases. **[high]**
* [Continue, resume and fork](continue-resume-fork.md) - Definitions of the three option fields for returning to a session and how fork branches history. **[high]**
* [Resume across hosts and session helper functions](resume-across-hosts.md) - Three ways to resume on a different host and the functions for listing, reading and mutating sessions. **[high]**
* [Resume by session ID](resume-by-id.md) - Resume a specific session with full prior context; where transcripts are stored and how directory lookup works. **[high]**
