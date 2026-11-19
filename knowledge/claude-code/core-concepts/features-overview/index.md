# core-concepts/features-overview

* [When to add each extension](build-setup-triggers.md) - Table of recognizable triggers that tell you which extension to add next, and when to update an existing one.
* [Hook vs skill and MCP vs skill](compare-hook-mcp-skill.md) - Hooks are deterministic lifecycle automation; skills are instructions Claude interprets; MCP supplies tools while skills supply knowledge. **[high]**
* [CLAUDE.md vs rules vs skills vs output styles](compare-instruction-features.md) - How the standing-instruction features differ in loading, scope and purpose, and the 200-line CLAUDE.md rule of thumb.
* [Skill vs subagent vs dynamic workflow](compare-skill-subagent-workflow.md) - How skills, subagents and dynamic workflows differ in context, who decides what runs next, and how they combine. **[high]**
* [Context cost and loading by feature](context-cost-by-feature.md) - When each extension loads, what enters context, and its cost; includes subagent startup context and how to hide skill descriptions. **[high]**
* [The extension layer](extension-layer-overview.md) - Overview of the features that extend Claude Code: CLAUDE.md, output styles, skills, MCP, subagents, workflows, hooks, plugins. **[high]**
* [How features layer and which wins](feature-layering-precedence.md) - Precedence and merge rules when CLAUDE.md, skills, subagents, MCP servers and hooks are defined at several levels. **[high]**
