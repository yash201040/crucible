# mods/plugins-mods-events

* [Settings hook events as classic.<Event>](classic-settings-hook-events.md) - Each settings hook event is also a mod event named classic.<Event>, receiving the same JSON a settings hook gets on stdin.
* [Matchers: filter which events a hook handles](filter-which-events-hook-handles.md) - The second argument to on() is a matcher object that limits a hook by event fields, with wildcards and a plugin field for other mods' UI.
* [Follow a turn: turn.start, turn.step, turn.complete](follow-a-turn.md) - Turn events expose each model request's token usage, allow routing a request to another model, and report the turn's final answer and totals. **[high]**
* [Guard or change a tool call (tool.call)](guard-or-change-tool-call.md) - A tool.call hook can refuse, change, retry, answer or withhold the result of any tool call, including subagent and MCP calls. **[high]**
* [Hold a tool call until the user decides ($.ui.ask)](hold-tool-call-until-user-decides.md) - A tool.call hook can await $.ui.ask to put a question dialog to the user while the tool call stays pending. **[high]**
* [Hook failures and the .catch handler](hook-failure-catch-handler.md) - A failing hook is skipped by default; chain .catch on on() to fail closed, using next.called and next.error. **[high]**
* [The order mods run in](hook-order-in-chain.md) - Hooks on one event form one chain ordered by origin: guard and prepend mods, installed mods, appendPlugins, then other built-ins; settings PreToolUse hooks sit at fixed points.
* [How a mod hook handles an event](how-a-hook-handles-event.md) - A mod hook is a middleware function that can observe, rewrite or answer an event, using the $, e and next arguments.
* [Rewrite or add to a prompt (prompt.submit)](rewrite-or-add-to-prompt.md) - A prompt.submit hook can rewrite the prompt text, add Claude-only context, or drop the prompt.
* [Change or refuse a settings read (settings.read)](settings-read-hook.md) - A settings.read hook can replace or deny the merged settings Claude Code builds or a mod's $.settings.read, with layers by precedence.
* [tool.check: approve or refuse before the user is asked](tool-check-permission-decisions.md) - A tool.check hook decides allow, ask or deny for a tool call before prompts, auto mode and PermissionRequest hooks, with an isReadOnly field. **[high]**
