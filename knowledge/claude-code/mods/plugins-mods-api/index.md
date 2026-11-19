# mods/plugins-mods-api

* [Mod commands and tools](add-command-or-tool.md) - A mod registers a user command with $.command.register and a Claude-callable tool with $.tool.register in a session.start hook. **[high]**
* [Background work and timers in mods](background-work-timers.md) - $.clock.every and $.clock.after replace setInterval and setTimeout; timer callbacks run outside any event. **[high]**
* [Call a model from a mod](call-a-model-from-a-mod.md) - $.model.complete sends a standalone prompt and $.model.fork sends the conversation plus a prompt; both bill to the session's credentials. **[high]**
* [Prompt caching in mod model calls](mod-prompt-caching.md) - Pass prompt or system as an array of { text } blocks and mark the static prefix with cache: true; breakpoints, TTL and where to put them. **[high]**
* [Mods API access namespaces](reach-files-processes-network.md) - $.fs, $.process, $.http, $.store, $.env, $.settings, $.session and $.mcp give a mod file, process, network, state and settings access with user permissions. **[high]**
* [Read settings from a mod](read-settings-from-a-mod.md) - $.settings.read returns merged settings, one source, or one top-level key; the key option needs v2.1.304.
* [Refused and dropped mod calls after an interruption](refused-calls-after-interruption.md) - After a user Stop, calls that start work are refused until the next input; how to detect and retry, and what each call returns. **[high]**
* [Mod calls refused in claude -p and SDK runs](refused-calls-in-non-interactive-runs.md) - In headless and Agent SDK runs, mod prompts count toward --max-turns and --max-budget-usd and are refused at the limit, so runs can end. **[high]**
* [Messages between sessions from a mod](send-receive-session-messages.md) - $.session.send delivers text to another session, subagent or teammate; session.receive and session.send events let a mod observe messages. **[high]**
* [Mod UI output calls: status, toast, log, notify](show-without-starting-a-turn.md) - Four $.ui calls show text without starting a turn; only $.ui.notify answers with isSent and a reason.
* [Start a turn from a mod with $.prompt.submit](start-a-turn-from-background.md) - A background job submits a prompt that Claude reads as from the mod, or as the user with asUser: true. **[high]**
