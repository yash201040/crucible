# agent-sdk-core-concepts/agent-sdk-agent-loop

* [Built-in tools and parallel execution](built-in-tools-and-parallelism.md) - Built-in tool categories in the SDK, tool permission options, and which tools run concurrently. **[high]**
* [Context window, caching and compaction](context-window-and-compaction.md) - What consumes context in the SDK, prompt caching, automatic compaction and how to influence it. **[high]**
* [Effort levels](effort-level.md) - The effort option values low to max, per-session and per-subagent, and how it differs from extended thinking. **[high]**
* [Result subtypes and stop_reason](handle-the-result.md) - ResultMessage subtypes, which fields every result carries, crash behavior and how errors raise from query(). **[high]**
* [Hooks commonly used in the loop](hooks-in-the-loop.md) - Hook events that fire in the SDK loop and how hooks relate to context and short-circuiting. **[high]**
* [The agent loop and turns](loop-and-turns.md) - Prompt, evaluate, execute tools, repeat, return result; what a turn is and how max_turns counts. **[high]**
* [SDK message types](message-types.md) - The five core message types yielded by the loop and the SystemMessage subtypes. **[high]**
* [Permission modes in the loop](permission-mode-summary.md) - One-line behavior and use case for each permission mode, plus bypassPermissions TypeScript requirement. **[high]**
* [Sessions and continuity in the loop](sessions-and-continuity.md) - Capturing the session ID, resume and fork, and pointers to session storage for stateless hosts. **[high]**
* [Turn and budget limits](turns-and-budget.md) - max_turns and max_budget_usd caps, subagent spend counting, budget headroom and streaming-input behavior. **[high]**
