---
type: "Release Digest"
title: "Skills, plugins and mods, 2.1.261 to 2.1.295"
description: "Release-note entries for skills, plugins, marketplaces, Claude Mods and plugin CLI commands from 2.1.261 to 2.1.295."
resource: "https://code.claude.com/docs/en/changelog"
tags: [skills, plugins, mods, marketplace, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "claude plugin install"
  - "claude plugin enable"
  - "claude plugin disable"
  - "claude plugin update"
  - "claude plugin uninstall"
  - "claude plugin list"
  - "claude plugin validate"
  - "claude plugin test"
  - "claude plugin eval"
  - "claude plugin configure"
  - "claude plugin marketplace add"
  - "--marketplace"
  - "--config"
  - "--values-stdin"
  - "--accept-command"
  - "--json"
  - "--strict"
  - "--plugin-dir"
  - "syncClaudeAiSkills"
  - "syncClaudeAiPlugins"
  - "/skill-doctor"
  - "/doctor prompt-audit"
  - "/checkup prompt-audit"
  - "/reload-plugins"
  - "/plugin"
  - "/plugin enable cc-plugin-you-should-know@builtin"
  - "$.ui.notify"
  - "$.ui.selection()"
  - "$.tool.register"
  - "isDeferred"
  - "$.model.complete"
  - "prompt.autocomplete"
  - "$.process.spawn"
  - "Button"
  - "ThemeKey"
  - "Color"
  - "omitClaudeMd"
  - "plugin-authoring"
  - "anthropic-skills"
  - "claude-ai"
  - "Skill(anthropic-skills:*)"
  - "Skill(claude-ai:*)"
  - "disable-model-invocation"
  - "verify"
  - "installed_plugins.json"
  - "ListPlugins"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.261 to 2.1.295"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Release-note rows (bug fixes removed) covering skills, plugins, marketplaces, the plugin CLI and Claude Mods (plugins that change deeper behavior). Newest first.

# How to use it

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.295 | 2026-10-08 | Warning from `claude plugin install`, `enable`, `disable`, `marketplace add` when the settings file they write to does not load. | `claude plugin install`, `claude plugin marketplace add` |
| 2.1.295 | 2026-10-08 | `claude plugin validate` advises when a plugin README has no install line; never changes exit code, even with `--strict`; hooks-module refusal errors name the rebinding line. | `claude plugin validate`, `--strict` |
| 2.1.295 | 2026-10-08 | Mods: `$.ui.notify` raises a native notification; `Button` accepts string and `Text` children. | `$.ui.notify`, `Button` |
| 2.1.295 | 2026-10-08 | Mod denial after a tool ran now says the tool ran and a plugin withheld its result; org mods' toasts show first. | |
| 2.1.293 | 2026-10-07 | `isDeferred` on `$.tool.register` for mods: `false` lists the tool schema in the prompt from the start instead of behind tool search. | `$.tool.register`, `isDeferred` |
| 2.1.293 | 2026-10-07 | claude.ai skill syncing checks about every 40 minutes (was 10) while no session is in use. | |
| 2.1.292 | 2026-10-06 | `claude plugin install --marketplace <source>` adds the marketplace (same policy checks) then installs. | `--marketplace`, `claude plugin install` |
| 2.1.292 | 2026-10-06 | Mods: `prompt.autocomplete` event; `$.model.complete` supports prompt caching (`cache: true` on a block). | `prompt.autocomplete`, `$.model.complete` |
| 2.1.292 | 2026-10-06 | `claude plugin test` fails when an `expect` inside a registered hook fails or a stub answer is refused. | `claude plugin test` |
| 2.1.292 | 2026-10-06 | A skill's or plugin file's `name` over 256 characters is ignored. | `name` |
| 2.1.290 | 2026-10-05 | `/claude-api managed-agents-onboard <url>` and `<quickstart-name>` (such as `deep-researcher`) set up Managed Agents via `ant apply`/`ant` CLI. | `/claude-api` |
| 2.1.290 | 2026-10-05 | Skills and custom commands refuse a `!` shell command with raw control characters other than tab and newline. | |
| 2.1.290 | 2026-10-05 | `ThemeKey` and `Color` types added to plugin hook typings; mod `$.process.spawn` denial message says the call ran. | `ThemeKey`, `Color`, `$.process.spawn` |
| 2.1.289 | 2026-10-03 | Plugin code pane opens large files faster; failed band/pane draw names the mod. | |
| 2.1.288 | 2026-10-02 | `$.ui.selection()` for mods returns the last selected text in fullscreen mode. | `$.ui.selection()` |
| 2.1.287 | 2026-10-01 | Claude Mods: plugins may modify deeper behavior; built-in mod "You should know" (side agent flags things) enabled with `/plugin enable cc-plugin-you-should-know@builtin` (first-party sessions with telemetry on). | `/plugin enable cc-plugin-you-should-know@builtin` |
| 2.1.287 | 2026-10-01 | Plugin listings note when a plugin's dependencies were not installed; updating retries an unfinished install. | |
| 2.1.287 | 2026-10-01 | `/skill` names typed mid-message are flagged to Claude as skills, including `disable-model-invocation` ones. | `disable-model-invocation` |
| 2.1.286 | 2026-09-30 | Plugin installs refuse npm sources that are git repositories or folders; dependencies only from registry packages. | |
| 2.1.286 | 2026-09-30 | If a skill named `verify` exists, Claude is told to run it right before committing (except docs-only/tests-only commits). | `verify` |
| 2.1.285 | 2026-09-29 | `claude plugin configure <plugin>` shows options and unset ones; `--values-stdin` saves values; `claude plugin install --config <server>.<key>=<value>` sets a bundled `.mcpb` server's settings. | `claude plugin configure`, `--values-stdin`, `--config` |
| 2.1.285 | 2026-09-29 | `claude mcp get` hides command, args and env values of plugin-provided stdio servers (names still shown). | `claude mcp get` |
| 2.1.283 | 2026-09-25 | `/doctor prompt-audit` (also `/checkup prompt-audit`) audits CLAUDE.md, skills, agents, commands for patterns written for older models. | `/doctor prompt-audit`, `/checkup prompt-audit` |
| 2.1.283 | 2026-09-25 | `Skill(anthropic-skills:<name>)` deny also blocks the skill when Desktop delivers it as a plugin; `claude plugin eval` requires git 2.31+. | `Skill(anthropic-skills:<name>)`, `claude plugin eval` |
| 2.1.283 | 2026-09-25 | Reverted 2.1.282 reservation of the `claude-ai` name: skills, commands, workflows, MCP servers so named load again; `Skill(claude-ai:*)` is an ordinary prefix rule. | `claude-ai`, `Skill(claude-ai:*)` |
| 2.1.283 | 2026-09-25 | `installed_plugins.json` that cannot be read is kept beside a rebuilt file; `claude plugin list` names it. | `installed_plugins.json` |
| 2.1.282 | 2026-09-24 | `anthropic-skills` and `claude-ai` namespaces: skill folders, commands, workflow commands no longer load; MCP servers so named list no skills or prompts; `Skill(...:*)` allow rules cover only claude.ai-synced skills. | `anthropic-skills`, `claude-ai` |
| 2.1.281 | 2026-09-23 | `claude plugin validate` reports dropped `.mcp.json` entries, undeclared `${user_config.*}` references, insecure URLs. | `${user_config.*}` |
| 2.1.280 | 2026-09-22 | Marketplaces whose name imitates a reserved name are refused when added and stop loading if already added. | |
| 2.1.277 | 2026-09-18 | `claude plugin install` on an installed plugin says when a newer version exists and names `claude plugin update`. | `claude plugin update` |
| 2.1.275 | 2026-09-17 | Skills and plugins enabled on claude.ai sync to terminal sessions signed in with it; opt out with `syncClaudeAiSkills: false` or `syncClaudeAiPlugins: false`. | `syncClaudeAiSkills`, `syncClaudeAiPlugins` |
| 2.1.275 | 2026-09-17 | `/plugin install <plugin> --marketplace <source>` offers to add the marketplace first; npm-source plugins fetched with `npm pack --ignore-scripts`, integrity-verified. | `--marketplace` |
| 2.1.275 | 2026-09-17 | `ListPlugins` tool description clarified: lists plugins enabled on the claude.ai account. | `ListPlugins` |
| 2.1.274 | 2026-09-17 | Plugin and marketplace clones leave Git LFS files as pointers. | |
| 2.1.271 | 2026-09-14 | `--accept-command <sha256>` on `claude plugin install` and `update` accepts exactly the command a prior `--json` run displayed, instead of `-y`. | `--accept-command`, `--json` |
| 2.1.269 | 2026-09-11 | `claude plugin eval` added; skills synced from claude.ai in cloud sessions are named `anthropic-skills:<name>`. | `claude plugin eval` |
| 2.1.268 | 2026-09-10 | `--json` on `claude plugin install`, `uninstall`, `update`, `enable`, `disable`; `errorDetails`/`noteDetails` in `claude plugin list --json`; `/plugin` changes take effect on menu close (no `/reload-plugins`). | `--json`, `/reload-plugins` |
| 2.1.265 | 2026-09-08 | `--plugin-dir` can point at a folder of plugins (each child with a manifest loads; additions picked up live). | `--plugin-dir` |
| 2.1.261 | 2026-09-04 | `/skill-doctor` shows unused loaded skills and their context cost. | `/skill-doctor` |

# Not found in the documentation pages

- `/checkup prompt-audit`
- `$.ui.selection()`
- `ThemeKey`
- `Skill(anthropic-skills:*)`
- `Skill(claude-ai:*)`
- `ListPlugins`
