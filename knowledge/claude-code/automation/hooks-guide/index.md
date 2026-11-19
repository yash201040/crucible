# automation/hooks-guide

* [Examples: context, audit and environment hooks](context-and-env-examples.md) - SessionStart compact re-injection, ConfigChange audit log, and direnv reload via CwdChanged, SessionStart and FileChanged with CLAUDE_ENV_FILE. **[high]**
* [Examples: auto-format and block protected files](format-and-protect-examples.md) - PostToolUse Prettier on Edit|Write and a PreToolUse exit-2 script that blocks edits to .env, package-lock.json and .git/.
* [Hook events and when they fire](hook-events-table.md) - All hook event names with their trigger conditions, plus the five handler types. **[high]**
* [Hook input, output, exit codes and JSON control](hook-io-and-exit-codes.md) - stdin JSON fields, exit 0 vs 2, structured hookSpecificOutput decisions, defer, and how multiple hooks combine. **[high]**
* [Hook limitations, timeouts and block cap](hook-limits-and-timeouts.md) - Default timeouts by hook type, SessionEnd budget, Stop block cap of eight, and behavior of hooks in -p mode. **[high]**
* [Where hooks are configured and how to disable](hook-locations-and-disable.md) - Hook scope by location (user, project, local, managed, plugin, skill, subagent), /hooks browser and disableAllHooks. **[high]**
* [Hook troubleshooting](hook-troubleshooting.md) - Fixes for hooks that do not fire, errors, JSON with no effect, and how to inspect what a hook did with debug logs.
* [Hooks versus permission modes and mods](hooks-and-permission-modes.md) - A hook deny holds in every mode including bypassPermissions; allow cannot override deny rules or certain prompts; mods can approve in some setups. **[high]**
* [Hooks overview and first hook](hooks-overview-first-hook.md) - Hooks are user-defined handlers run at lifecycle points for deterministic control; how to add and verify a Notification hook. **[high]**
* [HTTP hooks](http-hooks.md) - type http hooks POST the event JSON to a URL and read the decision from the response body; headers interpolate allowed env vars. **[high]**
* [Hook matchers and the if field](matchers-and-if-field.md) - What each event's matcher filters, example values, and permission-rule-syntax if filtering for tool events. **[high]**
* [Notification hook and matcher values](notification-hook-matchers.md) - Desktop-notification commands per OS and the Notification matcher values with versions where stated. **[high]**
* [Auto-approve permission prompts with a hook](permission-request-auto-approve.md) - A PermissionRequest hook returns a JSON allow decision, with updatedInput for interactive tools and setMode via updatedPermissions. **[high]**
* [Prompt-based and agent-based hooks](prompt-and-agent-hooks.md) - type prompt hooks make a single model call returning ok/reason; type agent hooks (experimental) run a subagent with tools. **[high]**
