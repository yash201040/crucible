# interface/statusline

* [Configure a custom status line](configure-status-line.md) - The statusLine setting runs a shell command that receives session JSON on stdin and shows its output in a bar at the bottom of Claude Code.
* [Prompt cache and spend limit fields](prompt-cache-and-spend-fields.md) - The prompt_cache and rate_limits.spend_limit objects in status line input: cache hit ratio, misses, miss causes, and gateway spend. **[high]**
* [Status line examples and troubleshooting](status-line-examples-and-troubleshooting.md) - Ready-made status line patterns (context bar, git, cost, rate limits, links, caching, Windows) and fixes for a blank or garbled status line.
* [Status line JSON input fields](status-line-json-fields.md) - Session data fields Claude Code sends on stdin to a status line script: model, workspace, cost, context window, effort, rate limits, PR, worktree. **[high]**
