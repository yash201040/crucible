# agent-sdk-customize-behavior/agent-sdk-skills

* [Commands in SDK sessions](commands-in-sdk-sessions.md) - Send /<name> in a prompt to run built-in commands, bundled skills, your skills or command files; slash_commands in the init message lists them. **[high]**
* [/compact and /clear in SDK sessions](compact-and-clear-commands.md) - Compact or reset conversation history from the SDK by sending /compact or /clear, with a compact_boundary message reporting compaction. **[high]**
* [Create and dispatch a skill](create-skills-for-sdk.md) - Author a SKILL.md in a project or personal skills directory and dispatch it from the SDK with /<name>.
* [Pre-approve tools for skills](pre-approve-tools-for-skills.md) - Skills run with session tools; pre-approve them via skill allowed-tools frontmatter or the allowedTools option, unless managed settings forbid it. **[high]**
* [Skills option and allowlist](skills-option-and-allowlist.md) - The skills option of query() controls which discovered skills Claude may invoke: all, a list of names, or none. **[high]**
* [Skills troubleshooting and name errors](skills-troubleshooting-errors.md) - Why SDK skills are not found or used, and the validation errors raised for invalid names in the skills list.
