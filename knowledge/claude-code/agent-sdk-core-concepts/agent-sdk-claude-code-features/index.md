# agent-sdk-core-concepts/agent-sdk-claude-code-features

* [Choosing an extension feature in the SDK](choose-the-right-feature.md) - Maps goals to CLAUDE.md, skills, subagents, agent teams, hooks and MCP with the SDK surface for each. **[high]**
* [CLAUDE.md and rules load locations](claude-md-and-rules.md) - Where CLAUDE.md, rules and local files load from and which setting source gates each; all levels are additive.
* [Filesystem and programmatic hooks in the SDK](hooks-filesystem-and-programmatic.md) - Two hook definition styles run side by side; callback return shape, hook types and TypeScript-only events. **[high]**
* [settingSources and what it loads](setting-sources.md) - Which filesystem settings each setting source loads and the default of all three when omitted. **[high]**
* [Inputs settingSources does not control](settingsources-exclusions.md) - Managed policy, global config, auto memory, claude.ai connectors and sandbox credentials load regardless; multi-tenant guidance. **[high]**
* [Skills through settingSources and the skills option](skills-in-sdk.md) - Skills are discovered from the filesystem; the skills option enables all, named or none; no programmatic registration. **[high]**
