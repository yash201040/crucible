---
type: "Release Digest"
title: "Skills, plugins and mods, 2.1.296 to 2.1.328"
description: "Release-note changes to skills, plugins, marketplaces, mods, Code Mode and bundled skills between 2.1.296 and 2.1.328."
resource: "https://code.claude.com/docs/en/changelog"
tags: [skills, plugins, mods, marketplace, code-mode, release-notes]
kind: "mixed"
maturity: "experimental"
since: ""
surfaces: []
requires: ""
identifiers:
  - "engines"
  - "plugin.json"
  - "claude plugin validate"
  - "--strict"
  - "claude plugin install"
  - "--json"
  - "unsetOptionCount"
  - "claude plugin list"
  - "claude plugin test"
  - "claude plugin eval"
  - "claude plugin restore-set-aside"
  - "prependPlugins"
  - "appendPlugins"
  - "pluginDigests"
  - "extraKnownMarketplaces"
  - "allowManagedModsOnly"
  - "allowManagedPermissionRulesOnly"
  - "--plugin-dir"
  - "engine.create"
  - "tool.list"
  - "tool.check"
  - "decider"
  - "e.isReadOnly"
  - "settings.read"
  - "skill.prompt"
  - "prompt.submit"
  - "prompt.change"
  - "session.append"
  - "$.model.complete"
  - "$.model.classify"
  - "$.tool.call"
  - "$.mcp.call"
  - "$.env.set"
  - "$.prompt.media"
  - "$.session.identity"
  - "$.session.usage"
  - "isPromptCovered"
  - "virtualText"
  - "Box"
  - "Text"
  - "Input"
  - "Image"
  - "ui.render"
  - "CLAUDE_CODE_PLUGIN_DIR_WATCH"
  - "CLAUDE_CODE_SYNC_SKILLS"
  - "/reload-skills"
  - "plugin-authoring"
  - "allowed-tools"
  - "CLAUDE_CODE_MODEL_CATALOG"
  - "subagentStatusLine"
  - "agent"
  - ".mcpb"
  - ".dxt"
  - "/plugin"
  - "ALL_PROXY"
  - "/claude-api"
  - "/design-sync"
  - "/security-review"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.296 to 2.1.328"
stale_after: "2027-01-19T00:00:00Z"
---

