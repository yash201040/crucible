# mods/plugins-mods-troubleshoot

* [Band, pane and ui.render problems](band-and-render-problems.md) - Causes for a missing band row, empty pane, refused ui.render, key errors and render exceptions, with the log lines to search.
* [Built-in guard messages](built-in-guard-messages.md) - Messages from the built-in guard that refuses a mod or one of its answers, with where each appears. **[high]**
* [Check whether mods can load](check-whether-mods-can-load.md) - Run claude plugin test from a directory with no mod to learn from its message whether settings, policy or a rollout switch block mods.
* [Diagnose a mod that does nothing](diagnose-a-mod-that-does-nothing.md) - When a mod's module or hook fails Claude Code skips it and continues; validate the mod, then read the one line naming it in the transcript, stderr or debug log.
* [Hook skipped and mod unloaded messages](hook-skipped-and-unloaded.md) - Lines for skipped hooks, unanswered commands, worker crashes, repeated session.start, failed reloads and refused $.agent.register. **[high]**
* [Lost edits and values, settings.read](lost-edits-and-values.md) - Why edits to installed plugins do not apply, why module variables and $.state reset, and how to debug settings.read hook answers.
* [Conditions that stop mods loading](mod-does-not-load-conditions.md) - Trust prompt not answered, --safe-mode, and hot reloading that stops being offered after three unanswered questions.
* [Module load errors](module-load-errors.md) - Messages when a mod's hooks module fails to load: missing modules key, load failure, userConfig mismatch, 2000-scope nesting, stack and parser errors.
* [Read the mod debug log](read-the-debug-log.md) - Start Claude Code with --debug or --debug-file to get a line for every module loaded or refused, hook failure and refused result.
* [Hooks module refusal messages](refusal-messages.md) - Reasons that follow 'hooks module <name> not loaded:' in the debug log or stderr, with their meaning.
* [Stopped toast after an interrupted turn](stopped-toast-after-interrupt.md) - The 'stopped · type a message to continue' toast means a mod tried to start work on its own after the user stopped a turn.
* [Toast, hotkey and surface problems](toast-hotkey-and-surface-problems.md) - Why a toast does not show, the band shows 'plugin panel hidden', hotkeys fail, or a drawing works in terminal but not in Desktop or VS Code.
* [Tool call denied after a hook changed input](tool-call-denied-by-hook-change.md) - In auto mode a call is denied when a mod or PreToolUse hook changed its input after the classifier reviewed it. **[high]**
