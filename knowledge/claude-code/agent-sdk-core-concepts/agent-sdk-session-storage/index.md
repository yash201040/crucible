# agent-sdk-core-concepts/agent-sdk-session-storage

* [Dual-write architecture and conflicts](dual-write-architecture.md) - The subprocess writes locally first and the SDK mirrors to the store; which copy survives and unsupported option combinations. **[high]**
* [Mirror writes are best-effort](mirror-writes-best-effort.md) - append retries up to three attempts, then drops the batch and emits a mirror_error system message. **[high]**
* [Session store quick start, adapters, conformance](quick-start-and-adapters.md) - InMemorySessionStore example, writing an adapter, reference S3/Redis/Postgres adapters and the conformance suite.
* [Resume from the store](resume-from-the-store.md) - How resume and continue load a transcript from the store into a temporary config dir and what happens when the store has nothing. **[high]**
* [SessionStore interface](session-store-interface.md) - Required append and load plus four optional methods, SessionKey shape and when each method is called. **[high]**
* [Store-backed helpers, forks, subagents, retention](store-helper-behaviors.md) - How getSessionMessages, forkSession, subagent transcripts and retention behave with a store, and which functions accept sessionStore. **[high]**
