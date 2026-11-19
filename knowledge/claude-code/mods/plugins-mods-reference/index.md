# mods/plugins-mods-reference

* [Box borderStyle names and spacing steps](box-border-and-spacing.md) - Valid borderStyle values and what each draws, and the xs to xl spacing steps in cells for terminal and VS Code.
* [breakPromptCache: send a changed prompt section or tool description](break-prompt-cache.md) - Return breakPromptCache: true after invalidating prompt.section or tool.describe so a running conversation reads changed text, at the cost of a prompt-cache restart. **[high]**
* [Button rules: action, hotkeys, variant, role, children](button-rules.md) - Extra Button behavior: keybinding action, digit hotkeys on the band, hotkey conflicts, variant and role values, and children.
* [Elements: props and which apps draw them](elements-table.md) - Table of Box, Text, Button, Link, Code, Markdown, Input, Select, Svg, Client, Raster and Image with main props and per-app support.
* [Events: commands, configuration and turns](events-commands-config.md) - command.*, config.*, settings.read and the turn.* events with what each hook can return. **[high]**
* [Events: interface, other mods, telemetry, settings hooks and API calls](events-interface-other-telemetry.md) - ui.* events, plugin.register and engine.create, telemetry events, classic.<Event>, and every mods API method as an event.
* [Events: prompts and what Claude reads](events-prompts.md) - Prompt events for typed text and Claude Code's own system prompt, context, attachments, @-mentions and attribution.
* [Events: session and subagents (agent.spawn, session.*)](events-session-and-subagents.md) - Session lifecycle and messaging events plus agent.offer and agent.spawn, including resumed subagent runs and refusing them. **[high]**
* [Events: tools (tool.call, tool.check, tool.describe)](events-tools.md) - Tool events fire around each tool call, with the tool.check agentId, ceiling and isReadOnly fields and tool.describe options. **[high]**
* [Files of a mod](files-of-a-mod.md) - Required and optional files in a mod plugin directory, and the register(on, options) entry point.
* [Limits: drawing, redraw, toast, panes and placed rows](limits-drawing-and-ui.md) - Tree size and nesting limits, redraw throttling, toast timing, pane placement widths and the placed-row cap.
* [Limits: hook time, process, model, fs, http, store](limits-hooks-and-api.md) - Time and size limits on mod hooks and mods API calls; a hook exceeding a time limit is skipped. **[high]**
* [Mods API methods by namespace](mods-api-methods.md) - Every $ namespace and method a mod hook can call, with version notes for agent, session, ui, theme and fs methods. **[high]**
* [Render sites: props, requestId and surfaces](render-sites-table.md) - Each ui.render e.component value with its e.props fields, e.requestId meaning and the apps that render it, plus viewport sizing.
* [Settings, environment variables and commands for mods](settings-env-and-commands.md) - Settings keys and env vars that affect mods, the sec-default guard, and the claude plugin validate and test commands. **[high]**
* [skill.prompt source and frontmatter fields](skill-prompt-fields.md) - Fields a skill.prompt hook can read about where a skill came from and its frontmatter; only text and frontmatter may be changed.
* [Text typography props and bold deprecation](text-typography-props.md) - size, weight, mono and tabular on Text, how terminal and VS Code treat them, and bold deprecated in favor of weight.
* [The hook function: $, e, next and their fields](the-hook-function.md) - Arguments passed to every mod hook, including next.signal, origin, budget, to, error and called, and the on() registration.
