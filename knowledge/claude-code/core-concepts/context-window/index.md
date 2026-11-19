# core-concepts/context-window

* [What enters the context window](what-loads-into-context.md) - What loads before the first prompt and as Claude works, with the page's illustrative token counts for each step. **[high]**
* [What survives compaction](what-survives-compaction.md) - Per-mechanism table of what is re-injected, rebuilt, reloaded on demand or summarized when a conversation compacts, with the file and skill caps. **[high]**
* [Managing a filling context window](when-context-fills-up.md) - Automatic compaction, manual /compact focus, /rewind summarize, /autocompact, /clear, delegating to subagents and 1M-token window support. **[high]**