# What changed

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.328 | 2026-11-19 | Apps that embed Claude Code can switch on the policy plugin's allowManagedModsOnly option; admin managed settings still win. | `allowManagedModsOnly` |
| 2.1.328 | 2026-11-19 | Code Mode: no UserPromptSubmit hooks on script output; faster in auto and bypass modes (0.75 s pause removed); better edit and failure messages; dev servers started as background tasks shown in /tasks. | `/tasks` |
| 2.1.327 | 2026-11-17 | Code Mode no longer refuses to start when an installed mod hooks tool calls; an administrator can still keep it off in managed settings. | |
| 2.1.327 | 2026-11-17 | claude plugin eval keeps its deny rules over a plugin's permission hook and flags calls the hook let through. | `claude plugin eval` |
| 2.1.327 | 2026-11-17 | /status lists broken agent, skill, command and output style files. | `/status` |
| 2.1.326 | 2026-11-16 | Code Mode's $ shell helper refuses some values; Code Mode permission checks stricter. | |
| 2.1.326 | 2026-11-16 | Mods: overflowX scroll on Box; maxLines and wrap clip on Text. | `Box`, `Text` |
| 2.1.326 | 2026-11-16 | Enabled plugins refused for a malformed plugin.json display field now load with hooks and MCP servers; a note appears in /plugin and claude plugin list. | `plugin.json`, `claude plugin list` |
| 2.1.326 | 2026-11-16 | Plugin uninstall also deletes files extracted from MCP bundles (.mcpb, .dxt) unless another plugin uses them. | `.mcpb`, `.dxt` |
| 2.1.326 | 2026-11-16 | Edits in a session's mods folder ask more often; some worktree sessions skip some plugin settings with a notice. | |
| 2.1.325 | 2026-11-13 | Plugin MCP bundles unpack under the plugins directory, not .mcpb-cache in the plugin folder. | `.mcpb`, `.dxt` |
| 2.1.325 | 2026-11-13 | Remote-marketplace plugins declared in prependPlugins or appendPlugins count as the organization's; pluginDigests is deprecated and ignored. | `prependPlugins`, `appendPlugins`, `pluginDigests` |
| 2.1.325 | 2026-11-13 | .claude/skills folders in --plugin-dir plugins no longer load from a session started above them; marketplace ref accepts any commit ID on a branch or tag (older clients cannot clone such a pin). | `--plugin-dir`, `ref` |
| 2.1.325 | 2026-11-13 | Plugin marketplace and plugin downloads use a CONNECT tunnel when ALL_PROXY is the only proxy set; claude plugin validate reports some unsafe paths and links. | `ALL_PROXY`, `claude plugin validate` |
| 2.1.325 | 2026-11-13 | /cost, $.session.usage(), --max-budget-usd and cost metrics count a mod's $.model.complete and $.model.classify calls. | `$.model.complete`, `$.model.classify`, `$.session.usage`, `--max-budget-usd` |
| 2.1.323 | 2026-11-12 | Added Code Mode, an experimental opt-in where Claude writes JavaScript to call its tools; can be turned off for an organization. | |
| 2.1.323 | 2026-11-12 | Added engines claude-code to plugin.json: plugins outside their version range are not installed, updated or loaded. | `engines`, `plugin.json` |
| 2.1.323 | 2026-11-12 | claude plugin validate type-checks a plugin's TypeScript hooks module (warnings; --strict fails) and reports the $ nouns a mod's engine.create hook adds, withholds or replaces. | `claude plugin validate`, `--strict`, `engine.create` |
| 2.1.323 | 2026-11-12 | Added unsetOptionCount to the claude plugin install --json result. | `unsetOptionCount`, `claude plugin install`, `--json` |
| 2.1.323 | 2026-11-12 | Mod pane props gain isPromptCovered. | `isPromptCovered` |
| 2.1.323 | 2026-11-12 | A star, namespace or negated hook on engine.create only observes; add or withhold a $ noun by hooking engine.create by name; tool.list plugin hooks apply to the model and every agent. | `engine.create`, `tool.list` |
| 2.1.323 | 2026-11-12 | Marketplace and plugin installs fail when a git submodule is not on the commit its repository records; a plugin's agent setting is deprecated and warns. | `agent` |
| 2.1.323 | 2026-11-12 | Removed the subagentStatusLine setting; managed policyHelper no longer takes environment variables from user or --settings files. | `subagentStatusLine`, `policyHelper` |
| 2.1.321 | 2026-11-09 | Mods Claude writes turn on without asking in auto and bypass modes and do not load in dontAsk mode; mods' $.tool.call and $.mcp.call raise no permission prompt (deny rules and policy still apply). | `$.tool.call`, `$.mcp.call` |
| 2.1.321 | 2026-11-09 | Managed extraKnownMarketplaces: a declared name cannot be added from another source; set-aside data recoverable with claude plugin restore-set-aside. | `extraKnownMarketplaces`, `claude plugin restore-set-aside` |
| 2.1.321 | 2026-11-09 | Nested skill loading: .claude/skills folders inside ~/.claude/plugins no longer load when Claude works on files there. | |
| 2.1.319 | 2026-11-06 | With the Bash sandbox on, nested skills below the start folder load only if you start or /cd there. | |
| 2.1.318 | 2026-11-04 | Added an effort option to a mod's $.model.fork; mod text attached at prompt.submit stays in the user's turn. | `$.model.fork`, `prompt.submit` |
| 2.1.317 | 2026-11-03 | plugin-authoring skill offers once to help share a working mod. | `plugin-authoring` |
| 2.1.314 | 2026-10-30 | Bundled dataviz skill updated (axis labels, donut and pie advice). | |
| 2.1.304 | 2026-10-19 | Mod tool.check answer can set decider person; added e.isReadOnly; settings.read hooks receive each settings layer and can rewrite merged settings. | `tool.check`, `decider`, `e.isReadOnly`, `settings.read` |
| 2.1.304 | 2026-10-19 | Compaction resends the skill list; /reload-skills now sends only new or changed skills; skills of one source can register at most 1,024 hooks and 16,384 matcher characters per session. | `/reload-skills` |
| 2.1.304 | 2026-10-19 | Under a policy that allows hooks from plugins only, a skill whose hooks are kept out no longer gets its allowed-tools. | `allowed-tools` |
| 2.1.305 | 2026-10-20 | Plugins Claude Desktop mounts by path lose allowed-tools when managed settings set allowManagedPermissionRulesOnly. | `allowManagedPermissionRulesOnly`, `allowed-tools` |
| 2.1.311 | 2026-10-26 | Sessions with CLAUDE_CODE_SYNC_SKILLS and feature-flag fetching off reuse a claude.ai skills list up to 10 minutes old. | `CLAUDE_CODE_SYNC_SKILLS` |
| 2.1.311 | 2026-10-26 | DISABLE_COMPACT in settings files and a mod's $.env.set can only turn compaction off; model settings load from a signed file on downloads.claude.ai on Bedrock, Mantle, Vertex and Foundry (CLAUDE_CODE_MODEL_CATALOG=off disables). | `$.env.set`, `CLAUDE_CODE_MODEL_CATALOG` |
| 2.1.301 | 2026-10-15 | Mod Input gains rows; a mod hook catch handler runs only when the hook throws or times out; $.env.set resolves with an object or deny. | `Input`, `$.env.set` |
| 2.1.300 | 2026-10-14 | Mods: virtualText prompt decoration, $.ui.view agentId, dir prop on Text, prompt.change hook, agent.spawn rewriting of workflow agent prompt and model. | `virtualText`, `prompt.change`, `agent.spawn`, `$.ui.view` |
| 2.1.299 | 2026-10-14 | Added $.prompt.media, $.session.identity() for managed mods; skill.prompt hook receives skill frontmatter, source, plugin name and path; session.append gains a queue door. | `$.prompt.media`, `$.session.identity`, `skill.prompt`, `session.append` |
| 2.1.299 | 2026-10-14 | Text gains size, weight, mono, tabular (bold deprecated); Box gains spacing steps xs to xl; plugin test ui.render roots carry part plugin; skills or commands with odd characters in names are not offered. | `Text`, `Box`, `ui.render`, `claude plugin test` |
| 2.1.299 | 2026-10-14 | claude plugin test fails a mod method call that has not answered within ten seconds. | `claude plugin test` |
| 2.1.299 | 2026-10-14 | Managed permission rules, managed hooks and org MCP tool names enforced better against user-installed mods. | |
| 2.1.296 | 2026-10-09 | /plugin notes a plugin whose hooks are left out because another enabled plugin has the same name. | `/plugin` |

# Not found in the documentation pages

- `unsetOptionCount`
- `claude plugin restore-set-aside`
- `pluginDigests`
- `tool.list`
- `decider`
- `prompt.change`
- `$.prompt.media`
- `$.session.identity`
- `$.session.usage`
- `isPromptCovered`
- `virtualText`
- `CLAUDE_CODE_MODEL_CATALOG`
- `subagentStatusLine`
