# agent-sdk-control-and-observability/agent-sdk-permissions

* [Accept edits mode](accept-edits-mode.md) - acceptEdits auto-approves file edits and common filesystem commands inside working directories.
* [Allow and deny rules options](allow-and-deny-rules.md) - How allowed_tools and disallowed_tools add to rule lists, glob support, and which calls never reach canUseTool. **[high]**
* [Auto mode and model fallback](auto-mode.md) - auto mode uses a classifier model; switching to an unsupported model drops the session to default mode.
* [Bypass permissions mode](bypass-permissions-mode.md) - bypassPermissions auto-approves tool calls except a short list that still reach hooks, rules or the callback. **[high]**
* [canUseTool shadowed warning](canusetool-shadowed-warning.md) - TypeScript SDK emits a process warning when a configuration makes auto-approval run before the canUseTool callback.
* [Don't ask mode](dont-ask-mode.md) - dontAsk turns every would-be prompt into a denial without calling canUseTool; intended for headless agents. **[high]**
* [Six-step permission evaluation order](evaluation-order.md) - How the SDK decides a tool call: hooks, deny rules, ask rules, permission mode, allow rules, then the canUseTool callback. **[high]**
* [Path patterns in Read and Edit rules](path-patterns-in-rules.md) - How to write path patterns for Read and Edit rules: Edit covers all file writers; // is absolute, / is working-directory relative.
* [SDK permission modes and setting them](permission-modes-overview.md) - The six SDK permission modes, default mode from v2.1.302, changing mode mid-session, and subagent inheritance. **[high]**
* [Plan mode and auto-mode review](plan-mode.md) - In plan mode file edits and AskUserQuestion reach canUseTool; with auto mode available a classifier reviews other calls.
