# core-concepts/prompt-caching

* [Actions that keep the cache](actions-that-keep-cache.md) - Edits, permission mode, output style, skills, /recap, /rewind and subagent spawns that leave the cached prefix intact.
* [How the prompt cache is organized](cache-layers-prefix-matching.md) - Prefix matching, the three request layers (system prompt, project context, conversation), and the model and effort caches. **[high]**
* [Cache lifetime and TTL buckets](cache-lifetime-ttl-buckets.md) - Five-minute versus one-hour TTL, which request bucket gets which by default, and how to verify the TTL used. **[high]**
* [Cache scope: machine and directory](cache-scope-isolation.md) - The Claude Code cache is effectively scoped to one machine and directory; parallel same-directory sessions can share it. **[high]**
* [Cache TTL controls and precedence](cache-ttl-controls-reference.md) - Settings and environment variables that choose the cache TTL per bucket and the order in which they win. **[high]**
* [Checking cache performance](check-cache-performance.md) - Cache token fields, the /usage Prompt cache (main) line with likely-cause text, status line fields and OpenTelemetry. **[high]**
* [Compaction, images and upgrades vs cache](compaction-images-upgrades-cache.md) - Compaction rebuilds the conversation cache, many images get oldest removed in batches, and upgrades rebuild from the top. **[high]**
* [Disable prompt caching variables](disable-prompt-caching-variables.md) - Environment variables that turn prompt caching off globally or per model family, with alias-resolution caveats.
* [MCP servers, plugins and deny rules vs cache](mcp-plugins-tool-denial-cache.md) - How connecting MCP servers, toggling plugins and denying whole tools affect cached tool definitions, with and without tool search. **[high]**
* [Model, effort and fast-mode cache effects](models-effort-fast-mode.md) - Switching models, changing effort or toggling fast mode each costs an uncached turn; exceptions for newer models and a PreModelSwitch hook. **[high]**
* [Resuming a session and the cache](resuming-a-session-cache.md) - A resumed session resends the whole conversation and reads whatever prefix is unchanged and within cache lifetime. **[high]**
* [Subagents, forks and cache sharing](subagents-and-cache.md) - Subagents warm their own cache; forks, session copies, resumed subagents and workflow fan-outs can read an earlier prefix. **[high]**
* [Where the cache lives and gateways](where-cache-lives-gateways.md) - Cache location by provider, and how LLM gateways or custom base URLs that handle cache_control markers change what stays cached. **[high]**
