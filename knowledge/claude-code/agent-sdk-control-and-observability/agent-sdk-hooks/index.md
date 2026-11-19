# agent-sdk-control-and-observability/agent-sdk-hooks

* [Asynchronous hook output](async-hook-output.md) - Return async true so the agent continues without waiting; usable only for side effects like logging.
* [onFailure block for failing callbacks](block-on-callback-failure.md) - By default a failing callback lets the action proceed with a warning; onFailure block makes the action blocked instead. **[high]**
* [Hook callback inputs and output fields](callback-inputs-and-outputs.md) - The three callback arguments, shared input fields, and top-level and hookSpecificOutput return fields including permission decisions. **[high]**
* [SDK hook events and SDK support](hook-events-reference.md) - Every hook event with whether the Python and TypeScript SDKs support it and what triggers it. **[high]**
* [Hook example patterns](hook-example-patterns.md) - Worked hook patterns: rewrite tool input, block with a reason, auto-approve read-only tools, parallel hooks, subagent tracking, webhooks, Slack. **[high]**
* [Hook timeouts and per-event outcomes](hook-timeout-behavior.md) - Default callback timeouts per event and what Claude Code does for each event when a callback times out. **[high]**
* [Hook troubleshooting](hook-troubleshooting.md) - Fixes for hooks not firing, over-broad matchers, ignored modified input, Python session hooks, permission prompt multiplication and loops. **[high]**
* [How SDK hooks work](how-sdk-hooks-work.md) - Hooks are callbacks fired on agent events; matching hooks receive input and return a decision object to allow, block, modify or add context. **[high]**
* [HookMatcher fields and matcher rules](matchers-and-hook-options.md) - The matcher, hooks, timeout and onFailure fields of a hook registration, and how patterns match tool names. **[high]**
