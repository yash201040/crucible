# agent-sdk-customize-behavior/agent-sdk-modifying-system-prompts

* [Append to preset and cross-user prompt caching](append-and-prompt-caching.md) - Add instructions after the claude_code preset and use excludeDynamicSections so identical configs share a cache entry. **[high]**
* [Changing the prompt of a resumed session](change-prompt-of-existing-session.md) - The system prompt is recorded on a session's first request; how to update instructions mid-session and the snapshot option. **[high]**
* [CLAUDE.md loading in the SDK](claude-md-loading.md) - CLAUDE.md is injected into the conversation via setting sources, independent of the system prompt.
* [Comparing four prompt customization approaches](compare-approaches.md) - CLAUDE.md, output styles, append and custom systemPrompt compared on persistence, tool guidance and safety, plus combining them.
* [Custom prompts and dynamic boundary caching](custom-prompts-and-boundary.md) - Replace the prompt with a string, a Python file form, or a TypeScript array split by SYSTEM_PROMPT_DYNAMIC_BOUNDARY for caching. **[high]**
* [Output styles in the SDK](output-styles.md) - Saved markdown instruction sets; frontmatter, locations, keep-coding-instructions and how to activate in the SDK.
* [Seeing what Claude received](see-what-claude-received.md) - The SDK stream omits system reminders; log raw API bodies or use a gateway to inspect them.
* [System prompt starting points](starting-points.md) - Minimal default, the claude_code preset, or a custom string, and how to decide between them. **[high]**
* [System reminders outside the system prompt](system-reminders.md) - Context Claude Code adds to the conversation (CLAUDE.md, hooks, skills, attribution) and the sentence a custom prompt should include.
* [Turning off built-in context](turn-off-built-in-context.md) - Settings and env vars that remove git instructions, attribution, CLAUDE.md, attachments and file-mention expansion. **[high]**
