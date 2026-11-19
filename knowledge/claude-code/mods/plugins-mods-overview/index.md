# mods/plugins-mods-overview

* [Mods built into Claude Code](built-in-mods.md) - Built-in mods listed under Built-in in /plugin, such as cc-plugin-diff and cc-plugin-sec-default, with where they run and how to turn them off.
* [Compare mods, settings hooks, skills and MCP servers](compare-mods-hooks-skills-mcp.md) - Table of what each extension kind is, what it can change and when to pick it.
* [Get, install and update a mod](get-install-update-a-mod.md) - Install a mod as a plugin from a marketplace, reload after shell installs, and try Anthropic's sample mods with --plugin-dir.
* [Trusting a mod: what it can reach and validate before install](trust-and-what-a-mod-can-reach.md) - A mod is unsandboxed code with the user's permissions; claude plugin validate lists its hooks and calls without running it. **[high]**
* [Turn mods on or off and see which are loaded](turn-mods-on-or-off.md) - Mods are on by default; ways to stop one, all installed mods for a session, or all in every session, plus the loaded-mods line in /plugin. **[high]**
* [What a mod is and what it can do](what-a-mod-is-and-does.md) - A mod is a plugin of JavaScript/TypeScript event handlers that run inside Claude Code and can draw UI, rewrite events and add commands. **[high]**
* [Where mods run (surfaces and headless)](where-mods-run.md) - Mod hooks run in every session that loads the plugin, including claude -p, the Agent SDK and cloud sessions, but drawing only in terminal, Desktop and VS Code. **[high]**
